# Morris & Soltan 2000, "The Erdős–Szekeres problem on points in convex position", BAMS 37(4), 437–458

Source: https://www.ams.org/journals/bull/2000-37-04/S0273-0979-00-00877-6/S0273-0979-00-00877-6.pdf
Full text: [[morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full]]

Authoritative survey of the planar problem and its higher-dim/abstract generalizations.

## What it establishes (planar ES)

- **Thm 2.2:** ES(n) exists (finiteness), attributed to ES 1935, Ramsey.
- **Thm 2.3:** $f(k,l) \le \binom{k+l-4}{k-2}+1$ via the recurrence
  $f(k,l)\le f(k-1,l)+f(k,l-1)-1$ (sketch: let $Y$ be left endpoints of $(k-1)$-cups; known
  cup/cap addition argument). Then $ES(n)\le f(n,n)=\binom{2n-4}{n-2}+1$.
- **Thm 2.4 (Tóth–Valtr):** $ES(n) \le \binom{2n-5}{n-3}+2$. Proof via projective transform: pick
  extreme point $a$, a point $b$ outside conv so no line determined by $X\setminus\{a\}$ meets
  $[a,b]$, and a line $l$ through $b$ avoiding conv; the transform sends $l$ to the line at
  infinity and $[a,b]$ to a downward vertical ray, turning "any subset containing $a$ is convex"
  into "its image is a cap". Then $\binom{2n-5}{n-3}+2$ points give an $(n-1)$-cap or $n$-cup.
- **Thm 2.5:** $f(k,l)=\binom{k+l-4}{k-2}+1$ exactly (tightness; the $A\cup B$ gluing construction
  with the slope condition (ii) that any line $A$–$B$ is steeper than within-block lines). So the
  ~$4^n$ bound is the square of the truth; loss is in the reduction to cups/caps.
- **Thm 2.6 (ES 1961):** $ES(n)\ge 2^{n-2}+1$. Recursive construction: $T_i$ ($\binom{n-2}{i}$
  points) with no $(i+2)$-cap and no $(n-i)$-cup, slopes bounded by 1; small copies near the unit
  circle at angles $\frac{\pi}{4}-\frac{i\pi}{2(n-2)}$; union has $2^{n-2}$ points; a convex subset
  uses at most $k+1+(l-k-1)+(n-l-1)=n-1$.
- **Thm 2.7:** ES(5)=9. Nine points with no convex pentagon must be one of (4,4,1),(4,3,2),
  (3,4,2),(3,3,3) (layer-count tuples); a subset of 8 is (4,3,1) or (3,3,2); Lemma 2.8 shows any
  (3,3,2),(4,3,1),(3,4,2) set determines a convex pentagon.
- **§2.4 (Question 1.3):** ES(6)=17 was open as of this survey (2000). Notes a 17-point no-hexagon
  set could realize 70 distinct hull-nesting tuples — why the n=5 layer-count method won't scale.

```claim
id: ms-toth-valtr-bound
statement: ES(n) <= C(2n-5, n-3) + 2 (equivalently C(2n-5, n-2) + 2).
hypotheses: n >= 3
holds-here: yes
status: proved
bearing: best binomial-form upper bound; stood for ~15 years. NOTE: C(2n-5,n-3)=C(2n-5,n-2) by symmetry, so the DIMACS abstract g(n)<=C(2n-5,n-2)+2 and the survey agree (flag resolved). (The specific constant is a distinct projective-transform argument, not a corollary of cups-caps tightness.)
anchor: research/sources/morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md
```

```claim
id: ms-cups-caps-tight
statement: f(k,l) = C(k+l-4, k-2) + 1 exactly; the cups-caps function is tight.
hypotheses: k,l >= 3
holds-here: yes
status: proved
bearing: the ~4^n ES bound comes ONLY from the reduction to cups/caps, not from f; an exact 2^{n-2} bound needs a non-counting (structural) argument.
follows-from: es35-cups-caps-bound
anchor: research/sources/morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md
```

## Not-helpful-for-planar parts

Higer-dim ES ($N_d(n)$), convex-body generalizations, zero-sum/interior-divisibility variants are
different problems; only used to distinguish them from this one.
