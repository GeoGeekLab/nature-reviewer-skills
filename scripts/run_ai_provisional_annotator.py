from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"Expected object at {path}:{number}")
            rows.append(value)
    return rows


def _post_json(url: str, payload: dict[str, Any], timeout: int = 600) -> dict[str, Any]:
    parsed = urlparse(url)
    if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost"}:
        raise ValueError("AI annotation may call only the isolated local HTTP server")
    request = urllib.request.Request(  # noqa: S310  # nosec B310
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310  # nosec B310
            value = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Annotation server HTTP {exc.code}: {body}") from exc
    if not isinstance(value, dict):
        raise ValueError("Annotation response must be a JSON object")
    return value


def _extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if match is None:
            raise
        value = json.loads(match.group(0))
    if not isinstance(value, dict):
        raise ValueError("Annotation output must be a JSON object")
    return value


def _domain_codebook(codebook: dict[str, Any], domain: str) -> list[dict[str, str]]:
    issues = codebook.get("issues")
    if not isinstance(issues, list):
        raise ValueError("Codebook issues must be a list")
    result = []
    for issue in issues:
        if not isinstance(issue, dict) or str(issue.get("domain")) != domain:
            continue
        result.append(
            {
                "issue_id": str(issue["issue_id"]),
                "definition": str(issue["definition"]),
                "coding_rule": str(issue["coding_rule"]),
                "negative_boundary": str(issue["negative_boundary"]),
            }
        )
    if not result:
        raise ValueError(f"No codebook issues found for domain {domain}")
    return result


def _gbnf_grammar(allowed: list[dict[str, str]]) -> str:
    terminals = " | ".join(json.dumps(json.dumps(issue["issue_id"])) for issue in allowed)
    return "\n".join(
        [
            'root ::= "{" ws "\\\"issue_ids\\\"" ws ":" ws "[" ws (items)? ws "]" ws "}"',
            'items ::= issue | issue ws "," ws issue | issue ws "," ws issue ws "," ws issue',
            f"issue ::= {terminals}",
            "ws ::= [ \\t\\n\\r]*",
        ]
    )


def _prompt(row: dict[str, Any], allowed: list[dict[str, str]]) -> str:
    codebook_text = "\n\n".join(
        "\n".join(
            [
                f"issue_id: {issue['issue_id']}",
                f"definition: {issue['definition']}",
                f"coding_rule: {issue['coding_rule']}",
                f"negative_boundary: {issue['negative_boundary']}",
            ]
        )
        for issue in allowed
    )
    allowed_ids = [issue["issue_id"] for issue in allowed]
    return f"""You are an annotation model for a controlled scientific-review benchmark.

Code which supplied domain issue IDs are explicitly and specifically identified in the REVIEW OUTPUT.

Rules:
- Judge the REVIEW OUTPUT against the MANUSCRIPT EXCERPT and supplied codebook.
- Do not infer condition, case type, target issue, pair, or gold.
- Generic requests for more experiments/details/citations do not count.
- Return only a subset of the ALLOWED ISSUE IDS. Zero IDs is allowed.
- Never invent a new label.
- Output JSON only, exactly: {{"issue_ids":["id-1","id-2"]}}

ALLOWED ISSUE IDS
{allowed_ids}

DOMAIN CODEBOOK
{codebook_text}

MANUSCRIPT EXCERPT
{row["manuscript_text"]}

REVIEW OUTPUT
{row["review_text"]}
"""


def annotate(
    packets_path: Path,
    codebook_path: Path,
    *,
    output_path: Path,
    metadata_path: Path,
    server_url: str,
    model: str,
    annotator_id: str,
    seed: int,
    max_tokens: int,
    retries: int,
) -> dict[str, Any]:
    packets = _jsonl(packets_path)
    codebook = _json(codebook_path)
    if not isinstance(codebook, dict):
        raise ValueError("Codebook must be a JSON object")

    outputs: list[str] = []
    metadata: list[str] = []
    seen: set[str] = set()
    started = time.time()

    for index, row in enumerate(packets, 1):
        annotation_id = str(row["annotation_id"])
        domain = str(row["domain"])
        if annotation_id in seen:
            raise ValueError(f"Duplicate annotation_id {annotation_id}")
        seen.add(annotation_id)

        allowed = _domain_codebook(codebook, domain)
        allowed_ids = {issue["issue_id"] for issue in allowed}
        prompt = _prompt(row, allowed)
        grammar = _gbnf_grammar(allowed)

        parsed: dict[str, Any] | None = None
        raw_text = ""
        usage: dict[str, Any] = {}
        finish_reason: Any = None
        attempts = 0

        while parsed is None and attempts <= retries:
            attempts += 1
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.0,
                "top_p": 1.0,
                "seed": seed + attempts - 1,
                "max_tokens": max_tokens,
                "stream": False,
                "grammar": grammar,
            }
            response = _post_json(f"{server_url.rstrip('/')}/v1/chat/completions", payload)
            choices = response.get("choices")
            if not isinstance(choices, list) or not choices:
                raise ValueError(f"{annotation_id}: no response choices")
            choice = choices[0]
            if not isinstance(choice, dict) or not isinstance(choice.get("message"), dict):
                raise ValueError(f"{annotation_id}: invalid response choice")
            raw_text = str(choice["message"].get("content", "")).strip()
            finish_reason = choice.get("finish_reason")
            candidate_usage = response.get("usage", {})
            if isinstance(candidate_usage, dict):
                usage = candidate_usage
            try:
                parsed = _extract_json(raw_text)
            except (json.JSONDecodeError, ValueError):
                if attempts > retries:
                    raise ValueError(
                        f"{annotation_id}: invalid JSON after {attempts} attempts: {raw_text[:400]}"
                    ) from None

        if parsed is None:
            raise RuntimeError(
                f"{annotation_id}: annotation parser reached an impossible empty state"
            )
        issue_ids = parsed.get("issue_ids", [])
        if not isinstance(issue_ids, list):
            raise ValueError(f"{annotation_id}: issue_ids must be a list")

        clean_concerns = []
        invalid_issue_ids: list[str] = []
        seen_issues: set[str] = set()
        for value in issue_ids:
            issue_id = str(value)
            if issue_id not in allowed_ids:
                invalid_issue_ids.append(issue_id)
                continue
            if issue_id in seen_issues:
                continue
            seen_issues.add(issue_id)
            clean_concerns.append({"issue_id": issue_id, "severity": "minor", "anchors": []})

        outputs.append(
            json.dumps(
                {
                    "annotation_id": annotation_id,
                    "annotator_id": annotator_id,
                    "concerns": clean_concerns,
                },
                ensure_ascii=False,
            )
            + "\n"
        )
        metadata.append(
            json.dumps(
                {
                    "annotation_id": annotation_id,
                    "annotator_id": annotator_id,
                    "domain": domain,
                    "attempts": attempts,
                    "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
                    "finish_reason": finish_reason,
                    "prompt_tokens": usage.get("prompt_tokens"),
                    "completion_tokens": usage.get("completion_tokens"),
                    "invalid_issue_ids": invalid_issue_ids,
                }
            )
            + "\n"
        )
        output_path.write_text("".join(outputs), encoding="utf-8")
        metadata_path.write_text("".join(metadata), encoding="utf-8")
        print(
            json.dumps(
                {
                    "progress": f"{index}/{len(packets)}",
                    "annotation_id": annotation_id,
                    "coded_issues": len(clean_concerns),
                    "attempts": attempts,
                }
            ),
            flush=True,
        )

    return {
        "annotator_id": annotator_id,
        "annotation_count": len(outputs),
        "unique_annotation_ids": len(seen),
        "elapsed_seconds": round(time.time() - started, 3),
        "annotations_sha256": hashlib.sha256(output_path.read_bytes()).hexdigest(),
        "metadata_sha256": hashlib.sha256(metadata_path.read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--packets", type=Path, required=True)
    parser.add_argument("--codebook", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--server-url", default="http://127.0.0.1:8080")
    parser.add_argument("--model", default="annotator-model")
    parser.add_argument("--annotator-id", required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--max-tokens", type=int, default=64)
    parser.add_argument("--retries", type=int, default=2)
    args = parser.parse_args()

    report = annotate(
        args.packets,
        args.codebook,
        output_path=args.output,
        metadata_path=args.metadata,
        server_url=args.server_url,
        model=args.model,
        annotator_id=args.annotator_id,
        seed=args.seed,
        max_tokens=args.max_tokens,
        retries=args.retries,
    )
    print(json.dumps(report, indent=2))
