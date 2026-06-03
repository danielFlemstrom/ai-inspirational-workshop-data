# Datakatalog

Fiktiv **Acme Norden AB**. **Flavor:** `ekonomi`. Se [DATA-POLICY.md](DATA-POLICY.md) · [DATA-DESIGN.md](DATA-DESIGN.md).

## Dag 1 – Acme spine (tier S)

**Huvudfil:** `modul-01-analys/data/fastighet-manad.csv` (7 fastigheter × 8 månader)  
**Notiser:** `modul-01-analys/data/manadsnotiser.txt`  
**Aggregerat:** `modul-02-granskning/data/koncern-manad.csv`  
**PBI-export:** `modul-08-power-bi/data/exercise-bi-export.csv`

| Modul | Fil(er) | Innehåll | Tier |
|-------|---------|----------|------|
| 00 Intro | `warmup-text.txt` | Intern Q2-notis, spine-sammanfattning | S |
| 01 Analys | `fastighet-manad.csv`, `manadsnotiser.txt` | Fastighets-KPI jan–aug 2025 | S |
| 02 Granskning | `rapportutdrag.txt`, `checklista.md`, `koncern-manad.csv` | Commentary + bilaga | S |
| 03 Jämförelse | `kommentar-q2.txt`, `kommentar-q3.txt` | Q2 vs Q3 2025 | S |
| 04 Strukturering | `email-ostrukturerad.txt` | E-post indexuppräkning | S |
| 05 Generering | `bullets-in.txt` | Bullets Q2 från spine | S |
| 06 Quick wins | `quick-win-mall.md` | Mall | — |
| 07 Context | `demo.json` (TODO) | Capstone | — |
| 08 Power BI | `exercise-bi-export.csv` | BI-export (spine) | S |

### Planterade mönster (facit)

| Typ | Exempel |
|-----|---------|
| Trend | Delta energi +3 %/mån, Beta OPEX upp |
| Avvikelse | Alpha jun intäkt, Gamma jun energi |
| Samband | Zeta service → energi |
| Falskt samband | Eta vakans ↑ + intäkt ↑ |

Facit: `modul-01-analys/facit.md` · `modul-01-analys/facit/spine-patterns.json`

## Dag 2 (tier M/L)

| Modul | Fil | Innehåll | Tier |
|-------|-----|----------|------|
| 21 | `medium-leases-120r.csv` | Hyreskontrakt (lease_id, property, region, rent_ksek, status) | M |
| 21 | `sampling-trap-600r.csv` | Transaktioner, outlier rad 512 RECON_EXCEPTION_Q2 | L |
| 22 | *(delar modul-21)* `medium-leases-120r.csv` | Stegvis styrning – samma M-fil | M |
| 23 | `case-brief-acme-cfo.md` | CFO-brief (fiktiv) | — |
| 23 | *(länk dag 1)* `modul-08-power-bi/data/exercise-bi-export.csv` | Standard BI-export för kundcase | S |
| 24 | `prompt-spar-mall.md` | Sparad prompt + metadata | — |
| 24 | *(länk dag 1)* `modul-06-quick-wins/data/quick-win-mall.md` | Koppling quick wins | — |

**Facit dag 2:**

| Modul | Facit |
|-------|-------|
| 21 | `modul-21-rorig-data/facit.md` · `facit/sampling-trap-600r.json` |
| 22 | `modul-22-styrning/facit.md` |
| 23 | `modul-23-kundcase/facit.md` |

### Beslut: kaos-xlsx (D2-B6)

`07-kaos-delvis.xlsx` är **inte** genererad. Format- och längd-demo sker via **CSV tier M** (`medium-leases-120r.csv`). Om xlsx behövs senare: lägg i modul-21 och uppdatera denna katalog.

---

**Regenerera CSV:** `python scripts/generate-datasets.py`
