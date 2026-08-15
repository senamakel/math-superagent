# Granville Lemma 5.4 / Theorem 5.5: verbatim statements and the delta=0 gap

Source: arXiv:2607.04166v3 (cs.CR, 14 Jul 2026), "Piercing Gilbreath's Conjecture",
V. Granville. Full text: `research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md` [[granville-2026-piercing-gilbreath-FULLPDF.full]].
Prior notes: `research/notes/granville-2607-04166-actually-read.md`,
`research/notes/lemma54-discarded-case-is-universal.md`.

Notation (right diagonal): `delta_0(q_n) = q_n`, `delta_1(q_n) = g_n = q_n - q_{n-1}`,
`delta_k(q_n) = |delta_{k-1}(q_n) - delta_{k-1}(q_{n-1})|` — our triangle read along the
diagonal through `q_n`, so `delta_k(q_n) = A_k[n-k]`. The **0-2 cycle** of a right diagonal
is its maximal `{0,2}` suffix before the terminal entry. `nu_2(q_n)` counts the 2s in it.
`g*_n = max(g_2, ..., g_n)` is the record gap (first differences). `tau_n` is the index
where the 0-2 cycle starts; `v_n = delta_{tau_n}(q_n)` is the entry in the new diagonal
aligned with the cycle's first position (Granville's "yellow" value, Table 13).

## Lemma 5.4 — verbatim (p. 16)

> Let `q_1, ..., q_{n-1}` be a valid, successful sequence and `nu_2(q_{n-1})` be the number
> of elements equal to 2 in the 0-2 cycle of its right diagonal `delta(q_{n-1})`. Then
> `q_1, ..., q_n` also succeeds if `g*_n <= 2*nu_2(q_{n-1}) + 2`, where `g*_n = max(g_2, ..., g_n)`.
> As usual, `g_k = delta_1(q_k) = q_k - q_{k-1}` is the gap between `q_k` and `q_{k-1}`.
> This lemma is not specific to prime numbers.

The stated hypothesis is the **descent budget** `2*nu_2(q_{n-1}) + 2`: each 2 in the old
cycle's tail supplies at most 2 of descent (`2*nu_2`), plus one terminal unit, against the
record-gap demand `g*_n`. This is the same supply-vs-demand inequality this run proved in
row coordinates (`b_k = b_1 + Sum_{i<k}(j_i+1) - (k-1)`), reflected onto the right diagonal.

## Theorem 5.5 — verbatim (p. 16)

> Let `q_1, ..., q_{n-1}` be a valid, successful sequence and `nu_2(q_{n-1})` be the number
> of elements equal to 2 in the 0-2 cycle of its right diagonal `delta(q_{n-1})`. Assume
> that `g*_n < n^alpha` where `g*_n` is the record gap at `q_n`, that is, the largest gap
> ever encountered so far. If there is a constant `beta` such that `nu_2(q_{n-1}) > n^beta`,
> with `beta > alpha`, then for `n` large enough, the sequence also succeeds at `q_n` if it
> succeeds at `q_{n-1}`.

The proof is one line: "It is a corollary of lemma 5.4. For the prime number sequence,
`alpha = 0.525` works as proved by Baker in 2001, see [3]. Independently and unrelated to
primes, `beta = 0.99` works, see part 4 in conjecture 5.1."

## The delta=0 case: is it a real gap, and does it make absorption generic?

The proof of Lemma 5.4 runs a descent inside the gray block (the new diagonal's segment
aligned with the old cycle): with the top-row entry `delta_{k-1}(q_{n-1}) in {0,2}`,

    delta_k(q_n) in {delta_{k-1}(q_n) - 2, delta_{k-1}(q_n)}    "unless delta_{k-1}(q_n) = 0.
    We can ignore that exception: when it happens, success is guaranteed."

The clean reading is a monotone "holds or drops by 2" descent. The exception is the
`0`-then-top-`2` case: then `delta_k = |0 - 2| = 2`, an **increase**, not a hold-or-drop.
The author discards it with an assertion ("success is guaranteed"), no argument.

**Measured (this run, primes < 2e6, columns n = 20..2499, 2480 columns, exact integers,
in-container, cross-verified by an independent lib.gilbreath route):** a zero occurs inside
the relevant block on **2480 of 2480 columns (100.0%)**; of 3,095,143 gray-block entries,
**1,546,291 (50.0%) are 0**. So the discarded case is not a rare edge case — it is the
dominant entrywise regime of the block, and the clean two-cases-only descent never holds
across a real row. **The published proof does not establish the lemma**; the argument it
actually runs rests, in the generic case, on an unproved parenthetical.

