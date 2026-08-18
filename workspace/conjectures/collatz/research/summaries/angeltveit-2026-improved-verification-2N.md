# Angeltveit 2026 — recursive verification algorithm

[[angeltveit-2026-improved-verification-2N.full]]

Source: https://arxiv.org/abs/2602.10466

The paper gives a recursive bit-by-bit algorithm for finite Collatz verification, using path merging, precomputed bitvectors, and a mod-9 sieve. It reports tests through `2^60`, not a completed record beyond Barina's `2^71`; estimates rather than results are given for `2^72`, `2^75`, and `2^77`. Its claimed subdoubling time growth is an implementation/theoretical algorithm claim, conditional on the stated sieve correctness and model. Thus it supplies a promising computational route, but no new verified frontier or proof of Collatz.