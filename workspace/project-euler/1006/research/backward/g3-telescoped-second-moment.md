# g3-telescoped-second-moment

```skeleton
goal: v(x) = floor(x+ka) - 10^(k-1) floor(x) + 9 sum_{j=1}^{k-1} 10^(k-1-j) floor(x+ja); Psi(k) is the second moment of this geometric floor-sum over m=0..k.
implies: Reduces the squares-of-values to one geometrically-weighted floor-sum whose second moment Lemma 4 evaluates; also removes the factor enumeration entirely.
rests-on: 
status: discharged — formulation (B) of code/mech/mech_psi.py, captured code/out/mech_psi.captured.txt: (A)==(B) in total and per-word multiset k=1..400, reproducing Psi(3)=20302 and Psi(10)=10699667 against brute. The telescoped form is verified; it is the exact object G4 must evaluate at full size.
```
