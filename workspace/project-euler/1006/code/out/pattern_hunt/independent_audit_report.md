# Independent audit of supplied integer sequences

Executed `python code/out/pattern_hunt/audit_existing_sequences.py`; raw output is beside this report. The parser found that several files are tabular records (index/value pairs), so the displayed “prefix” is the literal integer-token prefix, not automatically the mathematical sequence. Conclusions below therefore distinguish parsing facts from sequence claims.

## Exact-over-supplied-terms findings

- `counts.txt`: literal terms begin `1,2,2,3,3,4,...`. An exact order-3 recurrence was found on all 800 supplied integer tokens: `a_n=a_{n-1}+a_{n-2}-a_{n-3}` (1-based indices after the recurrence starts). This is a property of the supplied token sequence; inspect the file’s row format before interpreting it as the intended count sequence.
- `psi_exact.txt` and `psi_residues.txt`: their literal token streams begin `1,1,2,101,3,20302,...`, showing alternating index/value columns. Consequently, recurrence tests on raw tokens are not tests of Ψ(k). The anchor values are visibly present as pairs: `(3,20302)` and `(10,...)`; the prior validated report gives the residue anchor `10699667 mod 101001001`.
- `c1_terms.txt`, `lmin.txt`, `dj_raw.txt`, `dj_mod.txt`, and `counts.txt` likewise contain alternating index/value records. Their raw-token first differences fail immediately at token 2, so no raw-token linearity claim is supported.
- `vr_runvals.txt`: literal terms begin `0,10,10010,1010010,...`; these are decimal/run-value records, not a plausible ordinary Fibonacci sequence. The first differences have initial powers-of-10 behavior but are not constant; no exact recurrence of orders 1–5 was found on the literal supplied tokens.
- `vr_rungaps.txt`: literal prefix `1,3,2,3,3,2,3,...`; no exact order-1–5 constant-coefficient recurrence was found.
- `ext_recurrence.txt` and `extrecur_res.txt`: no exact order-1–5 constant-coefficient recurrence was found on their literal token streams.

## Explicit falsifiers for plausible patterns

- Constant first difference: first falsifier is token/index 2 for every listed nontrivial file where the first two terms differ.
- Raw Fibonacci identity `a_n=a_{n-1}+a_{n-2}`: first falsifier is index 3 for `counts` (`2 != 2+1`), and index 3 for `c1` raw tokens (`2 != 1+1` is actually equal there; the next interpretation is invalid because of alternating columns). Since these are row encodings, this test is not a mathematical claim about the underlying values.
- Exact low-order linear regularity: no order 1–5 recurrence was found for the raw streams of `psi_exact`, `psi_residues`, `c1_terms`, `lmin`, `dj_raw`, `dj_mod`, `vr_runvals`, `vr_rungaps`, `ext_recurrence`, or `extrecur_res`; the only positive raw-stream result was `counts`, order 3 `(1,1,-1)`.

## Conjectures (not established)

None. The audit found no new sequence conjecture that survives the file-format issue and exact supplied-term checks. Existing structural formulas—Sturmian `k+1` factor counts, `c1(k)=1+floor(k/phi^2)`, and `Lmin(k)=k+F(k)-1`—remain previously recorded/validated finite-range findings, not new conclusions of this audit.

## Limits

No OEIS/source lookup was used in this audit, and no larger run was made: scaling the same raw-token tests would not settle anything beyond the supplied data. A useful next step would first parse each file’s schema into `(index,value)` columns, then rerun the same exact tests on the value column only; that would answer a genuinely new question and avoid false regularities caused by alternating columns.
