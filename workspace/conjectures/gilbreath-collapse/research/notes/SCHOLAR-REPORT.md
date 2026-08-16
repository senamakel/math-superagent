# Scholar report — library digested against COLLAPSE

What the source library establishes, what it does not, and where the run still needs
to look. Each note under `research/summaries/` now carries fenced claim blocks;
`research/CLAIMS.md` and `research/ENTAILMENT.md` re-derive from them.

## What the library adds (and that it does not move the crux)

The seven imported structural results of `problem.md` are the *whole substance* of the
relevant literature. The genuine sources re-derive row membership (Lucas `p=2`),
row size (`2^{pc(d)}`), and give the run/digital/self-similar vocabulary (Callan
`S(x)S(y)=S(x+y)`; Wu 2-regularity; Shevelev Fermat factorization). Nothing in the
library **answers** the crux — which sets `M_d △ M_{d'}` occur, and whether `S²`
factors through pair correlations. The strongest external caution is that the closest
related classification (NCI, Amarilli–Monet–Suciu) is **open in general**; a closed
"which sets occur" classification is not something this run can borrow, only compute.

## The one genuinely useful reframing, from O'Donnell

`S(n,h)` is a sum of `(n−2)` Walsh characters: `S = Σ_d χ_{M_d}`, so
`S² = Σ_{d,d'} χ_{M_d△M_{d'}}`. Orthonormality gives `E[S²] = #{d,d' : M_d = M_{d'}}
= n−2` for uniform `h`, reproduced **without** number theory and agreeing with imported
result 2. This makes the whole problem literally the description of the index multiset
— confirming GOAL priority 1 is the crux, and that the collapse question reduces to:
*is every set in `{M_d △ M_{d'}}` a union of O(1) adjacent runs?* This is a facts-of-the-
library framing; the composition of items 4, 6, 7 the project wants is still unproved.

## Sources that do NOT help here (read once, now closed)

- **Rains–Sloane, Self-Dual Codes** — MacWilliams/Krawtchouk/invariant machinery is
  for codes with a *dual*; `Φ_n` is onto (image = whole space), so there is no dual and
  nothing binds. Do not re-read.
- **Wolfram 1984** — the capture is a landing page, not the article. Unusable.
- **Barbé** — the `.full.md` is a wrong download (Painlevé VI paper); behave as absent.
- **Harborth density** — global sparsity, background only, no per-set structure.

## Sources that bear but only as vocabulary

- Mathonet et al. (not p-regular, Nim-sum/evil structure) — digital vocabulary.
- Wu 2-regularity and Shevelev — run/digital recurrences behind items 5–7.
- Rowland/Meštrović/Wu — definitional anchors of `M_d` membership and size.

## Contradictions / cautions

- No source contradicts the imported seven results or the recast memory (all consistent).
- **Shevelev's Fermat-number language must be suppressed** to the combinatorial
  factorisation identity only — the problem forbids prime/divisor machinery. Noted in
  its summary; the factorisation itself (∏ F(k_i) over set bits) is used as pure algebra.

## What the run still lacks (forward gaps)

1. The multiset census `{M_d △ M_{d'}}` at small `n` — **which** sets occur, run-count
   distribution — is computed by a script that has not yet been *executed and captured*
   in this run (`code/out/verify_multiset.py` + `verify_E_S2.py` are written but not
   run; that is a coder step). GOAL priority 1.
2. The composition of items 4, 6, 7 into a theorem — unproved; no source bridges it.
3. A witness search (two strings, same pair-correlations, different `S²`) — not done;
   the library gives no reason for or against.
