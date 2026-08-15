# S1 fork resolution — the universal ν₂≥w transfer is dead (exact negative)

## The fork (board's open question)

The `rising-sea` and `adversarial` skeletons dropped the supply bound
`ν₂(q_n) ≥ c·n`, Route B's only open content, into two rungs (see board
`nu2-supply-split`, `nu2-supply-mod4-transfer`, `supply-nu2-factorization`):

- **S1 (transfer):** `ν₂ ≥ w/2` where `w` = Hamming weight of the halved-gap
  bits `h[m] = (gap_m/2) mod 2` (gaps ≡ 2 mod 4) over the fixed ancestor
  window `[2, n−1]`. Open question: is this a *universal F₂-combinatorial*
  identity (hence provable from Rule-90/XOR/ancestor-window alone, item S1
  carries zero number theory), or does it hold only for the prime bit string
  (in which case S1 just repackages S2's hardness)?
- **S2 (density):** `w(n) ≥ c'·n` — the two-point prime-gap mod-4 density
  (the hard, Hardy–Littlewood/Lemke-Oliver-level input).

## The resolution — S1 is FALSE universally; no positive constant works

Exact enumeration over all 2-then-odd gap strings (first gap 2, remaining gaps
in `{2,4}` so the halved-gap parity bit `(g/2)%2` is the free 0/1 choice),
computed to length m=14:

1. `ν₂ ≥ w/2` fails: violations grow with length (m=7: 10, m=12: 145,
   m=13: 258, m=14: 461 strings violate).
2. it fails even restricted to balanced strings — the all-2 string
   `[2,2,…,2]` of length 12 has w=12, nu2=1 ⇒ `2·ν₂−w = −10`.
3. **No positive constant c works at all**: every length the string
   `[2,4,4,…,4]` (w=1) gives nu2=0, so `ν₂/w = 0`. The worst-case universal
   transfer ratio is **0**, not 0.5.

## Why the identity cannot be recovered universally

The Rule-90/XOR interior law (`rule90-interior-xor`) and the
ancestor-window union fact (`nu2_vs_gap_parity.py`) are both real, but they
govern where the `{0,2}` suffix *begins*, not how many 2s it contains. The
value `nu2` depends on the actual sign pattern of the integer gaps, which the
halved-gap parities alone do not determine. The all-4-with-leading-2 string
produces a diagonal whose `{0,2}` suffix is empty (nu2=0) despite w=1.

## Prime-specific margin

For the prime bit string, min(2·ν₂−w) over n≥17 is **0**, reached at n=44 —
positive on the sampled range to n=30000, but *tight* (touches 0), not
comfortable. So even the constant 1/2 transfer barely holds for primes.

## Consequence for the route

The supply bound **cannot** be split into a number-theory-free S1 plus an S2.
Any universal transfer is a dead path (exact counterexamples above, growing
with length). The honest statement must carry S2's two-point content — as the
`adversarial` `supply-nu2-factorization` skeleton already predicted. This is
a real negative result to record so no one re-proposes universal-transfer.

## Verification route

Two independent constructions (sieve 2e5 re-derivation vs. the 3e4-term
`nu2_dense.txt` from sieve 1e6) agree on the prime transfer/fluctuation
values; the S1 counterexamples are exact enumeration of every {2,4} string
to the stated length (oracle, `complexity_class=exponential`,
`oracle_bound=m≤14` — this is the brute-force oracle of rule 9, used only
to test the analytic question, not as the method).
