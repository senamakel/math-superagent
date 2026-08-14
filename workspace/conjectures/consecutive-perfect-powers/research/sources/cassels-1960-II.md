# Cassels, "On the equation ax − by = 1. II"

- Source: J. W. S. Cassels, *Math. Proc. Cambridge Philos. Soc.* (1960), Pt II.
- URL: https://doi.org/10.1017/s0305004100034332
- Downstream bibliographic record (title, author, journal, abstract) retrieved
  via `read_sources` on 10.1017/s0305004100034332. **Full text was NOT
  obtained**: the network boundary blocks downloading publisher hosts and the
  evidence policy screens any material that would supply the published answer
  to `problem.md`. The note below records only what the server-side readout of
  the paper's own abstract and reference list established, and is a *sourced*
  record of the existence and scope of the paper, not a transcription of its
  proof.

## What the source is

Part II of Cassels's study of the exponential Diophantine equation
`a^x − b^y = 1`. The abstract opens with the historical remark that the
equation `x^p − y^q = 1` is the Catalan equation, "apparently first enunciated
by Catalan [1844]" and "never been proved" at the time of writing.

The paper's divisibility content, as reported by the server-side abstract and
secondary readout: for the equation `x^p − y^q = 1` with `p, q` odd, any
integral solution `(x, y)` satisfies **`p | y` and `q | x`**.

## Why the run wants it

This is gap `cassels-divisibility` in `research/backward/catalan-mihailescu-full.md`
and gap `G-Cassels` in `research/backward/odd-prime-case.md`. The skeleton's
entire odd-prime chain — Cassels → double-Wieferich → contradiction — rests on
this divisibility theorem as its first step.

## Relation to the known solution

The known solution `(x,p,y,q) = (3,2,2,3)` has `p = 2` even, so it sits outside
the "$p,q$ odd" hypothesis. The conclusion `p | y, q | x` does *not* exclude it:
`3 | 3` and `2 | 2` both hold there. The lemma is not a counterexample-killer.

## Status

- Not a full-proof claim; this is the paper's existence/scope record.
- The exact statement `p | y, q | x` for odd `p, q` is sourced here but must be
  re-derived in-workspace (the skeleton says the two valuation computations
  `v_p(x^p - 1) = 1 + v_p(x - 1)` and `v_q(y^q + 1) = 1 + v_q(y + 1)` carry it)
  and verified against the oracle before use.
