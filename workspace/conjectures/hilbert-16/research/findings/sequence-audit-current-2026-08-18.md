# Exact sequence audit — current pass

Read existing sequence artifacts and reran `python code/sequence_deeper_audit.py`.

Computed focal monomial counts:
`a_d = [4,30,97,236,485,890,1505]` for `d=4,6,...,16`.
Complements `c_h = binomial(h+4,4)-2a_d`, `h=d-2`, are
`[7,10,16,23,31,40,50]` for `h=2,4,...,14`.

Exact tool results: neither sequence is a low-degree polynomial over supplied terms;
`find_linear_recurrence` finds no constant-coefficient recurrence of order <=6 for
`c_h`; custom exact linear solves find no order 1..3 recurrence for `a_d`.
OEIS misses both sequences. These are observations, not proofs of nonexistence of
other structure.

The candidate
`c(h)=(h^2+14h+8)/8`
reproduces exactly h=4,6,8,10,12,14 and fails at h=2 (actual 7, predicted 5).
Thus it remains a conjecture only. Its first uncomputed falsifier is h=16 (d=18),
where it predicts `a_18=2392`; a larger run would settle that specific next term.
The existing exhaustive signed-permutation involution probe refutes the natural
symmetry-support explanation (all 312 signed-permutation involutions; no full match).

The denominator sequence `[8,192,18432,1105920,22295347200,37456183296000]` has
exact valuation pairs `(v2,v3)=[(3,0),(6,1),(11,2),(13,3),(19,5),(23,6)]` and odd
parts `[1,1,1,5,175,6125]`; no exact regularity was established.
