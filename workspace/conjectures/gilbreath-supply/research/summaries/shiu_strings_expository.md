# Summary — On Strings of Congruent Primes (Ethan Yang's expository account)

Source: Ethan Yang, expository account of Shiu's work. Source URL:
http://simonrs.com/eulercircle/analyticnt/ethan-shiustrings.pdf. Full text:
`[[shiu_strings_expository.full]]`. This is the freely-available presentation of
the primary (paywalled) Shiu 2000; the primary theorem is digested separately in
`shiu_strings_congruent_primes.md`. This file records the quantitative bounds and
the proof mechanism, which the primary digest does not.

## What this establishes

Presents Shiu (2000)'s strengthening of Chowla's conjecture: for any q ≥ 3,
(q,a)=1, arbitrarily long strings of consecutive primes all ≡ a (mod q). The
residue classes split into A+ = {a : ∀p|q, a ≡ 1 mod p} and
A− = {a : ∀p|q, a ≡ −1 mod p} (union A±); strings are longer for a ∈ A±.

**Theorem 1.1 (quantitative):** for a ∈ A±, there is a string
`pn+1 ≡ … ≡ pn+k ≡ a (mod q)` with `pn+k < x` and
`k ≫ (loglog x / logloglog x)^{1/φ(q)}`; for general (q,a)=1, length
`k ≫ ( (loglog x · loglogloglog x) / (logloglog x)^2 )^{1/φ(q)}`.

**Theorem 4.1 (quantitative density):** the number of such strings ending < x is
`≫ x^{1−ε(x)}` where ε_1 = C(q)·k·(logloglog x/loglog x)^{1/φ(q)} for a ∈ A±, and a
second, weaker ε_2 for general a.

**Method (why it works):** pick y with no Siegel-zero L-functions mod P(y,p₀)
(Lemma 3.1); build a Maier-style matrix M of columns = arithmetic progressions
mod Q(y); show the residues ≡ a (mod q) in M outnumber the others by a fixed
factor (|P1| vs |P2| estimates via smooth number counts and Bombieri–Vinogradov);
one column must then contain a long string of a-residue primes. The proof uses
only standard Littlewood/bombieri–Vinogradov machinery — not the generalised
Riemann hypothesis.

**It also states (not proved) the later strengthenings:**
- **Theorem 1.2 (Freiberg):** infinitely many *short-gap* equal-residue pairs:
  `pr ≡ pr+1 ≡ a (mod q)` with `pr+1 − pr < ε log pr`.
- **Theorem 1.3 (Freiberg/Maynard):** for q ≥ 3, m ≥ 2, infinitely many n with
  `pn+1 ≡ … ≡ pn+m ≡ a (mod q)` and `pn+m − pn+1 ≤ B` (bounded gap, B = B(q,a,m)).

## What it implies here

- For q = 4, a = 1 and a = 3 are both in A±, so there are arbitrarily long runs of
  primes all ≡ 1 (mod 4) and all ≡ 3 (mod 4). In the bit string
  `h[j] = ((q_{j+1}−q_j)/2) mod 2`, both cases give **arbitrarily long all-zero runs**
  (a ≡ 1 mod 4 ⇒ gap parity 0; a ≡ 3 mod 4 ⇒ gap ≡ 2 mod 4 ⇒ h = 0). This is the
  documented refutation of closed door #3 (no long constant runs).
- The quantitative density (Thm 4.1, ≫ x^{1−ε}) is the strongest *equal*-residue
  statement, later beaten by Maynard's positive-density 3.3 (digested in
  `maynard_dense_clusters_primes_subsets.md`). Both are the *wrong direction* for the
  switch density SUPPLY needs.
- The method — L-function-zero-free region plus Maier matrix — is precisely the kind
  of "L-function/toolkit" treatment ABGS says does NOT apply to the pair-frequency
  (switch) question. Reinforces why the switch side is the real barrier.

## What it does not settle

Nothing on the switch/differing-residue direction.

```claim
id: shiu-quantitative-strings
statement: Shiu's theorem quantified: strings of k consecutive primes ≡ a (mod q) exist
  with pn+k < x and k ≫ (loglog x/logloglog x)^{1/φ(q)} for a ∈ A± (weaker for general a);
  and the number of such strings ending < x is ≫ x^{1−ε(x)}.
hypotheses: q ≥ 3, (q,a)=1; a ∈ A± for the stronger bound.
holds-here: yes for q=4, a=1,3 (both in A±): arbitrarily long all-zero runs in the
  gap-parity string h, with quantitative density.
status: proved (Shiu 2000; this is the quantitative statement).
bearing: refutes door 3; equal-residue side is fully understood and positive-density (see
  also Maynard 3.3). The switch side is the only live difficulty.
anchor: shiu_strings_expository.full, Thms 1.1, 4.1
```
