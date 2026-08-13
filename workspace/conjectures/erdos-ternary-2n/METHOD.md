The 3-adic route is CLOSED, by this run's own theorem. Do not reopen it.

A previous run of this workspace proved `|A_k| = 2^(k-1)` for every `k`, where
`A_k` is the set of residues mod `2·3^(k-1)` whose low `k` ternary digits of
`2^r mod 3^k` lie in `{0,1}`. See `code/out/lifting_theorem.md` and the claim
`ternary-lifting-theorem` (status proved), confirmed independently by a
bijection argument — `2` is a primitive root mod `3^k`, so `r ↦ 2^r` hits each
of the `2^(k-1)` digit-free units exactly once — and by direct sieving to
`k = 26`. The sieve set **doubles at every level and never empties**, so no
congruence modulo any power of 3 can settle this conjecture at any finite
precision. The earlier version of this file prescribed exactly that route; it
was answered and it lost. Reproducing it is the one guaranteed waste available
here.

Note also that the count is not new: Narkiewicz (1980) obtained it by this
argument, and it is what yields `N(x) ≤ 1.62·x^(log_3 2)`. It is recorded here
as `STOLL-1`. Do not present it as a discovery.

Solve instead by coupling the two digit ranges that no existing method sees
together. Lagarias states the gap precisely (`LAG-4`): the real/truncated method
constrains only the top `~log_3 X` ternary digits of `2^n`, the 3-adic method
only the bottom `~log_3 X`, and neither touches the middle. Every known
approach, including the one just closed, lives entirely in one end. Reason about
what forces consistency between the two ends — the orbit `{2^n}` is dense in
`Z_3^*`, so the conjecture is exactly that this dense orbit meets the 3-adic
Cantor set of digit-free elements only at `{1, 4, 256}`, and a proof must see
the whole expansion at once rather than either end of it.

Two concrete lines, both starting from results already in this workspace:

Push the digit-count constraint. Dimitrov-Howe (`DH-1`, proved) gives that any
`2^x` with `x ∉ {0,2,8}` has a digit 2 or at least 26 digits equal to 1.
Combined with digit-freeness, any counterexample has **no 2s and at least 26
ones**. State exactly what that leaves open — how many ones, over what range of
`x`, and what a strengthening from 26 to a function of `x` would require. If the
26 can be made to grow with `x`, the conjecture follows; say what blocks that.

Push the density and dimension bounds. `LAG-2`, `LAG-3`, `AL-I-2` and `ABL-II-1`
give Hausdorff-dimension bounds on the exceptional set, with `dim_H E(Z_3) ≤ Γ ≤
log_3 φ ≈ 0.438`. Lagarias' Conjecture B is that the dimension is 0. Establish
what a proof of dimension 0 would and would not give for the thin sequence
`2^n`, since a dimension statement about a set is not a statement about which
integers lie in it — that distinction is the trap in this direction.

Formalise what is already proved. The lifting theorem is short and elementary
and is exactly the shape Lean 4 handles well: the order of 2 mod `3^k`, the
primitive-root bijection, and the 2-to-1 lifting. A machine-checked version is
worth having and is a bounded, finishable task. Report `#print axioms` output
and every remaining `sorry`; a Lean file asserted to be kernel-checked with no
artifact beside it is worth nothing.

Three cautions this problem has already earned:

A density statement about all integers whose ternary expansion avoids 2 does not
reach the thin sequence `2^n`. Neither does the independent-uniform-digits
heuristic, which gives `(2/3)^k` and explains only why the conjecture is
believed. Both are true and irrelevant; record them as heuristics and never as
proof.

The deliverable is non-existence for `n > 8`, so the failure mode is an argument
that proves too much. Every claimed obstruction must be run against the
witnesses `n = 0, 2, 8` using `digit_free` from the oracle. A lemma that forbids
`2^8 = 100111_3` is false and is recorded as refuted, not weakened. A lemma not
run against the witnesses is `asserted`, never `checked`.

On compute: work modulo `3^k` and never materialise `2^n` for large `n` — that
is the trap this problem sets, since `2^n` has about `0.63·n` ternary digits.
**Do not re-sieve past `k = 26`.** `A_k` is materialised as a set, the count is
now a proved theorem rather than something to measure, and `k = 30` would OOM
against the 8 GiB container cap for no information. The box has 28 CPUs and the
container has no CPU quota; `code/lib/parallel.py` with `code/lib/PARALLEL.md`
is in this workspace. Say in every captured output how many workers ran and what
range was covered — a result without its bound is not a result.
