import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Agentic Royalty Path",
        "schema": ROOT / "schemas" / "agentic-royalty-path.schema.json",
        "example": ROOT / "examples" / "agentic-royalty-path.example.yaml",
    },
    {
        "name": "Agentic Royalty Path Monetized Example",
        "schema": ROOT / "schemas" / "agentic-royalty-path.schema.json",
        "example": ROOT / "examples" / "agentic-royalty-path.monetized.example.yaml",
    },
    {
        "name": "Monetization Event",
        "schema": ROOT / "schemas" / "monetization-event.schema.json",
        "example": ROOT / "examples" / "monetization-event.cloudflare-x402.example.yaml",
    },
    {
        "name": "Path Royalty Weighting",
        "schema": ROOT / "schemas" / "path-royalty-weighting.schema.json",
        "example": ROOT / "examples" / "path-royalty-weighting.example.yaml",
    },
    {
        "name": "Provider Bridge",
        "schema": ROOT / "schemas" / "provider-bridge.schema.json",
        "example": ROOT / "examples" / "provider-bridge.cloudflare-x402.example.yaml",
    },
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> int:
    failed = False

    for target in VALIDATION_TARGETS:
        print(f"[validate] {target['name']}")
        print(f"  schema : {target['schema'].relative_to(ROOT)}")
        print(f"  example: {target['example'].relative_to(ROOT)}")

        schema = load_json(target["schema"])
        example = load_yaml(target["example"])

        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(example), key=lambda e: e.path)

        if errors:
            failed = True
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                print(f"Error: {location}: {error.message}")
        else:
            print(f"[ok] {target['name']} example is valid")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
