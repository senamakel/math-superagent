# What this folder is for

`rep_pairs.py` — oracle check attributing the correct effective integral-point
engine to the two representative binomial curves used in the
`research/approaches/effective-methods-wall.md` deliverable: `C(x,2)=C(y,3)`
(genus 1 elliptic -> David elliptic logarithms) and `C(x,2)=C(y,5)` (genus 2
hyperelliptic -> Bugeaud–Mignotte–Siksek–Stoll–Tengely hyperelliptic method).
It completes the square `(2x-1)^2 = 1 + 8*C(x,2)` and reads the genus off the
degree/parity of the resulting polynomial in `y`.
