# Librarian closure verification (2026)

**Cycle / source:** librarian, chasing nothing — verifying the library's recorded closure is coherent before pausing.

## What this cycle established

The library is CLOSED, and the closure holds on re-examination:

1. **Sole open REQUEST (G-supply) — settled negative.** `g-supply-two-point-crux-settled.md`:
   the mod-4 switch bit `h[j] = (gap_j//2) mod 2` (=1 iff gap ≡ 2 mod 4) is a
   **two-point** statistic (consecutive-pair residue switch count), so one-point
   PNT-in-AP / GRH / Dirichlet is structurally blind to it (explicit countermodel:
   ordering all 1-mod-4 then all 3-mod-4 primes achieves N_switch=1 with correct
   marginals). No unconditional positive-linear ν₂ ≥ c·n bound is provable from
   current methods; the unconditional literature (Ruzsa/Shiu/Martin, sub-density
   `x loglog x/log²x`) covers only the equal-residue NON-switch side. Leading-order
   ν₂ ≈ n/2 needs the open k-tuple conjecture. Honest deliverable: CONDITIONAL
   theorem at Hardy–Littlewood / two-point mod-4 level. Do not re-attempt.

2. **Named MathOverflow fetch — done.** `mathoverflow-gilbreath-what-is-known-thread.full.md`;
   no new dead route; A080839 note (Gilbreath-property sequences counted). Do not re-fetch.

3. **FRONTIER swept to the cited-by≥2 floor.** Every high-trust lead is already held
   (verified by matching the FRONTIER rows against `research/sources/`):
   - Arithmetic Z-game (10.1016/j.chaos.2016.05.016) → `cobeli-prunescu-zaharescu-2016`
   - Game with divisors/exponents (10.1080/10236198.2014.940337) → `cobeli-zaharescu-2014`
   - Ducci w/ algebraic numbers (10.1080/00150517.2011.12428072) → `caragiu-zaharescu-zaki-2011`
   - Nouveaux records Proth-Gilbreath (10.3917/pls.580.0068) → popularisation of the
     Colonna record; primary record page held (`colonna-proth-gilbreath-record-2026-08`)
   - Odlyzko 1993 itself (10.1090/S0025-5718-1993-1182247-7) → held (full + latex source)
   - "On a Conjecture Concerning the Primes" 1959 (10.2307/2001963) → `killgrove-ralston-1959`
   - Gatti preprints v1/v4 → held (2020 Wayback capture; v4 content mirrored)
   - Increasing integer sequences & Goldbach (10.1051/ita:2006017) → `torelli-2006`
   - Cháos Solitons & Fractals 2024 (10.1016/j.chaos.2023.114315) → surfaced only via this
     cycle's search; it is a Cîmpeanu-class *equal-residue* (mod-6) preprint, non-load-bearing,
     already assessed in `library-build-report.md` §G-supply. Do not fetch.
   The remaining cited-by≥2 rows are textbooks/popularisations (Ribenboim *Number of Primes
   Below a Given Limit*, Conway–Sloane *My Favorite Integer Sequences*, MathWorld-linked
   entries, Unsolved Problems 2nd ed.) or orthogonal papers that cite Odlyzko as a
   bibliographic hub with no bearing on the reduction. None is a claim source the run lacks.

4. **problem.md leads all held:** Odlyzko 1993; Killgrove–Ralston 1959; Proth 1878
   (`proth-1878-ncm-vol4-googlebooks.full.md`, retraction recorded — nothing to error-scan);
   generalisation family (Chase 2024, CHT 2026, Li 2026 modulo-k, Torelli); verification
   records 10^13 / 10^14 / 1.5×10^15 (sourced, cf. `verification-record-2026`).

## Verdict

NOTHING FURTHER. The canonical-reference tier is held, the sole REQUEST is settled
negative, the frontier's high-trust rows are all in `research/sources/`, and no gap
remains that a search could responsibly chase. Future librarian cycles should NOT
re-sweep the frontier or re-fetch the Gilbreath/Proth/Ducci corpus; the only defensible
future action is a NEW stated gap appearing in `research/REQUESTS.md`.
