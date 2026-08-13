# Literature check: the three `proposed` approaches (root-number, quadratic Chabauty, Φ-fibre Faltings)

Date: this round. Author: research specialist.

The inventor produced **no new candidates** this round (agent did not respond before
deadline). The one substantive task available was to take the three approach files
that sat at `status: proposed` (written by an earlier inventor round but never checked
against the literature) and either ground or refute each. All three are now closed;
two were already refuted by the run's own exact computations and this round confirmed
that refutation against published sources; the third (root-number-parity) was refuted
here on the literature plus the run's own hinge. Nothing here is a search reformulation
that anyone should re-propose.

## 1. root-number-parity-four-curves → **refuted** (this round, literature + run's hinge)

Reformulation: the four differences u, v, u+v, u−v through the centre give four
congruent-number curves E_d: y² = x³ − d²x (CM by Z[i], j = 1728); a point of 2E_d(Q)
forces rk E_d(Q) ≥ 1; parity (root number ≡ rank mod 2) was hoped to contradict.

- Established (Birch–Stephens, Topology 5 (1966)): R(n) = ord_{s=1} L(E_n, s) has
  parity fixed by n mod 8 — R(n) odd iff n ≡ 5,6,7 (mod 8). Restated as a necessary
  condition in "A necessary condition for p and 2p to be congruent for p ≡ 1 (mod 8)",
  J. Number Theory (2023), https://www.sciencedirect.com/science/article/pii/S002240492300018X
- Local root numbers computable (Dokchitser & Dokchitser, arXiv:0906.1815).
- Refutation: the parity law is a *necessary* condition compatible with any
  configuration of four rank-≥1 curves; the hoped-for additive-relation→root-number
  contradiction is unestablished speculation; and a Q-level mod-2 parity framework
  cannot separate Q from Q(√3,√133)/Q(√3), over which MSS provably exist
  (this run's `extension-field-mss-exist`). The finite residue-class check was never
  a route to a contradiction.

## 2. quadratic-chabauty-7to8 → **refuted** (pre-existing run computation, confirmed here)

Reformulation: when classical Chabauty fails (r ≥ g), apply quadratic Chabauty
(Balakrishnan–Besser–Dogra–Müller–Tuitman–Vonk; Chabauty–Kim depth 2) to the
Bremner II 7→8 transition curves.

- Established (literature): the quadratic-Chabauty theorem family is real, published
  and executed — Kim (Invent. Math. 161, 2005); Balakrishnan–Dogra et al. (Annals of
  Math. 189, 2019); "Quadratic Chabauty for modular curves" (Compositio Math. 2023);
  "Geometric quadratic Chabauty and p-adic heights" (Expo. Math. 41, 2023), r < g + ρ(J) − 1.
- Refutation: the run's exact computation (`code/out/bremner2_quartics.txt`) shows all
  three Bremner II eq. (13) quartics at λ=13 are **genus 1** (elliptic), so neither
  classical nor quadratic Chabauty's genus-≥2 hypothesis engages for the exact curves
  the approach proposed to run on. Correct tool: elliptic 2-descent/Selmer.

## 3. phi-triple-curve-genus-faltings → **refuted** (pre-existing run computation)

Reformulation: fix q₁ ∈ Φ and a ratio r; the fibre f(p,q) = q₁ + f(1,r) is a curve
whose genus one could compute, hoping for genus ≥ 2 and Faltings finiteness.

- Established (literature): Faltings 1983 (genus ≥ 2 ⇒ finite rational points).
- Refutation: f is homogeneous of degree 0 ((m,n)→(tm,tn) leaves f fixed), so the
  fibre is a quartic in ONE ratio with at most 4 rational lines — genus 0, no Faltings
  statement applies. This run's exact check (research/notes/verdict_facts_check.py).

## New primary sources added this round

- Garcia-Fritz & Pastén, "A note on Bremner's conjecture and uniformity", arXiv:2604.04850
  (2026). Proves (conditional on uniform rank bounds) that long APs of x-coordinates of
  rational points on E(Q) force large rank — a uniform version of Bremner's 1998 rank
  conjecture, via uniform Mordell–Lang / height-uniform Mordell (Dimitrov–Gao–Habegger).
  Bearing: a genuine MSS needs three points of 2E(Q) on E: y²=x(x²−c²) with x-coords in
  AP, so the obstruction concentrates on rank-scarcity of small-rank elliptic curves.
  Source: research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md.
- Rome & Yamagishi, "On the existence of magic squares of powers", arXiv:2406.09364 (2024).
  Proves existence of n×n magic squares of squares for all n ≥ 4 (settles
  Várilly-Alvarado's conjecture) via Hardy–Littlewood circle method; the 3×3 case remains
  open. Reconfirms 3×3 is the hard case. Source:
  research/sources/rome-yamagishi-magic-squares-of-powers-2024.full.md.

## Correction to existing work

`chabauty-coleman-hyperelliptic.md` (the adopted classical approach) previously asserted
that Bremner II "never writes down f(t)" for the 7→8 transition. That is wrong: Bremner II
eq. (12)–(13) gives the explicit quartics. The adopted file now says so and notes the run's
genus-1 computation. The adopted status is unchanged; what closed `quadratic-chabauty-7to8`
also narrows what `chabauty-coleman` can directly attack (the Category VII eq. (13) curves
are elliptic, needing 2-descent, not Chabauty).

```claim
id: root-number-parity-refuted-four-curves
statement: The root-number/parity argument on the four congruent-number curves
  E_d (d = u, v, u+v, u-v) cannot force non-existence: by Birch-Stephens the parity
  of R(n)=ord_{s=1}L(E_n,s) is fixed by n mod 8 (odd iff n ≡ 5,6,7 mod 8), which is a
  necessary condition compatible with any configuration of four rank-≥1 curves;
  the hoped-for additive-relation-to-root-number contradiction is unestablished;
  and a Q-level mod-2 parity framework cannot separate Q from the extension fields
  over which MSS provably exist.
hypotheses: E_d: y^2 = x^3 - d^2 x, CM by Z[i], parity conjecture/BSD for the rank.
holds-here: n/a (approach refuted; it cannot be the whole obstruction)
status: refuted
bearing: closes root-number-parity-four-curves; the 7->8 sub-question should be
  attacked by elliptic 2-descent/Selmer on the explicit Bremner II eq.(13) quartics
  (genus 1), not by root-number parity or by Chabauty.
anchor: research/approaches/root-number-parity-four-curves.md
```
