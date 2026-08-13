# fast_g.py as-is: G(20) overcount — where the 8 extra roots are

Companion to `code/out/fast_g_G20.txt` (full per-tuple table, 453 lines) and
`code/out/fast_g_as_is.txt` (raw `python code/pattern/fast_g.py` run).

## Results (mpmath-60, this run)

- `python code/pattern/fast_g.py` exactly as-is: **G(16)=9 AGREE** (only
  tuple g(16,5,5,6)=9), **G(20)=213 vs oracle 205** — overcount 8, matching
  the operator's earlier `G20_overcount.md`. Per-tuple values printed there
  (from the run): 9,8,8,7,7,10,9,12,10,9,9,8,11,10,11,9,9,12,10,12,10,13.
- Per-tuple strict recount with the eps-shifted endpoints
  `#{m ∈ ℤ : f(DL+1e-9) < m < f(DU−1e-9)}` reproduces the same 213
  (`g_int` column). The overcount is therefore **not** an endpoint-boundary
  artifact of the bisection: it is the counting rule itself.

## Where the 8 extra roots are — ONE clean pattern

The n-model identity `n_t = 2·Q_t` (tooth-phase counts `n_t =
[(c−t)·β + (s+t)·μ]/π`) holds exactly at every root: `n_p−n_q−2m ≡ 0` to 60
digits; and `n_p + n_q = s+c` exactly for **all** d (checked at random d),
so `n_p − n_q = 2f`.

Every crossing root of f has `n_p` exactly **half-integer** or exactly
**integer** (residue 1/2 vs 0 to 60 digits), and:

| p−q   | allowed n-model parity             | roots the f-docstring counts | roots the grid model counts |
|-------|------------------------------------|------------------------------|-----------------------------|
| odd   | n_p−n_q odd  ⇔  f half-integer     | ALL m (213)                  | only half-integer f        |
| even  | n_p−n_q even ⇔  f integer          | ALL m (213)                  | only integer f             |

The `n_integer_count.py` grid (1,048,577-pt, tol 1e-3, degenerate y<1e-5
excluded) selects exactly the parity-allowed family and reproduces **205** —
and its count is stable: the 8 differing tuples re-scanned at 4× density and
tol 1e-4 give the identical counts.

**The 8 overcounted tuples are the p−q ODD tuples whose f-interval contains
one integer f-level with no half-integer levels around it** — the integer-f
root is a fraudulent configuration under the model's own parity rule, and this
is the unique signature across all 22 tuples:

```
(17,6,5,6)  g_int=10 g_half=9  surplus 1   (extra m=-11, n_p=0.5, y_p=1.25e-1)
(18,5,5,8)  g_int= 8 g_half=7  surplus 1   (extra m=-11, n_p=0.5, y_p=1.25e-1)
(18,7,5,6)  g_int=11 g_half=10 surplus 1   (extra m=-12, n_p=0.5, y_p=1.25e-1)
(19,6,5,8)  g_int= 9 g_half=8  surplus 1   (extra m=-12, n_p=0.5, y_p=1.25e-1)
(19,8,5,6)  g_int=12 g_half=11 surplus 1   (extra m=-13, n_p=0.5, y_p=1.25e-1)
(20,5,6,9)  g_int=10 g_half=9  surplus 1   (extra m=-12, n_p=0.5, y_p=1.25e-1)
(20,5,7,8)  g_int=12 g_half=11 surplus 1   (extra m=-12, n_p=0.5, y_p=1.25e-1)
(20,9,5,6)  g_int=13 g_half=12 surplus 1   (extra m=-14, n_p=0.5, y_p=1.25e-1)
```

Every extra root sits at **n_p = 0.5** — the *smallest* p toothing level — with
SMALLEST d in the interval, |d−DL| = 2e-4 … 9.6e-4 (closest root to the lower
endpoint; not within the 1e-6 "near endpoint" flag, but the nearest one), all
at y_p = y_q = 1.249e-1 (non-degenerate). So the extras are neither
degenerate-collapse roots nor d ≥ 1e-6 endpoint crossings; they are genuine
interior f-integer crossings of the *wrong* parity family.

## Interpretation

`fast_g.py`'s docstring count `#{m ∈ ℤ : f(DL) < m < f(DU)}` is a necessary
condition (both planet types mesh ⇒ residues congruent mod 1 ⇒ f ∈ ℤ) but not
sufficient under the model's own admissibility rule (b): the n-model's
parity condition `n_p − n_q ≡ p − q (mod 2)` reduces the admissible roots to
the half-integer-f family for p−q odd; the form `g = #{half-integer levels m+½
between f(DL) and f(DU)}` is the parity-corrected count, and
`g_half` sums to exactly 205 over G(20).

