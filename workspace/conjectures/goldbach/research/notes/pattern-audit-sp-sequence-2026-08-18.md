# Pattern audit: existing S(p) data

## Exact computed facts

Parsed `code/out/seq_sp_vec_10000000.txt`: 112 `(p,S(p))` pairs, in first-appearance order. The S values are all even. No p>7 has S(p) divisible by 6. The mod-3-compatible residue law has exactly two small exceptions: `(p,S)=(5,12),(7,30)`.

`python3 code/sequence_audit.py` produced the same checks: 112 pairs, p max 751, S max 9883994; no violations for p>7. Existing `seq_rn_50000.txt` has 24,999 terms and `seq_gn.txt` 999 terms; their displayed initial/tail values are irregular and no claim is promoted from them.

Exact sequence-tool results: on the first 24 S terms, `analyze_sequence` reports common divisor 2 and no low-degree polynomial; `find_linear_recurrence` reports no constant-coefficient linear recurrence of order <=12. OEIS lookup on the first 24 computed S terms returned no match. On the first 32 r(n) terms, no low-degree polynomial and no constant-coefficient recurrence of order <=12 were found.

These are exact descriptive results over supplied data, not proofs of continuation. The congruence rule itself is elementary: if S(p)=p+q and p,q>3 are prime, then p,q are ±1 mod 3; their sum determines the residue of S(p). The live continuation claim's first falsifier is a newly computed p>7 with S(p) divisible by 6 or with the wrong residue relative to p mod 3. Memory tools were unavailable during this run; this workspace note is the durable fallback.