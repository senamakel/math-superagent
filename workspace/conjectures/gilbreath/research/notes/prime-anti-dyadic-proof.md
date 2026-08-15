# SPAD-prime-anti-dyadic — proof that the prime mod-4 switch bit is not eventually periodic

**Theorem (SPAD-prime-anti-dyadic, part (a)) — conditional on Shiu 2000.** Let

    h[j] = [ p_{j+2} − p_{j+1} ≡ 2  (mod 4) ]

be the halved-gap mod-4 switch bit (h[j]=1 iff gap_{j+2} ≡ 2 mod 4). Then h is
not eventually periodic with period 2^k for any k ≥ 0. In fact h is not
eventually periodic with *any* period.

**Hypotheses.** Shiu 2000 (strings of consecutive primes in a fixed residue
class mod 4) and the elementary theorem that every residue a coprime to 4
(here a = 3) occurs among infinitely many primes (Dirichlet; the a=3 case has
an elementary Euclid-style proof).

**Status.** CONDITIONAL on Shiu 2000 (held at abstract level only — paywalled, status asserted) + the elementary infinitude facts; the residue-arithmetic steps are proved.
The rest of the argument is pure elementary residue arithmetic. Holds-here: as
a statement about the prime sequence's mod-4 structure. It does NOT yield
ν₂ ≥ c·n (that converse is refuted, `spad-nondegenerate-linear-refuted`), so
this rung closes the dyadic skeleton as a *negative* result.

---

## Proof

Let g_j = p_{j+1} − p_j (j ≥ 2) be the prime gaps. Every prime ≥ 5 is odd and
every gap between two distinct primes ≥ 2 is even, so g_j ∈ {0, 2} (mod 4).
The switch bit is h[j] = [g_{j+2} ≡ 2 (mod 4)], and therefore

    g_j ≡ 2·h[j−2]   (mod 4),

i.e. **the gap residues mod 4 are completely determined by the switch bits.**
This is the load-bearing identity: h is not just an indicator of one residue,
it *is* the whole mod-4 residue sequence of the gaps (up to the 0/2 labelling).

**Claim 1 (periodicity transfer).** If h is eventually periodic with period p,
then the prime residues a_j = p_j mod 4 are eventually periodic with period p
and constant "step" C: more precisely a_{j+p} ≡ a_j + C (mod 4) for all large
j, with C = 2·|{r : h has 1 at residue r in one period}| (mod 4).

*Proof.* For all large t, h[t] = h[t+p], so g_{t+2} ≡ g_{t+2+p} (mod 4). Sum the
gaps from j to j+p−1:

    p_{j+p} − p_j = Σ_{t=j}^{j+p−1} g_t ≡ Σ_t 2·h[t]  (mod 4).

For a full period (p consecutive t, with j large enough that every h[t] in the
window is in the periodic tail), the sum Σ 2·h[t] is the same for every j, so
p_{j+p} − p_j ≡ C (mod 4) for a fixed C. Hence a_{j+p} ≡ a_j + C (mod 4) for
all large j. ∎

**Claim 2 (Shiu forces C = 0 and an all-1 tail).** Shiu's theorem gives, for
every M, a stretch of M consecutive primes all ≡ 1 (mod 4) that lies beyond
any prescribed index. Take M > 4p. Inside such a long ≡1-run, for a full
period-window of large indices j all of p_j are ≡ 1. Then p_{j+p} − p_j ≡ 0
(mod 4), so Claim 1 gives C = 0. With C = 0, by Claim 1 the residue sequence
a_j is eventually periodic with period p, and because a full period-window
inside the ≡1-run is all 1s, the entire eventual tail is ≡ 1 (mod 4). ∎

**Claim 3 (contradiction).** Dirichlet (or the elementary proof for a = 3)
gives infinitely many primes ≡ 3 (mod 4), so the primes mod 4 cannot have an
eventually all-1 tail. Contradiction. Hence h is not eventually periodic with
any period p, in particular not with period 2^k. ∎

---

## What this does and does not give

**Gives.** A proof that the prime mod-4 switch bit is aperiodic (with any
period, hence with every 2^k). This closes the last open rung of the dyadic
skeleton (`close-spad-prime-anti-dyadic`) as a *negative* result: the primality
side (a) is now proved, but the supply-bearing converse (b) it was meant to
feed is refuted, so the aperiodicity of the switch bit does NOT yield ν₂ ≥ c·n.

**Does not give.** Any supply bound. `spad-nondegenerate-linear-refuted`
(balanced + anti-dyadic h can still give wt(Φ h) = O(1)) kills the bridge, and
ν₂ ≥ c·n for the primes stays the named-open two-point mod-4 hypothesis
`abgs-2011-s9-mod4-switch-limit-open`.

**Empirical anchor (verification-numerical, not the proof).** The prime switch
bit's Hamming distance to the nearest 2^k-periodic prefix stays bounded away
from 0 out to 10^6 bits, even bias-corrected against the constant/constant-0
collapse (`code/out/prime_antidyadic.captured.txt`: A ≈ 0.426–0.437 for all
k, B ≈ 0.43–0.50 for k = 1..6; fresh anchor to follow in
`code/out/prime_antidyadic_anchor.captured.txt`). This independently witnesses
aperiodicity over the measured window, consistently with the proof.

```claim
id: spad-prime-anti-dyadic-proved
statement: The prime mod-4 switch bit h[j] = [p_{j+2} - p_{j+1} ≡ 2 (mod 4)]
  is NOT eventually periodic with any period p (in particular not with period
  2^k for any k). Proof: since prime gaps are even, g_j mod 4 = 2·h[j-2], so h
  determines the gap residues; if h were eventually p-periodic then (a) summing
  gaps over a period gives p_{j+p} - p_j ≡ C (mod 4) constant, i.e. prime
  residues mod 4 eventually satisfy a_{j+p} ≡ a_j + C (mod 4); (b) Shiu 2000
  supplies arbitrarily long runs of consecutive primes ≡ 1 mod 4, forcing
  C = 0 and an eventual all-1 tail; (c) infinitely many primes ≡ 3 mod 4
  (Dirichlet/elementary) contradict the all-1 tail.
hypotheses: prime sequence (standard gaps); Shiu 2000 strings-of-congruent
  primes mod 4; elementary infinitude of primes ≡ 3 mod 4. The switch-bit/
  gap-residue identity g_j mod 4 = 2·[g_j ≡ 2 mod 4] is exact (gaps even).
holds-here: yes (as a theorem about the primes' mod-4 structure)
status: conditional (Shiu 2000 asserted at abstract level only, paywalled; the residue-arithmetic steps are proved)
bearing: closes the last open rung of the dyadic skeleton as a NEGATIVE result
  (prime switch bit is aperiodic), but the supply-bearing converse is refuted
  (spad-nondegenerate-linear-refuted), so it does NOT yield nu2 >= c*n; that
  bound stays the named-open abgs-2011-s9-mod4-switch-limit-open.
anchor: research/notes/prime-anti-dyadic-proof.md;
  code/out/prime_antidyadic.captured.txt (Hamming-distance witness);
  code/out/prime_antidyadic_anchor.captured.txt (fresh per-period violations)
```
