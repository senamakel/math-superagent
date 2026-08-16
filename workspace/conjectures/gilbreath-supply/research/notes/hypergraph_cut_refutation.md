# Hypergraph-cut/Cheeger route to SUPPLY is refuted

This note is the single home of the claim block `hypergraph-coboundary-false-premise`,
so CLAIMS.md carries it exactly once (from this note, not from the approach file).
The source is `research/approaches/hypergraph-cut-cheeger.md` (the approach this
kills), and the obstruction is independent of (implied by) the rank correction
`fold-rank-is-n-2-nullity-2-alternating`.

## The approach being killed

Read `Φ_n` as the mod-2 incidence matrix of a hypergraph on `n` vertices
(vertex `j` = window position), hyperedge `d = {n−1−d+o : o ⊆ d}`. Then
`T(n,d) = ⊕_{v∈d} h_v` is the label parity across hyperedge `d`, and
`ν₂(n) = #{d : T(n,d)=1}` is the cut size. The load-bearing mechanism claimed:

> ker Φ_n = span(all-ones), nullity 1, ⟺ the hypergraph is connected (the only
> labellings h with every hyperedge even are h ≡ 0 and h ≡ 1),

so "the fold's hypergraph is connected", opening Cheeger/isoperimetric bounds on
the cut from a volume/balance input.

## Why the premise is false (hand-verified)

**(1) On the approach's own row range d∈[0,n−1]** the hyperedge `d=0` has
down-set `{0}`, so `T(n,0) = h[n−1]` — a *singleton* edge. That row forces
`h_{n−1} = 0`; the all-ones vector is therefore **not** in the kernel of the
`d∈[0,n−1]` matrix. For `n=4` the rows are
`[0,0,0,1], [0,0,1,1], [0,1,0,1], [1,1,1,1]`, which have only `h≡0` in the
kernel (nullity 0, not span(all-ones)). So the approach asserts both
"d∈[0,n−1]" and "ker = span(all-ones)", which are mutually contradictory.

**(2) Even on the operative rows d∈[2,n−1]** (where all-ones IS in the kernel)
the kernel is 2-dimensional, `span(even-alt, odd-alt)`, not `span(all-ones)`
(machine-verified n=2..20). Hence "connected ⟹ only 0 and all-ones cut evenly"
is false for this hypergraph: the even-cut labellings are the parity-class
constant ones, a richer family than graph connectivity predicts. This is because
hyperedges of size > 2 (e.g. `d=3` gives the 4-edge `{0,1,2,3}`) impose ONE
sum-parity constraint, not the pairwise-equal constraints a 2-uniform graph
would impose.

The literal cut-size reading `ν₂(n)=#{d:T(n,d)=1}` remains true, but the
connectivity reinterpretation that the isoperimetric machinery rested on is
gone, so no Cheeger-type lower bound survives.

```claim
id: hypergraph-coboundary-false-premise
statement: The claim that "ker Φ_n = span(all-ones), nullity 1, iff the fold's
  hypergraph is connected (the only labellings with every hyperedge even are h≡0 and
  h≡all-ones)" is false for SUPPLY's fold Φ_n. On the row range d∈[0,n-1] the d=0
  hyperedge is the singleton {n-1}, forcing h_{n-1}=0, so all-ones is not in that kernel
  (n=4: rows [0001],[0011],[0101],[1111], kernel={0}). On the operative range d∈[2,n-1]
  the kernel is span(even-alt, odd-alt), 2-dimensional (fold-rank-is-n-2-nullity-2-alternating).
  Hyperedges of size >2 impose one parity-sum constraint per edge, not the pairwise-equal
  constraints that make "connected ⇒ only global constants cut evenly" true for 2-uniform
  graphs. Consequently no Cheeger/isoperimetric conclusion that global non-constant even cuts
  are forbidden survives; the hypergraph-cut approach to SUPPLY is refuted.
hypotheses: >-
  fold Φ_n with entries C(k-1, j-(n-k)) mod 2 read as a hypergraph coboundary;
  hyperedge d = {n-1-d+o : o ⊆ d}; either row range d∈[0,n-1] or operative d∈[2,n-1].
holds-here: yes — this is the actual fold; the singleton-edge and corrected-kernel
  obstructions are verified.
status: checked (d=0 singleton edge hand-computed for n=4; operative kernel machine-verified
  n=2..20 by fold-rank-is-n-2-nullity-2-alternating)
bearing: >-
  Closes the hypergraph-cut/Cheeger line of attack on SUPPLY with a precise obstruction:
  the connectivity reinterpretation that was its load-bearing premise fails. The literal
  cut-size reading nu2(n)=#{d:T(n,d)=1} remains true but is not a route by itself.
anchor: research/approaches/hypergraph-cut-cheeger.md; code/fold_rank/rank_of_fold.py
follows-from: fold-rank-is-n-2-nullity-2-alternating
```

The approach file `research/approaches/hypergraph-cut-cheeger.md` carries the
same refutation as its `killed-by` and is marked `status: refuted`; this note is
where the claim block lives so it reaches CLAIMS.md and ENTAILMENT.md.
