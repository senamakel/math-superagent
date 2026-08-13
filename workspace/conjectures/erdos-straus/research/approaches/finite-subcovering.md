```approach
idea: Finite sub-covering by AP-identity families
mechanism: The extended sweep shows many residue classes k ≡ a (mod M) sit entirely inside {k : e(k)=0} — each such arithmetic progression is a subfamily for which x(k) = (n(k)+3)/4 is an identity, with the split 3/(n·x) = 1/y+1/z following from a prime q ≡ 2 (mod 3) dividing n(k)·(n(k)+3)/4 identically over the progression. Schinzel Theorem 1 forbids a single Z[x]-polynomial identity covering an entire open class, but does not forbid a finite union of identities each covering a sub-progression. The run's data already provides concrete candidate (r, M, a) rows; the task is to lift each from "observed on k ≤ 450" to "proved identity over the progression" and check whether the union covers all k for a given r — or at least a provable positive proportion.
status: proposed
precedent: none yet
first-step: Extract every (r, M, a) with e(k)=0 for all k ≡ a (mod M) within the 450-row sweep, verify each as a symbolic identity in k, and measure the union's density.
killed-by:
```