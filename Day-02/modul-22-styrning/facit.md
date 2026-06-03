# Facit – modul 22 Styrning

**Fil:** [medium-leases-120r.csv](../modul-21-rorig-data/data/medium-leases-120r.csv) (tier M, 120 datarader)

## Steg 1 – Inventering

| Fält | Facit |
|------|-------|
| Antal datarader | **120** |
| Kolumner | lease_id, property, region, rent_ksek, status |
| Unika region | **2** (Norden, Syd) |

## Steg 2 – Aggregering

| region | antal_kontrakt | Kommentar |
|--------|----------------|-----------|
| Norden | **60** | 30 Lager (jämna i) + 30 Kontor (i under 30) |
| Syd | **60** | 30 Lager (udda i) + 30 Kontor (i från 30) |

`summa_rent_ksek`: låt deltagare räkna i Excel – AI ska vara **nära**; avvikelse över 5 % → stoppa steg 3.

## Steg 3 – Hypotes

Inget facit-rätt svar – poängen är **spårbarhet** (property + region + osäkerhet), inga nya totalsummor.

## Facilitator

- Om steg 1 ≠ 120 → “därför radantal före analys” (koppla 2.1).  
- Om steg 3 körs med CSV bifogad → kedjan ogiltig – visa risk.  
- **Varför:** fel i steg 3 kommer från fel steg 2, inte “dålig slutprompt”.
