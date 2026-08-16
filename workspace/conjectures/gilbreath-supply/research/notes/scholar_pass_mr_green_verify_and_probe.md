# Scholar pass — verify Mauduit–Rivat/Green primary tier, test digit-sum↔gap-parity

This pass had three jobs: (1) confirm the two primary sources the previous
scholar session added (Mauduit–Rivat, Green) are what they claim to be,
(2) resolve whether those claims reached the ledger and durable memory, and
(3) probe the one open arithmetic question they bear on — whether the
digit-sum statistic (what they prove) is even correlated with the gap-parity
string h (what the SUPPLY fold reads).

## Source verification (both confirmed against full text)

- **Mauduit–Rivat**, "Sur un problème de Gelfond", *Annals of Math* 171(3) 2010.
  Full text lines 284–305 state Théorèmes 1–3 exactly as digested: for q,m>2,
  `#{p≤x : s_q(p)≡a mod m} = ((m,q−1)/m)·π(x;a,(m,q−1)) + O(x^{1−σ})`, and the
  equidistribution-if-α∉ℚ characterisation. Confirmed.
- **Green**, "Three topics in additive prime number theory", arXiv:0710.0823,
  Theorem 2.1.1 (lines 745–770): `E_{n≤X}Λ(n)(−1)^{s(n)} = O(X^{−δ})`, the
  binary case, self-contained via Vinogradov Type I/II sums. Confirmed.

## Ledger/memory resolution (three separate stores, three answers)

1. **`search_claims` (note-based claim ledger):** BOTH new claims are reachable —
   `mauduit-rivat-gelfond-sum-of-digits-primes-equidistributed` (status:
   proved/yes) and `mauduit-rivat-prime-digit-sum-equidistributed` (status:
   sourced/does-not-apply). The claims registered correctly.
2. **`research/CLAIMS.md` (rendered table) and `CONTEXT.md` Established:** both
   are STALE — neither lists the two new claims. These are derived files; I
   cannot hand-edit them. They will refresh on the next orchestrated write.
   **Do not read the absence of the claims there as their absence from the run.**
3. **Durable Cognee memory:** `remember_memory` writes succeed (three stored this
   pass), but `recall_memory` returns 404 "No data found" on every read — an
   environment-side read fault, 14 failures across the run against successful
   writes. The prior session's report that the claims were "stored in Cognee"
   cannot be confirmed by recall, but my re-stores this pass did succeed.

## The honest bearing — does NOT close the open request

The open request `walsh-spectral-subset-b904` asks for a Walsh-spectral/subset-sum
lower bound on `wt(Φ_n h)` for non-complicated h. Mauduit–Rivat and Green prove
the digit-sum parity of primes is equidistributed. **They fix the paradigm of a
weak, unconditional, provable arithmetic input — the exact shape the weakest-input
theorem would take — but the statistic they prove is `s_q(p)` (digit sum of the
prime value), while Φ reads `h[j]=((q_{j+1}−q_j)/2) mod 2` (mod-4 gap parity).
Different objects; no transfer.** Both notes carry this `does-not-apply`/inert
bearing explicitly. Filing them as closing the request would have been the
overclaim the scholar discipline exists to prevent.

## Probe for the transfer (UNEXECUTED — handoff)

Whether the MR statistic is even correlated with h is testable, and if
decorrelated the theorem is truly inert. `code/scholar/mr_gap_correlation_probe.py`
computes P(h=1 | digit-sum parity of q_j / q_{j+1}) over the first N primes and
checks pointwise independence. It is UNEXECUTED — the scholar role has no
execution tool, and I will not fabricate its output. tool_builder/coder should run:

```
python3 -m lib.capture --target code/out/mr_gap_correlation_probe.captured.txt -- python3 code/scholar/mr_gap_correlation_probe.py 300000
```

Until its output is read it establishes nothing.

```claim
id: mr-green-set-paradigm-not-transfer
statement: Mauduit–Rivat (Annals 2010, Théorèmes 1–3) and Green (arXiv:0710.0823, Thm 2.1.1) prove the digit-sum of primes is equidistributed with power-saving error — a weak, unconditional, provable arithmetic input. But the statistic is s_q(p) (digit sum of the prime value); the SUPPLY fold Φ reads h[j]=((q_{j+1}−q_j)/2) mod 2 (mod-4 gap parity, index-domain). These are different objects; no transfer exists in the library.
hypotheses: q,m>2 for MR Thm 3; q=2 binary case in Green; valid for primes unconditionally.
holds-here: yes for the digit-sum theorem itself; the transfer to h is absent — filing them as closing walsh-spectral-subset-b904 would be an overclaim.
status: proved (both sources verified against full text this pass)
bearing: fixes the paradigm for GOAL priority 2 (weakest arithmetic input) and the Walsh-side of open request walsh-spectral-subset-b904; does NOT close that request. Tests the digit-sum↔gap-parity correlation in code/scholar/mr_gap_correlation_probe.py (unexecuted).
anchor: research/sources/mauduit_rivat_gelfond_somme_chiffres_premiers_primary.full.md (Théorèmes 1–3, lines 284–305); research/sources/green_three_topics_additive_prime_number_theory.full.md (Thm 2.1.1, lines 745–770)
contradicts: none — both sources agree with each other and with recalled memory (none). Their "inert as proof" status is the honest position, matching the prior session's Pivato discipline.
answers: does NOT answer walsh-spectral-subset-b904 — recorded precisely so a later reader does not re-fetch them expecting closure.
```

## What the run still lacks

- **The finite-prefix transfer** (ergodic randomization → quantitative bound on
  the fixed prime h) — the single largest missing technical tool, confirmed still
  open, and now with a concrete probe attached to the MR side.
- The rendered CLAIMS.md / CONTEXT.md are stale with respect to the two new
  claims; they refresh on the next orchestrated write.
- recall_memory is broken (404) — durable recall must come from `search_claims`
  + `search_documents` + reading the render files, or from a fixed Cognee read.
