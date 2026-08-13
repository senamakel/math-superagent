# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Elementary reductions are still 'asserted', not checked, and one is WRONG. code/out/verify_elementary_reductions.md/.py (just written, exact Fraction arithmetic, k up to 4999) confirms research/approaches/oracle-findings.md: the identity x=n,y=(n+1)/2,z=n(n+1)/2 for n=4k+3 solves 3/n NOT 4/n (residual is exactly 1/n). Do not cite it as covering n=3mod4 anywhere. The corrected identity n=4k+3,x=(n+1)/4,y=n(n+1)/4+1,z=y(y-1) does work and is now a checked claim (n-3mod4-covering-corrected). Also promote n-even-trivial (4/2m=1/m+1/2m+1/2m) to checked -- verified. Priority: run prime-reduction (composite n reduces to its smallest prime factor) through code, not just cited from Elsholtz-Tao, so it becomes checked too. These three plus prime-reduction are the whole reduction to 'odd prime p, p=1 mod 24' -- get them off 'asserted' before spending more budget on new identity search for the six square classes mod 840.

The changes are in place. Here is a summary of what was done and why:

**TASKS.md** — reordered the active items so that verifying `prime-reduction` in code is the next concrete step, ahead of any new identity search for the six square classes. The directive's priority is unambiguous: get the reduction chain off "asserted" before spending budget on new families.

**`research/threads/elementary-reductions.md`** — opened a thread tracking the whole question "is the chain to `odd prime p ≡ 1 (mod 24)` actually checked here?" with the five claims it rests on and the first concrete next step (write the scaling-lift program for `prime-reduction`).

**CONTEXT.md** — updated the Established section to reflect the corrected state: `n-even-trivial` checked to m=1..5000 (not just m=1..49); `prime-reduction` still asserted and now explicitly flagged as the top gap, with a note not to cite it as checked.
