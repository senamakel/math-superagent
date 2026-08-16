# A hypothetical (99,14,1,2) is not vertex-transitive (hence not rank 3)

A deduction from the automorphism bounds already in the ledger. It is the
load-bearing fact behind the adopted approach `pq-2-6-2-classification`:
it shows a 99-graph does NOT inherit the "satisfies every t-vertex condition"
property that rank-3 graphs get for free, so the t-vertex-condition hierarchy
has room to bite.

```claim
id: srg99-not-vertex-transitive
statement: A hypothetical srg(99,14,1,2) has no vertex-transitive automorphism
  group; in particular it is not rank 3. Proof (pure arithmetic): if G were
  vertex-transitive and rank 3, the stabilizer G_x of a vertex would be
  transitive on the 14 neighbours and on the 84 non-neighbours of x, so
  |G_x| would be divisible by lcm(14,84) = 84, giving |G| = 99|G_x|
  divisible by 99*84 = 8316. But Makhnev-Minakova 2004 (in the ledger as
  `aut-bounds-established`) gives |G| divides 2*3^3*7*11 = 4158, and
  8316 = 2*4158, contradiction. (The stronger CW/CM bounds narrow |G|
  further; they are not needed.) Hence a 99-graph is not rank 3, and does
  not automatically satisfy the t-vertex condition for t >= 4 by the rank-3
  mechanism.
hypotheses: existence of srg(99,14,1,2) assumed; automorphism bound
  |G| | 4158 (Makhnev-Minakova 2004) taken from the ledger as asserted.
holds-here: yes (the deduction is about the hypothetical 99-graph).
status: checked (arithmetic computed here: lcm(14,84)=84, 99*84=8316,
  2*3^3*7*11=4158, 8316/4158=2). The premise |G| | 4158 rests on the
  asserted source claim `aut-bounds-established`, so the conclusion is
  proved-from-asserted-premise, not fully independent.
bearing: rank-3 graphs satisfy every t-vertex condition (Hestenes-Higman);
  rank-3 controls rook(3) and BvLS(243) therefore pass every vertex-condition
  rung trivially, while a 99-graph is provably NOT rank 3. So the 5-vertex
  condition is the first rung of the hierarchy where a 99-only obstruction can
  exist without touching the controls. This is the fact that makes the adopted
  `pq-2-6-2-classification` approach (vertex-condition-hierarchy filter) more
  than a relabelling.
anchor: research/approaches/pq-2-6-2-classification.md (grounding);
  premises from research/CLAIMS.md ids aut-bounds-established, c3,
  wilbrink-order11-sourced.
```

## Arithmetic check (independent of any graph)

- lcm(14, 84) = 84.
- 99 · 84 = 8316.
- 2 · 3³ · 7 · 11 = 2 · 27 · 77 = 54 · 77 = 4158.
- 8316 / 4158 = 2 exactly, so 4158 < 8316.

The contradiction needs only `|G| | 4158` (MM04); the finer CW/CM results
(2||G| ⇒ |G||6, 7||G| ⇒ G=Z7, |G|=2^a3^b with b∈{0,1}) are strictly
stronger and corroborate the same conclusion. A 99-graph's full automorphism
group has order dividing 4158, which is far too small for vertex-transitivity.

## What this does and does not prove

- It proves: no 99-graph is vertex-transitive / rank 3. A genuine, small,
  new structural fact.
- It does NOT prove nonexistence: small (indeed likely trivial) automorphism
  group is already the known frontier, and nothing here excludes a graph with
  trivial automorphism group.

## Negative-control note

Both controls are rank 3: rook(3) is the Hamming graph H(2,3), and
BvLS(243) is the rank-3 coset graph of the perfect ternary Golay code (the
ledger's `wikipedia-bvls-construction` records it vertex- and edge-transitive).
So this deduction is one of the few steps that separates 99 from BOTH controls,
and it does so in the direction the nonexistence argument needs: the controls
enjoy a regularity (all t-vertex conditions) that 99 provably cannot inherit
for free.
