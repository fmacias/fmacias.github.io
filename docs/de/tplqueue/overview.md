# Uebersicht

`TplQueue` ist bewusst in Vertraege, Runtime, Adapter und oeffentliche Consumer-Beispiele aufgeteilt.

## Oeffentliche Struktur

- `TplQueue.Abstractions`
  Oeffentliche Vertraege und gemeinsame Modelle.
- `TplQueue.Adapter`
  Retry-Strategien, Observer, Serializer, DI-Integration und die Top-Level-Fassade.
- `TplQueue.Usage`
  Kanonische ausfuehrbare Consumer-Beispiele und package-basierte Verifikation.

## Eingeschraenkte Struktur

- `TplQueue.Core`
  Ausfuehrungskern und Queue-Runtime. Das Paket ist oeffentlich, das Repository wird hier aber nicht roh importiert.

## Oeffentliche Dokumentationspolitik

Die Site stellt bereit:

- kuratierte oeffentliche Seiten fuer die gesamte TplQueue-Linie
- buildzeitigen Import der Dokumentation aus den oeffentlichen Repositories
- kuratierte Lizenz- und Zugriffsinformationen fuer `TplQueue.Core`
