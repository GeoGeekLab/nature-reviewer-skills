from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def load_router(path: Path) -> dict[str, Any]:
    """Load and minimally validate an orchestrator routing configuration."""
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("routes"), list):
        raise ValueError(f"Invalid router configuration: {path}")
    return value


def route_text(text: str, router: dict[str, Any]) -> dict[str, Any]:
    """Route manuscript text to domain skills and polar evidence gates deterministically."""

    def normalize(value: str) -> str:
        return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()

    folded = normalize(text)
    scored: list[tuple[int, str, list[str], list[str], list[str]]] = []
    for raw in router.get("routes", []):
        if not isinstance(raw, dict):
            continue
        signals = [str(item) for item in raw.get("signals", [])]
        matched = [signal for signal in signals if normalize(signal) in folded]
        if matched:
            scored.append(
                (
                    len(matched),
                    str(raw.get("route_id", "unknown")),
                    [str(item) for item in raw.get("primary_skills", [])],
                    [str(item) for item in raw.get("gates", [])],
                    matched,
                )
            )
    scored.sort(key=lambda item: (-item[0], item[1]))
    maximum = int(router.get("maximum_routes", 4))
    selected = scored[:maximum]
    if not selected and router.get("routes"):
        # A general polar manuscript still receives always-on evidence checks. No domain
        # skill is guessed when the supplied text contains no route evidence.
        selected = []
    routes = [item[1] for item in selected]
    skills = list(dict.fromkeys(skill for item in selected for skill in item[2]))
    gates = list(
        dict.fromkeys(
            [str(item) for item in router.get("always_apply", [])]
            + [gate for item in selected for gate in item[3]]
        )
    )
    matched_terms = {item[1]: item[4] for item in selected}
    responsibility_signals = [str(item) for item in router.get("conditional_ethics_signals", [])]
    responsibility_matches = [
        signal for signal in responsibility_signals if normalize(signal) in folded
    ]
    return {
        "routes": routes,
        "skills": skills,
        "gates": gates,
        "matched_terms": matched_terms,
        "responsibility_review": bool(responsibility_matches),
        "responsibility_matches": responsibility_matches,
    }
