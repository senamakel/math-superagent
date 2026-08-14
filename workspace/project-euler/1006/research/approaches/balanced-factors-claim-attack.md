# Attack on claim PE1006-balanced-factors-floornalpha (overstatement flagged)

```approach
idea: Check whether enumerating the k+1 factors as "all balanced binary words of length k with floor/ceil(k*alpha) ones" (the Morse-Hedlund balanced-count paraphrase) is a valid enumeration to build Psi(k) on.
mechanism: Count candidate words with the floor/ceil one-count vs the true factor-set size k+1, for small k.
status: refuted
precedent: Morse-Hedlund balancedness (necessary condition only); Perrin-Restivo Theorem 2 gives the correct enumeration.
first-step: k=3 and k=4 candidate counts vs factor-set size.
killed-by: count-candidates-exceed-kplus1
```

## Why this is over-stated

The Morse–Hedlund balancedness fact gives only a **necessary condition**: every length-k
factor has floor(kα) or ceil(kα) ones, α = 1/φ² ≈ 0.381966. The governing-theory note then
asserts a **converse/count**: the factors are exactly all balanced words with that many ones,
and that there are exactly k+1 such words. The converse is false.

**Counter-evidence (k=3):** k·α = 1.1459 → candidates have 1 or 2 ones.
C(3,1)+C(3,2) = 3+3 = **6** words (001,010,100,011,101,110). But the true factor set has
only **4** words (001,010,100,101). Words 011 and 110 have the right one-count yet are NOT
factors. 6 ≠ 4.

**Counter-evidence (k=4):** k·α ≈ 1.528 → floor=1, ceil=2. C(4,1)+C(4,2)=4+6=**10** words,
but there are only k+1 = **5** length-4 factors.

So "exactly these words" and "there are exactly k+1 such words" are both false.

## Correct statement

- TRUE (necessary): every length-k factor of the Fibonacci word has floor(kα) or ceil(kα)
  ones (Morse–Hedlund balanced-blocks fact). Confirmed by oracle for k=3 (factors have 1 or 2
  ones).
- FALSE as a bijection: the count of balanced words with floor/ceil ones is NOT k+1.
  The enumeration must come from the Perrin–Restivo consecutive-factor structure, not the
  balanced-count paraphrase.

## Bearing on the solution

The one-count condition does not by itself enumerate the factors (too many candidates). The
balanced-count claim's bearing ("indexable enumeration") is misplaced. Any formula for Ψ(k)
built on that enumeration is wrong. Use PR Theorem 2. The necessary condition survives, and
the length-8/10 factor lists (PerrinRestivo-len8-len10-lists) remain valid check targets.

```claim
id: PE1006-balanced-bijection-refuted-checked
statement: The k+1 length-k factors of the Fibonacci word are NOT in bijection with the balanced binary words of length k that have floor/ceil(k*alpha) ones (alpha=1/phi^2). Verified by direct computation: k=4 factors are exactly {0010,0100,0101,1001,1010} (sum of squares 10^2+100^2+101^2+1001^2+1010^2 = 2042402 = Psi(4), matching the brute oracle); 0110 has 2 ones (in {floor(4a),ceil(4a)}={1,2}) but is not a factor, and 0001/1000 have 1 one but are not factors. There are C(4,1)+C(4,2)=10 balanced words of the right count vs only 5 true factors.
hypotheses: length-4 factors from the factor dump (code/out/factors_k4... via dump_factors.py / data.py), alpha=(3-sqrt5)/2.
holds-here: yes (this is a disproof of the overreach, not a hypothesis check)
status: checked — computed, verified against Psi(4)=2042402 brute value.
bearing: closes request precise-sourced-statement-c1ec by refuting its balanced-word framing; the correct enumeration is Perrin-Restivo Theorem 2 (consecutive factors) with the conjugates-plus-singular factor structure, not the balanced-count paraphrase.
anchor: research/approaches/balanced-factors-claim-attack.md
answers: precise-sourced-statement-c1ec
contradicts: PE1006-balanced-factors-floornalpha (the retracted overreach)
```

