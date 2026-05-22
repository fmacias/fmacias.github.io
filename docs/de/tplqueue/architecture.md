# Architektur

Die TplQueue-Linie ist um eine klare Grenze zwischen Vertraegen, Runtime, Integrationen und Consumer-Verifikation aufgebaut.

## Schichten

### Vertraege

`TplQueue.Abstractions` definiert die gemeinsame Oberflaeche:

- `IJob`, `IJobRoot`
- `IDataJob`, `IDataJobRoot`
- `IQ`, `IParallelQ`, `IFifoQ`, `ICacheQ`
- `IObservable<IJobEvent>`

### Runtime

`TplQueue.Core` besitzt:

- Job-Graph-Ausfuehrung
- Queue-Dispatch-Semantik
- Retry-Policy-Auswahlpunkte
- Observer-Event-Publikation

### Integrationen

`TplQueue.Adapter` ergaenzt:

- `API`-Fassadenkomposition
- konkrete Retry-Strategien
- Observer
- Serializer
- Cache-Module
- Microsoft-DI-Unterstuetzung

### Consumer-Verifikation

`TplQueue.Usage` prueft die Paketlinie von aussen ueber ausfuehrbare Beispiele und package-basierte Integrationstests.
