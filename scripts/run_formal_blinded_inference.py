from __future__ import annotations

import argparse
import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from nature_reviewer_core.patterns import load_patterns
from nature_reviewer_core.retrieval import search_patterns

ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "benchmarks/pilot_v1/FORMAL_INFERENCE_LOCK_QWEN25_3B.json"


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


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _skill_context(skill_root: Path, manuscript_text: str) -> str:
    skill_md = (skill_root / "SKILL.md").read_text(encoding="utf-8").strip()

    references: list[str] = []
    reference_root = skill_root / "references"
    if reference_root.is_dir():
        for path in sorted(reference_root.glob("*.md")):
            references.append(
                f"### Reference: {path.name}\n{path.read_text(encoding='utf-8').strip()}"
            )

    patterns = search_patterns(
        load_patterns(skill_root),
        manuscript_text,
        limit=8,
        diversify=True,
    )
    pattern_text = []
    for index, result in enumerate(patterns, 1):
        pattern = result.pattern
        pattern_text.append(
            "\n".join(
                [
                    f"Pattern {index}: {pattern.title}",
                    f"Gate: {pattern.gate}",
                    f"Concern hypothesis: {pattern.concern}",
                    f"Evidence risk: {pattern.evidence_risk}",
                    f"Revision direction: {pattern.revision_direction}",
                    f"Default severity: {pattern.severity}",
                ]
            )
        )

    sections = [
        "DOMAIN SKILL INSTRUCTIONS",
        skill_md,
    ]
    if references:
        sections.extend(
            [
                "DOMAIN SKILL REFERENCE NOTES",
                "\n\n".join(references),
            ]
        )
    if pattern_text:
        sections.extend(
            [
                (
                    "LOCAL REVIEWER MEMORY HYPOTHESES\n"
                    "These are abstracted hypotheses retrieved only from the manuscript text. "
                    "Do not report a concern unless the excerpt itself supports it."
                ),
                "\n\n".join(pattern_text),
            ]
        )
    return "\n\n".join(sections)


def _post_json(url: str, payload: dict[str, Any], timeout: int = 900) -> dict[str, Any]:
    parsed = urlparse(url)
    if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost"}:
        raise ValueError("Formal inference may call only the isolated local HTTP server")

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
        raise RuntimeError(f"Inference server HTTP {exc.code}: {body}") from exc
    if not isinstance(value, dict):
        raise ValueError("Inference response must be a JSON object")
    return value


def _packet_condition_and_run(path: Path) -> tuple[str, int]:
    stem = path.stem
    for condition in ("generic", "skill-assisted"):
        prefix = f"{condition}_run_"
        if stem.startswith(prefix):
            return condition, int(stem.removeprefix(prefix))
    raise ValueError(f"Unrecognized packet filename: {path.name}")


