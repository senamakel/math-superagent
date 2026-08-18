# Immediate oracle and corrected counterexample capture

Commands run from `/workspace`:

```sh
python code/brute.py
python code/refute/run_fib_block_state_counterexample.py
```

The naive oracle reproduces both statement examples exactly:

```text
psi(3)= 20302
psi(10) mod M= 10699667
```

It also printed the bounded residues for k=1..20; the complete stdout is the
terminal capture from this run:

```text
1 1
2 101
3 20302
4 2042402
5 2250400
6 44353102
7 14581260
8 65706380
9 21161323
10 10699667
11 77738268
12 50567341
13 60501668
14 39049712
15 54716955
16 44184356
17 24648269
18 91059589
19 53059648
20 78244245
```

Corrected k=2 block-state counterexample stdout:

```text
smallest local summary collision: (2, 3, (2, 11, 101), '010', '101', (3, 11, 101), (3, 21, 201))
Fibonacci boundary checks:
1 (55, 21, 21) (55, 21, 21) False
2 (54, 231, 2121) (53, 221, 2021) True
3 (53, 2230, 203720) (51, 2120, 193620) True
4 (52, 22220, 20387620) (49, 20109, 18355519) True
5 (51, 212120, 1936777620) (47, 189999, 1732545419) True
6 (50, 2111119, 193578775619) (45, 1888898, 173154333418) True
7 (49, 21101109, 19357786575519) (43, 17877887, 16313319131317) True
```

`True` means the two boundary summaries differ. This is a bounded oracle/counterexample diagnostic, not a full-size evaluator. No value of Ψ(10^18) was computed or claimed.
