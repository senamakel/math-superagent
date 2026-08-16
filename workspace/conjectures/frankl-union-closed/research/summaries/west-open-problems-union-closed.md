# Doug West, "Union-Closed Sets Conjecture" — Open Problems page

**Note — replaces the structural digest.** Wikilink to full text:
[[west-open-problems-union-closed.full]]

Full text: `research/sources/west-open-problems-union-closed.full.md`.
Encyclopedic problem-collection entry (content through ~2002, then points to
Bruhn–Schaudt survey). Cited as the problem's canonical record page.

## What it establishes (precise statements)

**Statement & origin.** Non-trivial finite union-closed `ℱ` (contains a member
other than `∅`): some element in `≥ half` the members. Originator Peter Frankl,
1979 (stated in the intersection-dual form in [Fr]); conjecture stated in [Du]
(1985); attributed to Frankl. `n` = total elements appearing, `m = |ℱ|`.

**Equivalent phrasings (the three standard forms).**
1. **Union-closed (original).**
2. **Generator version**: if `ℱ` non-trivial union-closed containing `∅`, some
   *generator* (a member not expressible as a union of others) lies in `≤ half`
   the members.
3. **Lattice version**: every nontrivial finite lattice `L` has a join-irreducible
   element at/below `≤ half` the elements.
The lattice version is "intermediate in the transformation between the original
conjecture and the generator version."

**Trivial/settled small cases.** Trivial when `ℱ` contains a singleton or when
the average member size `≥ n/2`. Contains a 2-set `{x,y}`: partition `ℱ` into
`ℱ₀,ℱ_x,ℱ_y,ℱ_xy`; `|ℱ_xy| ≥ |ℱ_0|`, so one of `x,y` in `≥ half` (Sarvate–Renaud
SR1). **The 2-set method does not extend to 3-sets**: SR2 (also R. Graham
independently) give a UC family where none of the three elements of the smallest
set is in `≥ half` — corroborates the Ellis–Ivan–Leader fault line and
`eil-small-sets`.

**Verified-`m` ladder (pre-2002 historical):** `m` up to 11 (SR1), 18 (SR2), 24
(L1, Lo Faro), 27 (P, Poonen), 32 (GY, Gao–Yu), 40 (Ro, Roberts). **Poonen [P]
proved UC when the largest set in `ℱ` has size `≤ 7`** (a size bound on sets,
distinct from the `m≤40` bound and from the ground-set bound `n≤11` of
Bošnjak–Marković). Gao–Yu: `m` close to `2ⁿ`, by counting + extremal set theory.

**Minimal-counterexample structure (early, via [L2],[Ro],[NS]).** A minimal
counterexample (minimising `m`) has a member of size `≥ 9` (Lo Faro) and no
member of size `> (m+1)/4` (Roberts); at least **three** elements appear in
exactly `(m−1)/2` members (Norton–Sarvate). These are distinct from the
Roberts–Simpson `m ≥ 4·n−1` bound recorded in ROOT (which bounds `m` below by
ground-set size); West's rows bound set sizes within a minimal counterexample.

**Knill's `P`-density generalisation.** For posets `P,Q`, `Q^P` = order-preserving
maps; `P`-density of `x` in `L` = `|U^P|/|L^P|`. `L` has the `P`-density property
if some join-irreducible has `P`-density `≤ 1/p`, `p` = number of antichains. The
one-element `P` case (2 antichains) is the lattice version of Frankl. Knill:
**every modular lattice `L` and every poset `P` has the `P`-density property** —
a generalisation containing the modular-lattice case (Abe–Nakano).

## Hypotheses and holds-here

Holds-here: yes — same finite union-closed setting. This is the problem's own
canonical context page; it predates the entropy era, so none of the
`(3−√5)/2` / `0.38234` record belongs on it.

## What this lets the run do

- Confirms the **three equivalent forms** (union-closed ↔ generator ↔ lattice)
  that ROOT and the claims already use, from the canonical source.
- Adds the **Poonen largest-set-≤7** fact (size bound, distinct from the
  `m≤40` and `n≤11` bounds) and the **three-elements-in-(m−1)/2** minimal
  counterexample fact — both usable as constraints on a minimal counterexample.
- Corroborates (independently) the **3-set non-forcing** of Ellis–Ivan–Leader:
  West's entry already records that the 2-set argument fails for 3-sets.

## What it does not settle

West's page is pre-2002 and historical; it does **not** contain the entropy-era
record, the graph formulation, or the modern lattice classes (Bruhn–Schaudt
survey is where those live in this library). Do not read it for the current
constant.

```claim
id: west-poonen-largest-7
statement: Frankl's (union-closed sets) conjecture holds for every union-closed
  family whose largest member set has size at most 7 (Poonen 1992). Distinct
  from the m≤40 and ground-set n≤11 bounds.
hypotheses: finite non-trivial union-closed family, largest set ≤ 7 elements
holds-here: yes
status: asserted
bearing: an additional completed class (by max set size); a constraint usable on
  a minimal counterexample (a counterexample must contain a set of size ≥ 8)
anchor: research/sources/west-open-problems-union-closed.full.md
```
