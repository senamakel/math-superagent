# Claim — three-gap/three-distance theorem is the literature home of the autocorrelation counting

```claim
id: three-gap-three-distance-autocorrelation
statement: For an irrational slope alpha in (0,1), the partition of the unit circle
by the points {i*alpha}, 0 <= i <= n, has n+1 intervals whose lengths take at most
three values, one being the sum of the other two, with exact counts given by the
Three distance theorem in terms of the convergents q_k of alpha (Alessandri–Berthé,
Section 3); dually, the gaps between the successive integers j with {alpha*j} in an
interval of length beta take at most three values, with exact frequencies given by
Slater's Three gap theorem (Section 4). For the Fibonacci slope (partial quotients
all 1, q_k = F_{k+1}), the two-length regime n = q(1)+q(2)-1 = (m+1)q_k + q_{k-1} - 1
applies at n = F_m - 1, and the counting specialises to the closed form
A(d) = max(0, m-t) + max(0, m-(N-t)), t = (d*m) mod N, N = F_n, m = #ones(q_n)
of directive 1's cyclic autocorrelation of the standard word.
hypotheses: alpha irrational in (0,1); beta in (0,1/2) (or any interval of length beta, by density); convergents and partial quotients of alpha exist (always).
holds-here: true — the PE1006 word has slope alpha = 1/phi^2 (irrational), and the brute oracle matches the A(d) form exactly for k = F_n - 1, n = 3..12 (pattern-hunt note, task reproduce-dir1).
status: sourced
bearing: Gives directive 1's autocorrelation counting formula a literature anchor (Slater's

three-gap frequencies specialised to the all-1 continued fraction), closing the
previously recorded gap "no dedicated literature source for A(d)". The closed form
A(d) itself is still a verify-in-container identity; the theorem is the theory statement
it specialises.
anchor: research/sources/alessandri-berthe-three-distance-theorems.full.md (Sections 3 and 4, Three distance theorem + Three gap theorem with exact counts/frequencies), https://www.irif.fr/~berthe/Articles/3d.pdf
```

## Why this matters for PE1006

Directive 1 reduces Ψ(k) at k = F_n − 1 to a sum over lags d of
A(d)·(geometric weight), where A(d) is the cyclic autocorrelation of the
standard word q_n (the F_n rotations of q_n truncated to k letters are the
k+1 factors). The count A(d) = max(0, m−t) + max(0, m−(N−t)) is "how many of
the N rotation points lie in an arc of length determined by d" — precisely
the quantity the Three gap theorem (Slater's frequencies) counts exactly for
any interval of the circle. With the Fibonacci slope's continued fraction
all-ones, the gap/frequency expressions collapse to the max-form above.

## Status

The claim's *qualitative* content (three-distance/three-gap theorems, exact
gap frequencies) is sourced — read from the full text on disk, sections 3 and
4. The *specialisation* to the A(d) form is the run's own derivation, already
verified against the brute oracle at n = 3..12; it is asserted here as
holds-here: true on that basis, not on the source's word.