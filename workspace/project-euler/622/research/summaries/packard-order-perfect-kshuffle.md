# Packard, "The Order of a Perfect k-Shuffle" (TTU thesis)

Source: https://ttu-ir.tdl.org/bitstreams/6efc0c3f-086d-4400-bbfe-f6c8918e5790/download · full text: [[packard-order-perfect-kshuffle.full]]

## What it establishes

The order d_k(n) of a perfect k-shuffle on n = ks cards (k piles of s cards,
dealt pile-by-pile).

**Theorem 2.1**: the order of a k-shuffle on n cards equals the multiplicative
order of k mod (n−1), ord_{n−1}(k). (Special case k=2 is the out-shuffle case
this run needs, matching DGK Lemma 1.)

**Corollary 4.2** (verified at line 795 of the full text) — the Wieferich lift,
ladder rung R-lift:
> If b = order of k (mod p), then the order of k (mod p^n) divides b·p^{n−1}.

**Lemma 4.6/4.7** (surrounding text): if b = ord_p(k) then k^b = 1 (mod p),
and k^{b·p^{n-1}} = 1 (mod p^n); the order mod p^n equals b·p^{n−1} exactly
iff k^{b·p^{n-2}} ≢ 1 (mod p^n), i.e. iff p is not a Wieferich base-k lift.
So ord_{p^n}(k) = b·p^{n−1} precisely when v_p(k^b − 1) = 1.

## Consequences for this problem

For k=2 and the primes p | 2^60−1, once ord_p(2) is known the order mod p^a
is b·p^{a−1} when v_p(2^b−1)=1 (no Wieferich lift). This is what makes the
prime-power orders cheap to compute. Chappelon Thm 3.6 gives the complete
rule (order = d for k≤k0, dp^{k−k0} for k≥k0).

## Does not settle

- The lcm combination over distinct primes (that is Chappelon, CRT).
- The actual numerical answer.

## Status

Cor 4.2 proved in the source. Holds here (k=2, applicable to 2^60−1's prime
powers). Load-bearing for the exact prime-power orders.
