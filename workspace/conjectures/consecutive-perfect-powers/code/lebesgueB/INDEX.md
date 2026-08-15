# Index — code/lebesgueB

What each file here is for. Keep it current: describe files when created, refresh
after adding/renaming/deleting.

| File | Purpose |
| --- | --- |
| `verify_z[i]_mirror.py` | Machine-verifies the Z[i] proof of Lebesgue Case B (`x^p - y^2 = 1`, p odd prime >= 3, no solution) with EXACT integer arithmetic, keeping the unit **explicit** (`y+i = u(a+bi)^p`, u in {±1,±i}) — the mirror of `code/caseB/certify_lebesgue_caseB.py`. Steps: (1) x even impossible mod 4 + exact enumeration x<=10^6, p in {3,5,7,11,13} (0 squares); (2) gcd(y+i,y-i) a unit for every even y in [2,10^4]; (3) representation, norm `N(u(a+bi)^p)=(a^2+b^2)^p`, unit absorption, no random (a,b) yields a genuine solution; (4) b|Im, a|Re divisibility; `Im((a±i)^p)∉{±1}` (a in [1,500], p<=97); `Re((1+bi)^p)∉{±1}` (b in [1,500], p<=97). Correctness: all 13 checks PASS, exact integer arithmetic only (uses `lib.gaussint`), no floats; output in `code/out/lebesgueB_z[i].captured.txt`; note in `code/out/lebesgueB_z[i].note.md`.
