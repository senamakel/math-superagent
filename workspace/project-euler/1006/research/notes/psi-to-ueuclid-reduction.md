# Psi(k) → universal-Euclidean second-moment monoid: the reduction

Status: **derivation sketch, NOT yet verified** — the mechanical construction
itself is verified (mech_psi.py == brute k=1..400), but the reduction of the
sum over m to a single-second-moment floor sum is not. Do not trust the
coefficients here until checked against mech_psi k=1..150.

## Setup (all exact integer / Fraction arithmetic)

Infinite Fibonacci word S = limit of S_0='0', S_1='01', S_n = S_{n-1}S_{n-2}.
Slope a = p/q, p = fib(n-2), q = fib(n), q > k (solution.py indexing:
len(S_n) = F_{n+2}, ones = F_n; slope = F_n/F_{n+2}).

Cut the circle at {frac(-m*a) : m = 0..k}. Formulation (B) of mech_psi.py:
the value on the arc ending at cut point -m*a is
    v_m = g[k-m] - 10^(k-1) g[-m] + 9 * sum_{l=1}^{k-1} 10^(k-1-l) g[l-m]
where g[t] = floor(t*a) - [t == 0]  (left limit drops the floor by 1 when
the argument hits exactly 0, i.e. t == m, which happens only for t = 0 here
since x = -m*a and arguments are (l-m)*a, |l-m| <= k < q, gcd(p,q)=1).
Psi(k) = sum_{m=0}^k v_m^2.

## One family of floors

With a = p/q and writing m' = k - m (so m = k - m', m' runs 0..k):
    g[l - m] = floor((l - k + m') * p / q) - [l == m]
             = floor((p*m' + p*(l-k)) / q) - [l == m].
So the intercepts are b_l = p*(l - k) for l = -k, 0, 1, ..., k (l = -k
comes from g[-m] with m=k-m', i.e. l=-m' covers b = p*(-k)... no — see
below). Actually g[l-m] with m = k - m' gives intercept p*(l - k):
  g[k-m]   -> l = k:  intercept p*(k - k) = 0, and the [t==0] flag iff k==m.
  g[-m]    -> l = 0:  intercept p*(0 - k) = -p*k, flag iff 0==m.
  g[l-m], 1<=l<=k-1: intercept p*(l-k) in [-p(k-1), -p], flag iff l==m.

So ALL floors are floor((p*m' + b)/q) for b in B = {0, -pk, p(l-k) : 1<=l<=k-1} —
one family of floor sums with a *range* of intercepts, weight 10^(k-1-l) (and
the leading 10^(k-1) on the l=0 term, sign (-)).

## What the monoid must compute

Psi = sum_{m'=0}^k ( sum_l c_l * floor((p*m' + b_l)/q) )^2  (m'=k-m reindexed)
    = sum_{l,l'} c_l c_l' * C(l,l'),   C(l,l') = sum_{m'=0}^k f_{b_l}(m') f_{b_{l'}}(m'),
    f_b(m') = floor((p*m' + b)/q).

The directive-4 monoid (single intercept) gives S2 = sum z^m' f_b(m')^2. The
cross term C(l,l'), l != l', needs either (a) a two-intercept extension of
the node (T = sum z^t f(t) g(t) with a second intercept carried alongside),
which is exactly the loj138 万能欧几里得 generalisation on disk
(research/sources/loj138-universal-euclidean-floor-moments.full.md), or
(b) the expansion 2 f g = f^2 + g^2 - (f-g)^2 with f-g = floor over a
combined intercept — NOT valid because floor(x)+floor(y) != floor(x+y).

The number of distinct intercepts is O(k) (one per l), which would make the
naive pair expansion O(k^2) in the number of monoid runs — too slow at
k=10^18. The committed route (thread: mechanical-word-floor-sum) says: the
x_m are themselves the orbit frac(-m*a), so m is another floor-sum index;
carry the JOINT state in the same monoid rather than looping over m. The
precise joint formulation (which R/U path realises the double sum over m and
l, and how the geometric weights 10^(k-1-l) enter as z-powers) is NOT yet
derived. Derive it, check against mech_psi k=1..150 and Psi(10)=10699667,
THEN trust it.

## Anchors (from directive 6, verified outside the container)

Psi(3) = 20302; Psi(10) = 10699667 mod M; Psi(10^4) = 34432237 (10001
factors); Psi(10^6) = 20938836 (1000001 factors); target Psi(10^18) mod
M = 101001001. Old anchors 16242174 / 77578256 are INVALID (Toeplitz
collapse domain k=F_n-1). NextFib strict (bisect_right in
code/lib/fibword.py). In-container verification of the two new anchors is
open: k=10^4 by psi_direct (O(k^2), ~1e8 big-int ops, feasible); k=10^6 by
O(k^2) is ~1e12 — needs the window/residue route in a compiled setting or
the O(log) monoid itself as the check (which is acceptance test 5).