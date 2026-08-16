# Final answer — Project Euler 719

## The result

```claim
id: t-final-answer
statement: T(10^12) = 128088830547982, where T(N) is the sum of all S-numbers <= N (N=10^12).
hypotheses: S-number definition as in problem.md / GOAL.md; exact integer arithmetic; base 10.
holds-here: yes
status: checked
bearing: this is the answer to Project Euler 719.
anchor: code/out/final_answer.md
follows-from: a038206-expr-recursion, a038206-bfile-cover
```

## How it was computed and verified (two independent routes)

Both programs run by tool_builder; outputs recorded in `code/out/final.log`.

**(a) solution.py — digit-partition recursion (the method, O(sqrt(N)) root scan).**

Reduces T(10^12) to scanning roots m in [2, 10^6] and testing whether
str(m^2) splits into 2+ contiguous blocks summing to m. Exact-integer,
no answer-space enumeration. The recursion is the same as the OEIS
A038206/A104113 program (Branicky). Output:

    T(10000)        = 41333          (matches oracle)
    T(1000000)      = 10804656
    T(10^12)        = 128088830547982

Worked examples reproduced: 81 root 9 blocks (8,1); 6724 root 82 blocks
(6,72,4); 8281 root 91 blocks (8,2,81); 9801 root 99 blocks (98,0,1) — all
is_S True.

**(b) verify_bfile.py — OEIS A038206 b-file (independent of the recursion).**

Reads the downloaded A038206 b-file and sums m^2 over roots m with
2 <= m <= isqrt(N). The b-file's first 408 terms end exactly at
term 408 = 1000000 = isqrt(10^12) (term 409 = 1005291 > 10^6), so it
covers every S-root <= 10^6. Output:

    T(10^4) from b-file  = 41333
    T(10^12) from b-file = 128088830547982

**Confirmation.** The two routes agree:

    solution.py T(10^12)      = 128088830547982
    verify_bfile.py T(10^12)  = 128088830547982

The oracle T(10^4)=41333 is reproduced by both, and the four worked examples
by solution.py.

## Files

- `code/solution.py` — the method (root scan + digit-partition recursion).
- `code/verify_bfile.py` — independent b-file verification route.
- `code/brute.py` — naive oracle.
- `research/sources/oeis_a038206_b.full.md` — A038206 b-file (roots m).
- `research/sources/oeis_a104113_b.full.md` — A104113 b-file (S-numbers).
- `code/out/roots408.txt` — the 408 roots, last = 1000000.
