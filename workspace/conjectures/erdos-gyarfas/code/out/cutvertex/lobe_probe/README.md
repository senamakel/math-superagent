# Lobe probe — (2,2) cut-vertex shape

Question (Phase-4 structural candidate, Cut-Vertex Characterization): in a
minimal counterexample G with a cut vertex split into k=2 lobes of type
(d_1,d_2)=(2,2) (central vertex degree 4), each lobe L_i must be
power-of-two-free and take the shape *L = H − e + v* where H is connected
cubic, e an edge, v a fresh degree-2 vertex adjacent to the two endpoints of e.

## The probe

For every connected cubic graph H on n_H = 4..18 (nauty-geng `-q -c -d3 -D3`,
counts asserted equal to A002851: 1, 2, 5, 19, 85, 509, 4060, 41301) and
every edge e of H, form L = H − e + v and test L for a cycle of length 4 or 8
(16 is impossible since |L| = n_H + 1 ≤ 19).

## Headline result

**ZERO power-of-two-free lobes.**  Every lobe L = H − e + v with H connected
cubic on n_H ≤ 18 vertices contains a C4 or a C8.

Per n_H (cubic | constructions | with-C4 | with-C8 | pow2-free):

| n_H | cubic | constr. | with-C4 | with-C8 | pow2-free |
|----:|------:|--------:|--------:|--------:|----------:|
| 4   | 1     | 6       | 6       | 0       | 0 |
| 6   | 2     | 18      | 18      | 0       | 0 |
| 8   | 5     | 60      | 59      | 60      | 0 |
| 10  | 19    | 285     | 250     | 265     | 0 |
| 12  | 85    | 1530    | 1387    | 1467    | 0 |
| 14  | 509   | 10689   | 9826    | 10559   | 0 |
| 16  | 4060  | 97440   | 89834   | 96798   | 0 |
| 18  | 41301 | 1115127 | 1025689 | 1112200 | 0 |

Consequence: **no glued (2,2)-shaped (central degree-4 cut-vertex)
counterexample candidate of this lobe form exists with glued order
|H1|+|H2|−1 ≤ 35** (the pair search is vacuous below order 38).

## How the zero is established (two independent routes)

1. **Early-exit** `has_cycle_of_length(L, 4/8)` on every construction.
2. **Full enumeration** `distinct_cycle_lengths` — complete over all 12,588
   constructions for n_H ≤ 14, sampled (45,252 constructions) over 16/18.
   pow2-free = 0 in both.

Plus a separate 534-construction spot check on n_H ≤ 14 with full
enumeration AND networkx.simple_cycles (which always agree with the oracle).

## Glue machinery validation (so J3 is trusted when lobes finally appear)

`lobe_glue_machinery.py`: 2500 pairs of arbitrary lobes glued by identifying
their v-vertices.  On every pair:
- central vertex degree 4, all other degrees ≥ 3, connected, node
  connectivity exactly 1  → ALL PASS
- oracle cycle set == networkx simple_cycles set  → AGREE
- **no-cross-cycles identity**: glued cycle set == union of the two lobe
  cycle sets  → HOLDS on all 2500 pairs.

## Files

- `code/cutvertex/lobe_probe.py` — the probe (J1 + J2 + exhaustive
  re-verification + J3 pair search).
- `code/cutvertex/lobe_glue_machinery.py` — independent glue-route validator.
- `code/out/cutvertex/lobe_probe/lobe_probe.log` — full numeric log.
- `code/out/cutvertex/lobe_probe/pow2free_lobes.txt` — empty (as expected).
- `code/out/cutvertex/lobe_probe/glued_pairs.txt` — empty (as expected).

## Interpretation / caveats

- This is a **negative result for the prescribed lobe form**: it says the
  (2,2) cut-vertex shape cannot be built, from cubic-base lobes in this range,
  into a 1-connected δ≥3 pow2-free graph of order ≤ 37.  It does not rule
  out the shape in general.
- **Form caveat.**  The task prescribes L = H − e + v with H *cubic*, which
  forces every inner vertex to have degree exactly 3 and the two v-neighbours
  to be non-adjacent.  A general (2,2) lobe may instead have inner vertices
  of degree ≥ 4, or adjacent v-neighbours (then the preimage graph H is not
  simple-cubic and the probe does not cover it).  The zero bound is
  form-specific.
- **Boundary left open:** the first pow2-free lobe of this form, if it
  exists, sits at n_H = 20 (~510K cubic graphs, ~15M constructions).
  Computing it would settle whether the (2,2) shape is ever realisable at
  all from cubic bases — a natural next step, not run here.
