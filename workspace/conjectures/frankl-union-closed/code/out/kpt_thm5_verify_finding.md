# KPT Theorem 5 — corroborated computationally, and a counterexample constraint

<!-- regenerator-trigger -->

Source: Kabela–Polák–Teska, "The number of abundant elements in union-closed
families without small sets", arXiv:2212.09279, Theorem 5.
Full text: `research/sources/kabela-polk-teska-abundant-elements-2022.html.full.md`.

```claim
id: kpt-thm5-corrob-n4
statement: For every finite union-closed family F with empty set NOT in F,
k = min set size, n = max set size, and f = number of elements in MORE than
half the sets of F (strict: 2*count_x > |F|): (1) k>=n-3 => f>=k;
(2) k=n-4 => f>=k-1; (3) f >= min{n, 2k-n+1}. Verified COMPUTATIONALLY, 0
violations, over ALL 2546 empty-free union-closed families on n=1..4 (counts
n=1:1, n=2:6, n=3:60, n=4:2479; full enumeration guard = A102896 3,13,121,4959)
via the canonical oracle lib.uc (exact integer counts; strict test is exact
integer 2*c > |F|, no floats). Independently re-verified hand-computed
witnesses (2^4 minus {} f=4; {{a,b},{a,b,c}} f=2; {{a},{b},{a,b}} f=2;
{{a,b,c}} f=3) by a non-lib.uc inline route. Bound (3) equality f==min{n,2k-n+1}
hit by 65 families (n=1:1,n=2:5,n=3:16,n=4:43). Bound (2) tightness witness
needs n>=7 (k=n-4, k>=3), unreachable on n<=4. Exhaustive route stops at n=5
(2^32 subfamilies).
hypotheses: F finite union-closed, empty NOT in F; k=min set size, n=max set
size, f=# strict-abundant (more than half) elements; the strict vs >=half
convention matters (empty-free families).
holds-here: yes
status: verified-computational (n<=4 exhaustive via lib.uc; independent inline
witness route agrees); theorem itself is PROVED in the source — this is a
computational corroboration, plus the corollary below.
bearing: corroborates the sourced KPT Theorem 5 on all small union-closed
families and records its tightness pattern; the theorem is the source of a
minimal-counterexample constraint (see kpt-thm5-counterexample-corollary).
anchor: code/out/kpt_thm5_verify.py, code/out/kpt_thm5_verify.captured.txt,
code/out/kpt_thm5_indep.py, code/out/kpt_thm5_indep.captured.txt,
research/sources/kabela-polk-teska-abundant-elements-2022.html.full.md (Thm 5)
```

```claim
id: kpt-thm5-counterexample-corollary
statement: Let F be a finite union-closed family (empty NOT in F convention)
that FAILS Frankl's conjecture — i.e. no element is in more than half the sets,
so f=0. Then KPT Thm 5(3) forces 0 >= min{n, 2k-n+1}, hence 2k-n+1 <= 0,
i.e. n >= 2k+1: the largest set size is at least twice the smallest set size
plus one. Equivalently, a minimal counterexample (in the empty-free
convention) has max set size >= 2*min set size + 1. This is a PROVED
constraint derived from the sourced theorem, not a computation. It bounds the
ratio of largest to smallest set in any counterexample.
hypotheses: F counterexample to UC (no strict-abundant element), empty NOT in
F; k = min set size, n = max set size.
holds-here: yes (derived from KPT Thm 5(3), proved in source; corroborated
vacuously on n<=4 where no f=0 empty-free family exists)
status: proved (as a corollary of the sourced KPT Theorem 5(3))
bearing: a structural constraint on the abundance profile of a minimal
counterexample: its sets must span a size ratio of at least 2. Note the
empty-free convention (empty NOT in F) — under the empty-IN convention with
>= half abundance the parallel statement is the near-cube ratio we already
hold (no-degree-1-element-in-minimal-counterexample). This is the strict / 
empty-free dual.
anchor: research/sources/kabela-polk-teska-abundant-elements-2022.html.full.md
(Thm 5(3)); code/out/kpt_thm5_verify.py, code/out/kpt_thm5_verify.captured.txt
follows-from: kpt-thm5-corrob-n4
```

## Ceiling and honesty

- The corroboration is exhaustive and EXACT for n<=4; it does not prove the
  theorem for general n (the source's proof does that; this is independently
  verifying its statements on small families and its tightness).
- Bound (2)'s tightness witness needs n>=7 and is not reachable on n<=4 —
  recorded, not a failure.
- The corollary (n >= 2k+1 for a counterexample) is proved from the sourced
  theorem's bound (3), so it holds for ALL n, not just n<=4. It is a genuine
  structural constraint on a minimal counterexample, the first the abundance-
  profile thread has extracted that binds the size ratio rather than a count.
