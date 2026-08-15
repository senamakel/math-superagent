# Ash, Beltis, Gross, Sinnott — "Frequencies of Successive Pairs of Prime Residues" (Experimental Math. 20(4):400–411, 2011)

Full text: `research/sources/ash-beltis-gross-sinnott-2011-successive-prime-residue-pairs.full.md`
Source URL: author copy at `http://fmwww.bc.edu/gross/ABGS.pdf` (DOI 10.1080/10586458.2011.565256; Project Euclid em/1323367154 open). Peer-reviewed.

## What this is

The single dedicated peer-reviewed **heuristic** study of exactly the statistic G-supply needs — the count `N(a,d,m,x)` of consecutive prime pairs `p<q`, `p<x`, `p≡a, q≡a+d (mod m)`. The **mod-4 switch count** `#{n : p_{n+1} ≢ p_n (mod 4)}` = `#{gap ≡ 2 mod 4}` = Granville's `ν₂` bit is precisely `N(1,2,4,x)+N(3,2,4,x)` at m=4. Complements the held sources: **LOS 2016/2017** give the conjectural asymptotic framing, **Ruzsa 2001** gives only infinitude, **Shiu 2000** proves the *const* (non-switch) runs recur; this is the heuristic pair-frequency formula plus two rigorizable symmetries of it.

## What it establishes

- **Method (Pólya heuristic + inclusion–exclusion):** a heuristic formula `P_J(a,d,m,x) ≈ Prob(x prime, x≡a mod m, next prime ≡ a+d mod m)` as a truncated infinite series (§3). Requires `d+Jm ≤ 55` for the subset sums to be feasible, so numerical checks limited to `x ≤ 10^6`. The authors explicitly do not prove the series converges in J; `j→∞` limit unknown.
- **Proposition 4.1 (power-of-2 independence, PROVED for the heuristic):** if `m=2^k`, then `P_J(a,d,m,x)` is **independent of a**. Data check §6 (m=16, first 50M primes): the "broken diagonals" = pairs with fixed `a+d` are equal to ~1 part in 1000 (counts range 842431–843672), while off-diagonal entries vary 2.66×. So for **m=4 the switch and non-switch pair frequencies depend only on the shift d, not on the residue a** — the two switch pairs (1,3),(3,1) are equal and the two non-switch (1,1),(3,3) are equal, at least to the heuristic and numerically.
- **Proposition 4.2 (antidiagonal symmetry, PROVED):** `P_J(a,d,m,x) = P_J(−a−d,d,m,x)`; verified numerically (Sections 5,7; ratios within 0.0006–0.002).
- **Propositions 4.3/4.4 (vertical compatibility):** consistency of the heuristic across moduli `m | n` (a sum of finer counts). The heuristic is internally coherent — the mod-m pair counts telescope to the m=2 (single-prime) case.
- **m=4 data (10^3–10^6):** switch pairs (1,3),(3,1) ≈ 22521 each, non-switch (1,1),(3,3) ≈ 16574/16715 each — the ASH heuristic predicts switch ≈ 1.36× non-switch at these scales, and the anitdiagonal/power-of-2 symmetries give `N(1,2,4,x)≈N(3,2,4,x)` and `N(1,4,4,x)≈N(3,1...,4,x)`. (The labels differ across tables only by indexing convention; the content is that the switch pairs are the more frequent two at m=4.)
- **Section 9 open question (critical for G-supply):** whether `N(a,d,m,x)/π(x)` tends to a limit independent of a and d as `x→∞` is **open**; "we cannot tell whether they are tending toward a limiting ratio of 1." They note it "seems quite possible" the finite-scale switch-excess persists for almost all x (a Chebyshev-bias-style race, cf. Rubinstein–Sarnak 1994).

## Bearing for this run (Route B, G-supply)

- **Confirms the honest verdict already in the library:** no unconditional positive-density lower bound on the mod-4 switch count (ν₂ supply) exists. The best available is (a) the Hardy–Littlewood/LOS conjectural asymptotics and (b) this paper's heuristic with its proved power-of-2 independence symmetry. The necessary supply bound `ν₂(q_n) > n^β`, β>0.525, remains open and would be a genuine result.
- **Adds one rigorizable structural fact** not previously in the library as a dedicated source: the power-of-2 independence (Prop 4.1) says at m=4 the switch and non-switch frequencies are each residue-independent — so any future supply bound has a symmetric shape; the antagonists to look for are long runs of non-switch (`gap ≡ 0 mod 4`), whose frequency Shiu controls (infinitely recurring) but whose density is not bounded.
- The measured `ν₂/n ≈ 0.49–0.52` (this run) sits comfortably with the heuristic's slight switch-excess at finite x — the second-order bias LOS/Ash describe pushes switch count *above* n/2, which is exactly the direction G-supply needs (and is not needed to be *proved*, only to be a lower bound).

Status: sourced, peer-reviewed, heuristic-level. Claims held at assertion level (the heuristic is heuristic; Props 4.1–4.4 are proved *of the heuristic*, and only numerically verified for the true primes).

```claim
id: abgs-2011-s9-mod4-switch-limit-open
statement: Ash–Beltis–Gross–Sinnott 2011 §9 (Experimental Math. 20(4):400–411): whether N(a,d,m,x)/π(x) — the frequency of consecutive prime pairs p,q with p≡a, q≡a+d (mod m) — tends to ANY limit as x→∞ is OPEN; the authors state "we cannot tell whether they are tending toward a limiting ratio of 1". Therefore no unconditional positive-density (linear) lower bound on the mod-4 switch count #{n : p_{n+1} ≢ p_n (mod 4)} = #{gap ≡ 2 mod 4} exists in the literature.
hypotheses: primes; N(a,d,m,x) = #{p<q<x : p≡a, q≡a+d (mod m)}; m=4 for the switch statistic feeding Granville's ν₂ (N(1,2,4,x)+N(3,2,4,x)).
holds-here: yes
status: asserted (open problem named by the source; §9 is an explicit open question, not a theorem)
bearing: Route B (Granville ν₂). The entire remaining open content of the reduction — G-supply, ν₂(q_n) > n^β or any ν₂ ≥ c·n — is this named open problem, NOT a gap in the run's own argument. Route B yields a CONDITIONAL theorem whose hypothesis is the two-point consecutive-prime mod-4 correlation lower bound. Props 4.1/4.2 give the only rigorizable structural facts (power-of-2 residue-independence; antidiagonal symmetry), which delimit the shape of any future supply bound but do not supply one.
anchor: research/summaries/ash-beltis-gross-sinnott-2011-successive-prime-residue-pairs.md
```