Two distinct senses of "gap", kept apart:

- **Real proof gap: yes.** The descent in Lemma 5.4's proof, as written, does not establish
  the lemma, because its load-bearing case is asserted rather than argued and occurs in 100%
  of real columns. The lemma must be re-proved here before anything cites it, with the
  `delta-0` step (0 then 2) handled as the main case, not the exception.
- **Theorem refuted: no.** The lemma's *statement* survives all evidence: its conclusion and
  its `g*_n <= 2*nu_2 + 2` hypothesis hold on all 2480 columns tested (record gap 72 against
  budget 4098 at n = 3999, two orders of margin). And on the failure side the test is
  vacuous: every real prime column succeeds (Gilbreath holds this far), so the
  sufficiency implication `g*_n <= 2*nu_2+2 => success` was only ever confirmed with both
  sides true. The discriminating experiment — approaching the threshold from the failing
  side on sequences that *do* fail (Granville's "closest failing sister", or synthetic
  Poisson-gap sequences) — is still the one worth building.

So: absorption of a disturbance into `{0,2}` **is** the generic case in the real data (the
0-2 cycle dominates the diagonal, and zeros make it 50% of block entries), but the published
argument that it bounds the new diagonal's tail to reach 1 is incomplete. The repair — prove
that an interior zero guarantees success in general, rather than by inspection of
all-successful columns — is exactly the work the re-derivation must do.

## Demand side: Baker–Harman–Pintz, verbatim and as a corollary

The paper (p. 11, eq. 6):

> "As of today, the best asymptotic bound for the maximum gap between two primes, proved
> unconditionally (without assuming that the Riemann Hypothesis is true), is
> `p_{n+1} - p_n ≲ O(p_n^{0.525})`, established in 2001 by Baker [3] [= R. C. Baker,
> G. Harman, J. Pintz, *Bounded gaps between primes in short intervals*, Proc. London
> Math. Soc. 83:532-562, 2001]."

Standard form (my knowledge, matches the citation): unconditionally
`p_{n+1} - p_n << p_n^{0.525}` for all large `n`. This is what `alpha = 0.525` in Theorem 5.5
means, and it is **unconditional** — no unproved hypothesis on the demand side.

**Demand-side corollary (this run).** Since `p_n ~ n log n`, the record gap up to `q_n` is

    g*_n = max_{m <= n} (p_{m+1} - p_m) << max_{m <= n} p_m^{0.525} ~ (n log n)^{0.525}
        < C_eps n^{0.525 + eps}   for every eps > 0.

So the theorem's hypothesis `g*_n < n^alpha` holds for primes at `alpha = 0.525 + eps` for
any `eps > 0` — the entire residual requirement of Theorem 5.5 is the **supply** side, a
lower bound `nu_2(q_{n-1}) > n^beta` with `beta > 0.525`.

## Supply side: what is proved vs asserted (#print-style honesty)

Granville proves **no** lower bound on `nu_2`. What he runs:

- `beta = 0.99` by appeal to his own **Conjecture 5.1** (verdict: asserted, his own
  conjecture — not a theorem, and not a result any independent source establishes).
- `nu_2 ~ n/2`, an even stronger claim, from his Conjecture 5.1(4) and a heuristic tie to
  balanced diagonals / digit-counting in normal numbers (verdict: asserted heuristic).
- Measured here: `nu_2/n in [0.42, 0.52]` over n = 50..3999 (checked), `nu_2 = 2048` vs
  `n^0.525 = 77.8` at n = 3999 — the needed `n^beta` bound is beaten by a factor of 26 in
  the range. But range-measurement is not a proof.

Also asserted-not-proved in the same section: Theorem 2.5's proof is literally "Take
`kappa_0 = 0` and the theorem is proved!" — not a proof. The paper is cs.CR,
self-published, not peer reviewed; its value here is the **reduction** (GC to a `nu_2`
lower bound) and the elementary Lemma 5.4, not its proofs. Neither Lemma 5.4 nor Theorem
5.5 may be cited as established until re-derived.

Bottom line for the run: **Route B's entire open content is a lower bound on the density of
2s in the right diagonal**, `nu_2 > n^beta`, `beta > 0.525`. The BHP demand side is
unconditional and trivially satisfied. Lemma 5.4 is worth re-deriving (its proof gap is
local and repairable), and it is a GOAL.md-scale partial result; Theorem 5.5 as stated is
conditional on an unproved supply bound nobody has.

