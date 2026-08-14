# Index — code/scholar_oracle

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `oracle.py` | Exact-integer naive oracle. solutions(N) returns every (x,p,y,q) with x^p,y^q<=N and x^p-y^q=1 by enumerating the set of perfect powers and checking consecutive values. Verified correct by (a) reproducing worked example (3,2,2,3), (b) matching a direct pairwise enumerator for N in {9,100,1000}, (c) all N up to 1e8 returning exactly (3,2,2,3). |
