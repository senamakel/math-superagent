# Independent sequence audit — 2026-08-18

## Scope and method

Audited compact integer tables under `code/out` using the fresh programs:

- `code/pattern_hunt/audit_sequences_independent.py`
- `code/pattern_hunt/verify_audit_conclusions.py`

The first program separates explicit `(index,value)` rows from value-only tables, then tests:

1. exact rational homogeneous recurrences of orders 1–12;
2. known structural formulas (`counts=k+1`, `c1=1+floor(k/phi^2)`, strict-next-Fibonacci `Lmin`);
3. aligned modular relations between Ψ residues and `c1`;
4. aligned affine and first-difference relations between distinct sequences;
5. Fibonacci-index additive identities.

The second program independently reparses the tables and checks the positive identities and selected first falsifiers with exact integer arithmetic. No larger computation was run: extending the same scan would only enlarge finite evidence and would not settle a new structural claim.

## Exact outputs

Fresh audit output:

```text
counts.txt: rows=400 schema=index,value ... recurrence=(2, [2, -1])
c1_terms.txt: rows=400 schema=index,value ... recurrence=None
lmin.txt: rows=400 schema=index,value ... recurrence=None
psi_exact.txt: rows=25 schema=index,value ... recurrence=None
psi_residues.txt: rows=400 schema=index,value ... recurrence=None
ext_recurrence.txt: rows=40 schema=index,value ... recurrence=None
extrecur_res.txt: rows=400 schema=index,value ... recurrence=None
dj_raw.txt: rows=1145 schema=index,value ... recurrence=None
dj_mod.txt: rows=1145 schema=index,value ... recurrence=None
topelitz_defects.txt: rows=400 schema=index,value ... recurrence=None
vR_exact.txt: rows=3000 schema=index,value ... recurrence=None
s1_exact.txt: rows=3000 schema=index,value ... recurrence=None
counts=k+1 first bad: None
c1 floor law first bad: None
Lmin strict-next-Fibonacci law first bad: None
psi_residues.txt == c1_terms.txt mod 100 first bad: (5, 2250400, 2)
psi_residues.txt == c1_terms.txt mod 1000 first bad: (2, 101, 1)
psi_residues.txt == c1_terms.txt mod 101001001 first bad: (2, 101, 1)
cross s1_exact.txt vs vR_exact.txt: affine_slope=1 first_affine_bad=(3, 110, 10) difference_ratio=0 first_difference_bad=(2, 10, 10)
dj_raw.txt Fibonacci-index additive first bad: (3, 3, 2)
```

The full raw output is in `independent_sequence_audit_2026-08-18.txt`.

Independent second-route output:

```text
counts k+1: None
c1 floor law: None
Lmin law: None
Psi mod100=c1 first: (5, 2250400, 2)
Psi mod1000=c1 first: (2, 101, 1)
S1=VR first: (3, 110, 10)
dj Fibonacci additive first: (3, 3, 2)
```

## Interpretation

- The only exact recurrence reported by the schema-aware scan is for `counts.txt`, but that table is simply `count(k)=k+1`; the recurrence `a_n=2a_{n-1}-a_{n-2}` is the trivial recurrence of an affine sequence, not an exploitable relation for Ψ.
- No exact rational recurrence of order ≤12 survived on the correctly parsed value columns of Ψ, Ψ residues, `c1`, `Lmin`, extension data, `d_j`, Toeplitz defects, `S1`, or `V(R_k)`.
- Previously recorded structural formulas survive independently through their stored ranges:
  - `counts(k)=k+1` through 400;
  - `c1(k)=1+floor(k/phi^2)` through 400;
  - `Lmin(k)=k+NextFib_strict(k)-1` through 400 in this audit (the workspace separately records verification through 6764).
- No new cross-sequence relation survived. The tempting relations fail exactly at:
  - `Psi(k) mod 100 = c1(k)`: first failure `k=5`, `2250400 mod 100 = 0`, while `c1(5)=2`;
  - `Psi(k) mod 1000 = c1(k)`: first failure `k=2`, `101 mod 1000 = 101`, while `c1(2)=1`;
  - `Psi(k) mod M = c1(k)`: first failure `k=2`, `101 != 1 mod M`;
  - `S1(k)=V(R_k)`: first failure `k=3`, `S1(3)=110`, `V(R_3)=10`;
  - Fibonacci-additive `d_j`: first failure `j=3`, `d_3=3` versus `d_1+d_2=2`.

## Conjecture status

**No new surviving conjecture.** Therefore there is no new first-falsifier target to report. The positive floor/Fibonacci formulas are prior workspace findings, independently rechecked here; they are not newly discovered by this audit and do not by themselves solve `Psi(10^18)`.

## Validation commands

```sh
python code/pattern_hunt/audit_sequences_independent.py
python code/pattern_hunt/verify_audit_conclusions.py
```