```claim
id: lemma54-re-derived
statement: For a valid successful q_1..q_{n-1} with record gap g*_n = max(g_2,..,g_n) and nu_2(q_{n-1}) = number of 2s in the maximal {0,2} suffix (0-2 cycle) of its right diagonal delta(q_{n-1}), the extension q_1..q_n succeeds if g*_n <= 2*nu_2(q_{n-1}) + 2. The published proof runs a holds-or-drops-by-2 descent inside the gray block but discards the 0-then-2 step ("unless delta_{k-1}(q_n)=0... success is guaranteed") without argument; that discarded case is the generic one, occurring on 2480/2480 real columns (100%) with 50.0% of gray-block entries zero, so the published proof does not establish the lemma. The lemma's statement is not refuted: conclusion and hypothesis hold on all 2480 columns, but only in the all-successful direction, so the sufficiency test is vacuous on the failing side.
hypotheses: valid (strictly increasing odd, q_1=2,q_2=3) sequence; right diagonal delta_k(q_n)=|delta_{k-1}(q_n)-delta_{k-1}(q_{n-1})|; 0-2 cycle = maximal {0,2} tail before terminal entry; g*_n record first-difference gap; primes < 2e6, columns n=20..2499, exact integer arithmetic
holds-here: yes
status: checked
bearing: Route B (Granville nu_2) primary. Lemma 5.4 is NOT load-bearing as published; it must be re-proved here with the delta=0 case as the main case. The lemma's statement is credible and worth re-deriving (it is the run's own budget inequality in right-diagonal coordinates); its proof is the gap.
anchor: research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md, code/out/lemma54_iff_check.captured.txt, code/out/verify_granville_nu2_independent.captured.txt
answers: lemma54-discarded-case-is-universal
```

```claim
id: bhp-max-gap-unconditional
statement: Baker-Harman-Pintz 2001 (Proc. LMS 83:532-562), unconditionally: p_{n+1} - p_n << p_n^{0.525} for all large n. This is the demand side of Granville Theorem 5.5: alpha = 0.525 requires no unproved hypothesis.
hypotheses: n large; p_n the n-th prime; no additional hypothesis (proved unconditionally)
holds-here: yes
status: proved
bearing: Fixes the demand side of the nu_2 reduction unconditionally; the residual content of Route B is entirely the supply lower bound nu_2 > n^beta, beta > 0.525.
anchor: research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md (eq. 6, p. 11)
```

```claim
id: bhp-demand-corollary-g-star
statement: The demand-side corollary: for the prime right-diagonal, g*_n = max_{m<=n}(p_{m+1}-p_m) = O(n^{0.525 + eps}) for every eps > 0, since p_n ~ n log n and each gap is << p_m^{0.525}. Hence Granville Theorem 5.5's hypothesis g*_n < n^alpha holds for primes at alpha = 0.525 + eps, and the whole theorem reduces to the supply bound nu_2(q_{n-1}) > n^beta with beta > 0.525.
hypotheses: BHP unconditional bound; p_n ~ n log n (PNT); eps > 0 arbitrary
holds-here: yes
status: proved  (follows from bhp-max-gap-unconditional + p_n ~ n log n)
bearing: Closes the demand side as a corollary; states the open requirement (supply, a nu_2 density bound) that Route B must prove.
anchor: research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md (eq. 6)
follows-from: bhp-max-gap-unconditional
```

## Proof-state summary

| Claim | Status |
| --- | --- |
| Lemma 5.4 statement (`g*_n <= 2*nu_2+2 => success`) | **checked numerically** on 2480 all-successful columns; **proof not established** (delta=0 case discarded, generic). `status: checked`, `holds-here: yes`. |
| Theorem 5.5 (`nu_2 > n^beta, beta>0.525 => success`) | **asserted** — corollary of Lemma 5.4 plus Conjecture 5.1 for its own beta; no supply bound proved. |
| BHP `p_{n+1}-p_n << p_n^{0.525}` | **proved** (sourced unconditional). |
| `g*_n = O(n^{0.525+eps})` corollary | **proved** (this run, from BHP + PNT). |
| `nu_2 ~ n/2`, `nu_2 > n^0.99` supply bound | **asserted** (Granville Conj. 5.1); measured 0.42–0.52 here (checked, not proved). |