def run(
    pilot_dir: Path,
    *,
    server_url: str,
    server_model: str,
) -> dict[str, Any]:
    lock = _json(LOCK_PATH)
    if not isinstance(lock, dict):
        raise ValueError("Experiment lock must be a JSON object")

    generation = lock["generation"]
    if not isinstance(generation, dict):
        raise ValueError("Invalid generation configuration")
    run_seeds = generation["run_seeds"]
    if not isinstance(run_seeds, dict):
        raise ValueError("run_seeds must be an object")

    packet_dir = pilot_dir / "execution_packets"
    packet_paths = sorted(packet_dir.glob("*.jsonl"))
    if len(packet_paths) != 6:
        raise ValueError(f"Expected 6 execution packet files, found {len(packet_paths)}")

    raw_path = pilot_dir / "raw_outputs.jsonl"
    metadata_path = pilot_dir / "inference_metadata.jsonl"
    if raw_path.exists() or metadata_path.exists():
        raise FileExistsError("Refusing to overwrite existing formal inference outputs")

    raw_lines: list[str] = []
    metadata_lines: list[str] = []
    seen_blind_ids: set[str] = set()
    started = time.time()
    output_index = 0

    for packet_path in packet_paths:
        condition, run_index = _packet_condition_and_run(packet_path)
        seed = int(run_seeds[str(run_index)])
        packets = _jsonl(packet_path)

        for packet in packets:
            output_index += 1
            blind_id = str(packet["blind_id"])
            if blind_id in seen_blind_ids:
                raise ValueError(f"Duplicate blind_id across packets: {blind_id}")
            seen_blind_ids.add(blind_id)

            manuscript_text = str(packet["manuscript_text"])
            system_prompt = str(packet["prompt"])
            skill_context_sha256: str | None = None

            if condition == "skill-assisted":
                skill_path = str(packet.get("skill_path", ""))
                if not skill_path:
                    raise ValueError(f"{blind_id}: skill-assisted packet missing skill_path")
                skill_root = ROOT / skill_path
                context = _skill_context(skill_root, manuscript_text)
                skill_context_sha256 = _sha256_text(context)
                system_prompt = (
                    system_prompt
                    + "\n\n"
                    + context
                )
            elif "skill_path" in packet:
                raise ValueError(f"{blind_id}: generic packet unexpectedly contains skill_path")

            user_prompt = "Manuscript excerpt:\n\n" + manuscript_text
            payload = {
                "model": server_model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "temperature": float(generation["temperature"]),
                "top_p": float(generation["top_p"]),
                "seed": seed,
                "max_tokens": int(generation["max_completion_tokens"]),
                "stream": False,
            }

            inference_started = time.time()
            response = _post_json(f"{server_url.rstrip('/')}/v1/chat/completions", payload)
            latency = time.time() - inference_started

            choices = response.get("choices")
            if not isinstance(choices, list) or not choices:
                raise ValueError(f"{blind_id}: response has no choices")
            choice = choices[0]
            if not isinstance(choice, dict):
                raise ValueError(f"{blind_id}: invalid choice object")
            message = choice.get("message")
            if not isinstance(message, dict):
                raise ValueError(f"{blind_id}: invalid response message")
            review_text = str(message.get("content", "")).strip()
            if not review_text:
                raise ValueError(f"{blind_id}: empty review output")

            usage = response.get("usage", {})
            if not isinstance(usage, dict):
                usage = {}

            raw_lines.append(
                json.dumps(
                    {"blind_id": blind_id, "review_text": review_text},
                    ensure_ascii=False,
                )
                + "\n"
            )
            metadata_lines.append(
                json.dumps(
                    {
                        "blind_id": blind_id,
                        "packet_file": packet_path.name,
                        "condition": condition,
                        "run_index": run_index,
                        "seed": seed,
                        "system_prompt_sha256": _sha256_text(system_prompt),
                        "skill_context_sha256": skill_context_sha256,
                        "manuscript_sha256": _sha256_text(manuscript_text),
                        "latency_seconds": round(latency, 3),
                        "finish_reason": choice.get("finish_reason"),
                        "prompt_tokens": usage.get("prompt_tokens"),
                        "completion_tokens": usage.get("completion_tokens"),
                        "total_tokens": usage.get("total_tokens"),
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

            raw_path.write_text("".join(raw_lines), encoding="utf-8")
            metadata_path.write_text("".join(metadata_lines), encoding="utf-8")
            print(
                json.dumps(
                    {
                        "progress": f"{output_index}/108",
                        "blind_id": blind_id,
                        "condition": condition,
                        "run_index": run_index,
                        "latency_seconds": round(latency, 2),
                        "completion_tokens": usage.get("completion_tokens"),
                    }
                ),
                flush=True,
            )

    elapsed = time.time() - started
    expected = int(lock["execution"]["expected_raw_outputs"])
    if len(raw_lines) != expected:
        raise ValueError(f"Expected {expected} outputs, generated {len(raw_lines)}")

    summary = {
        "experiment_id": lock["experiment_id"],
        "raw_output_count": len(raw_lines),
        "unique_blind_ids": len(seen_blind_ids),
        "elapsed_seconds": round(elapsed, 3),
        "raw_outputs_sha256": hashlib.sha256(raw_path.read_bytes()).hexdigest(),
        "inference_metadata_sha256": hashlib.sha256(metadata_path.read_bytes()).hexdigest(),
    }
    (pilot_dir / "formal_inference_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pilot-dir", type=Path, required=True)
    parser.add_argument("--server-url", default="http://127.0.0.1:8080")
    parser.add_argument("--server-model", default="pilot-model")
    args = parser.parse_args()
    print(
        json.dumps(
            run(
                args.pilot_dir,
                server_url=args.server_url,
                server_model=args.server_model,
            ),
            indent=2,
        )
    )
