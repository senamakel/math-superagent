# Perrin — Sturmian words, Lecture 1: complexity, balance, slope (Master 2011)

<!-- source: http://www-igm.univ-mlv.fr/~perrin/Enseignement/Master2011/Slides/Lecture1/slides1.pdf | read 2026-08-19 -->

Full text: `research/sources/perrin-restivo-note-sturmian-words.full.md`

## What it establishes

Lecture-1 slides (of Perrin's 2011 Sturmian-words minicourse, based on Berstel–Séébold in Lothaire ACW 2002). Uses exactly PE1006's convention: alphabet {0,1}, Fibonacci word x = 0100101001001… = fixed point of φ(0)=01, φ(1)=0, finite words uₙ = φⁿ(0) with u_{n+1} = uₙu_{n−1} (= the problem's Sₙ).

**Complexity.** P(x,n) = Card(Fₙ(x)). A Sturmian word has P(x,n) = n+1 ∀n. **x is Sturmian iff there is exactly one right-special word of each length** (u is right-special if u0, u1 ∈ F(x)).

**Coven–Hedlund 1973.** For an infinite word: eventually periodic ⇔ P(x,n)=P(x,n+1) for some n ⇔ P(x,n) < n+1 for some n ≥ 1 ⇔ P(x,n) bounded. (The Morse–Hedlund dichotomy: an aperiodic word has P ≥ n+1 for all n.)

**Fibonacci word is Sturmian.** Proof sketch: every factor recurs; the left-special words are exactly the prefixes of x (φ(0uₙ)=01u_{n+1}, φ(1uₙ)=0u_{n+1}, and conversely u = φ(v) or φ(v)0 with v left-special).

**Balance.** h(x) = number of 1's (height); δ(x,y) = |h(x)−h(y)|; a set is balanced iff |δ| ≤ 1 on equal lengths. **A balanced factorial set X has Card(X∩Aⁿ) ≤ n+1.** X unbalanced iff ∃ palindrome w with 0w0, 1w1 ∈ X.

**Morse–Hedlund 1940.** x is Sturmian ⇔ x is balanced and aperiodic.

**Slope.** π(x) = h(x)/|x|; an infinite balanced word has slope α = lim π(xₙ); the **Fibonacci word has slope 1/τ² = 1/(3+√5)** (from |fₙ|=Fₙ, h(fₙ)=F_{n−2}); every factor u satisfies |π(u) − α| ≤ 1/|u|.

## Why it matters for PE1006

- First lecture in the same series as the (already digested) Lecture 2; pins, in the problem's own 0/1 convention: the k+1 count (Morse–Hedlund/Coven–Hedlund), the unique right-special factor per length (the run's R_k hinge), the balance bound (heights of length-k factors differ by ≤ 1), and the slope 1/τ² with factor-height bound |π(u)−α| ≤ 1/k.
- The balance bound Card(X∩Aⁿ) ≤ n+1 is the elementary reason there are at most k+1 factors; combined with the Fibonacci word's construction showing exactly k+1, this is a self-contained proof of the problem statement's "only k+1 different Fibonacci subwords of length k".

## What it does NOT establish

- No Ψ(k), no decimal weighting, no floor-sum evaluation, no O(log) method. Slides: statements with proof sketches.

## Claims anchored here

`governing-factor-complexity` (Morse–Hedlund k+1; balance ≤ n+1), `governing-sturmian` (slope 1/τ²), `unique-right-special-sturmian-sourced` (exactly one right-special per length).
