# Index — code/pe346

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | _(undescribed)_ |
| `check_reduction.py` | Verifies the structural reduction strong_sum = 1 - 31 - 8191 + pair_sum at checkpoints including 10^12, matching the known answer exactly. |
| `duplicates.py` | Counts distinct strong repunits vs raw (b,k) pairs below a bound; extracts the dedup correction (double-base repunits). Verified: correction=2 for all N in [10^4,10^12]. |
| `route3.py` | **Third independent PE346 solver, length-major enumeration**: outer loop over repunit length k (k=3.. while 2^k-1<=N), inner loop over bases b (while (pow(b,k)-1)//(b-1)<=N), exact integer arithmetic only, dedup in a set + {1}. Transposed from the base-major structure of brute.py/solution.py/verify.py and shares no code with them. Embeds hard-coded worked-example assertions (below 50 -> count 8 sum 171; below 1000 -> count 47 sum 15864); asserts PASS. At 10^12 gives sum=336108797689259276 count=1011529, matching the established answer; per-k base distribution (rows sum to 1011530 raw pairs = count+1, the expected single duplicate) is a sanity check. |
| `seq.py` | Sequence extractor: sorted strong repunits + per-power-of-ten count/sum, used for pattern analysis. |
| `solution.py` | Efficient PE346 solver, base-major with pw arithmetic: enumerate distinct (b^k-1)/(b-1) for b>=2, k>=3, plus 1. O(sqrt(N)*log N). Prints checkpoints N=50, 1000 and final N=10^12: sum 336108797689259276, count 1011529. |
| `verify.py` | _(undescribed)_ |
