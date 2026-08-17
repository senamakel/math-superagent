# Berstel — *Sturmian and Episturmian Words* (survey 2007)

Source: https://ligm.univ-eiffel.fr/~berstel/Articles/2007SturmianThessalonique.pdf
Full text: [[berstel-sturmian-episturmian-survey-2007.full]]

## What this source establishes

A survey of Sturmian/episturmian words with emphasis on central words (§2–3 of
the full text). Facts this run uses (verified in the full text §2.1–2.3):

- **Complexity notation and identity (eq. (1)):**
  c_w(n+1) − c_w(n) = Σ_{x ∈ S_n(w)} (deg(x) − 1),
  where S_n(w) are the right-special factors of length n. For a Sturmian word
  there is exactly one right-special factor per length with degree 2, giving
  c(n) = n+1. This is the *derivation* of the k+1 count, not just its statement.
- **Theorems 1/4 (Morse–Hedlund / eventual periodicity):** w eventually
  periodic iff c_w(n) ≤ n for some n; iff c*_w(k) < 2k for some k. The Fibonacci
  word (aperiodic, c = n+1) is on the minimal side.
- **Balanced ⇒ Sturmian, and 14 central-word characterisations (Props 5–24):**
  central words = palindromic prefixes of characteristic words = w with coprime
  periods p,q, |w| = p+q−2, etc. The Fibonacci central words are the palindromic
  prefixes of c_α, α = 1/φ².
- **The 2007 survey's slope statement:** it does not itself re-prove the
  Fibonacci slope, citing the DLT'95 standard; consistent with slope 1/φ² (see
  Note in `berstel-recent-results-sturmian-words-dlt95.md`).

## What it implies for PE1006

1. The k+1 complexity identity is derived, not just asserted: exactly one
   right-special factor per length k, degree 2, gives c(k+1) = c(k) + 1, c(1) = 2.
   This closes the "why k+1" question with a proof path if the solver ever needs
   it in the write-up.
2. Central words / palindromic prefixes give an independent description of the
   factor set (the k+1 factors = conjugates of the central word + the singular
   factor; Perrin–Restivo "every element of F of length |s_n| is a conjugate of
   s_n except one"). A possible second route to cross-check: conjugate-based
   generation at k = F(n)−1 (directive 1's domain).

## Claims anchored here

Corroborates `governing-factor-complexity` (derivation), and the central-word
description supports `mechanical-word-digit-rule`'s "conjugates of standard
words" parenthetical.

## What it does NOT establish

- No Psi / decimal / floor-sum content. Survey tier.