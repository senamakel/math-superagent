# Shared context

Lean-first run on Project Euler 622. The deliverable is not a number but a
`.lean` theorem tree with a passing `lean_check` carrying the final answer as an
equality of naturals; `native_decide` is refused, so the argument must be
structural. Python is used only to discover/check at small size; the kernel must
carry the proof. The workspace already has the oracle, the reduction, the Python
answer, and a source library — but **no Lean file has been formalised yet**.
Per the operator's directive, library building stops now: the immediate step is
Lean statement-first (the shuffle definition and the s(n) = ord_{n-1}(2)
reduction as theorems ending in `sorry`, checked with `lean_check` so a verdict
is filed).

See `problem.md` for the statement; `GOAL.md`, `TASKS.md`, `solution.md` and the
ledgers are all still unseeded.

## Established

- **Structural reduction (hand-verified against every stated example; machine
  check pending):** the out-shuffle on an even deck of size n has order
  `s(n) = ord_{n-1}(2)`, the multiplicative order of 2 mod the odd number n−1.
  Basis: matches `s(52)=8` (ord₂ mod 51), `s(86)=8` (ord₂ mod 85), and the
  `s(n)=8` set `n = 3^a·5^b·17 + 1`, `a,b∈{0,1}` → `{18, 52, 86, 256}`, sum 412.
  Computed by hand only — a first `brute.py` run must confirm it. The out-shuffle
  fixes top and bottom cards; the in-shuffle (which does not) would use ord of 2
  mod (n+1) and is the wrong variant here.
- Consequence of that reduction: `s(n)=60` ⟺ `ord_{n-1}(2)=60`, i.e. every
  prime-power factor `p^a || (n−1)` has `ord_{p^a}(2) | 60`, the lcm of those
  orders equals 60, and n even (n−1 odd). Enumerate those m = n−1, sum n = m+1.
  Hand-verified only.

## Ruled out

Nothing has been tried and failed yet; there are no recorded dead ends.

## Numbers

- Stated examples to reproduce: s(52)=8, s(86)=8, Σ{n : s(n)=8} = 412 (n∈{18,52,86,256}).
- Target: sum of all n with s(n)=60.
- No computed output exists yet (code/out is empty).

## Recalled

Cognee memory and scratch are both empty for this problem — no earlier run or
related-shape run has left anything. The reduction above is this run's own
hand-work, not recalled.

## Contradictions

None recorded. Caveat: the reduction is hand-derived, not yet program-confirmed;
if `brute.py` disagrees with 412 / the 8s, the reading of the shuffle (out vs in)
is wrong and nothing else holds.

## Gaps

- Machine confirmation of the reduction against all three stated examples
  (`code/brute.py`; then record the output in `code/out/` with a `checked` claim).
- The full `s(n)=60` enumeration with exact arithmetic, cross-checked by a second
  route (different prime-power enumeration), before it is trusted.
- The Lean formalisation: statement of the reduction, the prime-power/order lcm
  lemma, and the final sum as an equality of naturals with a passing `lean_check`.
  This is the actual deliverable.
