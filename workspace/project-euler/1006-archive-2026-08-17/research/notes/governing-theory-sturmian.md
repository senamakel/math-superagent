# Governing theory: Sturmian words and the Fibonacci word

## Why the problem's FACT holds

The problem states: for each positive integer `k`, there are exactly `k+1` distinct
Fibonacci subwords (contiguous substrings of the finite `S_n`) of length `k`.

**Identification:** `S_n` is the `n`-th finite Fibonacci word, and the sequence `S_n`
converges to the infinite Fibonacci word `F` (the fixed point of the substitution
`0 -> 01, 1 -> 0`). `F` is a **Sturmian word** of slope `(3 - sqrt5)/2`.

**Morse–Hedlund:** a balanced aperiodic word has factor complexity `p(k) = k+1` for all
`k`. The infinite Fibonacci word is balanced and aperiodic, hence has exactly `k+1`
distinct length-`k` factors. And the set of length-`k` factors of `F` equals the set of
length-`k` Fibonacci subwords of the finite `S_n`: every factor of `F` occurs already
inside some finite `S_n` (any length-`k` factor occurs infinitely often in the recurrent
word `F`, and before some fixed index; that prefix is a factor of some `S_n`), and every
factor of a finite `S_n` is a factor of `F` (each `S_n` is a prefix of `F`).

This is exactly the problem's FACT: `k+1` distinct length-`k` subwords.

## Worked example check (k=3)

Length-3 factors of `F = 0100101001001...`: scanning, the distinct length-3 substrings
are `001, 010, 100, 101` — four = 3+1. Interpreting as decimals ignoring leading zeros:
`1, 10, 100, 101`, squares `1 + 100 + 10000 + 10201 = 20302 = Psi(3)`. ✓ 

This matches the statement, and confirms both the "k+1 factors" fact and the
leading-zeros-ignored value interpretation.

## The structural theorem for enumeration

Perrin–Restivo, "A note on Sturmian words" (hal-00828351) **Theorem 2**: two length-`n`
factors `u, v` of a Sturmian set are consecutive in the lexicographic order iff
`u = r·ab·s`, `v = r·ba·s` (with appropriate `s`) or `u = r·a`, `v = r·b`. This gives a
linear-time "next factor" algorithm to generate all `n+1` length-`n` factors in
lexicographic order.

This is the structural ingredient a poly(log k) or closed-form computation of `Psi(k)`
can build on (see `research/approaches/` for how the sum-of-squares recurrence is
derived). It does not require enumerating `k = 10^18` words — the recurrence is over
`k` with a closed form / fast exponentiation.

## Answer to request `precise-sourced-statement-c1ec`: the indexed classification of length-n factors

**Fact (Morse–Hedlund, quoted in Poirier–Steiner, hal-03869990):** in a Sturmian word of
slope `α`, every length-`n` factor has either `⌊nα⌋` or `⌈nα⌉` occurrences of the letter
of frequency `α`. For the Fibonacci word, `α = 1/φ² = (3−√5)/2`, so every length-`k`
factor has `⌊k/φ²⌋` or `⌈k/φ²⌉` occurrences of `1`.

This is a **necessary condition only**. It is NOT a bijection: the set of all balanced
binary words of length `k` with `⌊kα⌋` or `⌈kα⌉` ones strictly contains the factor set and
has more than `k+1` elements (refuted in `research/approaches/balanced-factors-claim-attack.md`:
for `k=3`, `C(3,1)+C(3,2)=6` candidate words but only 4 factors; `k=4`: 10 candidates vs 5
factors). The indexed enumeration of the true factor set comes from the Perrin–Restivo
**consecutive-factor lex-order rule** (`PR-consecutive-factors-lex`), not from the
balanced-count paraphrase.

Verification of the *necessary* condition against the oracle: `k=3`, `α=(3−√5)/2 ≈ 0.381966`;
`kα = 1.1459`, so `⌊kα⌋=1`, `⌈kα⌉=2`. The four length-3 factors `001, 010, 100, 101` have
respectively `1,1,1,2` ones — all in `{1,2}`. ✓ (necessary condition holds; does not enumerate).

