# Erdős & Szekeres 1961, "On some extremum problems in elementary geometry", Ann. Univ. Sci. Budapest 3–4, 53–62

Source: https://renyi.hu/~p_erdos/1960-09.pdf
Full text: [[erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full]]

**This source fills REQUESTS.md gap `full-text-faithful-b96b`.** The librarian listed the 1961
full text as not freely digitized; it is in fact freely available at the Rényi institute URL
held in this workspace. The concrete construction below is the ground truth GOAL.md needs for
the oracle at n=5,6,7.

## The lower-bound construction (§2)

Define a **convex sequence** of length $k$: points $(x_\nu,y_\nu)$, $x_0<x_1<\dots<x_k$, with
$\frac{y_\nu-y_{\nu-1}}{x_\nu-x_{\nu-1}} < \frac{y_{\nu+1}-y_\nu}{x_{\nu+1}-x_\nu}$ (increasing
slopes = cup); **concave** reverses the inequality (cap). From [2] (1935): any set of more than
$\binom{k+l-2}{k-1}$ ... contains a concave sequence of length $k$ or convex of length $l$; and
there exists an extremal set $S_{kl}$ of $f(k,l)$ points with no concave length-$k$ and no convex
length-$l$.

Concrete $S_{kl}$: points $(x, g_{kl}(x))$ for $x=1,\dots,f(k,l)$, with $g_{kl}$ defined
inductively: $g_{k1}=g_{1l}=0$; for $k,l>1$,
$g_{kl}(x)=g_{k,l-1}(x)$ for small $x$, then $g_{kl}(x)=g_{k-1,l}(x-c)+c_{kl}$ for large $x$,
where $c_{kl}$ exceeds the max slope in the first block (so lines within first block are steeper
than any line in the second). Monotone increasing, all slopes positive. Then the max concave
sequence in $S_{kl}$ has length $k-1$ and max convex has length $l-1$.

**Full set $S$ of $2^{n-2}$ points with no convex $n$-gon**: let $S_1=\{(1,0)\}$ (single point)
and inductively $S_{k+1}$ is a copy of $S'_{k}$ placed via translations so that slopes of lines
connecting $S_k$ and $S_{k+1}$ are all $<-1/(n-k+\dots)$ (negative, steep), while slopes within
each $S_k$ are positive. Then $S=\bigcup_{k=1}^{n-1}S_k$ has $\sum_k \binom{n-2}{k-1}=2^{n-2}$
points. For any convex-position subset $P=\bigcup_i P_i$ with $P_i\subseteq S_{k_i}$,
$k_1<\dots<k_r$: within each $S_k$ only one point ($P_1$ concave, $P_r$ convex, middle singletons),
so $|P| \le k_1 + (k_r-k_2-1) + (n-k_r) = n-1$. Hence no convex $n$-gon.

```claim
id: es61-lower-bound
statement: For every n >= 3 there exists a set of 2^{n-2} points in general position containing no n points in convex position; hence ES(n) >= 2^{n-2}+1.
hypotheses: planar, general position
holds-here: yes
status: proved
bearing: THE extremal construction; every candidate upper-bound argument must fail on it at N=2^{n-2}. Oracle must reproduce its emptiness at n=5,6,7.
anchor: research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md
answers: full-text-faithful-b96b
```

## Implication for this run

This is the concrete construction (compressed union of $n-1$ blocks of sizes
$\binom{n-2}{k-1}$, slopes positive within a block, steeply negative between blocks) that the
oracle must realize with exact coordinates and verify has no convex $n$-gon at $n=5,6,7$
(GOAL.md completion criterion 3). The Morris–Soltan Thm 2.6 restates it as copies of $T_i$ near
points on the unit circle; the two are the same construction.
