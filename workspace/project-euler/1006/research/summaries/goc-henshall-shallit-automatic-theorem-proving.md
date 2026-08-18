# Goč, Henshall & Shallit — "Automatic Theorem-Proving in Combinatorics on Words"

Source: https://arxiv.org/pdf/1203.3758 (arXiv:1203.3758; CIAA 2012, LNCS 7381, pp. 180–191; journal version IJFCS 24 (2013) 781–798).

## What it establishes

The founding paper of the **mechanical theorem-proving school** (the approach
that became Shallit's *Walnut* tool) for automatic sequences:

- **Theorem 1 (the decision procedure).** If a property of a k-automatic
  sequence x can be expressed using quantifiers, logical operations, integer
  variables, addition, subtraction, indexing into x, and comparison of integers
  or of elements of x, then the property is **algorithmically decidable**.
  Method: build the automaton whose states carry base-k representations and
  check emptiness/universality/cycles mechanically.
- **Theorem 2.** Decidable whether two k-automatic sequences are shifts of each
  other. **Theorem 3.** The change-of-base induced sequence b(n) =
  (n mod 2) from a k-automatic x is automatic; more generally automaticity
  survives the natural digit operations.
- **Theorem 4 (main worked application).** The Thue–Morse word t has an
  **unbordered factor of length n iff the base-2 representation of n is not of
  the form 1(01\*0)\*10\*1** — resolving an open problem of **Currie and Saari**
  on unbordered factor lengths. **Theorems 5–6.** Rudin–Shapiro has an
  unbordered factor of every length; paperfolding's unbordered-factor lengths
  are recognised by an explicit small automaton.

The paper is dedicated to Sheng Yu (1950–2012). Its references include the
Currie–Saari "Least periods of factors of infinite words" paper this library
holds (`research/sources/currie-saari-least-periods-factors.full.md`) — the
run's own claim `fibonacci-least-period-set` rests on that same paper.

## Why it is in this library

The run's formalisation thrust (Lean arm, `pe1006-zeckendorf-automatic-digit-dp`
approach, Cobham–Bès–Frougny) concerns what can be decided/proved *mechanically*
about the Fibonacci word, and the same authors' decision-algorithm papers
(`research/sources/mousavi-schaeffer-shallit-fibonacci-automatic-ar5iv.full.md`,
`research/sources/hieronymi-decidability-sturmian-words-ar5iv.full.md`) are the
Fibonacci-specific and Sturmian-specific relatives of this general framework.
This paper supplies the *general* decidability statement (Theorem 1) those
specialise; it was a cited-by-2 frontier row with an obtainable primary source.

## Not established here

The Fibonacci word itself is NOT k-automatic (it is Fibonacci-automatic), so
Theorem 1 does not directly apply to it — that gap is exactly what
Mousavi–Schaeffer–Shallit and Hieronymi et al. fill. Nothing here changes the
PE1006 solution route (mechanical/floor-sum, not decision procedures).