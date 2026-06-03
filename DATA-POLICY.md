# Policy – övningsdata

Detta repo (**ai-inspirational-workshop-data**) är **enda källa** för fiktiv övningsdata och facit.  
Workshop-repot (`ai-inspirational-workshop/`) innehåller facilitator, övningar, PLAN – **ingen datafiler**.  
**Styrning workshop:** [content-policy.md](../ai-inspirational-workshop/admin/content-policy.md) (chain of command + målgrupper).

---

## Katalogstruktur

```
Day-NN/
  modul-NN-namn/
    data/           # deltagare + övningar (publikt)
    facit.md        # facilitator (förklaring, nycklar)
    facit/          # valfritt: JSON för genererade dataset
scripts/
  generate-datasets.py
DATA-CATALOG.md
```

**Modulnamn** ska matcha workshop-repot (`modul-01-analys`, …).

---

## Tiers

| Tier | Storlek | Användning |
|------|---------|------------|
| **S** | Små filer (~≤20 rader) | Dag 1 – “snäll” AI |
| **M** | ~120 rader | Dag 2 intro |
| **L** | ~600 rader | Dag 2 sampling-demo |

---

## Facit

| Typ | Var | Målgrupp |
|-----|-----|----------|
| **facit.md** | `modul-NN/facit.md` | **Workshopledare** – diskussion, nycklar |
| **facit/*.json** | Maskinläsbart | Workshopledare + scripts |
| **data/** | `modul-NN/data/` | **Deltagare** – bifogas i ChatGPT |

**Deltagare** ska inte få facit i standardpaket (vid zip/release: bara `data/`, eller tydlig märkning “endast facilitator”).

`exercise.md` i workshop-repot länkar **endast** till `data/`. Facit länkas från `facilitator.md`.

---

## Generera vs handunderhåll

| Innehåll | Hur |
|----------|-----|
| CSV (fastighet-manad, koncern-manad, PBI-export, leases, sampling) | `python scripts/generate-datasets.py` |
| Texter (mail, rapport, kommentarer) | Redigera filer i `data/` direkt |
| Ny modul | Skapa `Day-NN/modul-XX/data/` + uppdatera DATA-CATALOG.md + workshop `exercise.md` |

Efter ändring: commit **detta repo** först, sedan uppdatera länkar i workshop om paths ändrats.

---

## Fiktiv data

All data gäller **Acme Norden AB** (fiktiv). CC0 – se [LICENSE](LICENSE).  
Ingen koppling till verkliga bolag.

---

## Clone-layout (utveckling)

Repona ligger syskon under samma container (t.ex. `ai-ws/`):

```
ai-ws/
  ai-inspirational-workshop/        # workshop
  ai-inspirational-workshop-data/   # detta repo
```

Från `ai-inspirational-workshop/workshop/Day-01/modul-01-analys/exercise.md`:

`../../../../ai-inspirational-workshop-data/Day-01/modul-01-analys/data/...`

(fyra nivåer upp till `ai-ws/`, sedan in i data-repot)

---

## Deltagare

Publicera **detta repo** (eller release zip med `Day-*/modul-*/data/`).  
Deltagare clone + bifogar filer i ChatGPT Corporate enligt `exercise.md` i workshop-repot.

---

## Domänportabilitet (flavors)

Kursen ska vara **domänportabel**. Målet är inte att lära ut redovisning eller facility management i sig, utan **praktiska AI-arbetssätt**: prompting, filanalys, trender, avvikelser, sammanfattning, källmedvetenhet och kritisk granskning.

**Nuvarande flavor:** `ekonomi` (Acme Norden – fastighetsekonomi, första kund Sagax).  
**Senare (ej implementerat):** t.ex. `facility`, `hr`, `projekt` – samma övningsmönster, andra etiketter och exempeldata.

Se [DATA-DESIGN.md](DATA-DESIGN.md). **Språk & målgrupper:** [content-policy.md](../ai-inspirational-workshop/admin/content-policy.md).

### Regler vid generering och ändring av data

1. **Återanvändbar struktur** – bygg på generiska begrepp där det går:
   `entity`, `period`, `metric`, `variance`, `comment`, `category`, `risk`.

2. **Flavor = skin, inte kärna** – dagens CSV (`fastighet`, `intakt_msek`, …) är **ekonomi-skin** ovanpå samma övningslogik som senare kan heta `avdelning`, `kostnad`, `incidenter`, osv.

3. **Pedagogisk signal före realism** – varje dataset ska innehålla upptäckbara mönster:
   - 2–3 tydliga trender
   - 2–3 meningsfulla avvikelser
   - minst ett plausible samband
   - minst ett **vilseledande eller falskt** samband
   - korta fritextkommentarer som förklarar *några*, men inte alla, mönster

4. **Undvik överspecialiserad domänlogik** – övningarna får inte bero på IFRS, kontoplan, avancerade redovisningsregler eller branschjargong om det inte uttryckligen efterfrågas för den flavor som byggs.

5. **Designa för ledningsinsikt** – data ska stödja prompts som:
   - vilka avvikelser är viktigast?
   - sammanfatta trender för ledning
   - föreslå möjliga orsaker (hypotes)
   - skilja fakta från hypotes
   - lista vad som måste verifieras före beslut

6. **Bevara återanvändning** – nya fält ska kunna mappas till andra domäner, t.ex.:
   `cost`, `volume`, `utilization`, `incidents`, `satisfaction`, `capacity`, `forecast`, `actual`, `comment`.

7. **Optimera för 5-minuters-workshop** – inte perfekt realism. Deltagare ska hitta något användbart snabbt.

### Ny flavor (senare)

```
Day-NN/
  flavor-ekonomi/     # eller metadata + undermapp per flavor
  flavor-facility/
```

**Idag:** all dag-1-data under befintliga `modul-*/data/` = flavor `ekonomi`.  
**Vid ny flavor:** kopiera övningsmönster + generator, byt etiketter och facit – **ändra inte** prompt-progression eller modulnummer i workshop-repot i onödan.

