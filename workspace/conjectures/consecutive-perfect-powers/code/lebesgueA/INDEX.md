# Index — code/lebesgueA

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_v2_reduction.py` | Verifies the 4-step v_2 parity reduction for Lebesgue Case A (x^2 - y^q = 1, q odd prime) in exact integer arithmetic: (1) x even impossible, x<=10^6 q odd prime<=97, two independent exact enumerations; (2) x odd structural split x-1=2u, x+1=2v, uv=2^{kq-2}z^q, exactly one of u,v even; (3) Branch A empty, Branch B = {(3,1,1,1)} over q<=97,k<=8,a,b<=300; (4) round-trip (3,1,1,1)->(x,y)=(3,2). All 4 steps PASS in 2.86 s. Correctness established: step-1 full solution set is exactly [(3,2,3)] and the known Branch-B solution (3,1,1,1) is returned, so the known solution (3,2,3) is the claimed RETURNED solution and never excluded (falsifier discipline). |
