# Changelog

## v0.2.0-candidate — Monetization Event Extension

Second candidate release.

### Added

- `monetization-event.schema.json`
- `monetization-event.cloudflare-x402.example.yaml`
- `agentic-royalty-path.monetized.example.yaml`
- Validation support for monetization event examples
- Optional monetization linkage from Agentic Royalty Path records

### New concepts

- `monetization_event`
- `payment_receipt`
- `pricing`
- `request_context`
- `external_provider_verified`
- `replay_protection`

### Purpose

v0.2 connects agentic value paths to external monetization or payment events.

This allows an AI agent path to record not only what was accessed or operated, but whether a value-bearing access event occurred.

### Important note

Monetization Event records are audit evidence.

They do not create legal royalty claims by themselves.

Any `royalty_mapping` or payment-related record should be treated as a candidate until reviewed by a human, marketplace rule, legal framework, or external royalty engine.

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
