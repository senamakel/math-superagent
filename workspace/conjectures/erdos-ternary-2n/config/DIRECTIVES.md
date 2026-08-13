# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Your sieve_Ak.py found the central fact and stopped one step short of what it means. I extended it from k=12 to k=22 by LIFTING (each surviving class mod 2*3^(k-2) has exactly three preimages mod 2*3^(k-1); test only those), and the result is exact: |A_k| = 2^(k-1) for every k=1..22, no deviation. Write-up and claim ternary-sieve-count-doubles are in code/out/sieve_cannot_close.md. What it means, and this is the run's main result so far: the DENSITY |A_k|/(2*3^(k-1)) = (1/2)(2/3)^(k-1) tends to zero while the COUNT doubles. Closing a sieve needs |A_k|=0 at some finite k, and |A_k| grows without bound. So NO obstruction modulo any power of 3 can prove this conjecture at any finite 3-adic precision. That is the honest answer to 'show 2^n mod 3^k forces a digit 2' — it does not, at any k. Record it as a negative result about the method, not as a failure. Three things. (1) PROVE the 2-to-1 lifting rather than tabulating it. The sketch: adding j*2*3^(k-2) to the exponent multiplies 2^r by (2^(2*3^(k-2)))^j, and lifting-the-exponent should give 2^(2*3^(k-2)) = 1 + c*3^(k-1) mod 3^k with 3 not dividing c. Then the three lifts shift the top ternary digit by {0,c,2c} mod 3, exactly one of which lands on 2, so exactly two survive. VERIFY c and that congruence before recording proved — that sketch is not a verification, and if it is wrong I want to know. A proof turns |A_k|=2^(k-1) from a fact about k<=22 into a theorem. (2) Then state what the sieve cannot see, and go there: the conjecture is about the thin orbit 2^n, and no modular condition reaches it. Narkiewicz's bound is the known nontrivial result — get it, with its exact constant and method. (3) Keep using timeout and tee; your captures are landing and commands.log is being written, which is exactly right.



## 2 — from steer

Excellent library work — DH-1, LAG-2 and the SAYE claims are exactly the right sources and you found them fast. Now stop growing k. sieve_lift.py 26 took 333 seconds and pushed the container to 2.1 GiB of its 8 GiB cap, because you are materialising A_k as a set of 2^(k-1) residues: k=26 is 33.5 million, k=30 would be 536 million and the container would be OOM-killed, which loses everything in flight and writes nothing to the console. Larger k buys nothing anyway — |A_k| = 2^(k-1) is confirmed k=1..26 and the question is no longer what the count is but why. Two things instead. (1) PROVE the 2-to-1 lifting. Sketch to verify, not to assume: adding j*2*3^(k-2) to the exponent multiplies 2^r by (2^(2*3^(k-2)))^j, and lifting-the-exponent should give 2^(2*3^(k-2)) = 1 + c*3^(k-1) mod 3^k with 3 not dividing c; then the three lifts shift the top ternary digit by {0,c,2c} mod 3, exactly one of which is 2, so exactly two survive. Verify c and that congruence. Your own SAYE-2 already describes this class-splitting and SAYE-3 gives the Theta(2^K) versus Theta(3^K) complexity that matches it — connect them and you have |A_k| = 2^(k-1) unconditionally, not just to k=26. That turns my checked claim into a theorem and proves no power-of-3 obstruction can ever close. (2) Then build on DH-1, which is the state of the art: any counterexample has a digit 2 OR at least 26 digits equal to 1. That is a real constraint on the shape of a counterexample and it is where new work has to start. State precisely what DH-1 leaves open and what would improve the 26. Do NOT run another sieve past k=26 — if you want a larger k, count without storing, and say what the memory cost would be before running it.

Everything is in order. Here's what I changed and why.

**`TASKS.md`**: Reordered around the two things the directive asked for. Task 1 is now "prove the 2-to-1 lifting unconditionally" — connecting the LTE sketch to SAYE-2 (class-splitting) and SAYE-3 (complexity), with the bijection route noted as the clean path to `|A_k| = 2^(k-1)` as a theorem. Task 2 is "Build on DH-1" — state the gap precisely, identify what structural fact limits ones without forcing a 2, and connect to the sieve dynamics. Narkiewicz dropped to tertiary. Added the operational block: no sieving past k=26; if a larger k is needed, count without storing and state memory cost first.

**`CONTEXT.md`**: Bumped the verified range from k≤22 to k≤26 everywhere; added the resource numbers (333s, 2.1 GiB) and the directive's constraint on further sieving; added DH-1 to Established with its precise statement; added SAYE-2 and SAYE-3 as proved claims connecting to the lifting proof.

**`research/threads/lifting-proof.md`**: Updated the thread block to list SAYE-2 and SAYE-3 as `rests-on` and the next step as connecting c to d₁(2ʲ); updated the data range to k=26 with the resource note.

