# Erste Schritte

Installiere die benoetigten Pakete:

```bash
dotnet add package Fmacias.TplQueue --version 0.1.0-preview.1
dotnet add package Fmacias.TplQueue.Core --version 0.1.0-preview.1
```

`TplQueue.Core` wird unter eigenen Paket-Lizenzbedingungen verteilt und verlangt derzeit Lizenzakzeptanz.

## Minimale Komposition

Die kleinste oeffentliche Komposition sieht so aus:

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

## Kanonische ausfuehrbare Beispiele

Die vollstaendigen lauffaehigen Implementierungen liegen in `TplQueue.Usage`:

- [Oeffentliche Repository-Uebersicht](repositories/usage.md)
