# Agentic Royalty Path Standard

A standard for mapping AI agent action paths, browser receipts, execution logs, and monetization events into audit-ready royalty candidates.

## Purpose

Agentic Royalty Path Standard defines a minimal record format for capturing how an AI agent reaches a value-generating outcome.

It focuses on the path, not only the final artifact.

In AI-assisted development, research, commerce, and content workflows, value is increasingly generated through agentic sequences:

- reading or navigating resources
- operating browser or application environments
- executing tools
- observing results
- detecting issues
- producing derivative outcomes
- triggering monetization or payment events

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

Agentic Royalty Path extends this into dynamic path accounting:

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
v0.1 scope

v0.1 introduces the Agentic Royalty Path Core.

It defines:

goal
path layer
action receipts
agent log
path hash chain
monetization event placeholder
audit status
royalty candidate mapping
What this standard does not do

This standard does not create legal royalty claims by itself.

Instead, it records audit-ready evidence that a value-generating agent path occurred.

The royalty_mapping section should be treated as a candidate mapping until reviewed by a human, legal framework, marketplace rule, or external royalty engine.

Repository structure
schemas/
  agentic-royalty-path.schema.json

examples/
  agentic-royalty-path.example.yaml

scripts/
  validate_examples.py
Validate
python scripts/validate_examples.py
Version

Current candidate:

v0.1.0-candidate — Agentic Royalty Path Core
Roadmap
v0.1 — Agentic Royalty Path Core
v0.2 — Monetization Event Extension
v0.3 — Path Royalty Weighting
v0.4 — Provider Bridge Layer
v0.5 — Agent Commerce Audit Bridge

## v0.2 — Monetization Event Extension

v0.2 introduces the Monetization Event Extension.

This extension allows an Agentic Royalty Path to reference external monetization, payment, billing, or paid-access events.

Examples include:

- paid resource access
- API usage billing
- MCP tool payment
- agent commerce transactions
- subscription-based access
- logged free access events

The extension does not define a legal royalty claim by itself.

Instead, it records audit-ready evidence that a value-bearing access or payment event occurred during an AI agent path.

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
Added in v0.2
monetization-event.schema.json
monetization-event.cloudflare-x402.example.yaml
agentic-royalty-path.monetized.example.yaml
validation coverage for monetized path examples

## v0.3 — Path Royalty Weighting

v0.3 introduces Path Royalty Weighting.

This layer maps an AI agent value-generation path into candidate royalty shares.

It does not calculate legally enforceable royalties by itself.  
Instead, it provides an audit-ready candidate weighting record based on path evidence, origin dependency, monetization signals, action receipts, and review status.

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
Added in v0.3
path-royalty-weighting.schema.json
path-royalty-weighting.example.yaml
validation coverage for royalty weighting examples
Scoring factors

v0.3 introduces candidate scoring factors such as:

path_complexity
origin_dependency
action_receipt_confidence
monetization_signal
agent_decision_depth
human_review_depth
reproducibility_score
Royalty candidates

Each royalty candidate includes:

role
beneficiary reference
contribution basis
suggested share
evidence references
audit status
Important note

Path Royalty Weighting records are candidate records.

They do not create legal royalty claims.

Any suggested share must be reviewed by a human, marketplace rule, legal framework, or external royalty engine before payout.
