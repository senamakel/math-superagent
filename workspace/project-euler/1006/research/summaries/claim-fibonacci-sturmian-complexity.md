# Claim: Fibonacci word is Sturmian; factor complexity P(k) = k+1

Answers request `citable-statement-theorem-039a`: the fact that there are exactly
k+1 distinct length-k Fibonacci subwords is the standard factor-complexity
theorem, not a fact the run must reprove.

```claim
id: fibonacci-sturmian-complexity
statement: The infinite Fibonacci word f (limit of the morphism 0 -> 01, 1 -> 0,
equivalently the characteristic Sturmian word of slope 1/phi) is a Sturmian
word, and its factor complexity function counts exactly P(f, k) = k + 1 distinct
factors (subwords) of length k, for every integer k >= 0.
hypotheses: f is the infinite Fibonacci word; "factor" means contiguous substring;
length k is a nonnegative integer.
holds-here: true. PE1006's S_n are the finite Fibonacci-word prefixes whose limit
is the infinite Fibonacci word, so the k+1 distinct Fibonacci subwords of length
k in the problem ARE the k+1 length-k factors of the infinite Fibonacci word.
status: sourced
bearing: Establishes the "there are only k+1 different Fibonacci subwords of
length k" sentence in the problem statement as the standard factor-complexity
theorem (Lothaire C2, and Morse–Hedlund minimal complexity), fixing that Psi(k)
is a sum of squares over exactly k+1 terms (k -> 10^18 terms).
anchor: research/sources/lothaire-sturmian-words-C2.full.md (def: complexity
P(x,n)=Card(F_n(x)), Sturmian = P(s,n)=n+1, p. 89, sec 2.1.1);
research/sources/wikipedia-fibonacci-word.full.md (complexity n+1, lists the 4
length-3 subwords 001,010,100,101 — exactly the problem's Psi(3) example).
answers: citable-statement-theorem-039a
```

## What the sources say

**Lothaire C2 (Berstel), Section 2.1.1 "Complexity and balance"** defines the
complexity function of an infinite word x over an alphabet A as the number
P(x, n) = Card(F_n(x)) of factors of length n, and defines a **Sturmian word**
as an infinite word s such that P(s, n) = n + 1 for any integer n >= 0 (the
aperiodic infinite words of minimal complexity). Since P(s,1)=2, a Sturmian
word is over two letters — exactly the binary setting of the Fibonacci word.

**Wikipedia (Fibonacci word)** states directly: "The complexity function of the
infinite Fibonacci word is n+1: it contains n+1 distinct subwords of length n.
Example: there are 4 distinct subwords of length 3: 001, 010, 100, 101. Being
also non-periodic, it is then of minimal complexity, and hence a Sturmian word,
with slope 1/phi." These four subwords are precisely the problem's Psi(3) set,
so the statement example is confirmed by the encyclopedic tier.

Implication for the method: Psi(10^18) is a sum over ~10^18+1 distinct length-k
subwords, one per class. That the set is non-degenerate and exactly k+1 in size
comes from the structure above; the efficient evaluation (universal Euclidean
algorithm, O(log)) still must be justified separately (see the companion claim
`universal-euclidean-geometric-floor-sum`).
