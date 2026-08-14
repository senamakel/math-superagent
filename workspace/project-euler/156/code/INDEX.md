# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for PE156: f_naive(n,d) counts digit d in 0..n by literal string counting; f_incremental(limit,d) returns solutions of f(n,d)=n in one running pass. Verified: reproduces the full f(n,1) table n=0..12, first solutions [0,1,199981] within 0..200000, and that f(n,1)=3 never occurs there. O(limit*digits) time, O(1) space. Deliberately non-efficient; the fast method later checks against it. |
