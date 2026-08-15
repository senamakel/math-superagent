# Scholar — cyclotomic ramification claim: status and proposed check

This note is **NOT** a verification. This scholar session has no execution tool,
so nothing here has been run. It records (a) the claim under test, (b) the exact
check tool_builder/coder should run to upgrade its evidence, and (c) why the
claim is currently only `asserted`.

## Claim under test

`zeta-p-ring-of-integers-and-ramification` (and parallel
`ramification-of-p-cyclotomic`): for K = Q(zeta_p), p an odd prime, Z[zeta_p]
is the ring of integers, (p) = (1-zeta_p)^(p-1) with P = (1-zeta_p) the unique
prime over p (ramification index p-1, residue degree 1), P principal.

**Current status in the library: `asserted`** (Conrad factorize.pdf, captured
server-side; not re-derived in-workspace). This is load-bearing for the whole
both-odd cyclotomic approach, so it is worth an exact check.

## The exact check to run (program written, NOT yet executed)

`code/scholar_oracle/verify_ramification.py` contains three direct consequences
of the claim, all exact integer arithmetic (sympy, no floats):

1. **Norm_{Q(zeta_p)/Q}(1 - zeta_p) = p**: conjugates of 1-zeta_p are
   1-zeta_p^j (j=1..p-1), so Norm = prod_{j=1}^{p-1}(1-zeta_p^j) = Phi_p(1) = p.
   Checked by the program for p in {3,5,7,11,13,17,19}.
2. **prod_{j=1}^{p-1}(1 - zeta_p^j) = p**: the exact integer p is Phi_p(1);
   this is the ideal equation (p) = (1-zeta_p)^{p-1} evaluated with the p-1
   Galois-conjugate factors (ramification index p-1).
3. **Phi_p(X) ≡ (X-1)^(p-1) (mod p)**: coefficientwise mod p, matching
   (-1)^k·binom(p-1,k) (total ramification, residue-degree-1 criterion).

Run: `timeout 540 python3 code/scholar_oracle/verify_ramification.py`

**Nothing in this note claims these have passed.** They are proposed; the
program has not been executed in this scholar session (no execution tool).

## What a pass would and would not establish

- A pass would upgrade the *evidence* for the three identities from "asserted by
  Conrad" to "exact identities verified at stated primes" — verified-numerically,
  not proved for all p.
- It would **not** prove the ring-of-integers equality Z[zeta_p] = O_K (that
  needs the discriminant/monogenicity argument), and it would not prove the
  ramification claim for *all* p. Those remain asserted unless separately
  derived.

## Relation to the known solution

The known solution (3,2,2,3) has p=2 even; Q(zeta_p) with p odd prime never
arises for it. These ring-theoretic facts hold for every odd prime p
independently of any solution, so they neither include nor exclude the known
solution.

## What the scholar session actually established

This session added **no verified computation** — it has no execution tool. Its
contribution is confined to reading and confirming the source notes already in
the library and flagging that this foundational claim is still `asserted` and
should be upgraded by an exact check (above) before any both-odd lemma leans on
it.
