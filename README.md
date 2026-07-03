# Agentic Royalty Path Standard

A standard for mapping AI agent action paths, browser receipts, execution logs, monetization events, provider records, and commerce audit events into audit-ready royalty candidates.

## Purpose

Agentic Royalty Path Standard defines a structured record format for capturing how an AI agent reaches a value-generating outcome.

It focuses not only on the final artifact, but also on the path that produced it.

In AI-assisted development, research, commerce, and content workflows, value is increasingly generated through agentic sequences:

* reading or navigating resources
* operating browser or application environments
* executing tools
* observing results
* detecting issues
* accessing monetized resources
* triggering payment or usage events
* producing derivative outcomes
* creating audit-ready evidence for possible royalty attribution

This standard records those sequences as audit-ready value paths.

## Core idea

Traditional royalty accounting often focuses on static outputs:

```text
Origin
  ↓
Derivative
  ↓
Audit
  ↓
Royalty
```

Agentic Royalty Path extends this into dynamic path accounting:

```text
Origin
  ↓
Agentic Path
  ↓
Action Receipts
  ↓
Agent Log
  ↓
Monetization Event
  ↓
Provider Bridge
  ↓
Commerce Audit
  ↓
Royalty Candidate
```

The goal is to make AI agent value generation traceable, auditable, and connectable to royalty candidate mapping.

## Design principles

### 1. Path before payout

This standard records the path before calculating or executing any payout.

It does not assume that a royalty claim exists simply because an AI agent performed an action.

Instead, it creates audit-ready evidence that can later be reviewed by a human, marketplace rule, legal framework, or external royalty engine.

### 2. Candidate, not claim

Fields such as `royalty_mapping`, `royalty_candidates`, and `suggested_share` should be treated as candidate records.

They do not create legal royalty claims by themselves.

### 3. Provider-neutral

The standard can describe events from multiple external systems, including:

* edge monetization gateways
* payment networks
* API billing platforms
* MCP tool gateways
* agent commerce platforms
* marketplaces
* identity providers
* future settlement or usage-tracking systems

It is not tied to a single company, payment network, or protocol.

### 4. Audit-first

The standard prioritizes:

* traceability
* reproducibility
* evidence references
* permission boundaries
* authorization records
* risk controls
* human review
* legal non-claiming by default

## Version overview

```text
v0.1 — Agentic Royalty Path Core
v0.2 — Monetization Event Extension
v0.3 — Path Royalty Weighting
v0.4 — Provider Bridge Layer
v0.5 — Agent Commerce Audit Bridge
```

## v0.1 — Agentic Royalty Path Core

v0.1 introduces the minimum structure for recording AI agent value-generation paths.

It defines:

* `goal`
* `path_layer`
* `action_receipts`
* `agent_log`
* `path_hash_chain`
* `monetization_event`
* `audit`
* `royalty_mapping`

Core flow:

```text
Origin
  ↓
Agentic Path
  ↓
Action Receipts
  ↓
Agent Log
  ↓
Audit
  ↓
Royalty Candidate
```

## v0.2 — Monetization Event Extension

v0.2 introduces the Monetization Event Extension.

This extension allows an Agentic Royalty Path to reference external monetization, payment, billing, or paid-access events.

Examples include:

* paid resource access
* API usage billing
* MCP tool payment
* agent commerce transactions
* subscription-based access
* logged free access events

Core flow:

```text
Agentic Path
  ↓
Action Receipt
  ↓
Monetization Event
  ↓
Payment Receipt
  ↓
Audit
  ↓
Royalty Candidate
```

The Monetization Event Extension does not define a legal royalty claim by itself.

Instead, it records audit-ready evidence that a value-bearing access or payment event occurred during an AI agent path.

## v0.3 — Path Royalty Weighting

v0.3 introduces Path Royalty Weighting.

This layer maps an AI agent value-generation path into candidate royalty shares.

It provides candidate weighting records based on path evidence, origin dependency, monetization signals, action receipts, and review status.

Core flow:

```text
Origin
  ↓
Agentic Path
  ↓
Action Receipts
  ↓
Monetization Event
  ↓
Path Royalty Weighting
  ↓
Audit
  ↓
Royalty Candidate
```

### Scoring factors

v0.3 introduces candidate scoring factors such as:

* `path_complexity`
* `origin_dependency`
* `action_receipt_confidence`
* `monetization_signal`
* `agent_decision_depth`
* `human_review_depth`
* `reproducibility_score`

### Royalty candidates

Each royalty candidate can include:

