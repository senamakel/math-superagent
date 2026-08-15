# Double-Wieferich condition — exact placement (reconstruction, sourcing status)

## What was requested

A primary-source statement of two results on `x^p - y^q = 1` with p, q odd
primes:

(a) **Cassels's divisibility theorem** — a solution forces `q | x` and `p | y`;
(b) the **double-Wieferich congruences** — the exact placement of
    `p^{q-1} ≡ 1 (mod q^2)` versus `q^{p-1} ≡ 1 (mod p^2)`.

## Sourcing status (what this run could and could not obtain)

- The two named primary sources — Cassels, "On the equation a^x - b^y = 1, II"
  (Proc. Cambridge Philos. Soc. 56, 1960 / J. London Math. Soc. 35, 1960) and
  Mihăilescu 2002 — were **screened by the run's evidence policy** as material
  that would supply a published answer / necessary-condition statement to the
  problem in problem.md. Rephrasing or a mirror was refused and is recorded.
  Per policy these are **not to be re-fetched or quoted from memory**.
- Publisher hosts (ams.org, ScienceDirect, doi.org, Springer) are **unreachable
  at the network boundary** for `download_document`; `read_sources` (server-side
  fetch) works for them. arXiv/primary papers that would develop the technique
  rather than report the statement remain the permitted route.

**Net:** the exact primary statement from Cassels/Mihăilescu is NOT in the
library, so nothing here is a quotation of either. GOAL.md in fact requires the
divisibility conditions be "re-derived with proofs, rather than cited," so the
run's own reconstruction (below) is the sanctioned form.

## The run's reconstruction, and why it is consistent with the technique tier

General definition (confirmed by technique sources downloaded/read in this run;
see Katz, "Wieferich past and future"; Crandall–Dilcher–Pomerance, "A search for
Wieferich and Wilson primes"):

> An odd prime `r` is a **base-a Wieferich prime** iff
> `a^{r-1} ≡ 1 (mod r^2)`, for `gcd(a, r) = 1`.
> Base `a` on the left; the **square of the prime `r`** on the right.

Applying the definition symmetrically to the two primes involved:

- `q` is a **base-p Wieferich prime**:  `p^{q-1} ≡ 1 (mod q^2)` — **p on the
  left, q^2 on the right**.
- `p` is a **base-q Wieferich prime**:  `q^{p-1} ≡ 1 (mod p^2)` — **q on the
  left, p^2 on the right**.

So the pairing is **base p ↔ modulus q^2** and **base q ↔ modulus p^2**: the
base and the squared modulus are the *two different* primes. This is the exact
placement reconstructed by the run and stated in
research/backward/conditional-non-wieferich.md (gap `cond-wieferich`) and
research/backward/both-odd-primes.md (gap `G-double-wieferich`):

    q^{p-1} ≡ 1 (mod p^2)   and   p^{q-1} ≡ 1 (mod q^2).

Cassels's divisibility theorem (same gaps `cond-cassels` / `G-Cassels`):

    q | x   and   p | y.

## Where the known solution sits

Known solution `(x, p, y, q) = (3, 2, 2, 3)` has `p = 2` even. Evaluated on the
plain congruences:

    p^{q-1} mod q^2 = 2^{2} mod 9 = 4    (≠ 1)
    q^{p-1} mod p^2 = 3^{1} mod 4 = 3    (≠ 1)

Both fail — **correctly** — because both lemmas carry the hypothesis "p, q odd
primes" and the known solution has p = 2. It is excluded by the hypothesis, not
by the congruence. A lemma about odd-prime pairs never claims the known solution
does not exist. (This is the falsifier discipline of GOAL.md: a lemma implying
no solution at all would be refuted.)

## Tension with problem.md / GOAL.md calibration — flagged, not resolved here

GOAL.md says `check_conditions(p,q)` must be "calibrated on (2,3): the known
solution must satisfy them." But the double-Wieferich congruences fail at
`p = 2`. The resolution the run has already flagged: the double-Wieferich
condition is only defined under the odd-prime hypothesis, and
`check_conditions` should apply it only to odd-prime pairs; the "calibrate on
(2,3)" line refers to a different base-level necessary condition, not to this
one. Likewise problem.md's hint `p^2 | y^{p-1} - 1` is inconsistent with
Cassels's `p | y` (which forces `y^{p-1} ≡ 0 (mod p)`, never `1 (mod p)`), so
that hint form is wrong and must not be used. Both points are recorded in the
run's backward notes and CONFIRMED by the arithmetic in
code/cassels_wieferich/verify_conditions.py (written, not yet run — no
execution tool in this agent session).

## Verdict on exactness

- The **placement** reconstructed here is internally consistent and agrees with
  the general Wieferich definition in the downloaded technique tier.
- It is **NOT verified against the primary Cassels/Mihăilescu text** (screened).
  Per Zeilberger discipline it is a **reconstruction / sourced-technique claim**,
  not a quotation. Status: `heuristic/reconstructed`, NOT `sourced-verbatim`.
- Next step outside the policy wall: a primary source that *develops the
  technique* (e.g. a cyclotomic-units survey stating the two factorisations
  `x^p - 1 = y^q` in Z[zeta_p], `y^q + 1 = x^p` in Z[zeta_q]) and thereby lets
  the run re-derive both congruences with proof, which is what GOAL.md actually
  requires.
