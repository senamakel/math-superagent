# Established facts on Singmaster's conjecture — verified against primary sources

Convention note: `N(a)` counts all `(n,k)` with `0<=k<=n`, `C(n,k)=a` (both `k` and `n-k` counted). Every claim below that quotes a numeric multiplicity uses this convention unless stated.

## The conjecture and its statement (Singmaster 1971)

- Sourced: Wikipedia entry; MRSTT arXiv:2106.03335; Jenkins arXiv:1411.4111; de Weger JNT 63 (1997).
- `N(a) = #{ (n,k) : 0<=k<=n, C(n,k)=a }`. Only `a=1` occurs infinitely often; any other `a` appears only within the first `a+1` rows (proved trivially: if `C(n,k)=a` then `n<=a`; source Wikipedia).
- Conjecture: `N(a) = O(1)`. Believed true; usual guess `B=8`.

## The witness set: 3003 appears eight times (counting both halves)

- `3003 = C(3003,1) = C(78,2) = C(15,5) = C(14,6)` and mirrors `C(3003,3002)=C(78,76)=C(15,10)=C(14,8)`.
- Sourced: MRSTT (eq 1.2 lists all 8 explicitly); Singmaster Fibonacci Quarterly 13 (1975); Wikipedia; de Weger.
- **This is the falsifier for the run**: any claimed uniform bound `< 8`, or any lemma implying one, is refuted. In the half-triangle convention (`k<=n/2`) these are 4 occurrences (3003,1), (78,2), (15,5), (14,6).

## Known bounds (all grow with `a`; none uniform)

- Singmaster 1971: `N(a) = O(log a)`.
- Abbott–Erdős–Hanson 1974: `N(a) = O(log a / log log a)` (AEH also: average and normal order of N is 2; number of `a<=x` with N(a)>=3 is `O(x^{1/2})`).
- Kane 2004: `O(log t log log log t / (log log t)^2)`.
- Kane 2007 (best unconditional): `N(t) = O( (log t)(log log log t) / (log log t)^3 )`.
- Conditional on Cramér's conjecture (AEH): `N(t) = O_eps((log t)^{2/3+eps})`.
- Sourced: Wikipedia "Known bound" section; MRSTT introduction; Jenkins introduction quotes Kane's best bound identically.
- **These all grow with `a`. The conjecture asserts constancy — reproducing one is not a result.**

## MRSTT (2021/2022): Singmaster's conjecture in the interior

- Source: arXiv:2106.03335 (Quart. J. Math. 73 (2022) 1137–1177); Tao's blog.
- Theorem 1.3: For fixed `0<eps<1`, `t` sufficiently large depending on `eps`, there are at most TWO solutions to `C(n,m)=t` in the region `exp(log^{2/3+eps} n) <= m <= n/2` (left half), hence at most FOUR in `exp(log^{2/3+eps} n) <= m <= n - exp(log^{2/3+eps} n)`.
- Refinement: at most ONE solution in `exp(log^{2/3+eps} n) <= m <= n/exp(log^{1-eps'} n)` when `0<eps' < eps/(2/3+eps)`.
- Bound of two is best possible: the infinite Fibonacci-family solutions `C(n+1,m+1)=C(n,m+2)` lie in this interior (Lind/Singmaster/Tovey family).
- Remark 1.5: to prove the conjecture it suffices to handle `2 <= m <= exp(log^{2/3+eps} n)`, equivalently `2 <= m <= log t / log_2^{3/2-eps} t`. **This is the exact boundary of what MRSTT leaves open.**
- Remark 1.7: the implied "t sufficiently large" constants ARE effective, but far too large for numerical verification.
- Theorem 1.8: falling factorial analogue — at most two solutions in the interior.
- Also stated: de Weger's Conjecture (no nontrivial collisions beyond a list) would imply the full conjecture; verified for many (m,m') and for `n<=10^6` or `t<=10^60` (Blokhuis–Brouwer–de Weger 2017).

## The infinite family with N(a) >= 6 (constraint on B>=6)

- Source: Singmaster Fibonacci Quart. 13 (1975); Lind 1968; Tovey 1985; Wikipedia; MRSTT Remark 1.4; de Weger.
- The Diophantine equation `C(n+1,k+1) = C(n,k+2)` has infinitely many solutions: `n = F_{2i+2} F_{2i+3} - 1`, `k = F_{2i} F_{2i+3} - 1` (i=1,2,...). Equivalent Pell-type equation `u^2 - 5v^2 = -4`.
- This gives infinitely many `a` with `N(a) >= 6`. First members: 3003 (i=1), then `a = 61218182743304701891431482520 = C(104,39)=C(103,40)` (i=2).
- **Any proof giving B<6 is refuted.** Counted in half-triangle convention, these are 4 occurrences for the "at-least-6" family? No: the six occurrences are `C(a,1)`, `C(a,a-1)`, `C(n+1,k+1)`, `C(n+1,n-k)`, `C(n,k+2)`, `C(n,n-k-2)`.
- The equation has been completely solved: Lind/Singmaster/Tovey. Also `C(n+1,k+1)=C(n,k+2)` is the ONLY curve in the Jenkins family `C(x,y)=C(x-a,y+b)` with a=b=1 that has infinitely many lattice points.

## Small-k curves (effective work; the Diophantine target)

- `C(n,2)=C(m,3)`: completely solved by Avanesov (1966/67) via Skolem's method. Elliptic curve, rank 2.
- `C(n,2)=C(m,4)`: solved by de Weger (Quart. J. Math. 47 (1996)) and Pintér (1995), via Gelfond–Baker method. Elliptic curve, rank 2.
- `C(n,3)=C(m,4)`: essentially solved by Mordell (1963) y(y+1)=x(x+1)(x+2); curve has genus 3 (Faltings applies), double cover of elliptic curve Y^2+Y=X^3-X. de Weger 1997 gives all integral solutions; Conjecture B for rational solutions.
- `C(n,2)=C(m,5)`: solved by Bugeaud–Mignotte–Siksek–Stoll–Tengely 2008 (hyperelliptic curves).
- Finiteness for each fixed `(m,m')`: Beukers–Shorey–Tijdeman, via Siegel's theorem on integral points. **Effective? No — relies on Siegel, ineffective.** Kiss 1988: `C(x,2)=C(y,p)` finite for p prime.
- Sourced: MRSTT Remark 1.4/1.5 references; de Weger 1997 full text; Jenkins.

## Jenkins 2014: the curve/genus reformulation (the method this run is asked to pursue)

- Source: arXiv:1411.4111 full text.
- Equation `C(x,y)=C(x-a,y+b)` = curve `prod_{r=0}^{a+b-1}(x-y-r) - prod_{p=0}^{a-1}(x-p) prod_{q=1}^{b}(y+q) = 0`.
- Theorem: if `a != b`, finitely many natural solutions (proved via limiting ratio x/y being non-quadratic, ruling out Nagell–Maillet parametrization; NOT via Siegel/genus, which the author could not push through for the general family).
- For the `a=b` case excluding (1,1): the limiting ratio is the golden-ratio-like quadratic; the author could not rule out infinite lattice points — open. (This is exactly the Singmaster family.)
- Gives the framing: multiplicity of 6 = common integral intersection of two curves; multiplicity 8 = three curves meeting; general effective Siegel or effective Schmidt subspace theorem would give effective heights.
- **Faltings/Siegel give finiteness for each pair (already known) with NO computable count — the uniform-in-(k1,k2) obstruction is precisely what GOAL.md warns about.**
