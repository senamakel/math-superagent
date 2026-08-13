# Tasks

**Directive**: stop growing k. sieve_lift.py at k=26 used 333s and 2.1 GiB;
materialising A_k as a set will OOM-kill the container. |A_k| = 2^(k-1) is
confirmed k ≤ 26; the question is why, not what the next count is.

## 1. Prove the 2-to-1 lifting — turn |A_k| = 2^(k-1) from computed into a theorem (unconditionally, all k)

The bijection argument (Φ_k bijective onto (Z/3^k)^×, |S_k ∩ (Z/3^k)^×| = 2^(k-1))
already gives |A_k| = 2^(k-1) as a theorem. What remains is the **mechanism**:
prove that exactly two of three lifts survive at each step, using LTE.

The sketch: LTE gives `2^{2·3^(k-2)} ≡ 1 + c·3^(k-1) (mod 3^k)` with `3 ∤ c`.
Then the three lifts shift the top ternary digit by `{0, c, 2c} mod 3`, exactly
one of which is 2, so exactly two survive. SAYE-2 already describes this
class-splitting rule and SAYE-3 gives the Θ(2^K) vs Θ(3^K) complexity that
matches it — connect them.

Thread: `research/threads/lifting-proof.md`.

- [ ] Compute `c = (2^{2·3^(k-2)} - 1) / 3^(k-1) mod 3` for small k and verify `c ≠ 0 mod 3`.
- [ ] Prove the LTE step: `v_3(2^{2·3^(k-2)} - 1) = k-1` and the quotient is not divisible by 3.
- [ ] Formalise the digit-shift argument: why exactly one of `{d, d+c, d+2c} mod 3` is 2.
- [ ] Connect to SAYE-2 (class-splitting rule) and SAYE-3 (complexity Θ(2^K) vs Θ(3^K)).
- [ ] Write the theorem with proof. Record in CONTEXT.md as proved.

## 2. Build on DH-1 — the state of the art

DH-1 (Dimitrov & Howe): any counterexample n ∉ {0,2,8} has a digit 2 **OR** at
least 26 digits equal to 1. This is a real constraint on the shape of a
counterexample and it is where new work starts.

- [ ] State precisely what DH-1 leaves open: if a counterexample exists, its ternary expansion either contains a 2 (trivial — then it's not digit-2-free) OR has ≥ 26 ones. So a digit-2-free counterexample must have ≥ 26 ones. The gap: can we improve 26? What structural fact about the orbit limits how many ones can appear without a 2?
- [ ] What would improve the 26: a better bound on the number of ones in a digit-2-free power of 2, leveraging the 3-adic orbit structure. The DH method uses nested moduli; the question is whether the sieve dynamics (2-to-1 lifting, SIEVE-EXACT) can sharpen it.
- [ ] Connect DH-1 to the dense-orbit / Cantor-set formulation: the 26-ones constraint is a finite-combinatorics consequence of the orbit structure; making it grow with n would be a genuine partial result.

## 3. Narkiewicz bound — secondary (statement already extracted)

The bound N(x) ≤ 1.62 x^(log_3 2) is already extracted as EP-406 and LAG-1.
The primary Narkiewicz (1980) paper is not yet downloaded but the statement is
not in doubt — downloading it is a verification step, not a gap.

Thread: `research/threads/narkiewicz-bound.md`.

- [ ] Download the Narkiewicz primary source (JSTOR 43667894).
- [ ] Verify the constant and method against EP-406/LAG-1.

## Operational

- **No sieving past k=26.** If a larger k is needed, count without storing, and
  state the memory cost before running.
- Launch with `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
- State workers and range in every capture. Keep commands.log current.