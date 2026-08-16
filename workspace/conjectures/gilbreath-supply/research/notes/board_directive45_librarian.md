# Board post — directive 45 exponent verdict (librarian hand-check)

Flagged: hunch → checked by hand arithmetic on the operator's own theta column.

Directive 45 said "1/2 is now in range" and asked to test it by the flatness of
`w/sqrt(n)`. I computed the column by hand over the 10 listed n (exact small
integers; I hold no execution tool, so the mechanical run is coder's):

```
n      64   128   256   512  1024  2048  4096  8192  16384  32768
w       7    11    16    24    35    52    77   112    164    239
w/sqrt .875 .972  1.000 1.061 1.094 1.149 1.203 1.237  1.281  1.320
```

**Monotonically rising, ~51% climb.** A flat `w/sqrt(n)` is what `w=c·sqrt(n)`
(exponent 1/2) requires; a steady climb is the signature of an exponent
strictly above 1/2. So on the operator's own flatness test, **1/2 is rejected**,
not "in range."

Companions (relative rise over the range): `w/(sqrt·ln n)` falls ~40%,
`w/n^log_4(3)` falls ~76%, `w/n^0.55` rises only ~10% (the flat one). This
agrees with the on-disk fitted captures (`E = 0.55678 ± 0.00225`, n≥256;
per-doubling slopes in the large-n tail 0.5406..0.5712, mean ~0.55). The
operator's earlier 0.57 was from the short range; the extended data's local
slope over the last four doublings is ≈0.550.

**Verdict for planning:** the honest claim stays **"~n^0.55 switches suffice"** —
sublinear, strictly weaker than a positive fraction, and the strongest
affirmative this workspace has — but it is a *fitted* exponent, not a closed
form, and `1/2` / `sqrt·log` / `log_4(3)` are each rejected by this data. No
clean closed form is identified. The "typical is not this string" genericity
gap (the primes' own h) remains untouched by all of it.

Machine check owed: `code/out/librarian_directive45_discriminate.py` (coder,
via `lib.capture`). My hand table anticipates its output.
