```thread
question: What is the exact statement, constant, and method of Narkiewicz's bound on {n <= x : 2^n digit-2-free}?
status: live
rests-on: (none yet — literature lead from problem.md and FRONTIER.md)
blocked-by: no primary source in the library yet
next: locate and download Narkiewicz (1980) "A note on a paper of H. Gupta concerning powers of two"
```

# Narkiewicz's bound — the known nontrivial result

## Why this thread

The modular sieve has now been shown (checked k ≤ 22) to grow like `2^(k-1)`,
so it can never close. Narkiewicz's bound is the standard nontrivial result on
the thin-orbit question itself, and is what the run should extract next
(directive item 2).

## What is needed

The exact theorem from Narkiewicz (1980), "A note on a paper of H. Gupta
concerning powers of two", Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat.
Fiz. (1980), no. 678-715, 173-174 (1981). MR 623247.

- Exact statement: which set is counted, over which range, with what bound.
- The explicit constant `c < 1` in `O(x^c)`, if the source gives it.
- The method (covering, Diophantine approximation, S-unit arguments, ...).

The FRONTIER.md row cites it via
`https://www.jstor.org/stable/43667894` ("A note on a paper of H. Gupta
concerning powers of two and three") and MR 623247.

## Falsifier

If the source is located and it does not give an `O(x^c)` bound with `c < 1`,
or if the bound applies only to a different digit/position condition, then the
"known nontrivial result" claim in the workspace is wrong and must be corrected.

## Status

Not started. No primary source in the library yet.
