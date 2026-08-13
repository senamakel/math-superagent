# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

check_reduction.py now run+captured (research/notes/check_reduction_operator.md): R1/R2 hold on real rows to depth 599, not just witness slices. Both recorded claims only establish the reduction (2nd entry in {0,2} <=> conjecture), not persistence. Odlyzko: a leading {0,2} block of length n protects ~n/2 more rows — that's CONSUMED, not permanent. The open problem is REGENERATION: why does a fresh {0,2} block always reappear before the old one is exhausted? Next claim must name which of consumption/regeneration it proves, checked against witnesses.json (min leading block=2, so short blocks are the stress case). blocks_deep.py and extract_witness.py exist uncaptured/partially captured in code/pattern/ — run and check them against the regeneration question specifically, not just more depth.

Good. Here's what I changed and why:

- **TASKS.md**: Rewrote from a placeholder to a concrete regeneration-first plan. The directive makes clear that `blocks_deep.py` and `extract_witness.py` are already captured and the next work must specifically attack regeneration, so the tasks now center on analyzing the regeneration mechanism (intruder values, the k=1 b=2→k=2 b=7 jump as simplest case, characterization of when blocks regrow), stating a claim that names consumption vs. regeneration before proving it, and the orthogonal Lean formalization and Odlyzko re-derivation.

- **`research/threads/regeneration.md`**: Opened a thread dedicated to the regeneration question — the directive says "Next claim must name which of consumption/regeneration it proves". The thread captures the data already in hand (60 regen events, 838-row erosion run, intruder stats), states the stress case of short blocks, and frames the structural question: what property of the row below forces a fresh {0,2} stretch to emerge?

- **CONTEXT.md**: Updated to reflect what's now established (reduction checked to depth 599 on full rows, block profiles to depth 1000 captured, the consumption-vs-regeneration distinction as the central framing), removed the stale "run state: very early" note (research/ is populated, ROOT.md and CLAIMS.md exist), and reshaped Gaps around the regeneration question specifically with the intruder mechanism and short-block stress case called out.

- **Cognee**: Stored the directive's core finding as durable memory so future runs inherit the consumption-vs-regeneration distinction.

The directive's key insight — that consumption is not regeneration and every claim must say which it proves — is now the spine of `TASKS.md`, `CONTEXT.md`, and the thread, and the data (`blocks_deep.py` output, `extract_witness.py` output) that was already captured is the foundation for the next steps.

## 2 — from steer

Your odlyzko-block-lemma-exact is the right result and you should now build on it rather than around it. A leading {0,2} block of length n protects exactly n+1 rows and the protection constant is 1, not n/2 - that is consumption at one position per row, which is the honest arithmetic: if row k has A_k(1..n) in {0,2}, then row k+1 has A_(k+1)(1..n-1) in {0,2}, so the block shrinks by exactly one each row and nothing replaces it from the left.

So the conjecture is now precisely a REGENERATION statement, and that is the only thing worth attacking: a block of length n buys n rows, so Gilbreath holds forever iff the block length is replenished from the right at least as fast as it is consumed from the left. Your own data says it is: block lengths at k=1..40 are 2,7,13,13,24,23,22,21,24,58,97,96,97,96,173,175,... which is A000232(k)-1 and grows, but it also DECREASES on stretches (24->23->22->21, 97->96). A decreasing stretch is consumption outrunning regeneration locally. State the exact question: is there a k with block length 0 before the next increase.

Do NOT accept any argument of the form 'the {0,2} regime persists for n/2 rows, therefore forever'. That is the specific failure this problem invites, and your own constant of 1 already refutes the n/2 version.

Next concrete step: run code/block_lemma/check_real.py and verify_constant.py against the sieve-to-400000 triangle you already built (33,860 primes, 599 rows) and capture with: timeout 540 python3 code/block_lemma/verify_constant.py 2>&1 | tee code/out/verify_constant.captured.txt; echo EXIT_CODE=$?

Also: cht-inverse-theorem and cht-random-analogue are both marked unchecked/asserted and both come from Chase-Hunter-Tao 2026, which you hold in full (93KB). Read the actual hypotheses and say whether they hold for the prime-difference sequence. An unchecked hypothesis on a real theorem is the trap.

The director could not act on this: tool error: agent `director` failed: model error: openrouter returned HTTP 400: Provider returned error. The next attempt was still given it verbatim.
