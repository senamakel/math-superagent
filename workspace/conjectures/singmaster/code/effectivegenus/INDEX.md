# Index — code/effectivegenus

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `NOTES.md` | _(undescribed)_ |
| `rep_pairs.py` | Geometric-type oracle for representative Binomial-vs-Binomial curves C(x,2)=C(y,k). Using w=2x-1 gives w^2 = 1+8*C(y,k); degree of RHS in y determines the cover: degree 3 -> genus 1 elliptic, degree 5 -> genus 2 hyperelliptic. Output: C(x,2)=C(y,3) is genus 1 (effective engine: elliptic logarithms, g=1) and C(x,2)=C(y,5) is genus 2 (BMSST hyperelliptic method, g=2). Verified against the computed genus grid (k2=2: floor((k1-1)/2)). Correctness: degree/parity genus formula is classical; cross-checked by the full grid in code/out/genus_table.captured.txt. Run: timeout 60 python3 code/effectivegenus/rep_pairs.py, output code/out/rep_pairs.captured.txt. |
