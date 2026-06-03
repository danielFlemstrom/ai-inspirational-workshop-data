# Facit – modul 08 Power BI

**Fil:** [data/oefning-bi-export.csv](data/oefning-bi-export.csv) (samma spine som modul 01, BI-kolumner)

## Facilitator

- Export = **ögonblicksbild** – samma mönster som `fastighet-manad.csv` (Delta trend, Gamma jun, Alpha jun).
- BI = sanning; AI = tolkning av export.
- Kräv exportdatum/filter i prompten.

## Demo-prompt (kort)

```
context: CSV-export från Power BI, fastighets-KPI jan–aug 2025, fiktiv Acme.
task: Topp 3 observationer per region – trender eller avvikelser.
sources: endast bifogad CSV.
rules: Hänvisa till fastighet och period. Räkna inte om totalsumma.
output_format: tabell
```
