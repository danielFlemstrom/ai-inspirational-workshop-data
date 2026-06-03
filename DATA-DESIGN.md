# DATA-DESIGN – Acme spine (dag 1)

## Flavor

| | |
|---|---|
| **Aktiv flavor** | `ekonomi` |
| **Kundkontext** | Sagax – fastighetsekonomi |
| **Fiktivt bolag** | Acme Norden AB |

Övningarna i workshop-repot är **domänneutrala i metod** (analys, granskning, jämförelse, …). Data och texter bär ekonomi-skin.

---

## Princip

Datasetet ska vara **pedagogiskt manipulerat**, inte maximalt realistiskt.

> Om gruppen inte hittar 2–3 intressanta saker på 5 minuter är datat för platt.

## Workshopmål som data ska tjäna

1. Identifiera **trender**
2. Identifiera **avvikelser**
3. Resonera kring **möjliga orsaker** (hypotes, inte sanning)
4. **Sammanfatta** till ledning (modul 05)

*(Gäller alla flavors – oberoende av om entity heter fastighet, avdelning eller site.)*

---

## Generisk modell → flavor `ekonomi` (nu)

| Generiskt | Ekonomi (implementerat) | Facility (exempel senare) | HR (exempel senare) |
|-----------|-------------------------|---------------------------|---------------------|
| entity | `fastighet` | `fastighet` / `site` | `avdelning` |
| period | `period` | `period` | `period` |
| metric (intäkt/volym) | `intakt_msek` | `ytka_m2` / `hyresintakt` | `headcount` |
| metric (kostnad) | `opex_msek` | `underhall_ksek` | `sjukfranvaro_dagar` |
| utilization | `vakans_pct` | `belaggning_pct` | `capacity_pct` |
| volume / aktivitet | `energi_kwh`, `service_arenden` | `felanmalningar` | `incidenter` |
| comment | `kommentar` | `kommentar` | `kommentar` |
| aggregation | `region` | `region` | `koncernenhet` |

**Regel:** ändra kolumnnamn vid ny flavor – **behåll** samma planterade mönster (trend, avvikelse, samband, falskt samband).

---

## Spine-filer (flavor ekonomi)

| Fil | Roll |
|-----|------|
| `fastighet-manad.csv` | Huvudkälla – moduler 01–05 |
| `manadsnotiser.txt` | Fritext – förklarar delvis mönster |
| `koncern-manad.csv` | Aggregering – modul 02 |
| `oefning-bi-export.csv` | BI-export – modul 08 |

## Planterade mönster

| # | Typ | Entity | Facit |
|---|-----|--------|-------|
| 1 | Trend | Delta | energi_kwh ~+3 %/mån |
| 2 | Trend | Beta | opex_msek stiger |
| 3 | Avvikelse | Alpha | intakt jun 12,0 – lease incentive |
| 4 | Avvikelse | Gamma | energi jun +35 % |
| 5 | Samband | Zeta | service_arenden + energi upp |
| 6 | Falskt samband | Eta | vakans ↑ och intäkt ↑ |

## Underhåll

- **CSV:** `python scripts/generate-datasets.py`
- **Texter:** redigera i `modul-*/data/` – synka med spine (samma perioder, samma entity-namn)
- **Facit:** `facit.md` + `facit/spine-patterns.json`
- **Ny flavor:** se [DATA-POLICY.md](DATA-POLICY.md) § Domänportabilitet
