# Approach — block-transfer bijection giving s(d) in closed form

```approach
idea: Classify the solution set as a base-10 "block transfer": prove that for
k ≤ d−1 the map x ↦ k·10^10 + x is a bijection from the block-0 solutions to
the block-k solutions, so s(d) is a closed-form geometric sum instead of an
enumerated total.
mechanism: The place-value identity gives, for 0 ≤ x < 10^m and k ≤ d−1,
  f_d(k·10^m + x) − f_d(x) = k·m·10^{m−1}
(numerically verified in code/pattern_mech_gen.py and code/pattern_residue.py).
At m=10 this is exactly k·10^10, hence
  f_d(k·10^10 + x) = f_d(x) + k·10^10.
Therefore f_d(x)=x ⟺ f_d(k·10^10 + x) = k·10^10 + x: translation by k·10^10
carries block-0 solutions to block-k solutions.  Since every solution satisfies
n ≤ d·10^10 (Khovanova–Marton Prop 9.1), the full solution set is the disjoint
union over k=0..d−1 of the translates, giving
  s(d) = d·Σ_{x∈S_0(d)} x + (d(d−1)/2)·10^10·|S_0(d)|,
where S_0(d) = {x < 10^10 : f(x,d)=x} is the block-0 seed set.  This converts
the whole computation into (i) a proof of the residue identity, (ii) an
enumeration of the small seed set S_0(d), and (iii) a closed-form sum — no
jump iterator over [0, d·10^10] at all.
status: proposed
first-step: prove the residue identity f_d(k·10^m + x) − f_d(x) = k·m·10^{m−1}
for k ≤ d−1, 0 ≤ x < 10^m (induction on m using the place-value closed form),
then specialise m=10 and verify the closed form against the on-disk sums
s(1)=22786974071, s(5)=100000000000, s(9)=360000000000.
```

## Which parts are established, which are speculation

- **Established numerically (this run).** The residue identity is checked on
  20 000 random x per (d,k) pair in `code/pattern_residue.py`, and the
  translation self-similarity on thousands of samples in
  `code/pattern_fun.py` / `code/pattern_mech_gen.py`. The block-transfer
  formula reproduces the known extreme cases exactly: d=5 and d=9 are pure
  {k·10^10} sets (hence s(5)=10^11, s(9)=36·10^10), and d=1 has only block 0.
- **Sourced.** The bound n ≤ d·10^10 and the periodicity mod 10^10 within
  [r·10^10,(r+1)·10^10) are Khovanova–Marton §9 (on disk).
- **Speculation / the actual work.** A *proof* of the residue identity (the
  run has only sampled it), and the full induction that decomposes S_0(d) the
  same way down to a base case. This is the genuinely different move: a
  bijective classification theorem, not an evaluation-plus-skip search.
