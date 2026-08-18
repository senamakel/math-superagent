# g4-universal-euclidean-floor-sum

```skeleton
goal: The universal Euclidean (Chtholly) algorithm evaluates Psi(k) mod M in O(log k), carrying the tuple (count, sum x^j, sum x^j floor, sum x^j floor^2), x = 10^-1 mod M.
implies: The final step: makes Psi(10^18) computable in exact integers without enumerating 10^18 representatives; the cleanest closing lemma of the reduction.
rests-on: monoid-composition-formulas-verified, universal-euclidean-geometric-floor-sum, req-close-universal-euclidean, governing-universal-euclidean
status: open — the primitive's correctness is discharged on the library's word and code/lib/ueuclid.py is built with O(n) direct-loop oracle + O(log) split (verified outside the container); what is OPEN is the WIRING of the G3 telescoped v through this monoid: no in-container captured file yet shows Psi(10^4)=34432237 and Psi(10^6)=20938836 recomputed through the monoid, and k=10^18 has not been run under two Fibonacci approximants.
```
