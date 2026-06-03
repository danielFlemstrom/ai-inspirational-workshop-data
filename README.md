# ai-inspirational-workshop-data

Fiktiv **Acme Norden AB** – övningsdata, facit och generator för [ai-inspirational-workshop](../ai-inspirational-workshop/).

---

## Clone

**Rekommenderat:** syskon till workshop-repot under samma container:

```text
ai-ws/
  ai-inspirational-workshop/        # facilitator + övningar
  ai-inspirational-workshop-data/   # detta repo
```

```bash
mkdir ai-ws && cd ai-ws
git clone git@github.com:danielFlemstrom/ai-inspirational-workshop.git
git clone git@github.com:danielFlemstrom/ai-inspirational-workshop-data.git
```

**Deltagare:** clone detta repo och följ `exercise.md` i workshop-repot.

---

## Innehåll

| | |
|---|---|
| **Data** | `Day-NN/modul-NN-namn/data/` |
| **Facit (facilitator)** | `Day-NN/modul-NN-namn/facit.md` (+ ev. `facit/*.json`) |
| **Katalog** | [DATA-CATALOG.md](DATA-CATALOG.md) · [DATA-DESIGN.md](DATA-DESIGN.md) |
| **Policy** | [DATA-POLICY.md](DATA-POLICY.md) |

---

## Generera CSV

```bash
python scripts/generate-datasets.py
```

Skapar/uppdaterar `fastighet-manad.csv`, `koncern-manad.csv`, PBI-export samt Day-02 CSV/facit.

Övriga texter (mail, rapport, kommentarer) redigeras direkt i respektive `data/`-mapp.

---

## Licens

CC0 – se [LICENSE](LICENSE). All data är fiktiv.
