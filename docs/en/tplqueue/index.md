# TplQueue

`TplQueue` is a `.NET` component line for controlled queue execution, retry-oriented dispatch, and observer-driven diagnostics around concurrent work.

This section is the public documentation hub for the TplQueue line on `fmacias.github.io`.

Start with:

- [Overview](overview.md)
- [Architecture](architecture.md)
- [Getting Started](getting-started.md)
- [Public Repositories](repositories/index.md)
- [Core License](core-license.md)

## Public repository map

- [TplQueue.Abstractions](https://github.com/fmacias/TplQueue.Abstractions): public contracts and shared models
- [TplQueue.Core](https://github.com/fmacias/TplQueue.Core): execution kernel and queue runtime
- [TplQueue.Adapter](https://github.com/fmacias/TplQueue.Adapter): adapter modules, retry policies, observers, serializers, and the top-level facade
- [TplQueue.Usage](https://github.com/fmacias/TplQueue.Usage): public package-consumption samples, integration tests, and observer-oriented validation

## Why `TplQueue.Usage` exists

`TplQueue.Usage` is the public verification surface for the preview package line.

It shows how a consumer can:

- reference the published packages
- compose jobs and job roots
- create queues through the public facade
- subscribe observers without depending on restricted source repositories

That repository is where the package line is exercised the way an external application would consume it.
