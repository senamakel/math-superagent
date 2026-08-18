Solve by computational commutative algebra, with the mathematics carried in
Lean wherever it will go. The object is a **locally nilpotent derivation** `D`
on `k[x_1, …, x_n]`, and the question is always about `ker D`: whether it is
finitely generated, what its generators are, and what invariant separates the
kernels that are from the kernels that are not.

Reason about *that kernel*. The instruments are the degree function and its
associated filtration, the plinth ideal and the image ideal `D(k[x]) ∩ ker D`,
local slices and the Dixmier map, the rank and corank of `D`, the Makar-Limanov
and Derksen invariants, and the van den Essen algorithm for computing a kernel
by a Gröbner basis in an extended ring. A candidate counterexample is a
derivation whose kernel has an infinite minimal generating set with a provable
degree pattern; a candidate theorem is a bound on generator degrees that a
slice-free dimension-4 derivation must satisfy.

**Prefer the argument a computer algebra system can finish and Lean can check.**
Given two routes to the same partial result, take the one whose core is an ideal
membership, a Gröbner basis over `Q`, a resultant vanishing or a finite case
split on a degree pattern, over the one ending in a paragraph. State every claim
as a Lean type before spending an attempt on it; where Mathlib cannot carry
locally nilpotent derivations or invariant subalgebras yet, state the missing
notion under `code/lean/Lib/` and record what is absent — **which parts of this
subject are statable in today's Mathlib is itself a reportable finding.**

Three cautions this problem earns before any work starts.

**A non-terminating Gröbner computation proves nothing.** It is the shape of
every wrong claim available here: *the kernel is not finitely generated because
the program did not finish*. Every computational claim states its ceiling — the
degree reached, the wall clock, the memory — and is labelled a measurement. An
infinite minimal generating set is established by exhibiting the pattern and
proving it.

**Finite generation of the kernel and triviality of the action are different
statements**, and characteristic zero and characteristic `p` are different
subjects. Every cited result must be checked for which it is about; quoting a
positive-characteristic record into the characteristic-zero frontier is the most
likely way a claim here is silently wrong.

**Dimension is the whole content.** Test every argument at `n = 5`, where a
counterexample exists, and at `n = 3`, where finite generation is a theorem. An
argument that does not distinguish those two has not engaged the problem.
