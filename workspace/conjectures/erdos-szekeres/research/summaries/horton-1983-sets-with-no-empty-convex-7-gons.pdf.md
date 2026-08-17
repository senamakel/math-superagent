> **Note — what this source establishes and what it implies here.**

# Horton 1983 — sets with no empty convex 7-gons

**Source:** J. D. Horton, *Canad. Math. Bull.* 26(4) (1983) 482–484, DOI 10.4153/CMB-1983-077-8. Cambridge core PDF held.
Full text: [[horton-1983-sets-with-no-empty-convex-7-gons.pdf.full]]

## The setting (kept strictly distinct from the ES(n) conjecture)

For $n\ge 3$, $g(n)$ is the least $N$ such that every $N$-point set in general
position contains the vertex set of a convex $n$-gon whose **interior contains
no point of the set** — an *empty* convex $n$-gon. This is the Erdős–Szekeres
problem with an additional emptiness constraint, *not* the ES(n) convex-position
conjecture this run attacks. Known: $g(3)=3$, $g(4)=5$, $g(5)=10$ (Harborth).
Whether $g(6)$ exists was (and remains per this paper) open; the author believes
$g(6)$ does exist. <!-- scholar-digested 2026 -->

## What the paper establishes

The main theorem: for every $k$ there is a $2^k$-point set $S_k$ with **no empty
convex 7-gon**. Consequently $g(7)$, and hence $g(n)$ for all $n\ge 7$, does
**not** exist. $g(6)$ left open.

**Construction.** $S_k = \{(i, d(i)) : 0 \le i < 2^k\}$ where, writing the
fixed-width binary expansion of $i$ as $(a_1\dots a_k)$ with leading zeros, and
$c = 2^k+1$,
$$d(i) = \sum_{j=1}^{k} a_j\, c^{\,j-1}.$$

Symmetries exploited (the trefoil/layer structure):
(a) $i<2^{k-1}$ = left half $L$; (b) $i\ge 2^{k-1}$ = right half $R$, a translate
of $L$; (c) $i$ even = bottom half $B$; (d) $i$ odd = top half $T$, a translate
of $B$; (e) $L,R,B,T$ are all scaled translates of each other (halving the first
coordinate and multiplying the second by $c$ maps $B$ onto $L$); (f) the $180°$
rotation about $((2^k-1)/2,\; \tfrac12\sum_j c^j)$ maps $T$ onto $B$; (g) all of
$T$ lies above any line through two points of $B$ (and $B$ below any line through
two of $T$), ensured by taking $c$ large; (h) for two indices sharing the same
last $x$ binary digits and a third with different ones, above/below the joining
line is decided by the last-$x$-digit sequences (a local, digit-determined
coloring).

**Proof sketch** (the mechanism worth keeping). Any empty convex $n$-gon $A$ in
$S_k$ is first normalized (via the scaled-translate maps) so it meets both $T$
and $B$. Then $A\cap B$ contains at most 3 points: two points $p_i,p_j\in A\cap B$
force no $p_h$ with $i<h<j$ above the segment; and a digit-comparison argument
($x,y$ = rightmost differing positions, the $c^{j-1}$ placement making "larger
$d$" mean "has a 1 at that position", then a parity/order contradiction via
observation (h)) shows $d(h)<d(i),d(j)$. Four points $i<h<\ell<j$ in $A\cap B$
would force $d(h)<d(\ell)$ and $d(\ell)<d(h)$, a contradiction — so $A\cap B\le 3$.
By the 180° symmetry (f), $A\cap T\le 3$ too. Hence $|A|\le 6$: no empty convex
7-gon. ∎

## Implications for this run

- **Structural datum, not a tool.** The Horton $S_k$ is the empty-analogue of the
  ES 1961 lower-bound construction both in form (a digit-coded staircase whose
  recursion by halves/eighth parts controls convexity) and in the recursive
  self-similar layer structure (left/right/bottom/top halves are scaled
  translates). It is a second independent example of the *recursive
  self-similar* shape that extremal no-convex-$n$-gon constructions take — 
  relevant to the [[extremal-structure]] thread's question of how close an
  extremal set must be to the ES construction, but it does **not** bear on the
  ES(n) upper bound: a convex 7-gon (not required empty) trivially exists in
  $S_k$ for $k\ge 3$.
- **Kept out of Established as context only.** GOAL.md explicitly forbids
  adjacent results (empty hexagons etc.) from counting. Horton confirms the
  boundary: emptiness and convexity are different invariants, and an empty-side
  construction says nothing about the convex-position conjecture.
- Computation: `code/out/horton_verify.py` (queued for coder) checks general
  position and absence of empty convex 7-gons for $k=3,4$ (and optional $k=5$)
  over exact integer determinants.

**Claim blocks** (this note is the canonical digest; the same statements are also
recorded in the librarian's acquisition report
`research/summaries/LIBRARIAN-ACQUISITIONS-HORTON-AND-GAPS.md`; both point at the
primary [[horton-1983-sets-with-no-empty-convex-7-gons.pdf.full]]):

```claim
id: horton-no-empty-7gon
statement: For every k there is a 2^k-point general-position set with no empty convex 7-gon; hence g(n) — the least N such that every N-point set contains an empty convex n-gon — does not exist for any n >= 7. (g(3)=3, g(4)=5, g(5)=10 (Harborth), g(6) unknown.)
hypotheses: empty convex polygons; g(n) as defined; k arbitrary
holds-here: yes (empty-analogue, distinct from the ES(n) convex-position question)
status: proved
bearing: confirms the empty-side recursion structure is real; supplies a self-similar-recursive extremal example; does NOT bear on ES(n) upper bound
anchor: research/summaries/horton-1983-sets-with-no-empty-convex-7-gons.pdf.md
follows-from: horton-s-k-construction
answers: (none; adjacent-problem source)
```

```claim
id: horton-s-k-construction
statement: The Horton construction is S_k = {(i,d(i)) : 0 <= i < 2^k}, d(i) = sum_{j=1}^k a_j c^{j-1}, c = 2^k+1, (a_1..a_k) the fixed-width binary expansion of i. Its left/right/bottom/top halves are scaled translates of each other, 180-degree rotation swaps T and B, T lies entirely above every line through two points of B, and above/below a joining line is decided by the rightmost differing binary digit (observation h). Any empty convex polygon meeting both T and B has <= 3 vertices in each.
hypotheses: c = 2^k+1 chosen large enough for property (g)
holds-here: yes
status: proved
bearing: a concrete digit-coded construction with recursive self-similar convexity control; the empty analogue of the ES 1961 staircase; structural input to the extremal-structure thread
anchor: research/summaries/horton-1983-sets-with-no-empty-convex-7-gons.pdf.md
follows-from: (none)
answers: (none)
```
