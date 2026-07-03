# Changelog

## v0.1.0-candidate — Agentic Royalty Path Core

Initial candidate release.

### Added

- `agentic-royalty-path.schema.json`
- `agentic-royalty-path.example.yaml`
- Validation script for schema/example consistency
- GitHub Actions validation workflow
- Core record fields:
  - `goal`
  - `path_layer`
  - `action_receipts`
  - `agent_log`
  - `path_hash_chain`
  - `monetization_event`
  - `audit`
  - `royalty_mapping`

### Notes

v0.1 defines the minimum structure for recording AI agent value-generation paths.

The standard treats royalty mapping as an audit-ready candidate, not as a legal claim.