For p−q EVEN tuples the parity-corrected form equals the docstring count
(g_int = g_grid for all 11 even tuples — their roots have n_p − n_q even, so
f is integer and the two counting rules coincide on the same family). For
p−q ODD tuples the two families are completely disjoint: f integer gives
n_p − n_q even (parity-violating), f half-integer gives n_p − n_q odd
(parity-allowed). g(16,5,5,6) is p−q ODD, so the docstring counts the
parity-violating integer-f family (m=−10..−2, n_p = 0.5..8.5) and the grid
counts the parity-allowed half-integer-f family (m=−9.5..−1.5, n_p = 1..9);
both families happen to contain 9 members, which is why g = 9 under both
counts. The oracle value 9 therefore does NOT discriminate the two families —
G(20)=205 does, and only the parity-allowed family survives every one of the
22 tuples. The parity rule is the bookkeeping of the mirror-pair symmetry
(two indistinguishable planets of the same type placed at ±β count once,
which halves the naive level count); the discrete levels themselves step by
half-integers because f = (n_p − n_q)/2 with n_p, n_q integers.

## Verdict

The f-crossing model is not wrong about geometry — it finds all the right
roots plus one spurious family. The G(500)-capable counting rule must count
f-levels of the correct parity class: **g = #{m ∈ ℤ/2 : f(DL) < m < f(DU),
2m ≡ p−q (mod 2)}**, which equals g_half for p−q odd and g_int for p−q even.
This reproduces 9 / 9 / 205 exactly and is an O(1)-per-tuple arithmetic count
once f(DL), f(DU), and the monotonicity of f are known.

```claim
id: fast_g_overcount_is_parity_family
statement: code/pattern/fast_g.py run as-is counts integer f-levels
  #{m in Z : f(DL) < m < f(DU)} and returns G(16)=9 (AGREE) but G(20)=213 vs
  the stated 205, an overcount of exactly 8. The 8 extra roots are, in all
  eight differing tuples, the f-INTEGER crossings of p-q ODD tuples whose
  interval contains an unmatched integer level: each sits at n_p = 0.5
  (half-integer n_p NOT allowed for p-q odd), at the smallest d in the
  interval with |d-DL| in 2e-4..9.6e-4 (nearest to, but not within 1e-6 of,
  the lower endpoint), y_p=y_q=1.249e-1 > 0 (not degenerate). The identity
  n_p + n_q = s+c holds exactly for all d (n_p-n_q = 2f, checked to 60
  digits); the parity-admissible root family is n_p - n_q = p - q (mod 2),
  i.e. f half-integer for p-q odd; counting only that family (g = #{m+1/2 in
  (f(DL), f(DU))} for p-q odd, unchanged for p-q even) reproduces 205.
hypotheses: f = Q_p - Q_q strictly increasing on (DL,DU); the n-model
  integrality n_p,n_q in Z plus cross-parity n_p - n_q = p - q (mod 2) is the
  meshing admissibility rule; every root of f at an integer or half-integer
  level is interior and non-degenerate.
holds-here: yes — computed at mpmath-60 over all 22 G(20) tuples, grid
  re-verified at 4x density and 10x tighter tolerance
status: checked
bearing: the parity-corrected counting rule g = #{levels m with
  f(DL)<m<f(DU), 2m = p-q (mod 2)} matches the oracle for every tuple and is
  the basis for a G(500) count that does not enumerate; any G(500) from the
  plain integer-level form of fast_g.py would overcount by this family
anchor: code/out/fast_g_G20.txt; code/out/fast_g_G20_note.md;
  code/pattern/fast_g.py as-is
source: tool_builder computation, PE620 oracle values from problem.md
```

## Files

- `code/pattern/fast_g.py` — run exactly as-is (no edits); its G(20)=213
  primed this investigation. saved run: `code/out/fast_g_as_is.txt`.
- `code/pattern/fast_g_per_tuple.py` — per-tuple strict f-count + per-root
  diagnostics; output `code/out/fast_g_G20.txt`.
- `code/out/n_integer_model_rerun.txt` — fresh run of the grid model
  (1M grid, tol 1e-3, degenerate-excluded): G(16)=9, G(20)=205.