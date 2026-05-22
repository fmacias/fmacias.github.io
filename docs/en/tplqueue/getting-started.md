# Getting Started

Install the packages you need:

```bash
dotnet add package Fmacias.TplQueue --version 0.1.0-preview.1
dotnet add package Fmacias.TplQueue.Core --version 0.1.0-preview.1
```

These commands target the published preview packages on `nuget.org`. No workspace-local package feed is required for the normal public consumer path.

`TplQueue.Core` is distributed under package-specific license terms and currently requires license acceptance.

## Minimal composition

The smallest useful public composition looks like this:

```csharp
var api = API.Create(CoreApi.Create(), retryPolicies, dispatchers);

IJob extract = api.JobFactory.Job(
    ct => Task.CompletedTask,
    name: "Extract");

IJobRoot load = api.JobFactory.JobRoot(
    ct => Task.CompletedTask,
    name: "Load");

load.After(extract);

using IParallelQ queue = api.QFactory.Parallel(
    Guid.NewGuid(),
    "main",
    maxParallelism: 1,
    queueLogger);

queue.Enqueue(load, CancellationToken.None);
await queue.Wait().ConfigureAwait(false);
```

## Canonical runnable examples

Use `TplQueue.Usage` for the full runnable implementations:

- [Usage repository overview](repositories/usage.md)
