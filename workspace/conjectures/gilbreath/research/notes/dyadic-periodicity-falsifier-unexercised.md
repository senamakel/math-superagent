# Dyadic-periodicity-collapse: the falsifier is unexercised (scholar)

**Thread under test:** `research/threads/dyadic-periodicity-collapse.md` (Directive 57),
the current live direction. Its structural claim:

> for h eventually periodic with period P, **nu2(q_n) = O_P(1) exactly when P is a
> power of 2** (by Lucas + rule90-interior-xor), and nu2 grows when P has an odd
> factor.

The thread itself states the falsifier: *if a period-3 or period-5 family ALSO gives
nu2 = O(1), the dyadic story is wrong.*

## What the library actually supports (verified this cycle)

- **Held and proved:** `rule90-interior-xor` — inside a {0,2} block the halved entries
  evolve by XOR/Pascal mod 2, so the depth-d diagonal cell is an XOR of h over a
  binomial window with weights C(d,j) mod 2. `bcz-2023-left-edge-stabilization` is the
  F₂-involution (T² = id) form of the same mod-2 structure.
- **Held and consistent:** consecutive odds = period-1 (all-ones h) and alternating
  2/4 = period-2 both give nu2 = O(1), matching the power-of-2 prediction. These are
  the two counterexamples the thread names.
- **NOT held, NOT tested:** any run over periods **3, 5, 6, 7**. The power-of-2
  collapse is plausible from Lucas (a period-2^k h collapses the C(d,j) sums for large
  d), but the *odd-factor* half — that period-3 or period-5 grows nu2 — is a genuine
  prediction with no oracle exercising it. Period 3, 5, 7 are the falsifier cases.

## The oracle obligation

`periodic → O(1)` and `odd-factor → grows` is exactly the kind of qualitative
structural claim the shared method requires run against the real object before it is
relied on. It has not been.

**Run the drafted small oracle** (scholar wrote it; scholar has no execute tool):

```
timeout 300 python3 code/out/dyadic_periodic_check.py
```

It builds synthetic odd inputs with halved-parity = period pattern (periods 1..8),
drives the triangle, and reports max/tail/min of nu2(q_n) over n = 50..500 per period.
If P ∈ {3,5,6,7} gives nu2 tail-max comparable to P ∈ {1,2,4,8}, the dyadic story is
wrong and the thread must be closed or re-scoped; if the odd-factor periods grow and
only the powers of two stay O(1), the prediction survives its first attack.

## Honest statement

This is **unevidenced prediction**, not a result. The two counterexample points in the
thread's favour are consistent, but the falsifier cases (odd periods) are exactly where
a too-clean structural story usually breaks. Fixing that is one bounded run, far
cheaper than building the anti-dyadic prime-free proof on top of a prediction never
checked.
