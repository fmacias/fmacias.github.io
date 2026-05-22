# Overview

`TplQueue` is split intentionally into contracts, runtime, adapters, and consumer-facing usage material.

## Public structure

- `TplQueue.Abstractions`
  Public contracts and shared models.
- `TplQueue.Adapter`
  Retry policies, observers, serializers, DI integration, and the top-level facade.
- `TplQueue.Usage`
  Canonical runnable consumer samples and package-based verification.

## Restricted structure

- `TplQueue.Core`
  Execution kernel and queue runtime. The package is public, but the repository itself is not part of the public documentation import path.

## Public documentation policy

The site exposes:

- curated public pages for the full TplQueue line
- build-time imported documentation for the public repositories
- curated public/license guidance for `TplQueue.Core`

For runnable examples, `TplQueue.Usage` is the canonical source:

- `PackageConsumptionSmokeConsole`
- `QueueObserverConsole`
- `QueueObserverSignalRDashboard`
