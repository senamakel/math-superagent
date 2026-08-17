# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `Boundary.lean` | Formal statement of the open run gap G-nonfibonacci-pairs-are-bounded and its two supporting lemmas (column injectivity for C(n,k)=a at n>=2k; the counting identity N(a)=2*H(a)+2 under the run's both-mirrors-plus-trivial convention). All three end in := by sorry (recorded statements, not proofs); the `#print axioms` census names exactly the three `sorryAx` holes. Verdict: compiles, statements elaborate, not formalised — intended. Kept faithful to the informal lemma: boundary cut T(n)=exp((log n)^(2/3+eps)), both left-half boundary reps, pair {k1,k2} with 2<=k1<k2 excluded if k2=k1+1 (Fibonacci/Pell family), Claim is finiteness of the remaining boundary-collision pair set. |
| `Statement.lean` | Lean formalisation of Singmaster's conjecture: the `occurrences` set (all (n,k) with 0≤k≤n, C(n,k)=a, both mirrors + trivial pair), `N a` via Set.ncard, and the theorem `singmaster_conjecture : ∃ B, ∀ a, 1<a → N a ≤ B` ending in `:= by sorry`. Elaborates under the both-mirrors-plus-trivial convention (N(3003)=8). |
| `Statement.md` | Prose companion to Statement.lean: the lean_check verdict verbatim, what the theorem means, the both-mirrors-plus-trivial counting convention (N(3003)=8), and where the statement could differ from problem.md (genus/Faltings/effectivity route is out of scope for the statement; ncard returns 0 on infinite sets). |