**`research/threads/dh1-gap.md`**: New thread — states precisely what DH-1 leaves open (any digit-2-free counterexample needs ≥26 ones), what would improve it (coupling via Cantor-set formulation, transfer-operator spectral gap, growth argument), and concrete next steps connecting DH-1 to SIEVE-EXACT.

No threads were closed — all three remain live. No research request filed — DH-1 is already in the claim ledger and the Narkiewicz primary source is not the priority the directive sets.

## 3 — from steer

The lifting is now PROVED, unconditionally, in code/out/lifting_theorem.md with claim id ternary-lifting-theorem, status proved. It supersedes ternary-sieve-count-doubles, which only asserted the count for k<=22. Three lemmas. (1) 2^(2*3^(k-2)) has order 3 mod 3^k, so it equals 1 + c*3^(k-1) with 3 not dividing c; checked c=1 for k=2..15. (2) The three lifts r + j*2*3^(k-2) of a residue all agree mod 3^(k-1), because 2*3^(k-2) is the order of 2 mod 3^(k-1) — so they share their low k-1 ternary digits and can differ only in the k-th. (3) That k-th digit is d + v*j*c mod 3 where v = 2^r; since 3 divides neither v (a power of 2) nor c, the map j -> d + v*c*j is an affine bijection of Z/3, so the three top digits are 0,1,2 in some order. Exactly one lift has top digit 2 and dies; exactly two survive. Hence |A_k| = 2|A_{k-1}|, |A_1|=1, so |A_k| = 2^(k-1) for ALL k. Verified: zero violations over k=3..13 with 200 random r each. Consequence, and this is the run's main result: the sieve set doubles at every level and never empties, so NO congruence modulo any power of 3 can prove this conjecture at any finite precision. Stop sieving — sieve_structure.py enumerating A_k explicitly is data you no longer need, and the answer to how |A_k| behaves is now a theorem rather than a table. Two things instead. (1) Formalise this in Lean 4 — it is three short lemmas about orders in (Z/3^k)* and an affine bijection of Z/3, which is well within reach, and a machine-checked version would be a real artifact. Report #print axioms and every sorry. (2) Go where the sieve cannot see: DH-1 says any exception has a digit 2 or at least 26 digits equal to 1. State precisely what DH-1 leaves open, what improving 26 would take, and whether Lagarias's density bound and DH-1 can be combined.

All changes are in place and consistent. Here's my report.

**What I changed and why:**

The directive states the lifting theorem is now **proved unconditionally** (`ternary-lifting-theorem` in `code/out/lifting_theorem.md`) and directs two new lines of work — Lean formalisation and the DH-1 × Lagarias combination — while stopping sieving. I made these changes:

1. **`TASKS.md`** — rewritten so task 1 is now the Lean 4 formalisation (was: proving the lifting, which the directive says is done), task 2 is the DH-1 × Lagarias combination, and sieving is explicitly stopped. The lifting-proof work is removed from the active plan.
2. **`research/threads/lifting-proof.md`** — marked **dead** (proved, superseded) rather than live, so no role re-opens it.
3. **`research/threads/lean-formalization.md`** — new live thread for the three-lemma Lean formalisation.
4. **`research/threads/dh1-gap.md`** — question widened to the Lagarias combination, matching the directive's second item.
5. **`CONTEXT.md`** — the "Established" entry now records the lifting as an unconditional three-lemma proof (with the supersession of `ternary-sieve-count-doubles` and the stop-sieving instruction), and "Gaps" names the two new live directions.

I attempted to file a `request_research` for the DH-1 × Lagarias composition question, but the tool declined to queue it — the library already carries the individual claims (DH-1, LAG-2, LAG-4). The composition gap is nonetheless captured as a live task in `TASKS.md` and the dh1-gap thread, which is where it should direct work.

## 4 — from steer

verify_mechanism.captured.txt logs FAIL 'k=2 c=0: digits [0,0,1] not a full cycle' but this is a script bug, not a theorem contradiction. verify_mechanism.py reads digit at (r // 3**k) % 3; the newly-split digit at level k is at ternary position k-1, so it should read (r // 3**(k-1)) % 3. Recomputed by hand for c=0,k=2 (r=2^{0,2,4} mod 27 = 1,4,16): position k-1=1 gives digits [0,1,2], a full cycle, matching ternary-lifting-theorem. Fix the index, rerun, and update the captured output; do not file this as a contradiction of the proved theorem, and do not let it sit unexplained in CONTEXT.md.

Done. Three changes made, all from the directive:

1. **Fixed the bug** in `code/out/verify_mechanism.py` — `(r // 3**k) % 3` → `(r // 3**(k-1)) % 3`, matching the correct index `verify_mechanism2.py` already used and the operator's hand recomputation for c=0,k=2.

2. **Added a housekeeping task** to `TASKS.md` to rerun the fixed script so the captured output no longer shows the spurious FAIL.

3. **Explained the FAIL in CONTEXT.md** under Contradictions rather than letting it sit unexplained — tagged "Not a contradiction (script bug, now fixed)" with the same hand-check the operator gave.
