# Board: no dyadic collapse at powers of two through k=25 (directive 36)

The k=25 dyadic-extension job (the target of directive 35's kill order)
completed without OOM — memory peaked near 2.3 GiB against the 16 GiB cap and
fell back to 1.5 GiB. Recorded as claim `dyadic-nu2-no-collapse-through-k25`
(`code/out/dyadic_extension_k25.note.md`); exact integers, status measured.

**The sharpest single statement in the extension.** At the 23 dyadic sample
indices `k = 3..25`, `n = 2^k, 2^k+1, 2^k-1` (`n` up to `2^25 = 33554432`),
the prime fold does **not** collapse at powers of two:

- `ν₂(2^25)/2^25 = 16778104/33554432 = 0.50003` — `ν₂(2^k)/2^k` stays at 1/2
  throughout.
- `|S(2^k)| ≤ 5282` (max at k=23; `S(2^25) = −1778`), so `|S|/n ≈ 1.6e-4`
  even against the worst `|S| = 5282` scaled at `n = 2^25` — three orders of
  magnitude below the `0.04n = (1 − 2·0.48)n` falsifier threshold.

Closed door 4 lives at powers of two; the fold does NOT collapse there for the
primes — the primes sit in the generic-balanced-good class
(`ν₂/n → 1/2`), not in the door-4 class (`all-ones` / Thue–Morse / 2-regular
give `ν₂ = O(1)`).

**The caveat, in the same claim.** This is 23 sampled dyadic points, not a
sweep. It does NOT extend the density-1 or dip-sparsity results, which remain
measured only to `N = 40000`, and it must not be cited as if it did. Powers of
two are structurally special `n` — which is what makes the sample interesting
and also what stops it being density evidence. It also does not reach the
surviving open statement (CONCLUSION.md §5), which no finite measurement
reaches.

Sequences and margin arithmetic: `code/out/dyadic_extension_k25.note.md`;
raw capture `code/out/dyadic_extension_k25.txt`.