```claim
id: PE1006-factors-one-count-necessary
statement: Every length-k factor of the infinite Fibonacci word (Sturmian, slope a=1/phi^2=(3-sqrt5)/2)
  has either floor(k*a) or ceil(k*a) occurrences of the letter 1 (Morse-Hedlund balanced-blocks fact).
hypotheses: Sturmian word of slope a; for Fibonacci a=1/phi^2.
holds-here: true — verified on k=3: k*a=1.1459, all four factors 001,010,100,101 have 1 or 2 ones.
status: sourced — Morse & Hedlund 1940, quoted in Poirier-Steiner (hal-03869990), necessary condition; VERIFIED directly in the Poirier-Steiner full text by the scholar ("each block of length n in a Sturmian sequence of slope alpha has floor(n*alpha) or ceil(n*alpha) occurrences of the letter of frequency alpha") and checked vs oracle k=3.
bearing: necessary restriction on the factor set; NOT an enumeration (the exact balanced-set bijection has
  been refuted — see the Correction note below and research/approaches/balanced-factors-claim-attack.md).
anchor: research/summaries/morse-hedlund-balanced-blocks-floor-alpha.md.
```

**Correction of a prior overstatement.** An earlier claim `PE1006-balanced-factors-floornalpha`
asserted the length-k factors are *exactly* the balanced binary words with `⌊kα⌋`/`⌈kα⌉` ones
and that there are exactly `k+1` such words. That bijection is **false** and has been removed:
the balanced-count paraphrase over-enumerates (see `research/approaches/balanced-factors-claim-attack.md`).
The enumeration that answers `precise-sourced-statement-c1ec` is the Perrin–Restivo
consecutive-factor rule (`PR-consecutive-factors-lex`), which indexes the `k+1` factors in lex
order without requiring the false balanced-set bijection.

## Sources

- Perrin & Restivo, "A note on Sturmian words", https://hal.science/hal-00828351/file/noteSturmianWords.pdf
- Wojcik, "Formal intercept of Sturmian words" (Morse–Hedlund Thm 1), https://hal.science/hal-01827511/document
- Lothaire (Berstel–Séébold), "Sturmian Words", https://doi.org/10.1017/cbo9781107326019.003
- Cyclic complexity note, Prop 6 & 7, https://hal.science/hal-01829144v1/document

```claim
id: PE1006-kplus1-FACT
statement: The infinite Fibonacci word F (fixed point of 0->01,1->0, slope (3-sqrt5)/2)
  is a Sturmian word, so it has exactly k+1 distinct factors of length k for every k>=1;
  and this equals the set of the problem's length-k Fibonacci subwords (factors of finite S_n).
hypotheses: F is balanced and aperiodic (holds: slope irrational -> aperiodic; Sturmian -> balanced).
holds-here: true — this is precisely the problem's stated FACT.
status: sourced — Morse-Hedlund theorem; verified against the k=3 example (4 factors: 001,010,100,101).
bearing: turns "exactly k+1 subwords" from an unexplained statement into a named theorem, and fixes
  the governing object (Sturmian word) for deriving Psi(k) via the lex-order consecutive-factor rule.
follows-from: MH-kplus1-factors
anchor: this note; LO: hal-00828351, hal-01827511, cbo9781107326019.003, hal-01829144v1.
```

```claim
id: PE1006-factors-dependent-slop-only
statement: Two Sturmian words have the same set of factors iff they have the same slope;
  the length-k factor set depends only on slope, not on intercept or finite truncation.
hypotheses: Sturmian words over a binary alphabet.
holds-here: true — justifies computing from the infinite Fibonacci word rather than a specific S_n.
status: sourced — Prop 7 of the cyclic-complexity note (hal-01829144v1), VERIFIED directly in the full text ("Fact(x)=Fact(y) iff x,y are Sturmian of the same slope").
bearing: licenses treating Fibonacci subwords as the Sturmian factor set of fixed slope.
anchor: research/summaries/character-of-sturmian-words.md.
```
