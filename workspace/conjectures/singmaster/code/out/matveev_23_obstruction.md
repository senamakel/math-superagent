# Matveev 2000 route for C(x,2)=C(y,3): executed obstruction and honest constants

Program: `code/matveev/check_matveev_23.py`
Capture: `code/out/check_matveev_23.captured.txt` (EXIT_CODE=0, ALL CHECKS PASSED)
Date/run: single process, `timeout 540`; no workers needed (O(1) per y, all exact).

## What is established

**P1 — the '"adopted"' approach is vacuous as written (theorem, exact).**
The equation `C(x,2)=C(y,3)` is `3x(x-1) = y(y-1)(y-2)` (U = V, each side =
6·C(x,2)). `research/approaches/matveev-explicit-2-3.md` proposed applying
Matveev 2000 Thm 2.3 to the linear form `Lambda = Σ b_j ln p_j`, `b_j =
v_{p_j}(U) − v_{p_j}(V)`. At **every** solution, U = V as integers, so the
two prime factorizations are identical, every `b_j = 0`, and `Lambda ≡ 0`.
Matveev Thm 2.2/2.3 requires `Lambda ≠ 0` and `b_n ≠ 0`. Therefore the
direct equal-products log-ratio cannot be the subject of the theorem.
Verified exactly on all four nontrivial solutions (5,5),(16,10),(56,22),
(120,36) — the last three are exactly the witness.json (2,3) entries
(120, 1540, 7140), so the witness set is reproduced, not contradicted.
Counting convention: names both mirrors + the trivial pair; the curve
solutions are listed as (x,y) pairs, mirror-free, because the curve itself
is the object.

**P3 — the complete solution set up to y ≤ 10^6 (oracle, exact).**
Exact quadratic-discriminant scan, O(1) per y: exactly
(2,3), (5,5), (16,10), (56,22), (120,36), matching Avanesov's Theorem A23
as reproduced by Stroeker–de Weger 1999 Table T23 (the held primary).
Note (2,3) is the trivial value-1 pair C(2,2)=C(3,3)=1; the nontrivial
(2,3) witnesses of the run are the other four.

**P2 — effective constants that ARE obtainable, computed end to end.**
The nonzero forms occur on the difference equations `C(x,2) = C(y,3) + d`
(`U − V = 6d`), where `d ≠ 0` forces at least one `b_j ≠ 0`. For the anchor
solution of each d (smallest y with the equality), the Matveev 2000 constants
were computed in full: K = Q, D = κ = ρ = 1, C3 = n, C1, C2 from (2.4),
ω from (2.5), B from (2.14), C′0 from (2.15), and the bound
`ln|Λ| > −112·2ⁿ·C2·C′0·D²·ω·ln(2eB)` from (2.16). Using
`|Λ| = |ln(1+6d/V)| ≤ 12|d|/V` this yields an explicit upper bound on V,
hence on y. Results (n ≥ 2 forms only; the 1-term forms d = ±3, +2 were
skipped because Thm 2.2 is stated for the homogeneous rational case with
n > 2, confirmed in the held source page 724):

| d | anchor (x,y) | n | log10 y max (from the explicit constant) |
|---|---|---|---|
| −1 | (3,4) | 2 | 2.85e10 |
| +1 | (7,6) | 4 | 9.49e17 |
| +3 | (368,75) | 6 | 3.40e27 |

These are effective, explicit, and per-pair — and astronomically large,
which is precisely the point: **an effective bound need not be a usable
bound**, and for d = 0 the honest effective route is David's method on
elliptic logarithms (SDW 1999, complete for (2,3) with rank-2 curve
Y²+Y = X³−9X+20), not ordinary-logarithm Matveev.

## Claims

```claim
id: matveev-empty-form-on-solution-locus
statement: Let U = 3x(x-1), V = y(y-1)(y-2). At every integer solution of
  U = V (i.e. of C(x,2) = C(y,3)) the prime-factor log-ratio form
  Lambda = sum_j (v_{p_j}(U) - v_{p_j}(V)) ln p_j is IDENTICALLY ZERO, so it
  cannot be bounded below by Matveev 2000 Theorem 2.2 (which requires
  Lambda != 0, b_n != 0). The '"adopted"' approach in
  research/approaches/matveev-explicit-2-3.md is vacuous as written.
hypotheses: x, y >= 2 integers; U = V; Matveev 2000 Thm 2.2 hypotheses
holds-here: yes — the three nontrivial (2,3) witnesses (120, 1540, 7140) are
  among the four solutions checked exactly; the logic is a general theorem
  (equal integers have equal prime factorizations).
status: proved (exact integer arithmetic; no floating point in the equality
  check)
bearing: closes TASKS.md item 3 as an honest negative for the d=0 curve:
  ordinary-logarithm Matveev cannot give the (2,3) effective bound; the
  correct route (David / elliptic logarithms, SDW 1999) is already complete.
  Effective constants DO exist for the nonzero difference forms d != 0 and
  are computed above, exhibiting the effective-vs-usable gap explicitly.
anchor: code/out/check_matveev_23.captured.txt
```