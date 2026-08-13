# Proof skeleton: backward from a failure

```skeleton
goal: Gilbreath's conjecture — for the iterated absolute-difference triangle of the primes, A_k(0) = 1 for all k ≥ 1.
implies: |
  Assume the conjecture fails. Let K be the first row index (K ≥ 2) where A_K(0) ≠ 1.
  By the reduction (DISCHARGED, gilbreath-reduces-to-second-in-02, second-entry-4-kills),
  A_K(0) ≠ 1 ⟺ A_{K-1}(1) ∉ {0,2}, i.e. A_{K-1}(1) ∈ {4,6,8,…}.

  The step law (DISCHARGED, step-law-theorem-proved) gives b_{k+1} ≥ b_k iff
  (edge, intruder) = (2,4), else b_{k+1} = b_k − 1. Since this is the FIRST failure,
  b_k ≥ 1 for all k < K. In particular b_{K-1} ≥ 1, and since A_{K-1}(1) ∉ {0,2},
  we must have b_{K-1} = 1 exactly — the block has eroded to a single entry at
  position 1, and that entry is not 0 or 2. (If b_{K-1} ≥ 2, then A_{K-1}(1) ∈ {0,2}
  by definition of the block.)

  So the failure configuration is: row K−1 has b_{K-1} = 1, A_{K-1}(1) ∈ {4,6,8,…},
  and A_{K-1}(0) = 1. Then A_K(0) = |1 − A_{K-1}(1)| = A_{K-1}(1) − 1 ≥ 3.

  Now the block lemma (DISCHARGED, odlyzko-block-lemma-exact) gives the backward
  structure: every entry in the {0,2} block of any row is a diagonal-subtriangle
  value determined entirely by the {0,2} entries of the initial row that anchors it,
  via the Rule 90 / Pascal-mod-2 evolution (DISCHARGED, rule90-interior-xor).

  The three gaps below trace this failure configuration backward through the
  triangle to a constraint on the initial prime row, and then show that constraint
  is incompatible with the primes.

  CB-dying-pair characterizes exactly what A_{K-1}(1) can be at the failure row.
  CB-backward-propagation traces the failing value back through the erosion run
  that led to b=1, using the drain law and the XOR edge evolution, to constrain
  entries in the initial prime row near the block boundary.
  CB-prime-exclusion proves that the constrained entries cannot occur in the
  actual prime gap sequence.

status: sketched
rests-on: gilbreath-reduces-to-second-in-02, second-entry-4-kills, step-law-theorem-proved, odlyzko-block-lemma-exact, rule90-interior-xor, closure-0d-double-edge
```

```gap
id: CB-dying-pair
lemma: |
  At the first failure row K, the dying row K−1 satisfies b_{K-1} = 1,
  A_{K-1}(0) = 1, and A_{K-1}(1) ∈ {4,6,8,…}. Let e = A_{K-2}(1) be the
  edge and y = A_{K-2}(2) be the intruder at row K−2. Then
  A_{K-1}(1) = |e − y|, and since b_{K-1} = 1, we have |e − y| ∉ {0,2}.
  By the step law, this means (e,y) ≠ (2,4) and also (e,y) is not any
  pair giving a difference in {0,2}. Specifically the possibilities are:

  - e = 0: then |0 − y| = y, so y ≥ 4 and y ≠ 4? No: y = 4 gives |0−4| = 4
    which is the failure. y = 6 gives |0−6| = 6, etc. All y ≥ 4 work.
  - e = 2: then |2 − y| ∉ {0,2}. This means y ≠ 0,2,4. So y ≥ 6.

  Characterise the full set of (e, y) pairs at row K−2 that lead to failure
  at row K−1. Then determine which of these can actually be reached from a
  prior row with b_{K-2} ≥ 2, using the drain law and the XOR edge evolution
  (DISCHARGED, step-law-theorem-proved, rule90-interior-xor).

status: open
next: |
  Enumerate all (e, y) ∈ {0,2} × {0,2,4,6,8,…} such that |e−y| ≥ 4.
  Then trace each backward one step: what (e', y') at row K−3 with
  b_{K-3} ≥ 2 could produce this (e, y)? Use the drain law
  y_{k+1} = y_k − 2·[x_k=2] and the XOR edge rule. A sat_solver task:
  encode the backward constraint system for depth 3 and ask whether any
  dying pair is reachable from b ≥ 2.
```

