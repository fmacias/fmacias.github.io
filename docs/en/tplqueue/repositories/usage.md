# TplQueue.Usage

`TplQueue.Usage` is the canonical public consumer-facing sample and verification repository.

## Key responsibility

- package-consumption samples
- package-based integration tests
- observer-facing DTO projection examples
- release-smoke consumer scenarios

## Imported documentation

- [Repository landing page](../reference/usage/index.md)
- [Repository docs index](../reference/usage/docs/index.md)
- [PackageConsumptionSmokeConsole README](../reference/usage/samples/PackageConsumptionSmokeConsole/README.md)
- [QueueObserverConsole README](../reference/usage/samples/QueueObserverConsole/README.md)
- [QueueObserverSignalRDashboard README](../reference/usage/samples/QueueObserverSignalRDashboard/README.md)

## Why this repository matters

The product repositories now use `TplQueue.Usage` as the canonical source for runnable snippets. The full samples stay there, while the product docs keep only the small issue-specific excerpts that explain a focused API concern.

## Public install path

The published preview packages are consumable from `nuget.org`. The imported `TplQueue.Usage` development and operations pages still document the sibling `..\TplQueue.NugetLocal` feed for maintainers working inside the product workspace, but that local feed is not required for normal public package consumption.
