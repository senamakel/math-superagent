# Lebesgue descent — proving the exponent-2 Case-A sub-claim in full

Status: live (rising-sea). Not yet a claim.

## The goal

Bank the exponent-2 Case A as **proved**, not verified-numerically. The claim
to upgrade is `exp2-descent-subclaim-no-extra`: the descent equation

```
r^q - 2^{mq-2} s^q = ±1,    q odd prime, m ≥ 1, r,s ≥ 1, gcd(r,s)=1
```

has only the solution (q,m,r,s) = (3,1,1,1). The library has it only
verified-numerically (q ≤ 29, m ≤ 7, r,s ≤ 300).

## Why this is the rising-sea move

The chisel school is grinding on the odd-prime descent (Mihailescu, class
group). That is genuinely hard and it is the sibling's move. The exponent-2
Case A, by contrast, is a classical theorem (Lebesgue 1850) that the workspace
has *reduced* to a sub-claim but not *proved*. It is the foundation every
downstream lemma is calibrated against, and the only part of the full proof
whose conclusion must CONTAIN the known solution (3,2,3) — that makes it the
cleanest possible object for the rising-sea method: change the ground so the
known solution is the ordinary one and the descent is forced.

## Native setting

The bijection (machine-verified in code/exp2_descent/verify_equivalence.py):

```
forward:  x = 2r^q + 1,  y = 2^m r s   satisfies x^2 - y^q = 1
backward: x^2 - y^q = 1 (x odd ≥ 3)  ⟹  y^q=(x-1)(x+1),  x-1=2u, x+1=2v,
          gcd(u,v)=1, v-u=1  ⟹  {u,v} = {r^q, 2^{mq-2}s^q}  ⟹  r^q - 2^{...}s^q = ±1
```

So the sub-claim IS Lebesgue's theorem. The equation is native to the second
degree: mod-q and mod-2-adic structure of `x^2 ≡ 1 (mod y^q)` — i.e. the ring
`Z[√ ·]` / a descent on q, not the cyclotomic obstruction. The known solution
sits at the bottom of that descent.

## The classical Lebesgue descent (what a proof must do)

From a hypothetical solution `x^2 = y^q + 1`, the descent produces a strictly
smaller solution `x'^2 = y'^q' + 1`, so infinite descent forces the minimal
case (q=3, then x^2 - y^3 = 1 → (3,2), already proved by Thue here). Key
structural facts to establish:
- parity / reduction of q: an odd prime power q forces q to be 3;
- the factorisation in `Z[√y^q]` or the `(x-1)(x+1) = y^q` split with
  gcd(x-1,x+1)=2;
- descent step: from a solution build a smaller one, so minimality pins q=3.

## Falsifier

Every sub-lemma must be run against the known solution: (q=3,m=1,r=s=1) must
be RETURNED, never excluded. A descent that descends below the known solution
and then says "no solution" is correct only if it started above it; state
where the known solution sits (it is the minimal/terminal point).

## Checklist / acceptance

A proof lands (claim `exp2-caseA-proved`) iff:
1. each descent step is exact integer algebra, machine-checkable;
2. the claim is not merely numerical (the existing sub-claim range is a
   cross-check, not the proof);
3. the known solution (3,2,3) / (q,m,r,s)=(3,1,1,1) is returned, not excluded;
4. second, independent route: either the two-route (Z-factorisation + Thue in
   the q=3 case => (3,2)) or the oracle, or a formalisation.
