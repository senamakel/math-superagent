# Pattern-finder report — round 7: the C3 triangle-graph spectrum family

## What changed since round 6

Rounds 1–6 catalogued every *graph-level* family count (triangles, pentagons,
hexagons, outer blocks, distance-2, coclique bounds, eigenvalue multiplicities)
as a quartic-in-`u` closed form governed by `k = u²+u+2`, `v = 1+k²/2`, and the
`a = √(4k−7) | 63` integrality. None of those rounds ever tabulated the
**triangle-graph (C3) spectra across the family** — the eigenvalue sequences of
the 231-vertex (at 99) regular graph whose  vertices are the triangles. That is
genuinely new data, and its closed forms and the eigenvalue-gap structure have
not been recorded anywhere in the run.

## Finding 1 — the C3 spectrum family sequences (NEW, exact, derived)

For the family `srg(v,k,1,2)`, `k=u²+u+2`, `v=1+k²/2`, with graph eigenvalues
`r=u`, `s=−(u+1)`, Phillips eq 4.3 predicts the 3-clique graph C3(Γ) has:

```
d^1,  rt^m_r,  st^m_s,  (−3)^(nT−v)
d  = 3(k/2 − 1)                 (C3 degree)
rt = k/2 + r − 3 = (u−1)(u+4)/2
st = k/2 + s − 3 = (u−3)(u+2)/2
m_r, m_s = multiplicities of graph eigenvalues r, s
nT = vk/6                        (number of triangles / C3 vertices)
```

**Exact multiplicity closed forms** (checked, sympy derivation; the earlier
round's `f(r)=[4,54,132,3280,250914]`, `g(s)=[4,44,110,2992,243104]` carry
respectively rt and st):

```
m_r = u(u²+u+2)(u²+2u+3) / (2(2u+1))
m_s = (u+1)(u²+2)(u²+u+2) / (2(2u+1))
```

**The C3 −3 multiplicity:**
`nT − v = (u²+2)(u²+u−4)(u²+2u+3)/12`, family `[−3, 132, 648, 110823, 81348462]`.

**The multiplicity pairing (settled by direct spectrum computation on BvLS):**
the measured C3 spectrum of BvLS is `30^1, 12^132, 3^110, (−3)^648` — eigenvalue
12 (= rt, u=4) carries multiplicity 132 = m_r, and eigenvalue 3 (= st) carries
110 = m_s. A first cut had the pairing swapped; the direct computation fixes it.

**Family table (all exact):**

| u | k | v | C3 nT | d | rt^m_r | st^m_s | (−3)^(nT−v) |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 9 | 6 | 3 | 0^4 | −3^4 | −3 (degenerate: nT<v) |
| 3 | 14 | 99 | 231 | 18 | 7^54 | 0^44 | −3^132 |
| 4 | 22 | 243 | 891 | 30 | 12^132 | 3^110 | −3^648 |
| 10 | 112 | 6273 | 117096 | 165 | 63^3280 | 42^2992 | −3^110823 |
| 31 | 994 | 494019 | 81842481 | 1488 | 525^250914 | 462^243104 | −3^81348462 |

So the **99 triangle graph, if it exists, is a 231-vertex 18-regular graph with
spectrum `18^1, 7^54, 0^44, (−3)^132`** — a necessary spectral condition.

## Finding 2 — the C3 eigenvalue gap is the divisor-63 set (NEW, exact)

The gap between the two nontrivial C3 eigenvalues is exactly the a-parameter:

```
rt − st = 2u + 1 = a = √(4k−7)
```

family `[3, 7, 9, 21, 63]` — precisely the odd-divisors-of-63 set that
characterises the feasible family. This is a clean restatement of the integrality
characterisation on the *triangle graph* side: the C3 nontrivial eigenvalues are
separated by the same `a | 63` integer. It is a coherence fact (a consistency
identity), not a 99-specific contradiction: it holds for all five members
including the existing 9 and 243.

## Finding 3 — the predicted C3 spectra are valid regular-graph spectra (CHECKED)

Every predicted C3 spectrum has integer trace 0 and sum of squares = 2·edges =
`nT·d`, over all five family members. So there is no spectral obstruction at 99
at the level of "is the predicted spectrum a legitimate degree-regular graph
spectrum" — trace 0 and edge-count consistency hold exactly.

(`code/out/c3_spectrum_validity.py`; enumeration of the actual graph not
attempted — at 99 C3 is 231 vertices.)

## Sequences with no further structure

- rt family `[0,7,12,63,525]`, st family `[−3,0,3,42,462]`, −3-mult
  `[−3,132,648,110823,81348462]`: none is a low-order constant-coefficient
  linear recurrence (checked), none a low-degree polynomial (quartic-in-`u`
  growth). All are EXACTLY the closed forms above. The multiplicity sequences `[4,54,132,…]`, `[4,44,110,…]` reproduce the earlier `f(r)/g(s)`.
- **OEIS misses recorded:** `[0,7,12,63,525]`, `[−3,132,648,110823,81348462]`
  and `[0,7,12,63,525,525]` all MISS (no catalogued entry). Not catalogued, so
  no closed form is looked up; the structure comes from the problem.

## The connection to n3 and the sum-of-squares cap

The C3 degree-sum `nT·d` equals at each member the admissible n3 cap
`v·k(k−2)/4` computed in report 6 — e.g. at 99 both give 4158, at 243 both
26730. This is the same algebra (both are `v·k(k−2)/4`: the C3 sum-of-squares
term and the Reimbayev n1 coefficient). Not a new contradiction; a coherence
identity across two apparently separate counts.

## Bearing and honest status

- The C3 spectrum family is a **new, exact, complete** description of a quantity
  (the triangle-graph spectra) that prior rounds never tabulated. Its closed
  forms are derived, its multiplicity pairing is settled by direct measurement
  on BvLS, and every value is exact.
- It is **not** a nonexistence proof at 99: the predicted `18^1,7^54,0^44,(−3)^132`
  spectrum is a valid regular-graph spectrum (trace 0, sum-sq = 2|E|), and 9 and
  243 satisfy the same identities. As with every parameter-determined family
  sequence, a 99-graph's C3 would necessarily carry this spectrum, so it is a
  hard target for any construction/verification, not a lever that forces
  anything.
- The one genuinely 99-attuned observation is that the C3 eigenvalue gap equals
  `a = 7` at 99 (the a=7 member): any argument must be a=7-specific, consistent
  with the run's standing frontier.

## Files

- `code/out/c3_spectrum_sequences.py` — initial family sequence computation.
- `code/out/c3_spectrum_closed_form.py/.py3` — sympy closed forms (multiplicity
  pairing corrected in closed_form3).
- `code/out/c3_spectrum_table.py` — the final exact table.
- `code/out/c3_spectrum_check.py` — direct spectrum of rook + BvLS C3 graphs.
- `code/out/c3_spectrum_validity.py` — trace-0 / sum-of-squares validity check.
