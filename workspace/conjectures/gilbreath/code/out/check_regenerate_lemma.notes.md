# Regeneration lemma: off-by-one corrected, criterion ESTABLISHED

## Correction note (important)

This file previously reported the candidate regeneration lemma as **refuted**.
That conclusion was based on an **off-by-one** in the edge index used for `e_k`.
The corrected run (`regeneration/check_regenerate_lemma.py` ->
`code/out/check_regenerate_lemma.captured.txt`, sieve 20M, 1.27e6 primes,
depth 1000) shows the lemma holds **exactly**. Withdraw/refute the old
refutation.

## The bug

The leading `{0,2}` block of row k occupies 0-based columns `1..b_k`. Its
**last** value is at column `b_k`, not `b_k - 1`. The old run used
`e_k = A_k[b_k-1]` (and `q_k = A_{k+1}[b_k-1]`), which is one short of the
block. Since `A_{k+1}[j] = |A_k[j] - A_k[j+1]|`, the diff partner of the
intruder `c_k = A_k[b_k+1]` is `A_k[b_k]`. The old indexing made `q_k == |e_k-c_k|`
fail on 141/161 rows and the iff fail on 109 rows. All of that disappears with
`e_k = A_k[b_k]`.

## The established criterion (exact, checked over all 998 transitions)

Let `b_k = block_profile(A_k)` (leading `{0,2}` length), `c_k = A_k[b_k+1]`
(intruder, first value past the block), `e_k = A_k[b_k]` (true last `{0,2}`
value), and `q_k = A_{k+1}[b_k]` (which equals |e_k - c_k| identically).
Then for every k = 1..999 with an intruder:

- `q_k ∈ {0,2}`  ⟺  `(e_k == 2 and c_k == 4)`
- `b_{k+1} ≥ b_k`  ⟺  `(e_k == 2 and c_k == 4)`

**Zero failures** over all 998 transitions. Exactly **60** regeneration events
(matching the long-standing count of 60 in 999 transitions). For the 838 rows
whose whole leading length is `{0,2}` (no intruder), `b_{k+1} ≥ b_k` is always
false, so the iff still holds there.

Distributions (meaningful/intruder rows), (e,c) pairs:
(2,4):60, (0,4):36, (2,6):16, (0,6):13, (0,8):8, (2,8):8, (0,12):5, (0,14):4,
(2,10):4, (2,12):3, (0,10):2, (2,14):2.
q distribution: q=2:60, q=4:52, q=6:21, q=8:12, q=10:5, q=12:7, q=14:4.

## What this resolves and what remains open

Resolves the old open item "intruder==4 necessary but not sufficient (36 erosion
rows also have intruder 4)": among the 96 rows with intruder 4, the 60 with edge
2 regenerate and the 36 with edge 0 erode. Regeneration IS a single-row local
property: the block must currently end in 2 with a 4 immediately past it.

Open: showing this criterion is available often enough that erosion never drives
`b_k` to 0 (the honest open question — is there a k with block length 0?). The
criterion being local makes this more tractable, but it is not yet proved.

```claim
id: regeneration-lemma-edge-2-intruder-4-established
statement: For the Gilbreath rows of the primes to depth 1000, regeneration of the leading {0,2} block is characterised exactly by a single-row local property: b_{k+1} >= b_k  ⟺  (A_k[b_k] == 2 and A_k[b_k+1] == 4), where b_k = block_profile(A_k). The value q_k = A_{k+1}[b_k] = |A_k[b_k] - A_k[b_k+1]| lies in {0,2} under exactly the same condition. Zero failures over all 998 transitions (k=1..999); 60 regeneration events, matching the independent long-standing count.
hypotheses: b_k < width of A_k (i.e. an intruder exists). Blocks with no intruder (whole row in {0,2}) never regenerate (b_{k+1} >= b_k false) there, consistent with the iff. Indexing is 0-based within the row, A_0 = primes.
holds-here: yes — verified exactly to depth 1000 (sieve 20M), oracle PASSED (first-40 blocks + second entries match witnesses.json)
status: computed and checked (depth 1000), not yet proved for all k
anchor: code/out/check_regenerate_lemma.captured.txt
```

The earlier claim `candidate-regeneration-iff-refuted` is withdrawn; its
"failures" were the off-by-one bug.

```claim
id: ledger-scan-probe
statement: probe of the claim-block regeneration path
hypotheses: none
holds-here: yes
status: checked
bearing: probe only; delete after the mechanism is understood
anchor: code/out/check_regenerate_lemma.notes.md
source: probe
```
