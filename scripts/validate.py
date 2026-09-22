#!/usr/bin/env python3
"""Minimal validation for the Minitongue repository.

This script checks the file structure and ensures the repository metadata files
parse cleanly enough to be used as a proto language specification.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

VALID_JUDGMENTS = {"grammatical", "ungrammatical", "marginal"}

def _warn(msg: str) -> None:
    print(f"WARN: {msg}")


def _error(msg: str) -> None:
    print(f"ERROR: {msg}")


def validate_tsv(path: Path, required_headers: list[str]) -> bool:
    if not path.exists():
        _error(f"Missing required file: {path.relative_to(ROOT)}")
        return False
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        rows = list(reader)
    if not rows:
        _error(f"Empty TSV: {path.relative_to(ROOT)}")
        return False
    header = rows[0]
    if header != required_headers:
        _error(f"Incorrect header in {path.relative_to(ROOT)}: expected {required_headers}, found {header}")
        return False
    return True


def validate_json(path: Path) -> bool:
    if not path.exists():
        _error(f"Missing required file: {path.relative_to(ROOT)}")
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        _error(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return False
    if not isinstance(data, dict):
        _error(f"JSON root in {path.relative_to(ROOT)} is not an object")
        return False
    return True


def validate_examples(path: Path) -> bool:
    ok = True
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for row in rows:
        if not row:
            continue
        ex_id = row.get("example_id", "")
        if ex_id and not re.fullmatch(r"EX-[0-9]{4,}", ex_id):
            _error(f"Malformed example_id: {ex_id}")
            ok = False
        judgment = row.get("judgment", "")
        if judgment and judgment not in VALID_JUDGMENTS:
            _error(f"Invalid judgment for {ex_id}: {judgment}")
            ok = False
        for field in ["text", "ipa", "segmentation", "gloss", "translation"]:
            if not row.get(field, "").strip():
                _error(f"Missing {field} for {ex_id}")
                ok = False
    return ok


def validate_lexicon(path: Path) -> bool:
    ok = True
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    for row in rows:
        if not row:
            continue
        lexeme_id = row.get("lexeme_id", "")
        sense_id = row.get("sense_id", "")
        if lexeme_id and not re.fullmatch(r"L-[0-9]{4,}", lexeme_id):
            _error(f"Malformed lexeme_id: {lexeme_id}")
            ok = False
        if sense_id and not re.fullmatch(r"L-[0-9]{4,}-S[0-9]{2,}", sense_id):
            _error(f"Malformed sense_id: {sense_id}")
            ok = False
        if not row.get("definition", "").strip():
            _error(f"Missing definition for {sense_id or lexeme_id}")
            ok = False
    return ok


def main() -> int:
    required_files = [
        ROOT / "AGENTS.md",
        ROOT / "grammar.md",
        ROOT / "lexicon.tsv",
        ROOT / "examples.tsv",
        ROOT / "schema.json",
        ROOT / "scripts" / "validate.py",
    ]

    problems = 0
    for path in required_files:
        if not path.exists():
            _error(f"Missing required file: {path.relative_to(ROOT)}")
            problems += 1

    if not validate_tsv(ROOT / "lexicon.tsv", [
        "lexeme_id", "lemma", "ipa", "pos", "features", "etymology",
        "sense_id", "definition", "usage", "notes"
    ]):
        problems += 1

    if not validate_tsv(ROOT / "examples.tsv", [
        "example_id", "judgment", "text", "ipa", "segmentation", "gloss",
        "translation", "rule_refs", "violated_rule_refs", "lexeme_refs", "notes"
    ]):
        problems += 1

    if not validate_json(ROOT / "schema.json"):
        problems += 1

    if not validate_examples(ROOT / "examples.tsv"):
        problems += 1

    if not validate_lexicon(ROOT / "lexicon.tsv"):
        problems += 1

    if problems:
        print(f"Repository validation failed with {problems} issue(s).")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
