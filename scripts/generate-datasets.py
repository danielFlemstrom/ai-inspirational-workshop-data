#!/usr/bin/env python3
"""Generate synthetic CSVs into this repo (Day-01 / Day-02 modul folders).

    python scripts/generate-datasets.py

Static text files (warmup, emails, manadsnotiser, …) are hand-maintained.
Facit: modul-*/facit.md or facit/*.json – see DATA-POLICY.md.

Day-1 spine: fastighet-manad.csv (pedagogiskt planterade trender, avvikelser,
samband och ett falskt samband). Se DATA-DESIGN.md.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAY1 = ROOT / "Day-01"
DAY2 = ROOT / "Day-02"

PERIODS = [f"2025-{m:02d}" for m in range(1, 9)]


def write_csv(path: Path, header: list[str], rows: list[list]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def _period_rows(
    fastighet: str,
    region: str,
    intakt: list[float],
    opex: list[float],
    vakans: list[float],
    energi: list[int],
    service: list[int],
    kommentarer: list[str],
) -> list[list]:
    assert len(PERIODS) == len(intakt) == len(opex) == len(vakans) == len(energi) == len(service) == len(kommentarer)
    return [
        [
            fastighet,
            region,
            PERIODS[i],
            intakt[i],
            opex[i],
            vakans[i],
            energi[i],
            service[i],
            kommentarer[i],
        ]
        for i in range(len(PERIODS))
    ]


def tier_s_fastighet_manad() -> list[list]:
    """Acme spine – 7 fastigheter × 8 månader (tier S)."""
    rows: list[list] = []

    # Alpha – engångsintäkt jun
    rows += _period_rows(
        "Alpha",
        "Norden",
        [4.2, 4.3, 4.1, 4.4, 4.5, 12.0, 4.6, 4.5],
        [3.2, 3.2, 3.1, 3.2, 3.2, 3.3, 3.2, 3.2],
        [1.5, 1.5, 1.4, 1.5, 1.5, 1.5, 1.4, 1.5],
        [9500] * 8,
        [1, 1, 2, 1, 2, 1, 1, 2],
        ["", "", "", "", "", "ENGANGSINTAKT LEASE INCENTIVE", "", ""],
    )

    # Beta – stigande underhåll/OPEX
    rows += _period_rows(
        "Beta",
        "Norden",
        [3.5, 3.5, 3.4, 3.5, 3.5, 3.5, 3.6, 3.5],
        [2.80, 2.85, 2.90, 2.95, 3.05, 3.15, 3.25, 3.35],
        [2.0, 2.0, 2.1, 2.0, 2.0, 2.0, 2.1, 2.0],
        [7100, 7150, 7200, 7250, 7300, 7350, 7400, 7450],
        [2, 2, 3, 3, 4, 4, 5, 5],
        ["", "", "PLANERAT TAKUNDERHALL", "", "", "", "", "UNDERHALL KLART"],
    )

    # Delta – energi +3 % per månad (tydlig trend)
    delta_energi = [round(10000 * (1.03**i)) for i in range(8)]
    rows += _period_rows(
        "Delta",
        "Norden",
        [5.0, 5.0, 5.1, 5.0, 5.1, 5.0, 5.1, 5.0],
        [3.8, 3.9, 4.0, 4.0, 4.1, 4.2, 4.3, 4.4],
        [1.8, 1.8, 1.7, 1.8, 1.8, 1.8, 1.7, 1.8],
        delta_energi,
        [1, 1, 2, 2, 2, 3, 3, 3],
        ["", "", "ENERGI UPPTREND", "", "", "", "", ""],
    )

    # Gamma – energispike jun (+35 % mot maj)
    rows += _period_rows(
        "Gamma",
        "Norden",
        [2.8, 2.8, 2.9, 2.8, 2.9, 2.8, 2.9, 2.8],
        [2.1, 2.1, 2.2, 2.1, 2.2, 2.3, 2.2, 2.1],
        [3.2, 3.1, 3.0, 3.1, 3.0, 3.2, 3.1, 3.0],
        [7800, 7900, 8000, 8100, 8000, 10800, 8200, 8100],
        [2, 2, 3, 3, 4, 8, 3, 2],
        ["", "", "", "", "", "FELANMALNING VENTILATION", "", ""],
    )

    # Epsilon – stabil baseline Syd
    rows += _period_rows(
        "Epsilon",
        "Syd",
        [2.8, 2.8, 2.9, 2.8, 2.8, 2.9, 2.8, 2.8],
        [2.2, 2.2, 2.2, 2.3, 2.2, 2.2, 2.3, 2.2],
        [2.4, 2.4, 2.3, 2.4, 2.4, 2.4, 2.3, 2.4],
        [6000, 6050, 6100, 6080, 6120, 6100, 6080, 6100],
        [1, 1, 1, 2, 1, 1, 1, 1],
        [""] * 8,
    )

    # Zeta – serviceärenden ↑ → energi ↑ (riktigt samband)
    rows += _period_rows(
        "Zeta",
        "Syd",
        [2.6, 2.6, 2.7, 2.6, 2.7, 2.7, 2.8, 2.8],
        [2.0, 2.0, 2.1, 2.1, 2.2, 2.3, 2.4, 2.5],
        [2.5, 2.5, 2.4, 2.5, 2.5, 2.5, 2.4, 2.5],
        [6200, 6250, 6300, 6500, 6800, 7200, 7800, 8400],
        [1, 1, 2, 4, 7, 10, 14, 18],
        ["", "", "", "FLER SERVICEARENDEN", "", "KYLA/VENTILATION", "", ""],
    )

    # Eta – falskt samband: vakans ↑ men intäkt ↑ (ny hyresgäst + index)
    rows += _period_rows(
        "Eta",
        "Syd",
        [3.1, 3.1, 3.2, 3.4, 3.5, 3.8, 4.0, 4.1],
        [2.3, 2.3, 2.4, 2.4, 2.5, 2.5, 2.6, 2.6],
        [2.1, 2.3, 2.8, 3.2, 3.8, 4.2, 4.5, 4.8],
        [6400, 6450, 6500, 6550, 6600, 6650, 6700, 6750],
        [1, 2, 2, 2, 3, 3, 3, 2],
        ["", "NY HYRESGAST MALMO", "", "", "", "", "INDEXJUSTERING HYRA", ""],
    )

    header = [
        "fastighet",
        "region",
        "period",
        "intakt_msek",
        "opex_msek",
        "vakans_pct",
        "energi_kwh",
        "service_arenden",
        "kommentar",
    ]
    out = DAY1 / "modul-01-analys/data/fastighet-manad.csv"
    write_csv(out, header, rows)
    return rows


def tier_s_koncern_manad(fastighet_rows: list[list]) -> None:
    """Aggregera spine till region × månad (bilaga i granskning)."""
    agg: dict[tuple[str, str], dict[str, float]] = {}
    for row in fastighet_rows:
        region, period = row[1], row[2]
        key = (region, period)
        if key not in agg:
            agg[key] = {"intakt": 0.0, "opex": 0.0, "vakans_sum": 0.0, "n": 0}
        agg[key]["intakt"] += float(row[3])
        agg[key]["opex"] += float(row[4])
        agg[key]["vakans_sum"] += float(row[5])
        agg[key]["n"] += 1

    header = ["region", "period", "intakt_msek", "opex_msek", "vakans_pct_snitt", "kommentar"]
    rows = []
    for region in ("Norden", "Syd"):
        for period in PERIODS:
            key = (region, period)
            if key not in agg:
                continue
            a = agg[key]
            kommentar = ""
            if region == "Norden" and period == "2025-06":
                kommentar = "ALPHA LEASE INCENTIVE"
            rows.append(
                [
                    region,
                    period,
                    round(a["intakt"], 1),
                    round(a["opex"], 1),
                    round(a["vakans_sum"] / a["n"], 1),
                    kommentar,
                ]
            )
    write_csv(DAY1 / "modul-02-granskning/data/koncern-manad.csv", header, rows)


def tier_s_pbi_export(fastighet_rows: list[list]) -> None:
    """BI-export för modul 08 – samma spine, PBI-vänliga kolumner."""
    header = [
        "fastighet",
        "region",
        "period",
        "intakt_msek",
        "opex_msek",
        "vakans_pct",
        "energi_kwh",
    ]
    rows = [[row[0], row[1], row[2], row[3], row[4], row[5], row[6]] for row in fastighet_rows]
    write_csv(DAY1 / "modul-08-power-bi/data/exercise-bi-export.csv", header, rows)


def tier_s_facit_json(fastighet_rows: list[list]) -> None:
    """Maskinläsbart facit för spine-mönster."""
    meta = {
        "tier": "S",
        "flavor": "ekonomi",
        "fil": "fastighet-manad.csv",
        "rader": len(fastighet_rows),
        "monster": {
            "trend_energi_delta": {
                "fastighet": "Delta",
                "beskrivning": "energi_kwh ~+3 % per månad jan–aug",
            },
            "avvikelse_energi_gamma": {
                "fastighet": "Gamma",
                "period": "2025-06",
                "beskrivning": "energi +35 % mot maj (10800 vs 8000)",
            },
            "avvikelse_intakt_alpha": {
                "fastighet": "Alpha",
                "period": "2025-06",
                "intakt_msek": 12.0,
                "kommentar": "ENGANGSINTAKT LEASE INCENTIVE",
            },
            "trend_opex_beta": {
                "fastighet": "Beta",
                "beskrivning": "opex_msek stiger varje månad",
            },
            "samband_zeta": {
                "fastighet": "Zeta",
                "beskrivning": "service_arenden och energi_kwh stiger tillsammans",
            },
            "falskt_samband_eta": {
                "fastighet": "Eta",
                "beskrivning": "vakans_pct stiger medan intakt_msek också stiger – ny hyresgäst/index, inte orsakverkan",
                "diskussion": "AI kan felaktigt skylla intäktsuppgång på vakans eller tvärtom",
            },
        },
    }
    facit_dir = DAY1 / "modul-01-analys/facit"
    facit_dir.mkdir(parents=True, exist_ok=True)
    (facit_dir / "spine-patterns.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def tier_m_leases() -> None:
    header = ["lease_id", "property", "region", "rent_ksek", "status"]
    rows = []
    for i in range(60):
        rows.append(
            [
                f"L-{i+1:04d}",
                f"Lager-{i+1:03d}",
                "Norden" if i % 2 == 0 else "Syd",
                120 + (i % 7) * 3,
                "active",
            ]
        )
    for i in range(60):
        rows.append(
            [
                f"L-{i+61:04d}",
                f"Kontor-{i+1:03d}",
                "Norden" if i < 30 else "Syd",
                85 + (i % 5),
                "active",
            ]
        )
    write_csv(DAY2 / "modul-21-rorig-data/data/medium-leases-120r.csv", header, rows)


def tier_l_sampling_trap() -> None:
    header = ["txn_id", "region", "amount_ksek", "type", "flag"]
    rows = []
    for i in range(1, 601):
        region = "Norden" if i % 3 else "Syd"
        amount = round(10 + (i % 17) * 0.7, 2)
        typ = "rent"
        flag = ""
        if i == 512:
            amount = 999.99
            typ = "adjustment"
            flag = "RECON_EXCEPTION_Q2"
        rows.append([f"T-{i:05d}", region, amount, typ, flag])
    out = DAY2 / "modul-21-rorig-data/data/sampling-trap-600r.csv"
    write_csv(out, header, rows)
    meta = {
        "tier": "L",
        "rows": 600,
        "facit_row": 512,
        "facit_flag": "RECON_EXCEPTION_Q2",
        "facit_amount": 999.99,
    }
    facit_dir = DAY2 / "modul-21-rorig-data/facit"
    facit_dir.mkdir(parents=True, exist_ok=True)
    (facit_dir / "sampling-trap-600r.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def main() -> None:
    fastighet = tier_s_fastighet_manad()
    tier_s_koncern_manad(fastighet)
    tier_s_pbi_export(fastighet)
    tier_s_facit_json(fastighet)
    tier_m_leases()
    tier_l_sampling_trap()
    # Legacy – ta bort om den finns kvar
    legacy = DAY1 / "modul-01-analys/data/manadsresultat.csv"
    if legacy.exists():
        legacy.unlink()
    print("OK: Day-01 spine (fastighet-manad, koncern-manad, PBI-export)")
    print("OK: Day-02 modul-21 CSVs")


if __name__ == "__main__":
    main()
