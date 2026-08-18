# Integer-sequence pattern hunt (2026-08-18)

## Scope and method
Inspected the exact and modular sequence artifacts in `code/out`: `psi_exact`, `psi_residues`, `c1_terms`, `lmin`, `counts`, `dj_raw`, and `ext_recurrence`/`extrecur_res`. Existing tools were executed: `analyze_existing_sequences.py`, `analyze_exact_new.py`, `check_dj_oeis.py`, and `check_small_moduli.py`. These are exact integer scans; recurrence searches test homogeneous constant-coefficient recurrences of orders up to 12, while Berlekamp–Massey results are modular diagnostics only.

The governing structural theory remains Sturmian/mechanical-word factor complexity and the established formulas in the workspace. No full-size brute force was used. The existing stored oracle ranges are the evidence: Psi exact k=1..25, Psi residues k=1..400, c1/Lmin/counts k=1..400, d_j j=1..1145, ext-recurrence k=1..40.

## Exact outputs

- `psi_exact`: first terms are `1, 101, 20302, 2042402, 204252402, 30445654403, 3054587854503, 407470828064704`; no exact homogeneous recurrence of order <=12 fits the 25 terms. BM complexity modulo 101001001: 13 on the 25-term exact prefix and 200 on the 400-term residue sequence.
- `c1`: `c1(k)=1+floor(k*(3-sqrt(5))/2)` is true for every stored k=1..400; first falsifier: none. No exact order <=12 recurrence. BM complexity modulo 101001001: 232/400 (not evidence of a global recurrence).
- `counts`: `count(k)=k+1` for all stored k=1..400; no falsifier.
- `lmin`: `Lmin(k)=k+NextFib_strict(k)-1` for all stored k=1..400; existing independent artifacts extend verification to at least 6764/10000. No exact order <=12 recurrence; no falsifier for the stated formula in the tested range.
- `d_j`: 1145 stored terms agree exactly with the local OEIS A019587 comparison for j=1..1145. No exact order <=12 recurrence; BM complexity modulo 101001001 is 573/1145. First falsifier of the OEIS comparison: none in the stored range.
- `ext_recurrence`: no exact order <=12 recurrence through 40 terms; no claimed recurrence survived this test.

## Modular conjecture attacks / first falsifiers

- `Psi(k) mod 4 = c1(k) mod 4`: true on the stored tested range (k=1..400).
- `Psi(k) mod 8 = c1(k) mod 8`: false first at k=2: `Psi(2)=101 ≡ 5 (mod 8)`, while `c1(2)=1`.
- The same equality modulo 16 is also false at k=2.
- The supplied exact data falsifies simple exact affine/Fibonacci-additive Psi laws already at k=2.

## OEIS lookup status

The local reference material identifies the Fibonacci word as OEIS A003849 and the `d_j` comparison as A019587. No locally established OEIS match was found for the raw consecutive Psi values, c1, Lmin, or ext-recurrence columns. Thus no external OEIS identification is asserted for those sequences.

## Extra-term attack

No new large run was launched. Extending the same finite scans would only add bounded evidence and would not settle the unresolved structural O(log) evaluation of Psi(10^18); this is why the existing exact ranges were used as the oracle. The available polynomial-time/small-oracle programs already provide the requested additional checks without enumerating full-size factors.

## Validation command

```sh
python code/pattern_hunt/analyze_existing_sequences.py
python code/pattern_hunt/analyze_exact_new.py
python code/pattern_hunt/check_dj_oeis.py
python code/pattern_hunt/check_small_moduli.py
```

All commands exited successfully. The outputs above are copied from that run; recurrence non-detections are finite diagnostics, not proofs of non-C-finiteness.
