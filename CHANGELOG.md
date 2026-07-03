# Changelog

## v0.5.0-candidate — Agent Commerce Audit Bridge

Fifth candidate release.

### Added

- `agent-commerce-audit-bridge.schema.json`
- `agent-commerce-audit-bridge.example.yaml`
- Validation support for agent commerce audit bridge examples
- Audit bridge structure for AI agent commerce actions
- Authorization boundary records for commerce-related agent actions
- Transaction context records for payment and settlement references
- Risk control records for commerce audit review

### New concepts

- `agent_commerce_audit_bridge`
- `commerce_action`
- `agent_context`
- `authorization_boundary`
- `transaction_context`
- `provider_refs`
- `path_refs`
- `risk_controls`
- `commerce_action_confirmed`

### Purpose

v0.5 introduces an audit bridge for AI agent commerce actions.

v0.1 recorded AI agent value-generation paths.  
v0.2 connected those paths to monetization events.  
v0.3 introduced candidate royalty weighting.  
v0.4 mapped external providers into the standard.  
v0.5 records commerce actions performed or initiated by AI agents and connects them to authorization, provider, transaction, path, and audit records.

### Important note

Agent Commerce Audit Bridge records are audit records.

They do not execute transactions, create legal royalty claims, approve payouts, or determine final settlement rights by themselves.

Any commerce action, payment record, or royalty candidate should be treated as provisional until reviewed by a human, marketplace rule, legal framework, or external royalty engine.

## v0.4.0-candidate — Provider Bridge Layer

Fourth candidate release.

### Added

- `provider-bridge.schema.json`
- `provider-bridge.cloudflare-x402.example.yaml`
- Validation support for provider bridge examples
- Provider-neutral bridge structure for external monetization and payment infrastructure

### New concepts

- `provider_bridge`
- `provider`
- `capabilities`
- `protocol_bindings`
- `event_mapping`
- `data_policy`
- `trust_boundary`
- `bridge_status`

### Purpose

v0.4 introduces a bridge layer for mapping external provider events into Agentic Royalty Path records.

v0.1 recorded AI agent value-generation paths.  
v0.2 connected those paths to monetization events.  
v0.3 introduced candidate royalty weighting.  
v0.4 defines how external infrastructure providers can be connected in a provider-neutral way.

### Important note

Provider Bridge records are interoperability records.

They do not execute payments, create legal royalty claims, or determine final payout rights by themselves.

Any external provider event should be treated as audit evidence until reviewed by a human, marketplace rule, legal framework, or external royalty engine.

## v0.3.0-candidate — Path Royalty Weighting

Third candidate release.

### Added

- `path-royalty-weighting.schema.json`
- `path-royalty-weighting.example.yaml`
- Validation support for path royalty weighting examples
- Candidate scoring model for agentic value paths
- Candidate royalty share mapping

### New concepts

- `path_royalty_weighting`
- `scoring_model`
- `scoring_factors`
- `royalty_candidates`
- `suggested_share`
- `payment_context`
- `weighting_status`

### Purpose

v0.3 connects agentic value paths to candidate royalty weighting.

v0.1 recorded the path.  
v0.2 connected monetization events.  
v0.3 introduces a way to suggest how value generated along that path may be attributed among contributors.

### Important note

Path Royalty Weighting records are audit-ready candidate records.

They do not create legal royalty claims by themselves.

Any `suggested_share` should be treated as provisional until reviewed by a human, marketplace rule, legal framework, or external royalty engine.

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