```gap
id: CB-backward-propagation
lemma: |
  Trace the failure configuration backward through the full erosion run
  that reduced the block from its last regeneration to b = 1.

  At the last regeneration before failure (say at row R < K−1), we have
  (edge, intruder) = (2,4), b_R ≥ 1, and b_{R+1} ≥ b_R (jump j ≥ 0).
  After that, the block erodes by 1 per row for d = K−1−R rows until
  b_{K-1} = 1.

  During these d erosion rows, the edge evolves by the XOR rule
  (DISCHARGED, rule90-interior-xor): at depth t into erosion (0 ≤ t < d),
  the edge x_{R+t} = A_{R+t}(b_{R+t}) has halved value
  h_t = XOR_{j: binom(t,j)=1 mod 2} h_init[p+j] where h_init is the
  halved {0,2} block of row R and p is the edge position relative to the
  block start. The intruder drains by the drain law
  (DISCHARGED, step-law-theorem-proved): y_{R+t+1} = y_{R+t} − 2·[x_{R+t}=2].

  For the block to die at K−1, we need:
  - b_{K-1} = 1: this means d = b_R − 1 + (something from jump), i.e. the
    erosion consumed all but the last block entry.
  - At row K−2 (the last erosion row), (x_{K-2}, y_{K-2}) must be a dying
    pair from CB-dying-pair.

  The backward constraint: at row R, we know the full halved block pattern
  (length b_R, values in {0,1}) and the initial intruder y_R = A_R(b_R+1).
  After the regeneration at R, the intruder at R+1 is some value y_{R+1}
  (DISCHARGED: tracked in depth-1000 data). The erosion run of length d
  with edge flips at specific rows maps this to a dying pair.

  Prove: for the prime triangle, this backward constraint forces a
  specific pattern in the initial prime gaps (row 1, positions near b_R)
  that involves a long stretch of halved gaps whose XOR over binom(t,·)
  windows is all-zero for many consecutive t.

status: open
next: |
  From the depth-1000 data, extract the 26 erosion runs. For each run,
  record: the halved block at start, the initial intruder, the sequence of
  (edge, intruder) pairs across the run, and the run length. Verify that
  no run ends with b=1 and a dying pair. Then formalize: if a dying pair
  did occur at the end of an erosion run, what XOR constraints on the
  halved block does that impose? A tool_builder task:
  code/gap_analysis/erosion_run_dying_check.py.
```

```gap
id: CB-prime-exclusion
lemma: |
  The constrained initial pattern derived in CB-backward-propagation —
  a stretch of consecutive halved prime gaps whose XOR over binom(t,·)
  windows is all-zero for t = 0,1,…,d−1, at a specific alignment —
  cannot occur in the actual prime gap sequence for any stretch length
  exceeding some absolute bound L.

  Equivalently: the halved prime gaps are "XOR-non-degenerate" — no
  window of length W has the property that every binom(t,·)-kernel
  XOR of that window is 0 for t = 0,…,W−1 at a given alignment.

  This is a structural property of the primes. It is plausibly provable
  from known results on prime gaps (e.g., that prime gaps are not all
  multiples of some small modulus, that they contain 2 infinitely often,
  etc.) or from the 2-separation hypothesis (DISCHARGED in the general
  class, conjectural for primes).

  A weaker but sufficient form: the primes contain gaps ≡ 2 mod 4
  infinitely often and with bounded gap between occurrences, which forces
  the halved XOR pattern to have 1s frequently enough.

status: open
next: |
  Check empirically: in the depth-1000 data, what is the longest stretch
  of halved prime gaps whose XOR over consecutive binom(t,·) kernels
  (t = 0,1,2,…) is all-zero at the same alignment? If the maximum is
  small (say ≤ 10), then CB-prime-exclusion holds numerically to depth
  1000. A tool_builder task:
  code/gap_analysis/halved_xor_degeneracy.py.

  Theoretical: connect this to known results. The halved prime gap is
  (p_{n+1} − p_n)/2 − 1 for n ≥ 2 (CHT normalization). Ask
  request_research: what is the longest run of consecutive prime gaps
  all ≡ 0 mod 4? This gives consecutive halved gaps all ≡ 1 mod 2, i.e.
  halved bit = 1 — the opposite of what we need, but the same kind of
  question. The literature on prime gap residues mod 4 should bound
  such runs.
```