# es_construct block tightness: interior blocks achieve cup+cap = n exactly

**Evidence captured in `code/out/commands.log`** (runs of `block_tightness.py`, `block_tightness_n8.py`, `block_tight_sum.py`, and the direct `es_block` probe).

## The identity

For the verified ES construction `lib.es_construct` (blocks T_i of X_n, |T_i| = C(n-2,i)):

- Endpoint blocks i = 0 and i = n-2 are singletons (cup = cap = 1).
- **Every interior block T_i (1 ≤ i ≤ n-3) achieves `longest_cup(T_i) = n-i-1` and `longest_cap(T_i) = i+1`, hence `longest_cup + longest_cap = n`, the maximum possible in both directions at once** (the declared bounds are no-(n-i)-cup ⇒ cup ≤ n-i, and no-(i+2)-cap ⇒ cap ≤ i+2; achieving n-i-1 and i+1 is one below each bound simultaneously).

Captured, n = 3..11: **identity holds for all interior blocks at every n.** Example (n=6): blocks C(4,i)=[1,4,6,4,1]; cup row [1,4,3,2,1] against bounds [6,5,4,3,2]; cap row [1,2,3,4,1] against bounds [2,3,4,5,6]; `cup_i + i` = [1,5,5,5,5], `cap_i - i` = [1,1,1,1,-3].

## The boundary

At n = 12 the `es_block`/`cupcap` implementation **violates** the identity for the first time:
```
VIOLATION n=12 i=4: |T|=210 cup=8(exp 7) cap=5(exp 5)
VIOLATION n=12 i=5: |T|=252 cup=7(exp 6) cap=6(exp 6)
VIOLATION n=12 i=6: |T|=210 cup=6(exp 5) cap=7(exp 7)
```
and the underlying `cupcap(8,6)` itself gives cup=8, cap=5 (bound cup ≤ 7): the *block builder* stops being tight at (k,l) = (8,6) and beyond, even though `cupcap(k,l)` for k,l ≤ 7 is tight.

## What this does and does not establish

- **Established (checked):** the *identity* `longest_cup(T_i) = n-i-1 ∧ longest_cap(T_i) = i+1` holds for the `es_construct` blocks at n = 3..11 and fails at n = 12.
- **Not established:** any theorem about all possible (k,l) — the identity's failure at n=12 is a property of *this recursive block builder* (`cupcap`'s cross-slope separation stops being strict enough at (8,6)), not a claim about the true extremal cups-and-caps set. The classical f(k,l) = C(k+l-4,k-2)+1 tightness (Morris–Soltan Thm 2.5) is a different, proved statement and is unaffected.

## Bearing

The identity is the sharpest per-block regularity observed in the run's verified construction: each interior block is *simultaneously* tight against its cap bound and its cup bound, so the whole 2^{n-2}-point set carries exactly the cup/cap budget the ES no-n-gon argument needs, with no slack in any interior block. This is a candidate structural lemma about the ES construction (GOAL 2/4), worth stating precisely and attacking; the n=12 boundary marks where the *implementation* stops being tight, so any attempt to extend the identity to all n must use a different block builder than `cupcap`.

```claim
id: es-construct-block-tightness
statement: In the verified es_construct ES construction, every interior block T_i (1≤i≤n−3) of X_n satisfies longest_cup(T_i)=n−i−1 and longest_cap(T_i)=i+1, so longest_cup+longest_cap=n; endpoints are singletons. Holds for n=3..11 and fails first at n=12 in the cupcap/es_block implementation (cupcap(8,6) gives cup=8 cap=5 against bound cup≤7).
hypotheses: the es_construct block builder (exact-rational cups/caps recursion), n in 3..11 for the positive result; the identity is about this construction's blocks, not about all extremal sets.
holds-here: yes — this is the run's own verified lower-bound construction; the identity is a per-block structural regularity of the extremal template.
status: checked (exact-arithmetic oracle, captured in code/out/commands.log: block_tightness.py, block_tightness_n8.py, block_tight_sum.py, direct es_block probe)
bearing: GOAL 2/4 — the sharpest per-block cup/cap regularity of the ES construction; a candidate structural lemma. The n=12 boundary is a property of the recursive block builder, not a statement about the true extremal cups/caps set (classical f(k,l) tightness is unaffected).
anchor: code/out/commands.log (block_tightness*, cupcap_tightness, direct probes)
```
