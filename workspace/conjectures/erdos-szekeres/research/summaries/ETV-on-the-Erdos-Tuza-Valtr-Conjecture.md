# Baek, "On the Erdős-Tuza-Valtr Conjecture", arXiv:2206.04260 (2022)

<!-- source: https://arxiv.org/pdf/2206.04260v2 | full text at research/sources/ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md -->

**Publication.** Jineon Baek, arXiv:2206.04260v2 [math.CO], 9 Oct 2022. No journal informa-
tion given in the paper. (Baek is also first author of the "Erdős–Szekeres Conjecture Revisited"
SoCG 2025 paper already in this library — the split-k-gon result.)

## Why this source matters

This is the **primary treatment of the Erdős–Tuza–Valtr (ETV) conjecture** — the strengthened
reformulation of the ES conjecture that the library's other sources reference as "Conjecture 3.1"
(Balko–Valtr) and "the ETV reformulation." It gives the exact statement, proves the ETV conjecture
is **equivalent** to the ES conjecture (Theorem 1.5, attributed to Erdős–Tuza–Valtr [5]), and proves
the **first new case of ETV since 1935** (Theorem 1.6). It also contains a structural machine —
slope labelings, the α-statistic, and the (α,β)-plane — that is directly relevant to GOAL's request
for *structural constraints on a hypothetical extremal (2^{n-2}-point, no-convex-n-gon) set*.

## The ETV conjecture, exactly

- **(Def 1.2)** An *a-cap* (resp. *a-cup*) is a set of a points lying on the graph of a downwardly
  (resp. upwardly) convex function. (Equivalently for ordered points: consecutive triple slopes
  increasing = cup, decreasing = cap.)
- **(Def 1.3)** A *triplet* is (n,a,b) with 2 ≤ a,b ≤ n ≤ a+b−2. N(n,a,b) = max points in general
  position with **no subset forming an n-gon, an a-cap, or a b-cup**.
- **(Conj 2, Erdős–Tuza–Valtr)** For any triplet (n,a,b):
  N(n,a,b) = Σ_{i=n-b}^{a-2} C(n-2, i).
- P(n,a,b) is the statement N(n,a,b) equals that sum.
- **P(n,n,n) = Conjecture 1 (ES)**: n-caps and n-cups are n-gons, and the sum = 2^{n-2}.
- **(Thm 1.5, ETV)** Conjecture 1 and Conjecture 2 are **equivalent**: for fixed n, P(n,a,b)
  implies P(n,a′,b′) whenever a≥a′, b≥b′. (So any counterexample to ETV for one triplet disproves
  the ES conjecture. This is exactly the mechanism Balko–Valtr exploited to refute the *set-theoretic*
  generalizations.)

## What Baek proves (main new result)

- **(Thm 1.6, Main)** P(n,4,n) holds: any (n-1 choose 2) + 2 points in general position contain a
  **4-cap or an n-gon**. This is the first new case of Conjecture 2 since the 1935 cups-caps theorem.
  It lies strictly between the ES conjecture (top of the pyramid) and the cups-caps theorem (bottom):
  the triplet (n,4,n) has n < a+b−3, so it is *not* a consequence of the cups-caps theorem.
- **(Thm 2.6, set-theoretic cups-caps)** Max size of an a-cap and b-cup free *arbitrary configuration*
  (3-uniform hypergraph coloring with a vertex order) is (a+b-4 choose a-2). This is the combinatorial
  generalization of the ES cups-caps theorem.
- **(Thm 2.7)** Any *arbitrary configuration* of size (n-1 choose 2)+2 contains a 4-cap, an n-cup, or
  a (3,n−1)-gon. (Combinatorial generalization of Thm 1.6.) This is what the inductive proof actually
  establishes; it holds for order-colored 3-uniform hypergraphs, not merely realizable point sets.
- **(Thm 2.6 ⇒ |S| bound)** Every a-cap,b-cup-free configuration has size ≤ (a+b-4 choose a-2).

## The structural machine (the tool this run can reuse)

