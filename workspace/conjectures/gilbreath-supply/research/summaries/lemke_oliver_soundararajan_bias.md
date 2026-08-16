# Summary — Unexpected Biases in the Distribution of Consecutive Primes

Source: R. J. Lemke Oliver, K. Soundararajan, PNAS 113(31) (2016) E4446–E4454.
Source URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4978288/. Full text:
`[[lemke_oliver_soundararajan_bias.full]]`.

## What this establishes

Proposes and numerically supports a *conjectural* (Hardy–Littlewood-based)
asymptotic for the frequency of patterns `(a_1,…,a_r)` of r consecutive primes in
reduced residue classes mod q:

**Main Conjecture:**
```
π(x;q,a) = li(x)/φ(q)^r · ( 1 + c_1(q;a) loglog x / log x + c_2(q;a)/log x + O((log x)^{-7/4}) )
c_1(q;a) = φ(q)/2 · ( (r−1)/φ(q) − #{1≤i<r : a_i ≡ a_{i+1} mod q} )
```
The leading bias factor `c_1` depends on how many *transitions disagree*
(`a_{i+1} ≢ a_i mod q`). More transitions into the *same* class → more negative bias.

**Conjecture 1.2 (mod 3 and mod 4, robust and unconditional-looking):**
For q = 3 or 4 and a = 1 or −1 mod q, for all x ≥ 5,
```
π(x; q, (a,−a)) > π(x; q, (a,a))
```
with, for large x, `π(x;q,(a,−a)) − π(x;q,(a,a)) = (x/4)(log x)^{-2} log(2πq/log x) + O(x/(log x)^{11/4})`.
So the *switch/differing* pairs (a,−a) exceed the *equal* pairs (a,a) **always**, from the
very start — never merely asymptotically, unlike Chebyshev's bias which is false infinitely
often. This is the nearly-robust mod-4 pair bias.

**Conjecture 1.4 (not Markovian):** the transition matrix from p_n to p_{n+2} is not the
square of that from p_n to p_{n+1}; the primes mod q are not Markovian.

**Conjecture 1.6 (prime-power symmetry):** for q a prime, v ≥ 2, patterns whose
*differences* (mod q^v) agree have equal frequency up to O(x^{1/2+ε}). For q=2^v
(power-of-2 modulus), `π(x;2^v,(a,b))` depends essentially only on `b−a mod 2^v`.

## What it implies here

1. **The switch side is the *preferred* the side.** LOS conjecture that, for mod 4,
   the differing pairs (1,3),(3,1) not only have positive density but *exceed* equal
   pairs (1,1),(3,3) at every x ≥ 5. This is *exactly* evidence for the switch-density
   input SUPPLY needs — positive switch density. If Conjecture 1.2 holds, switch
   density is not merely positive but ≥ 1/2 (roughly). It is a *conjecture*, conditional
   on Hardy–Littlewood-style heuristics, not a theorem — but it strengthens the heuristic
   basis for expecting SUPPLY's arithmetic input to be true.

2. **Powder of 2 is special for pairs.** Conjecture 1.6 says for modulus 2^v the pair
   frequency depends only on the difference b−a mod 2^v. This matches ABGS Prop 4.1's
   power-of-2 independence and reinforces that the mod-4 *pair* structure (difference
   carries the information) is the right level — and that SUPPLY's `h[j]
   = ((q_{j+1}−q_j)/2) mod 2` (which tracks the difference/2 parity) is aligned with the
   carrier of the bias.

3. **Consistent with, weaker than, ABGS.** ABGS only leaves equality open; LOS conjecture
   the stronger statement that differing strictly dominates. This is a *contradiction of
   emphasis*: ABGS says don't assume even positivity is known; LOS conjectures positivity
   robustly. Both are heuristic; they don't conflict factually (ABGS's §9 openness and
   LOS's Conjecture 1.2 can both be true). Flag: LOS is a heuristic/conjecture; not a
   proof of positive switch density.

## Not settled

Positive mod-4 switch density is still unproved (LOS is conjecture). Conjecture 1.2's
formula for the difference is heuristic. Nothing here implies SUPPLY; it only supports
the arithmetic input that the reduction needs but that is still open.

```claim
id: los-switch-preferred-mod4
statement: For q=4 (or 3) and a = 1 or −1 mod q, conjectured for all x ≥ 5:
  π(x;q,(a,−a)) > π(x;q,(a,a)), with difference ~ (x/4)(log x)^{-2} log(2πq/log x).
  The differing-residue consecutive pairs dominate the equal ones at every x.
hypotheses: q = 3 or 4; a = ±1 mod q.
holds-here: yes — this is precisely the switch-density side SUPPLY needs.
status: asserted (conjecture, Hardy–Littlewood-based)
bearing: if true, mod-4 switch density is not just positive but ≥ ~1/2 (off-diagonal
  dominates); supports expecting the switch-density input to be true, but gives no theorem.
  Consistent with ABGS §9 openness (both can hold).
anchor: lemke_oliver_soundararajan_bias.full, Conjecture 1.2
```

```claim
id: los-scale-bias-slowdecay
statement: The bias factor in pair frequencies decays on the slow scale
  c_1(q;a)·loglog x / log x (secondary/lower-order), not → a different limiting value.
  The primes mod q are not Markovian (transition to p_{n+2} ≠ square of that to p_{n+1}).
hypotheses: Hardy–Littlewood k-tuple conjectures.
holds-here: yes (as a conjecture).
status: asserted (conjecture)
bearing: even at the asymptotic level the equal/switch imbalance is lower-order, so the
  *positive density* of switch pairs is the robust fact, not a precise ratio.
anchor: lemke_oliver_soundararajan_bias.full, Main Conjecture, Conj 1.4
```
