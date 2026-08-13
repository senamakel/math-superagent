```thread
question: What precisely does DH-1 leave open, and can the sieve dynamics improve the "26 ones" bound?
status: live
rests-on: DH-1, SIEVE-EXACT, ternary-sieve-count-doubles, DENSE-ORBIT
blocked-by: none
next: state the gap exactly; identify what structural fact about the 3-adic orbit constrains how many ones can appear without a 2
```

# Building on DH-1 — the state of the art

## What DH-1 says

Dimitrov & Howe (proved): for n ∉ {0,2,8}, the ternary expansion of 2^n
contains a digit 2 **or** at least 26 digits equal to 1.

Equivalently: any digit-2-free counterexample to the Erdős conjecture
(i.e., any n > 8 with 2^n having no digit 2) must have at least 26 digits
equal to 1 in its ternary expansion.

Source: `research/summaries/dimitrov-howe-ar5iv-full.md`, claim `DH-1`.

## What this leaves open

The 26 is a finite combinatorial bound derived from nested-modulus constraints
(DH-2 method). A counterexample, if one exists, cannot be too "thin" — it must
spend digits on ones. The gap has two dimensions:

1. **Can 26 be improved?** The DH method uses moduli chosen for large 2-part of
   ord_p(3) and large 3-part of ord_p(2). A larger computation or a better
   modulus selection might push the bound higher. But the directive says: build
   *on* DH-1, not just re-run their computation.

2. **What does the 26-ones constraint mean for the orbit?** The sieve dynamics
   (SIEVE-EXACT) shows that at every level k, exactly 2^(k-1) residue classes
   survive, each corresponding to a {0,1} digit pattern of length k with low
   digit 1. The question is: for an *actual* 2^n (not just a residue class
   that survives all finite levels), can the digit pattern have arbitrarily
   many ones without ever hitting a 2? DH-1 says: at least 26 ones. The
   structural question: does the 3-adic orbit impose a coupling between the
   occurrence of ones and the inevitability of a 2?

## What would improve the 26

- **A growth argument**: show that the number of ones must grow with n (or with
  the digit length) for any digit-2-free sequence compatible with the 3-adic
  orbit. If `#ones(n) ≥ f(log n)` with `f` unbounded, that would be a genuine
  partial result.
- **Coupling via the Cantor-set formulation**: the orbit {2^n} is dense in
  Z_3^×, and Σ_{0,1} ∩ Z_3^× is the {0,1}-Cantor set. The intersection of a
  dense orbit with a thin fractal is the right framing (LAG-3, LAG-4). DH-1
  says: if an orbit point lands in the Cantor set, it must have ≥ 26 ones.
  Can the Hausdorff dimension arguments from LAG-3 bound how many ones are
  forced?
- **Transfer-operator approach**: the 2-to-1 lifting (SIEVE-EXACT) is a Markov
  chain on the digits. The ones-count is a statistic on the paths. If the
  transfer operator has a spectral gap, the distribution of ones converges to
  a stationary measure; deviations from the mean are exponentially suppressed.
  DH-1's 26 is then a tail bound — can it be made quantitative?
- **Saye's recursion**: SAYE-3 gives an explicit Θ(2^K) recursion that
  enumerates all digit patterns realisable by some 2^n at depth K. Running it
  and tracking the ones-count per pattern would give the exact distribution at
  finite depth, and possibly a recurrence for the minimum ones-count at each
  depth.

## What to do

1. State the gap precisely: "DH-1 says ≥ 26 ones; what structural property of
   the 3-adic orbit limits how sparse the ones can be?"
2. Extract the DH modulus-selection method — which moduli gave the 26, and
   what would a larger computation cost?
3. Connect to SIEVE-EXACT: the bijection gives every {0,1} pattern of length k
   with low digit 1 is realised by exactly one residue class mod 2·3^(k-1).
   Not all such patterns correspond to the same n across different k — that's
   the consistency condition. DH-1 constrains the consistent patterns.
4. If Saye's recursion is available (it is in the library), run it to depth
   that reproduces the 26 bound and study the ones-count distribution.

## Status

- DH-1: proved, sourced, in the claim ledger.
- Gap stated: open. No improvement attempted yet.
- Connection to sieve dynamics: not yet drawn.