For a 4-cap,n-cup-free configuration S near maximal size:

- **(Thm 3.2)** A *slope labeling* always exists: assign each edge an integer label s(xy) ∈
  {1,…,a−2} so that s(xy) ≤ s(yz) ⇒ xyz is a 3-cup. Concretely s(xy) = (max cap length starting at
  edge xy) − 1.
- **(Cor 4.1)** In the 4-cap (a=4) case labels are 1 or 2; an edge of label 1 extends a cup leftward,
  an edge of label 2 extends a cup rightward.
- **(Thm 3.6)** Define α_i(p) = max length of a cup ending at p whose last edge has label ≤ i.
  Then (α_1(p),…,α_{a-2}(p)) is **injective** into the grid simplex
  T_{a,b} = {(x_1≤…≤x_{a-2}) ∈ N^{a-2} : 1 ≤ x_1 ≤ … ≤ x_{a-2} ≤ b−1}, which has size
  (a+b-4 choose a-2). **This injectivity alone proves Thm 2.6.**
- **(Def 4.2, the (α,β)-plane)** For (n,4,n): α=α_1, β=α_2, mapping points injectively into the
  triangle T_{4,n} = {(a,b): 1≤a≤b≤n−1}. A near-maximal S of size (n-1 choose 2) − k is identified
  with T_{4,n} minus k "holes." Horizontal edges are label 1, vertical edges label 2 (Cor 4.3).
- **(Def 4.4/4.5)** Two cups C1 (p→r), C2 (q→s) are *interweaved* if p<q≤r<s. An (n−1)-cup C (p→q)
  is *laced* if there are cups Cp ending at p and Cq starting at q with |Cp|+|Cq| = n−1.
- **(Lem 5.2)** If a 4-cap,n-cup-free configuration contains **a pair of interweaved laced (n−1)-cups**,
  it contains a (3,n−1)-gon.
- **(Thm 5.10)** Any 4-cap,n-cup-free configuration of size (n-1 choose 2)+2 contains a pair of
  interweaved laced (n−1)-cups. **Combined with Lem 5.2 this is the whole proof of Thm 2.7.**
- **(Conj 5, open)** Any 4-cap,n-cup-free configuration of size (n-1 choose 2)+k (1≤k≤n) contains k
  mutually interweaved laced (n−1)-cups. Proved for k=1,2 and k=n; the general case is open.

## Direct bearing on this run

1. The ETV **conjecture is equivalent to the ES conjecture**, so any progress on ETV triplets is
   progress on ES(n)=2^{n-2}+1. Baek settled P(n,4,n); the open cases are the rest of the pyramid.
2. The **α-statistic/grid-simplex injectivity** is a genuine structural constraint: an
   a-cap,b-cup-free configuration near the extremal size must be a nearly-full T_{a,b} grid. This is
   exactly the "what must an extremal set look like locally" structure GOAL's MEMORY.md is to hold.
3. **Caution / abstract trap matches the run's warning:** Thm 2.7 holds for *arbitrary configurations*
   (abstract order-colored hypergraphs), NOT only realizable point sets. Like Peters–Szekeres' and
   Balko–Valtr's abstract results, it is proof over the combinatorial model; a result proved over
   all abstract configurations can be false over realizable ones (Balko–Valtr's counterexamples were
   all non-pseudolinear). Do not cite Baek's Thm 2.7 as proof for *planar* point sets beyond what the
   realizable case gives.

## claim blocks (for CLAIMS.md)

