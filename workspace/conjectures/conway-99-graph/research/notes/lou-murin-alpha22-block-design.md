# Lou & Murin 2014 — acquired; interaction with established claims

```claim
id: lou-murin-alpha22-block-design-reduction
statement: In a putative srg(99,14,1,2) G with independence number alpha=22
  realised by an independent set S, the 77 vertices outside S each send exactly
  4 edges into S (all 77 outside vertices have |N(b) ∩ S| = 4), and the trace
  map b -> N(b) ∩ S indexes a (22,4,2) block design: 77 blocks of size 4,
  every treatment (element of S) in 14 blocks, every pair of treatments in
  exactly 2 blocks. Not every such block design lifts to a graph: a design
  with a repeated block or a block sharing >=3 treatments would give two
  outside vertices >=4 or 3 common neighbours, violating mu=2. The cyclic and
  2-rotational families are candidate encodings; the natural 2-rotational
  construction would force an automorphism of order 11 (which Lou-Murin Thm 6.3
  and the stronger in-library order-11 exclusions rule out), so that particular
  construction fails. Together with alpha <= 22 (also Lou-Murin Thm 4.3), the
  independence number of a prospective (99,14,1,2) satisfies 10 <= alpha <= 22
  (lower bound from Guseinov, in-library), and the extremal alpha=22 case is a
  finite (22,4,2)-design existence question.
hypotheses: existence of srg(99,14,1,2) assumed; S an independent set of size 22;
  mu=2 forces exactly two common neighbours of any nonadjacent pair.
holds-here: yes as a reduction (the block-design encoding is exact and follows
  from alpha=22 + mu=2); the alpha<=22 upper bound itself is separately
  confirmed by the run's checked closed form alpha=(u*k+2)/2=22 at u=4,k=14
  (claim coclique-bound-closed-form). The alpha>=10 lower bound rests on
  Guseinov (asserted-by-source, unrefereed).
status: sourced (unrefereed PRIMES paper; equations re-derivable) for the
  reduction; the alpha<=22 value is checked (confirmed by the run's own closed
  form). The (22,4,2) block-design route is a live constructive angle, not a
  settled result.
bearing: gives the run a design-theoretic certificate on the extremal
  independent-set case: alpha=22 forces a (22,4,2) block design, so either (a)
  no admissible (22,4,2) block design exists (killing alpha=22 and pulling
  alpha down) or (b) one lifts to a graph. This is a finite design question that
  fits the pq-2-6-2-classification and spread-resolvable-partial-sts angles.
anchor: research/sources/lou-murin-srg991412-2014.full.md (Sec. 4.3, Sec. 7)
```

## Source and caveat

- **Source acquired this cycle**: Suzy Lou & Max Murin, MIT PRIMES-USA 2014,
  https://math.mit.edu/research/highschool/primes/materials/2014/Lou-Murin.pdf
  — this is the "Lou & Murin" lead the library had listed as unobtainable.
  Full text at `research/sources/lou-murin-srg991412-2014.full.md`.
- **Unrefereed**: a PRIMES high-school-mentored write-up. All theorems are leads
  to be re-derived, not established facts. The two most load-bearing —
  alpha <= 22 (confirmed by the run's own closed form, so reliable) and the
  (22,4,2) block-design reduction (exact given alpha=22 and mu=2, so reliable
  as a reduction) — are the ones worth carrying. The automorphism-order results
  (no p>14, 13, 11) are weaker duplicates of in-library sourced results and add
  nothing new.
- **Interaction with established work**: the run's checked claim
  `coclique-bound-closed-form` already gives alpha = 22 by a different (spectral)
  route; Lou-Murin Thm 4.3 reaches the same number by RMS–AM, so the two routes
  cross-verify the bound 22. Lou-Murin's Section 7 (the block-design lift of the
  extremal case) is genuinely new to the library.
