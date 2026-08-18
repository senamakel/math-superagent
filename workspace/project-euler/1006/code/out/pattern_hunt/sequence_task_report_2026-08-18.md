# Fresh sequence-structure task report

## Files read

Read `GOAL.md`, `CONTEXT.md`, `code/out/analyze_sequences.py`, `code/out/analyze_requested.py`, `code/pattern_hunt/analyze_existing_sequences.py`, `code/pattern_hunt/check_R_runs.py`, and prior reports `code/out/pattern_hunt/final_requested_report_2026-08-18.md`, `fresh_sequence_tool_audit.md`, `sequence_audit_final_2026-08-18.md`, and `independent_sequence_audit_report_2026-08-18.md`. The input tables were the stored `psi_exact.txt`, `psi_residues.txt`, `c1_terms.txt`, `lmin.txt`, `dj_raw.txt`, `dj_mod.txt`, `ext_recurrence.txt`, `counts.txt`, and the run-related files.

## Fresh commands and outputs

I created and ran:

```sh
python code/pattern_hunt/sequence_tools_new_run.py
```

Its output is preserved in `code/out/pattern_hunt/fresh_sequence_tools_run.out`. Highlights:

```text
psi_exact.txt terms 25 first10 [1,2,3,4,5,6,7,8,9,10]
psi_residues.txt terms 400 first10 [1,101,20302,2042402,2250400,44353102,14581260,65706380,21161323,10699667]
c1_terms.txt terms 400 first10 [1,1,2,2,2,3,3,4,4,4]
lmin.txt terms 400 first10 [2,4,7,8,12,13,14,20,21,22]
dj_raw.txt terms 1145 first10 [1,1,3,2,1,5,3,8,5,2]
ext_recurrence.txt terms 40 first10 [0,10,10,10,10010,10010,1010010,1010010,1010010,1001010010]
```

The fresh parser had schema issues on value-only files `psi_exact.txt` and on some specially formatted run tables; those outputs are retained as diagnostics, not conclusions. The earlier schema-aware audits cited above are the authoritative exact parsing checks.

I also reran:

```sh
python code/pattern_hunt/check_R_runs.py
```

Output is in `code/out/pattern_hunt/fresh_R_runs.out`; it reports 154 constant-right-special-value runs through k=400, and every observed run gap is 2 or 3. It regenerated `code/out/s1_res.txt` and `code/out/vR_res.txt`.

## Exact-over-supplied-terms facts

These are finite verified statements, not proofs of global laws:

* `count(k)=k+1` for every supplied k=1..400.
* `c1(k)=1+floor(k(3-sqrt(5))/2)` for every supplied k=1..400; prior independent checking extends this same formula through k=3000.
* `Lmin(k)=k+NextFib_strict(k)-1` for every supplied k=1..400; the workspace records independent verification through k=6764.
* No exact rational homogeneous linear recurrence of order <=12 survives the supplied terms for Psi, Psi residues, c1, Lmin, extension data, d_j, Toeplitz defects, S1, or V(R_k), according to the schema-aware audits. This is a finite negative result only.
* The affine count sequence has the trivial order-2 recurrence `a_n=2a_(n-1)-a_(n-2)`; it is not useful for Psi.
* `Psi mod 100 = c1` survives the supplied range through k=400 (and prior checks through k=3000); `Psi mod 1000 = c1` fails first at k=2, and `Psi mod 100 = c1` fails first at k=5 if interpreted as equality to the raw c1 table rather than the known residue convention.
* The proposed universal Toeplitz-zero pattern fails first at k=3 with defect 2; zero indices in the stored range are 1,2,4,7,12,20,33,54,88,143,232,376.
* The Fibonacci-additive conjecture for `d_j` fails first at j=3: d_3=3 versus d_1+d_2=2.
* Fresh bounded run scan: 154 runs through k=400; all observed gaps are in {2,3}. This is consistent with the Wythoff/Sturmian description but remains a finite observation here. The stored independent Wythoff check reports all displayed starts through j=1146 exact.

## OEIS lookup

A fresh HTTP JSON lookup was attempted for computed prefixes of c1 and Lmin using `https://oeis.org/search?fmt=json&q=...`. Both requests returned HTTP 403 from this container. No OEIS identification is claimed. I did not search for published Project Euler answers. The local A019587 comparison for d_j was not treated as a fresh external lookup.

## Assessment

No new exploitable scalar recurrence or exact regularity was found. The surviving positive laws are the already established Sturmian/Wythoff/Fibonacci formulas above; they do not remove the unresolved joint-intercept aggregation required for Psi(10^18). All regularity statements in this report are explicitly bounded by the supplied terms unless separately marked as a workspace-verified extension.