```claim
id: etv-equivalent-to-es
statement: The Erdős–Tuza–Valtr conjecture is equivalent to the Erdős–Szekeres conjecture: for any triplet (n,a,b) with 2≤a,b≤n≤a+b−2, N(n,a,b)=Σ_{i=n-b}^{a-2} C(n-2,i), and P(n,a,b) implies P(n,a′,b′) for a≥a′, b≥b′. P(n,n,n) is exactly ES(n)=2^{n-2}+1 (N(n,n,n)=2^{n-2}).
hypotheses: planar point sets in general position (no three collinear, distinct x-coordinates; rotation makes the latter WLOG); N(n,a,b) = max size with no n-gon, a-cap, or b-cup.
holds-here: true — this is the strengthened form of the exact conjecture this run targets.
status: asserted-by-source (Theorem 1.5, attributed to Erdős–Tuza–Valtr [5] Ramsey-remainder, EJC 1996).
bearing: the structural/cups-caps route: settle ES(n) by settling any ETV triplet, especially ones the α-statistic machinery reaches. Opposite: any counterexample to any ETV triplet disproves the ES conjecture, so the run must not assume ETV across all triplets.
anchor: research/sources/ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md
```

```claim
id: baek-ETV-n4n
statement: P(n,4,n) holds: any (n-1 choose 2)+2 points in general position contain a 4-cap or an n-gon. Equivalently N(n,4,n) = (n-1 choose 2)+1. This is the first new case of the ETV conjecture since the 1935 cups-caps theorem.
hypotheses: planar point sets in general position; the triplet (n,4,n) with 2≤4,n≤n+2 (always true).
holds-here: true — a restricted-class/partial result on the exact problem, one level below the full ES conjecture in the ETV pyramid.
status: asserted-by-source (main theorem of arXiv:2206.04260; claimed proved by the author; not independently re-derived here).
bearing: a genuine partial result to state in ROOT.md's restricted-classes section: the ETV form is settled for a=4, b=n. Also the sum (n-1 choose 2)+1 ≈ n²/2 is polynomially far below 2^{n-2}, so it does NOT touch the n-gon diameter itself for large n — the n-gon needs 4-caps absent for very large sets.
anchor: research/sources/ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md
```

```claim
id: etv-alpha-statistic-injective
statement: For any a-cap,b-cup-free configuration S with a slope labeling, the α-statistic p ↦ (α_1(p),…,α_{a-2}(p)) is injective into the grid simplex T_{a,b} = {(x_1≤…≤x_{a-2}): 1≤x_1≤…≤x_{a-2}≤b−1}, which has size (a+b-4 choose a-2). Hence |S| ≤ (a+b-4 choose a-2) (set-theoretic cups-caps). In the 4-cap,n-cup case, α=α_1, β=α_2 map points injectively into the triangle {(a,b):1≤a≤b≤n−1}, horizontal edges label 1, vertical edges label 2.
hypotheses: a-cap,b-cup-free configurations (order-colored 3-uniform hypergraphs), with an existing slope labeling (always exists by Thm 3.2).
holds-here: true as a structural constraint on abstract configurations; for realizable sets it holds a fortiori (they are a subclass of configurations).
status: asserted-by-source (Theorem 3.6 and consequences, arXiv:2206.04260; proofs given; not independently re-derived here).
bearing: a concrete structural fact about a hypothetical extremal set: a set with no n-gon that is 4-cap-n-cup-free of size close to (n-1 choose 2) must be a nearly-full (α,β)-triangle. This is the kind of local structure MEMORY.md should hold, and the grid picture is testable with the run's exact-arithmetic oracle.
anchor: research/sources/ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md
```

```claim
id: baek-interweaved-laced-cups
statement: Any 4-cap,n-cup-free configuration of size (n-1 choose 2)+2 contains a pair of interweaved laced (n−1)-cups (Thm 5.10), and any such pair forces a (3,n−1)-gon (Lem 5.2), hence an n-gon in this setting. A generalization (Conj 5) — size (n-1 choose 2)+k forces k mutually interweaved laced (n−1)-cups — is open for general k.
hypotheses: 4-cap,n-cup-free configurations (arbitrary, not necessarily realizable), n≥3.
holds-here: true over all abstract configurations, hence over realizable planar sets (the relevant direction).
status: asserted-by-source (Theorem 5.10, Lemma 5.2, arXiv:2206.04260; proofs given; not independently re-derived here).
bearing: the inductive engine of the proof; a candidate structural lemma about extremal sets the run could attempt to push (e.g. toward Conj 5 for a realizable specialization).
anchor: research/sources/ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md
```
