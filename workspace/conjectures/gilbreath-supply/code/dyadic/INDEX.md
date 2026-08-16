# Index — code/dyadic

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `stratify_by_popcount.py` | TASK A — falsifier for the dyadic-gap-character route: stratifies S(n)=sum_{d=2}^{n-1}(-1)^{T(n,d)} by popcount(d) for n=400,1000,4000 on the real prime-residue string and a fixed-seed random-{1,3} control. Uses the O(n log n) per-term SOS transform lib.supply_fold.s_terms_sos; cross-checks totals against s_sos and, at n=200, s_direct and s_char_runs (three routes agree: sos=dir=char=0, ones=99). Conclusion (measured, not proved): weight is NOT concentrated in low popcount — |
| `stratum_recheck.py` | Fresh re-check of the popcount/run-count stratification of S(n) for the SUPPLY dyadic-gap route. Reproduces the earlier table (code/out/dyadic_stratify_by_popcount.captured.txt) as a pipeline check, then groups per-depth terms (-1)^{T(n,d)} for n=400/1000/4000 by popcount(d) and by downset run-count: counts of +1/-1 terms, net sign-sum per class, |
| `verify_character_identity.py` | TASK B — independent full verification of the corrected character identity (-1)^{T(n,d)} = prod over runs R=[u,v] of downset(d) of chi(r[a_R])*chi(r[b_R]), a=n-1-d+u, b=n-1-d+v+1, chi(x)=-1 iff x%4==3. Oracle = literal submask XOR t_direct(n,d,h) over the switch string h (NOT r — a first run wrongly fed r to t_direct and failed; fixed). Swept n=20..120, all d in [2,n-1]: 6868/6868 pairs pass. NEGATIVE CONTROL: spurious (-1)^{#runs(d)} factor, which fails on 449 pairs including d=3 — proving the no-extra-sign form is the true one. Exact arithmetic. |
