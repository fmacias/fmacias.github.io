# Architecture

The TplQueue line is organized around a strict boundary between public contracts, execution runtime, integration modules, and external consumer samples.

## Layers

### Contracts

`TplQueue.Abstractions` defines the shared surface:

- `IJob`, `IJobRoot`
- `IDataJob`, `IDataJobRoot`
- `IQ`, `IParallelQ`, `IFifoQ`, `ICacheQ`
- `IObservable<IJobEvent>`

### Runtime

`TplQueue.Core` owns:

- job graph execution
- queue dispatch semantics
- retry-policy selection points
- observer event publication

### Integrations

`TplQueue.Adapter` adds:

- `API` facade composition
- concrete retry policies
- observers
- serializers
- cache modules
- Microsoft DI support

### Consumer validation

`TplQueue.Usage` proves the package line from the outside through runnable sample applications and package-based integration tests.

## Public/private boundary

The public site can import documentation from `TplQueue.Abstractions`, `TplQueue.Adapter`, and `TplQueue.Usage` because those repositories are public.

`TplQueue.Core` is documented here through curated public pages instead of raw repository import. That keeps internal implementation detail private while still exposing package, architecture, and licensing information.
