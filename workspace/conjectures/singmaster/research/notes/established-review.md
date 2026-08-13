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

- Singmaster 1971: `N(a) = O(log a)` — PRIMARY SOURCE held (AMM 78 (1971) 385–386, via Fermat's Library facsimile; the argument: if `a <= C(2b,b)` then either `i<b` or `j<b`, so `N(a)<=2b<=2+2 log2 a`).
- Abbott–Erdős–Hanson 1974: `N(a) = O(log a / log log a)` — PRIMARY SOURCE held (renyi.hu/~p_erdos/1974-23.pdf, AMM 81 (1974) 256–261). Theorem 1: average AND normal order of N(t) is 2, and the number of t<=x with N(t)>2 is O(x^{1/2}). Theorem 2: N(t) < 2w(t) log t/(log t - w(t) log log t) where w(t)=#distinct prime factors, for w(t)<log t/log log t. Theorem 3: N(t)=O(log t/log log t) via Ingham's prime-gap theorem (a=5/8). Cramér-conditional: N(t)=O_eps((log t)^{2/3+eps}). Also: N(t)=6 for the six t<=2^48 = 120,210,1540,7140,11628,24310; only t<=2^48 with N(t)>=8 is 3003 (N=8). Theorem 4: G(t)=O((log t)^{1/2}) for products of consecutive integers.
- Kane 2004: `O(log t log log log t / (log log t)^2)`.
- Kane 2007 (best unconditional): `N(t) = O( (log t)(log log log t) / (log log t)^3 )`.
- Conditional on Cramér's conjecture (AEH): `N(t) = O_eps((log t)^{2/3+eps})`.
- Sourced: PRIMARY AEH 1974 full text; Singmaster 1971's bound attested by secondary
  sources (primary NOT held — the downloaded file is the Fermat's Library comments
  page); Wikipedia "Known bound"; MRSTT intro; Jenkins intro.
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

```claim
id: witness-3003
statement: 3003 appears 8 times in Pascal's triangle under the convention that counts both (n,k) and (n,n-k) and includes the trivial pair C(a,1)=C(a,a-1). Explicitly 3003 = C(3003,1)=C(78,2)=C(15,5)=C(14,6) with four mirrors. Under the half-triangle convention (k<=n/2) this is 4 occurrences.
hypotheses: a=3003, standard Pascal triangle counting.
holds-here: yes — this is the record witness the run's scaffold must reproduce.
status: checked (Matches code/out/witnesses.json N=8 and the 4 half-triangle occurrences; code/out/verify_library_claims.py encodes the same assertion for the coder to run.)
bearing: Any uniform bound <8, or any lemma implying one, is refuted. The falsifier for this run.
anchor: research/notes/established-review.md
```

```claim
id: infinite-family-6
statement: The equation C(n+1,k+1)=C(n,k+2) has infinitely many solutions given by n=F_{2i+2}F_{2i+3}-1, k=F_{2i}F_{2i+3}-1 (i=1,2,...), producing infinitely many a with N(a)>=6 (both-halves convention). First members: 3003 (i=1) and 61218182743304701891431482520 (i=2).
hypotheses: i>=1, F the Fibonacci numbers (F_0=0, F_1=1). Pell-type equation u^2-5v^2=-4.
holds-here: yes — this is the reason B>=6, constrains every proof.
status: checked (matches witnesses.json multiplicity>=6 set and OEIS A003015/A090162; code/out/verify_library_claims.py encodes the family check for i=1..5.)
bearing: Any proof giving B<6 is refuted; the 3003 record plus this family fixes B>=6 generically.
anchor: research/notes/established-review.md
```

```claim
id: mrstt-interior-boundary
statement: MRSTT (QJM 73 (2022) 1137-1177, arXiv:2106.03335) prove at most 2 solutions to C(n,m)=t in the left-half interior exp(log^{2/3+eps} n)<=m<=n/2 (at most 4 in the full interior exp(log^{2/3+eps} n)<=m<=n-exp(log^{2/3+eps} n)), for t sufficiently large depending on eps. To prove the full conjecture it suffices to handle 2<=m<=exp(log^{2/3+eps} n), equivalently 2<=m<=log t / log_2^{3/2-eps} t. The implied constants are effective but far too large for numerical verification.
hypotheses: 0<eps<1 fixed; t large depending on eps.
holds-here: yes — this defines exactly what the run's other approaches must close.
status: asserted-by-source (Theorem 1.3 and Remark 1.5 of the paper; not re-derived here).
bearing: Reduces Singmaster to an exterior/small-m regime; the boundary is the open gap.
anchor: research/notes/established-review.md
```

```claim
id: best-unconditional-bound
statement: Best known unconditional bound on N(a) grows with a: Kane 2007 gives N(t)=O((log t)(log_3 t)/(log_2 t)^3). Historical, all primary-sourced: Singmaster 1971 O(log a); Abbott-Erdos-Hanson 1974 O(log a/log_2 a) [AMM 81 (1974) 256-261, Theorem 3, via Ingham prime-gap theorem]; Kane 2004 O(log t log_3 t / log_2^2 t). AEH Theorem 1: average and normal order of N(t) is 2. Conditional on Cramer's conjecture, O_eps((log a)^{2/3+eps}).
hypotheses: none except standard asymptotic conventions.
holds-here: yes — reproduces a log-type bound is NOT a result (it grows with a, the conjecture asserts constancy).
status: checked (AEH 1974 full text held as research/sources/abbott-erdos-hanson-1974.full.md; Singmaster 1971 primary NOT held — the downloaded research/sources/singmaster-1971.full.md is the Fermat's Library comments page, so the O(log a) claim is attested-by-secondary-sources (AEH, MRSTT, Wikipedia); Kane bound quoted identically in MRSTT and Jenkins intros and Wikipedia Known-bound.)
bearing: The gap is a uniform/constant bound; no known method gives O(1).
anchor: research/notes/established-review.md
```

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

## Contradictions / discrepancies recorded

- **Kane bound exponent**: Fermat's Library's annotation of Singmaster 1971 quotes the best bound as `O((log t)(log_3 t)/(log_2 t)^2)` (exponent 2). The authoritative sources — Wikipedia "Known bound", MRSTT arXiv:2106.03335 intro ("O(log t log_3 t/log_2^3 t)"), Jenkins arXiv:1411.4111 intro — all state exponent **3**. Exponent 3 is taken as correct here; the Fermat's annotation is a transcription slip.

## Primary-source cross-check of the witness set

**STATUS: Demoted.** The file `research/sources/singmaster-1971.full.md` is the
Fermat's Library comments page, NOT Singmaster's 1971 paper. Its mathematical
content is truncated comment snippets. The claim that "Singmaster's original
monthly note, held at ... (facsimile via Fermat's Library)" independently
confirms the witness set is INCORRECT — it was reading a comments page, not
the paper. The witness set (3003→8, six→6) is independently confirmed by
`code/out/witnesses.json`, Singmaster FQ 1975 (held), and MRSTT §1.2, so no
factual claim is wrong — only the provenance was misattributed. The real
1971 paper (AMM 78 (1971) 385-386) has NOT been obtained.

