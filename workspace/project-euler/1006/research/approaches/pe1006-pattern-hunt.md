# Approach: extract exploitable structure from the computed Ψ(k) data (pattern-hunt)

Status: CLOSED (structure found and verified; final method left to the solver role)

## What was tried

Given the run had computed Ψ(k) for k=1..20 (brute), I generated:

- exact Ψ(k), k=1..25
- residues Ψ(k) mod 101001001, k=1..400
- Lmin(k) = minimal prefix length of the Fibonacci word containing all k+1
  distinct length-k factors, k=1..400
(all via `code/pattern_hunt/gen_sequences.py`, verified against brute oracle:
counts k+1, set-stability under extension, Ψ(10) mod M = 10699667.)

## Sequence-tool verdicts (exact, over the terms supplied)

- Residue sequence Ψ(k) mod M: NO constant-coefficient linear recurrence of
  order ≤ 12; no low-degree polynomial fit; noise-flat (sample autocorrelation
  within 2σ, uniform leading digit, zero collisions over k=1..400). So no
  exploitable scalar regularity survives mod-M reduction.
- OEIS: exact Ψ(1..10) not found; residues(1..5) not found → no catalogued
  closed form; structure must be derived from the problem (mechanical word /
  floor-sum route).
- Lmin(1..24) matched OEIS A344953 ("positions of words in A341258 that end
  with 1"), a hit that led to a closed form.

## What survived (verified regularities)

1. **Lmin(k) = k + NextFib(k) − 1**, NextFib(k) = least Fibonacci > k.
   Verified exactly k=1..6764 by three independent implementations (bit-mask
   full sweep, plain-substring sampled, standalone bit-mask), zero mismatches,
   all Fibonacci-boundary checks pass, agrees with A344953 note terms 1..61.
   Consequence: prefix length ≥ 3k is always sufficient for a brute oracle;
   at block boundary k=F_m−1 the needed prefix is exactly 2k. Conjecture
   (computationally verified), not proof — but the k+1-once-per-k Sturmian
   factor structure is the natural explanation.
2. **Directive-1 autocorrelation formula exact**: for k = F_n−1 the k+1
   factors equal the N rotations of the truncated standard word, and
   Ψ(k) = Σ_{j,jp} A(jp−j) 10^{2k−2−j−jp} with
   A(d) = max(0,m−t)+max(0,m−(N−t)), t=(d·m) mod N, holds EXACTLY for
   n=2..12 (k up to 232), matching brute Ψ at every shared point.

## Refuted

- Lmin(k) = floor(k·φ²) is FALSE (fails at k=2; 992 failures for k≤1000).

## Why this closes the search

The two regularities above are load-bearing for the efficient method: directive
1 reduces Ψ at k=F_n−1 to a single lag-sum with geometric weights, and Lmin
bounds how long a prefix any oracle or factor-enumeration must read. The smoke
test of the final solution should reproduce Ψ(10) mod M = 10699667 and, where
reachable, these exact Ψ(k) values and Lmin(k).

Files: research/notes/pattern-hunt-pe1006.md, code/out/Lmin-formula-verified-6764.md,
code/pattern_hunt/*.py, code/out/psi_residues.txt, psi_exact.txt, lmin.txt.