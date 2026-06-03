# Facit – modul 01 Analys

**Fil:** [data/fastighet-manad.csv](data/fastighet-manad.csv) · valfritt: [data/manadsnotiser.txt](data/manadsnotiser.txt)  
**JSON:** [facit/spine-patterns.json](facit/spine-patterns.json)

## Trender (ska hittas)

| Fastighet | Mönster |
|-----------|---------|
| **Delta** | `energi_kwh` ~**+3 % per månad** jan–aug (10000 → ~12300) |
| **Beta** | `opex_msek` stiger varje månad (2,80 → 3,35) |

## Avvikelser (ska prioriteras)

| Fastighet | Period | Observation |
|-----------|--------|-------------|
| **Alpha** | 2025-06 | `intakt_msek` **12,0** – kommentar **ENGANGSINTAKT LEASE INCENTIVE** |
| **Gamma** | 2025-06 | `energi_kwh` **10800** vs maj **8000** (~+35 %) – ventilation |

## Samband (hypotes – verifiera)

| Fastighet | Observation |
|-----------|-------------|
| **Zeta** | `service_arenden` och `energi_kwh` stiger tillsammans |

## Falskt samband (tillitsdiskussion)

| Fastighet | Observation |
|-----------|-------------|
| **Eta** | `vakans_pct` stiger (2,1 → 4,8) medan `intakt_msek` också stiger – **ny hyresgäst Malmö + index**, inte “vakans = lägre intäkt” |

## Facilitator

- Mål: 2–3 trender, 2–3 avvikelser, minst ett samband på ~5 min.
- Fråga om Eta: *“Föreslog AI orsak–verkan? Stämmer det med kommentarfältet?”*
- “Jag litar på **raden**, inte modellens summering.”