* candidate ID
* contributor role
* beneficiary reference
* contribution basis
* suggested share
* evidence references
* review notes

Any suggested share must be reviewed before payout or settlement.

## v0.4 — Provider Bridge Layer

v0.4 introduces the Provider Bridge Layer.

This layer defines how external infrastructure providers can be mapped into the Agentic Royalty Path Standard.

Examples include:

* edge monetization gateways
* payment networks
* API billing platforms
* MCP tool gateways
* agent commerce platforms
* marketplaces
* identity providers

Core flow:

```text
External Provider
  ↓
Provider Bridge
  ↓
Monetization Event
  ↓
Agentic Royalty Path
  ↓
Path Royalty Weighting
  ↓
Audit
  ↓
Royalty Candidate
```

### Provider Bridge concepts

v0.4 introduces:

* `provider`
* `capabilities`
* `protocol_bindings`
* `event_mapping`
* `data_policy`
* `trust_boundary`
* `bridge_status`

The Provider Bridge Layer is provider-neutral.

It can describe Cloudflare-style monetization gateways, x402-style payment flows, API billing systems, MCP tool payment gateways, agent commerce platforms, marketplace settlement systems, or future external provider events without hard-coding the standard to one company or protocol.

## v0.5 — Agent Commerce Audit Bridge

v0.5 introduces the Agent Commerce Audit Bridge.

This layer records AI agent commerce actions as audit-ready records.

Examples include:

* purchases
* subscriptions
* paid resource access
* API calls
* MCP tool usage
* quote requests
* contract acceptance
* refund requests
* disputes

Core flow:

```text
Agent Commerce Action
  ↓
Authorization Boundary
  ↓
Provider Bridge
  ↓
Payment / Usage Event
  ↓
Agentic Royalty Path
  ↓
Audit
  ↓
Royalty Candidate
```

### Agent Commerce Audit concepts

v0.5 introduces:

* `commerce_action`
* `agent_context`
* `authorization_boundary`
* `transaction_context`
* `provider_refs`
* `path_refs`
* `risk_controls`
* `audit`

The Agent Commerce Audit Bridge does not execute transactions.

It records commerce-related actions performed or initiated by AI agents and maps them into audit-ready value-path records.

## Repository structure

```text
schemas/
  agentic-royalty-path.schema.json
  monetization-event.schema.json
  path-royalty-weighting.schema.json
  provider-bridge.schema.json
  agent-commerce-audit-bridge.schema.json

examples/
  agentic-royalty-path.example.yaml
  agentic-royalty-path.monetized.example.yaml
  monetization-event.cloudflare-x402.example.yaml
  path-royalty-weighting.example.yaml
  provider-bridge.cloudflare-x402.example.yaml
  agent-commerce-audit-bridge.example.yaml

scripts/
  validate_examples.py

.github/
  workflows/
    validate.yml
```

## Validation

Validate all examples against their schemas:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
[validate] Agentic Royalty Path
[ok] Agentic Royalty Path example is valid

[validate] Agentic Royalty Path Monetized Example
[ok] Agentic Royalty Path Monetized Example example is valid

[validate] Monetization Event
[ok] Monetization Event example is valid

[validate] Path Royalty Weighting
[ok] Path Royalty Weighting example is valid

[validate] Provider Bridge
[ok] Provider Bridge example is valid

[validate] Agent Commerce Audit Bridge
[ok] Agent Commerce Audit Bridge example is valid
```

## Important note

This standard does not execute payments.

It does not create legal royalty claims.

It does not approve payouts.

It does not determine final settlement rights.

Instead, it provides audit-ready records for identifying value-generation paths, connecting them to external events, and mapping them to possible royalty candidates.

Any commerce action, payment event, authorization event, royalty candidate, or suggested share should be treated as provisional until reviewed by a human, marketplace rule, legal framework, or external royalty engine.

## Current candidate

```text
v0.5.0-candidate — Agent Commerce Audit Bridge
```

## First arc summary

The first candidate arc establishes five layers:

```text
Path
  ↓
Monetization
  ↓
Weighting
  ↓
Provider
  ↓
Commerce Audit
```

Together, these layers define a foundation for AI agent value-path accounting.

Agentic Royalty Path Standard is designed as a bridge between AI agent behavior, external monetization infrastructure, audit records, and royalty candidate mapping.

## Roadmap

Possible future extensions:

```text
v0.6 — Settlement Review Layer
v0.7 — Human Settlement Gate
v0.8 — Marketplace Rule Engine Bridge
v0.9 — Multi-Agent Value Path Graph
v1.0 — Agentic Value Accounting Standard
```

