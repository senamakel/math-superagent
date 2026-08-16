# Index — code/casasalvero

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `eliminate_n3.py` | Exact elimination proof of Casas-Alvero for n=3 over QQ: lex Groebner of {f(r1), f'(r1), f(r2), f''(r2)}, shows rad(eliminated ideal) = pure-power locus P = <a2-a1^2/3, a3-a1^3/27> (E⊆P by reduction mod GB(P); P⊆rad(E) by Rabinowitsch). Includes hand/resultant independent route (rad(<Res(f,f'),27f(-a1/3)>)=P), oracle checks (x-2)^3 is a CA pure power, x^3-x fails over QQ, and the char-2 negative control (x^3-x^2, x^3+x are counterexamples — the step 'divide by 6' fails in char 2). Corrects the task's sign typo a3=-a1^3/27 → a3=+a1^3/27. Writes capture to code/out/elimination_n3.captured.txt; exit 0 iff all checks pass. |
