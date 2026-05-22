# TplQueue

`TplQueue` ist eine `.NET`-Komponentenlinie fuer kontrollierte Queue-Ausfuehrung, retry-orientierte Dispatch-Logik und beobachtergestuetzte Diagnostik rund um nebenlaeufige Arbeit.

Dieser Bereich ist der oeffentliche TplQueue-Dokumentationsknoten auf `fmacias.github.io`.

Startpunkte:

- [Uebersicht](overview.md)
- [Architektur](architecture.md)
- [Erste Schritte](getting-started.md)
- [Oeffentliche Repositories](repositories/index.md)
- [Core Lizenz](core-license.md)

## Oeffentliche Repository-Uebersicht

- [TplQueue.Abstractions](https://github.com/fmacias/TplQueue.Abstractions): oeffentliche Vertraege und gemeinsame Modelle
- [TplQueue.Core](https://github.com/fmacias/TplQueue.Core): Ausfuehrungskern und Queue-Runtime
- [TplQueue.Adapter](https://github.com/fmacias/TplQueue.Adapter): Adapter-Module, Retry-Strategien, Observer, Serializer und die Top-Level-Fassade
- [TplQueue.Usage](https://github.com/fmacias/TplQueue.Usage): oeffentliche Package-Beispiele, Integrationstests und observer-orientierte Validierung

## Warum `TplQueue.Usage` existiert

`TplQueue.Usage` ist die oeffentliche Verifikationsoberflaeche fuer die aktuelle Preview-Paketlinie.

Dort wird gezeigt, wie ein Consumer:

- die veroeffentlichten Pakete referenziert
- Jobs und Job-Roots zusammensetzt
- Queues ueber die oeffentliche Fassade erstellt
- Observer abonniert, ohne auf eingeschraenkte Quellcode-Repositories angewiesen zu sein

Dieses Repository validiert die Paketlinie so, wie eine externe Anwendung sie tatsaechlich verwenden wuerde.
