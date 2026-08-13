# Tasks

## 1. Prove the 2-to-1 lifting — turn |A_k| = 2^(k-1) from computed into a theorem

The data says exactly two of three lifts survive at each step for every
k = 1..22. The sketch: LTE gives `2^{2·3^(k-2)} ≡ 1 + c·3^(k-1) (mod 3^k)`
with `3 ∤ c`. Then the three lifts shift the top ternary digit by
`{0, c, 2c} mod 3`, exactly one of which is 2, so exactly two survive.

**Before recording as proved**: compute `c` explicitly and verify the
congruence. If the sketch is wrong, the data still holds, but the mechanism is
different — find the real mechanism.

Thread: `research/threads/lifting-proof.md`.

- [ ] Compute `c = (2^{2·3^(k-2)} - 1) / 3^(k-1) mod 3` for small k and verify `c ≠ 0 mod 3`.
- [ ] Prove the LTE step: `v_3(2^{2·3^(k-2)} - 1) = k-1` and the quotient is not divisible by 3.
- [ ] Formalise the digit-shift argument: why exactly one of `{d, d+c, d+2c} mod 3` is 2.
- [ ] Write the theorem with proof. Record in CONTEXT.md as proved.

## 2. Get Narkiewicz's bound — the known nontrivial result

The standard reference: Narkiewicz (1980), "A note on a paper of H. Gupta
concerning powers of two". The bound is `|{n ≤ x : 2^n digit-2-free}| = O(x^c)`
with explicit `c < 1`. Find the primary source, extract the exact statement,
the constant, and the method.

Thread: `research/threads/narkiewicz-bound.md`.

- [ ] Locate and download the Narkiewicz paper.
- [ ] Extract the exact theorem statement, constant, and method.
- [ ] Record in a claim block; add to CONTEXT.md Established.
- [ ] If the bound is reproduced here: state the verification range and the oracle used.

## 3. What the sieve cannot see — redirect after the negative result

The modular sieve never empties. The conjecture is about the thin orbit `2^n`,
and no condition modulo a power of 3 reaches it. The next direction is the
literature's partial results:

- [ ] Lagarias (2009): Hausdorff dimension of digit-avoiding set, 3-adic dynamics.
- [ ] Dimitrov & Howe (2021/2023): powers of 3 with few nonzero bits (dual problem).
- [ ] Saye (2022): computational bounds, OEIS A351927/A351928.
- [ ] State precisely what each partial result establishes and what gap remains.

## Operational

- Launch with `timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`.
- State workers and range in every capture. Keep commands.log current.