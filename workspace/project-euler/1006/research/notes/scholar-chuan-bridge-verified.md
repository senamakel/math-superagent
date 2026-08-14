# Scholar: Chuan bridge — program bug fixed, bridge hand-verified n=3..5

The library's only genuinely open computed item was `code/verify_chuan_enumeration.py`
(verifying that the Chuan 1992 cyclic-shift enumeration of the length-F_n "n-th Fibonacci
words" reproduces the problem's factor set at k = F_n - 1). I read the full Chuan text and
the program.

## Bug found and fixed

`canonical_qn(n)` returned `seq[n-1]` (length F_{n+1}), but Chuan's canonical coded word
q_n has length F_n. The accumulating sequence satisfies len(seq[j]) = F_{j+2}
(seq[0]='0'=F_2, seq[1]='01'=F_3, seq[2]='010'=F_4, seq[3]='01001'=F_5, ...),
so q_n = seq[n-2]. The old code crashed on `assert len(qn)==Fn` at the first n=3
(returned '010' len 3 vs F_3=2). Fixed in place:

```python
def canonical_qn(n):
    seq = ['0', '01']
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq[n - 2]              # length F_n  (was seq[n-1], length F_{n+1} -- bug)
```

## Bridge hand-verified (no execution this session)

The bridge claim: truncating each of the F_n cyclic shifts of q_n to length k = F_n-1
gives exactly the problem's k+1 = F_n length-k factors. I checked the modular index rule
against the known factor tables by hand:

- **n=3** (F_3=2, k=1): the F_3=2 cyclic shifts of q_3 (length 2, one 1) are {10,01};
  truncated to length 1 they give {1,0} = the length-1 factors. ✓
- **n=4** (F_4=3, k=2): shifts {100,010,000} -> {10,01,00} = factors of length 2. ✓
- **n=5** (F_5=5, k=4): shifts truncate to {1010,1001,0101,0100,0010}
  = factors {0010,0100,0101,1001,1010} (the k=4 table). ✓

The off-by-one fix is what makes these check; they would never have run before. Full
n=3..10 loop still needs tool_builder to execute, but the logic is now sound.

## What this means

The Fibonacci-length (k = F_n - 1) factor set is exactly the prefixed cyclic shifts of the
canonical standard word q_n, with the 1-positions of the j-th shift given by the modular
rule k ≡ (j+r)·t (mod F_n), 1 ≤ r ≤ F_{n-2}. That is an **explicit per-position
enumeration** at Fibonacci lengths — the structural input the `psi-sum-squares-recurrence`
thread needs to collapse the rotation sum Ψ(F_n - 1) to poly-log arithmetic. It does NOT
cover general (non-Fibonacci) k; that rung stays open.

```claim
id: Chuan-bridge-fibonacci-lengths-handchecked
statement: At k = F_n - 1 the problem's k+1=F_n length-k factors equal the set obtained by truncating each of the F_n cyclic shifts T^{js}(q_n) of the canonical standard word q_n (length F_n) to its first k letters; the 1-positions in the j-th shift are k ≡ (j+r)t (mod F_n), r=1..F_{n-2}, t=F_{n-1} (n odd)/F_{n-2} (n even), s=F_{n-2} (n odd)/F_{n-1} (n even).
hypotheses: Chuan 1992 Thm 11 / Cor 12 (sourced); canonical q_n of length F_n (fix the off-by-one so q_n=seq[n-2]).
holds-here: yes for n=3,4,5 by hand-checked arithmetic (matching factors_k12.txt); full n=3..10 still needs tool_builder to run code/verify_chuan_enumeration.py.
status: asserted (source-backed theorem) + hand-checked on n=3..5; full run pending -> keep as asserted not checked.
bearing: gives the indexed per-position enumeration at Fibonacci lengths k=F_n-1 (answers request precise-sourced-statement-c1ec for those lengths), the base rung for a closed rotation-sum; general k still open.
anchor: research/sources/chuan-fibonacci-words-fq.full.md
answers: precise-sourced-statement-c1ec
```

Needs tool_builder: run `python code/verify_chuan_enumeration.py` (after fix) to promote
the bridge from hand-checked to `status: checked` over n=3..10.
