# Literature grounding of the three proposed approaches

Research role report. Each candidate's file under `research/approaches/` has been
updated with `status`, `precedent`, `holding-claims`, `falsifies`, `buy`, and a
`killed-by` line. This note is the reading behind them.

## 1. mod4-pascal-invariant — Sierpinski dot product — **refuted**

- **What it is called:** the "mod-4 linearization" (Odlyzko 1993 §2, eq. 201);
  the claimed lift is a "Lucas/Kummer mod-2^t Pascal congruence". The mod-2
  form is CHT 2026 **Lemma 3.10** (parity formula): `a(i,j) ≡ Σ_k C(i,k) a_{j+k}
  mod 2`.
- **Theorem it relies on and its hypotheses:** the congruence
  `d_{k+1}(n) ≡ d_k(n)+d_k(n+1) (mod 4)` for even `d_k(n)`. Hypotheses (rows
  are (odd,even,even,...)) hold here. It is real.
- **The lift fails:** `|a−b| = a+b − 2·min(a,b)`, so `|a−b| ≡ a+b (mod 2^t)`
  iff `min(a,b) ≡ 0 (mod 2^{t−1})`. This always holds mod 4 (min of two evens
  is even) but fails mod 8 (`|2−6|=4 ≢ 0 (mod 8)`, `2+6=8≡0`). **Mod 4 is the
  ceiling**, and mod 4 conflates 0↔4 and 2↔6 — precisely the values the
  conjecture must exclude. So no free mod-2^t invariant can certify the exact
  `{0,2}` value. CHT themselves state Lemma 3.10 is parity-only and they don't
  use it for the value. Hand-verified algebra; no execution tool this session.
- **Who applied it here:** Odlyzko (parity evidence), CHT (parity lemma only).
  Nobody lifts it to the exact value; the lifting is the unsolved part.
- **Buy:** none beyond what is already known — parity of `d_k(1)/2` is
  trivially always 0 or 1; the value question is untouched.
- **Sources:** arXiv:2607.08712 (CHT, Lemma 3.10, Remark 4.5);
  Odlyzko 1993 (§2) in the library.

## 2. backward-extension-automaton — finite-state local decidability — **refuted**

- **What it is called:** the *valid-extension set* problem for finite Gilbreath
  sequences (Muney 2026), and Gilbreath *polynomials* / the K-criterion
  (Alkan et al. 2023).
- **The exact criteria are global, not local.** Alkan et al. (Mathematics
  11(18):4006): `S=(s_1..s_n)` is Gilbreath iff parity alternates and
  `min K(s_1..s_m) ≤ s_{m+1} ≤ max K(s_1..s_m)` for **all** m, with
  `max K_S = s_1·(n−1)! + … + s_n·0! + 1` — factorial weights over the *whole*
  prefix. Muney (arXiv:2606.23721): the "parity interval" prediction fails
  (interior holes, smallest at length 5); the correct membership criterion is
  an order-sensitive analogue of Brown's subset-sum completeness criterion —
  again global. Hence no bounded `(K,W)` Markov state exists; the finite-state
  assumption is false.
- **The trap-state hope fails in the general class:** Eppstein 2011 builds
  2-then-odds sequences with gaps ≤ f(n) whose right edge escapes and re-enters
  1 infinitely often (good set is not a trap). His escape condition
  (`gap > row-sum of the entire previous row`) is global.
- **Buy (still real):** Muney's valid-extension set is the backward analogue of
  the run's leading `{0,2}`-block; useful as a re-description, but its exact
  global criterion is as hard as the conjecture.
- **Caveats:** Alkan text not downloaded (MDPI 403); account rests on the
  exa_search digest and the pre-existing `gilbreath-polynomials-imply-gc` claim
  in `research/notes/library-state.md`. Marked sourced/asserted, not re-derived.
- **Sources:** arXiv:2606.23721 (Muney, full text in library),
  mdpi.com/2227-7390/11/18/4006 (Alkan, digest-only),
  11011110.github.io (Eppstein, full text in library).

## 3. rule90-absorbing-boundary — CA boundary absorption — **refuted (as a route to regeneration)**; the Rule-90 identification is real

- **What it is called:** Rule 90 / XOR cellular automaton = Pascal mod 2 =
  Sierpinski gasket. The identification of the `{0,2}` interior with Rule 90 is
  proved in this run's block-lemma apex result and confirmed by CHT §1.
- **Why the absorption half is refuted for the general class:** CHT **Lemma
  3.7(iii)** proves a `{0,d}`-valued block stays `{0,d}`-valued in **all
  descendants** — no decrease in magnitude; CHT Theorem 1.6 isolates long
  shallow `{0,d}`-blocks as one of only two obstructions. Eppstein 2011 gives
  arbitrary escape/re-enter delay. So no uniform `B(v)` absorption time holds
  in the 2-then-odds class.
- **The engine is linear, the needed step is not:** Rule 90 is linear over
  GF(2) and governs only the `{0,1}` interior; once a value ≥2 enters, `|a−b|`
  is no longer XOR and leaves the linear-CA regime. The nonlinear boundary step
  is exactly the conjecture.
- **Buy:** the within-block Rule-90 structure is real but already captured by
  the proved block lemma; no additional progress toward regeneration.
- **Sources:** arXiv:2607.08712 (CHT §1, Lemma 3.7(iii), Thm 1.6);
  11011110.github.io (Eppstein); `research/notes/block_lemma.md` (this run's
  Sierpinski/XOR apex).

## Net

All three proposed lines reduce to the same known obstruction (regeneration /
the `{0,d}`-block dichotomy) and none resolves it; all are now filed `refuted`
with named reasons, so they will not be re-proposed. The usable residue: the
Rule-90/`{0,2}` interior structure (already proved), Muney's valid-extension
sets as a descriptive object, and CHT's two-separated-set non-concentration
hypothesis as the precise form of what separates the primes from the Eppstein
counterexamples.
