"""Generate the Hercher/Diophantine comparison table for m=92..200.

This is numerical evidence for gap G-min-element-lower in
research/backward/no-nontrivial-cycle.md; it is not a proof of cycle
exclusion.  The source table actually bounds K, the number of odd members,
not the minimum element x_min.  Accordingly H(m) below is labelled
H_K(m): the exact integer lower bound on K supplied by Hercher Corollary 24.
The requested name H(m) is retained as an alias for this table quantity.

Source (final published JIS version), Corollary 24, Table 1:
research/sources/hercher-2023-no-collatz-m-cycles-jis-published.full.md
lines 1188-1212:
  m <= 98       : K > 7.76 * 10^19  (line 1190)
  m <= 117      : K > 2.74 * 10^19  (line 1192)
  m <= 276      : K > 4.68 * 10^18  (line 1194)
  m <= 3079     : K > 3.97 * 10^17  (line 1196)
  m <= 12055    : K > 1.30 * 10^17  (line 1198)
  ...
  m <= 948987   : K > 4.30 * 10^15  (line 1200)
  m <= 1.14e6   : K > 3.81 * 10^15  (line 1202)
  ...
  m <= 1.33e9   : K > 1.64 * 10^12  (line 1204)
  m <= 1.54e9   : K > 8.90 * 10^11  (line 1206)
  m <= 9.46e9   : K > 1.37 * 10^11  (line 1208)
  all m         : K > 7.20 * 10^10  (line 1210)

For 92 <= m <= 200 only the first two rows apply. Decimal scientific
notation in the source is converted to exact integers here.

The logarithms use Python float arithmetic deliberately, and are labelled
numerical evidence.  The symbolic expression is
log10(3*log(2)) - log10(c_0) + 8.616*log10(m), with c_0 left symbolic.
"""
from __future__ import annotations

import math
from pathlib import Path

# Exact integer bounds from the published source, not rounded floats.
# See source lines cited in the module docstring.
HERCHER_ROWS: tuple[tuple[int, int, int], ...] = (
    (98, 77600000000000000000, 1190),
    (117, 27400000000000000000, 1192),
    (276, 4680000000000000000, 1194),
    (3079, 397000000000000000, 1196),
    (12055, 130000000000000000, 1198),
    (948987, 4300000000000000, 1200),
    (1140000, 3810000000000000, 1202),
    (1330000000, 1640000000000, 1204),
    (1540000000, 890000000000, 1206),
    (9460000000, 137000000000, 1208),
)
MU = 8.616
START_M = 92
END_M = 200
SOURCE = "research/sources/hercher-2023-no-collatz-m-cycles-jis-published.full.md"


def hercher_bound(m: int) -> tuple[int, int]:
    """Return (exact K lower bound, source line) for a given m."""
    for upper_m, bound, line in HERCHER_ROWS:
        if m <= upper_m:
            return bound, line
    # The all-m row (line 1210) would apply beyond the displayed rows.
    return 72000000000, 1210


def log_values(m: int, h: int) -> tuple[str, float, float]:
    """Return symbolic log threshold, c0=1 log threshold, and deficit.

    Float results are numerical evidence only.  H is exact before conversion
    to float for the logarithm.
    """
    symbolic = (
        "log10(3*log2) - log10(c_0) + 8.616*log10(m)"
    )
    log_threshold_c0_1 = math.log10(3.0 * math.log(2.0)) + MU * math.log10(m)
    deficit = log_threshold_c0_1 - math.log10(h)
    return symbolic, log_threshold_c0_1, deficit


def make_rows() -> list[tuple[int, int, int, str, float, float]]:
    """Build rows (m, H_K, source line, symbolic expression, log10 threshold, deficit)."""
    rows = []
    for m in range(START_M, END_M + 1):
        h, line = hercher_bound(m)
        symbolic, threshold, deficit = log_values(m, h)
        rows.append((m, h, line, symbolic, threshold, deficit))
    return rows


def render(rows: list[tuple[int, int, int, str, float, float]]) -> str:
    """Render the complete, source-cited table as text."""
    lines = [
        "Hercher/Diophantine collision comparison, m=92..200",
        f"Source: {SOURCE}, Corollary 24 Table 1, lines 1188-1212",
        "H(m) is the exact Hercher lower bound on K (odd members), not x_min.",
        "Float columns are numerical evidence; c_0 is symbolic in the formula.",
        "",
        "m | H(m)=H_K(m) exact | source line | log10(threshold) symbolic | "
        "log10(threshold), c0=1 | deficit",
        "-" * 130,
    ]
    for m, h, line, symbolic, threshold, deficit in rows:
        lines.append(
            f"{m:3d} | {h:>20d} | {line:11d} | {symbolic:62s} | "
            f"{threshold: .12f} | {deficit: .12f}"
        )
    deficits = [row[5] for row in rows]
    lines.extend(
        [
            "",
            f"min deficit = {min(deficits):.12f} (at m={rows[deficits.index(min(deficits))][0]})",
            f"max deficit = {max(deficits):.12f} (at m={rows[deficits.index(max(deficits))][0]})",
            "Trend over m=92..200: deficit grows strictly with m. Within a constant-H "
            "interval log10(threshold) increases as 8.616*log10(m), and at the table "
            "step 116 -> 117 H drops from 7.76e19 to 2.74e19 so log10(H) falls and the "
            "deficit jumps up again. Min deficit -2.6519 at m=92, max +1.4734 at m=200.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = make_rows()
    text = render(rows)
    output = Path(__file__).resolve().parents[1] / "out" / "collision_table.txt"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")

    body = text.splitlines()
    # header is lines 0..6 (title, source, two notes, blank, column header, separator)
    header_end = 7
    first5 = body[header_end:header_end + 5]
    last5 = body[header_end + len(rows) - 5:header_end + len(rows)]
    print("First 5 rows (numerical evidence):")
    print("\n".join(body[:header_end]))
    print("\n".join(first5))
    print("\nLast 5 rows:")
    print("\n".join(last5))
    print("\nExtrema and trend:")
    print("\n".join(body[-3:]))
    print(f"\nCaptured full table: {output}")


if __name__ == "__main__":
    main()
