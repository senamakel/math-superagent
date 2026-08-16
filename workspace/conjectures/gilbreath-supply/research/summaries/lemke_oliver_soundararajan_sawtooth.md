# Summary — The distribution of consecutive prime biases and sums of sawtooth random variables

Authors: Robert J. Lemke Oliver, Kannan Soundararajan.
Source: arXiv:1709.06168 (Math. Proc. Camb. Phil. Soc. 165 (2018) 457–478).
Source URL: https://ar5iv.labs.arxiv.org/html/1709.06168
Full text: `research/sources/lemke_oliver_soundararajan_sawtooth.full.md`

## What this source establishes

Companion to LOS 2016 (*Unexpected biases*, already in the library). LOS 2016 conjectured for the
pattern count of r consecutive primes in reduced residue classes mod q

> π(x; q, a) = li(x)/φ(q)^r · (1 + c₁(q;a)·(log log x)/(log x) + c₂(q;a)·(1/log x) + O((log x)^(−7/4)))

where **c₁ is the "immediate repetition" term**: c₁(q;a) = (φ(q)/2)((r−1)/φ(q) − #{i : aᵢ ≡ aᵢ₊₁ mod q}).
**This is exactly the switch-density object the run's K=1 reduction is about** — c₁ is a
bias *against* immediate repetitions (switches), i.e. favouring the equal-residue side.

This paper studies the **secondary term c₂(q;a), a genuinely higher-order (K≥2) object**
not captured by c₁. For r ≥ 3 it is an explicit combination of pair terms plus
Σⱼ (1/j)((r−1−j)/φ(q) − #{i : aᵢ ≡ aᵢ₊ⱼ₊₁ mod q}), so understanding r=2 suffices. For prime q and
a ≢ b (mod q),

> c₂(q; (a,b)) / q = C(b−a) + O((log q)²/√q),  with
> C(k) = (1/φ(q)) Σ_{χ≢χ₀ mod q} conj(χ(k))·L(0,χ)·L(1,χ)·A_{q,χ}

where A_{q,χ} = ∏_{p∤q}(1 − (1−χ(p))²/(p−1)²). Only *odd* characters contribute (L(0,χ)=0 for
even χ), so **C(k) = −C(−k) is odd**. The diagonal is exactly c₂(q;(a,a)) = ((q−2)/2)log(q/2π),
size q log q; off-diagonal c₂ is usually size ~q, occasionally ~q·log log q of either sign
(conjecturally the max).

Main theorems (all in the q → ∞ limit, C(k)/C(−k) symmetric about 0):
- **Thm 1.1**: the distribution of C(k) (a probability measure on R) converges to a continuous,
  symmetric limit distribution; the moment generating function converges for all x, so the
  moments uniquely determine the limit.
- **Thm 1.2**: the analogous statement for the normalized discrete Fourier transform of the
  classical Dedekind (sawtooth) sum ŝ_q(t).
- **Thms 4.1/4.2**: all moments of C(k) exist and do not grow too fast; the connection to the
  error term in Σ_{n≤N} φ(n) is made precise.

## Why it matters for SUPPLY / the reopened question

This is the library's primary "K=2 and above" reference for the consecutive-prime residue
object. It says the structure that distinguishes the primes at order K≥2 is **not** merely the
switch/repetition term but a secondary term controlled by L(0,χ)L(1,χ) and Dedekind sums. That
is exactly the kind of *arithmetic input strictly weaker/other than pointwise mod-4 switch
density* that GOAL priority 2 wants: the fold is being asked to see more than K=1, and this is
where the primes' own ≥K=2 structure is catalogued.

Two cautions recorded (not proved, so not claims):
- The c₂/C(k) machinery is about residue-pattern *frequencies*, i.e. averages over many primes;
  SUPPLY needs a *fixed-prefix* statement. Transfer is conjectural.
- The diagonal (a,a) term dominates (size q log q) and is completely explicit; the
  run's K=1 reduction concerns the switch side. c₂ is the refinement *on top of* switch density,
  not a replacement for the K=1 term.

## Evidence class

Proved theorems (in the paper), in the q → ∞ distributional sense. The bearing on SUPPLY is
interpretive, not a proof.

```claim
id: los-sawtooth-secondary-bias-term
statement: The order-2 (secondary) bias in the pattern count of consecutive primes mod q is captured by
  C(k) = (1/φ(q)) Σ_{χ≢χ0} conj(χ(k)) L(0,χ) L(1,χ) A_{q,χ}; C is odd in k, the diagonal term is explicit,
  and the distribution of C(k) over k mod q converges (q→∞) to a continuous symmetric limit whose moments
  determine it.
hypotheses: q prime, (a,q)=(b,q)=1, r=2 (reduced from general r), q → ∞.
holds-here: the switch side is a ≢ b mod q; C(b−a) is the K≥2 correction to the run's switch-density
  (K=1) term c₁. The distributional limit is about many-prime frequencies, not a fixed prefix.
status: proved (LOS 2018, arXiv:1709.06168), distributional-in-q.
bearing: the primes DO carry a catalogued higher-order (K≥2) bias structure beyond switch density,
  expressible through L-values and Dedekind sums — a candidate arithmetic input for GOAL priority 2,
  strictly beyond the K=1 term, but the transfer from frequency averages to a fixed prefix is open.
anchor: ARCHIVED source, introduction eq. (1.1)–(1.5), Thms 1.1, 1.2, 4.1, 4.2.
```
