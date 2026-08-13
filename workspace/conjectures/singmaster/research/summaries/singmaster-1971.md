# Singmaster 1971 — TOMBSTONE: primary source NOT obtained

Source: D. Singmaster, "How often does an integer occur as a binomial coefficient?",
Amer. Math. Monthly 78 (1971) 385–386.

**STATUS: NOT HELD.** The file `research/sources/singmaster-1971.full.md` is the
Fermat's Library comments/annotation page (8538 bytes, mostly navigation, sign-in
prompts, and truncated comment snippets ending in ellipsis). It is NOT the paper.

## What the Fermat's Library page contains (and does not)

The Fermat's Library page reproduces two pages of the JSTOR facsimile (pages
385–386), which include the Research Problem statement, the Proposition
(`N(a) = O(log a)`), and the "Added in proof" note. However:

- The "Added in proof" is partly visible but the surrounding discussion is
  truncated Fermat's Library user comments, not the paper.
- The actual proof text visible in the facsimile image is not machine-readable
  in the .full.md; only the commenters' paraphrases are text.
- One comment says: "To prove the O(log a) bound we start by defining N(a) as
  the ..." — truncated with ellipsis.
- Another comment quotes the Kane 2007 bound with exponent 2 rather than 3,
  a known transcription error.

## What is reliably known about the paper (from secondary attestation)

- **Definition**: N(a) = number of times a occurs as C(x,y). N(1)=∞; N(a)<∞ for a>1.
- **Proposition**: N(a) = O(log a). Proof sketch (from AEH 1974, MRSTT, Wikipedia):
  let b be first with C(2b,b) > a; monotonicity forces i<b or j<b for any solution
  C(i+j,j)=a; hence N(a) ≤ 2b ≤ 2 + 2·log₂ a.
- **Conjecture**: N(a) = O(1).
- **"Added in proof"**: M(8)=3003, only N(a)≥8 with a<2^23; six N(a)=6 values
  below 2^23: 120, 210, 1540, 7140, 11628, 24310. (This is the witness frame,
  independently confirmed by `code/out/witnesses.json` and Singmaster FQ 1975.)

## Bearing for this run

The O(log a) bound, the conjecture statement, and the witness frame are all
reliably attested by multiple independent secondary sources (Singmaster's own FQ
1975 paper, AEH 1974, MRSTT, Wikipedia, de Weger 1997). But **no constant or
exponent should be quoted as directly from this primary** — the primary has not
been obtained. Demoted from `sourced (primary facsimile read)` to
`attested-by-secondary-sources`.

```claim
id: singmaster-1971-original
statement: Singmaster 1971 (AMM 78, 385-386; primary NOT held, attested by
  Singmaster FQ 1975, AEH 1974, MRSTT): N(a)=O(log a) via N(a)<=2+2 log_2 a;
  conjecture N(a)=O(1); M(8)=3003 is the only N(a)>=8 with a<2^23, and the six
  N(a)=6 values <2^23 are 120,210,1540,7140,11628,24310.
hypotheses: a>1; N counts C(x,y)=a over positive x,y (both symmetric copies).
holds-here: yes — the original bound and witness frame.
status: attested-by-secondary-sources (primary not held; file at
  research/sources/singmaster-1971.full.md is Fermat's Library comments page,
  not the paper; secondary attestation from Singmaster FQ 1975, AEH 1974
  primary, MRSTT §1, Wikipedia)
bearing: O(log a) is the baseline (grows with a, not a result); the witness
  frame independently confirms N(3003)=8 and the six N=6 values.
anchor: research/summaries/singmaster-1971.md
```
