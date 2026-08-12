# Ghasemi–Varmazyar, "On the Erdős–Gyárfás conjecture for some Cayley graphs"

**Source:** Matematički Vesnik 73, 1 (2021), 37–42. Full text on disk:
`research/sources/ghasemi-varmazyar-erdos-gyarfas-cayley-2p2.full.md`.
PDF URL: http://elib.mi.sanu.ac.rs/files/journals/mv/282/mvn282p37-42.pdf (open access).

## The primary founding quote

The Introduction quotes Erdős–Gyárfás [3 = Erdős, "Some old and new problems in
various branches of combinatorics", Discrete Math. 165/166 (1997) 227–231]
verbatim:

> "we are convinced now that this is false and no doubt there are graphs for every
> r every vertex of which has degree ≥ r and which contain no cycle of length 2^k,
> but we never found a counterexample even for r = 3."

**This is the primary-source statement of the conjecture's history and of the
authors' own belief.** It confirms what the run's ROOT.md already records: the
conjecture is not a confident positive claim — the proposers suspected it is
false. Valuable because it is the actual cited text, not a paraphrase. (Note the
paper attributes the 1995/1997 dating loosely; the standard date is 1995/1997 —
Erdős gives it in the 1997 collection. The Strong form: Liu–Montgomery later
disproved the "false for every r" conviction for large r/r-dense graphs, but the
δ≥3 case r=3 remains open.)

## What the paper proves (new settled class)

**Theorem 2.1–2.4.** Every **connected Cayley graph** on a group of order **2p²**
or **4p** (p odd prime) contains a cycle of length 4, 8, or 16.

- Order 2p²: the three non-abelian groups G1(p)=⟨a,b|a^p=b²=1,bab⁻¹=a⁻¹⟩,
  G2(p)=⟨a,b,c|a^p=b^p=c²=1,[a,b]=1,c⁻¹ac=a⁻¹,c⁻¹bc=b⁻¹⟩, and
  G3(p)=⟨a,b,c|a^p=b^p=c²=1,[a,b]=[a,c]=1,c⁻¹bc=b⁻¹⟩. G1 falls to the earlier
  Ghaffari–Mostaghim result (length 4, 8 or 16); the paper handles G2 (Thm 2.1:
  a 4- or 16-cycle) and G3 (Thm 2.2: a 4-, 8- or 16-cycle) by explicit vertex
  sequences after automorphic normalisation of the generating set S.
- Order 4p: the authors handle H2(p)=⟨a,b|a^(2p)=1,b²=a^p,b⁻¹ab=a⁻¹⟩
  (Thm 2.3: always a 4-cycle) and H3(p)=⟨a,b|a^p=b⁴=1,b⁻¹ab=a^r,r²≡−1(p)⟩
  (Thm 2.4: always a 4-cycle). H1 is again the Ghaffari–Mostaghim case.

The proofs are case analyses on the possible generating sets S (which elements
of order 2, p, 2p, 4 occur), using automorphisms of the group to normalise S, then
exhibiting explicit (4-, 8-, or 16-)cycles as sequences of elements.

## Why it matters for the run

Adds another **restricted-class** result to the settled list (Cayley graphs were
already partially covered by Ghaffari–Mostaghim; this extends to order 2p² and
4p and is peer-reviewed in Matematički Vesnik 2021). More importantly it is the
**cheap, verified primary source for the Erdős–Gyárfás founding quote**, resolving
a Phase-1 library priority ("the original statement in a primary source").

```claim
id: EG-ghasemi-varmazyar-cayley-2p2-4p
statement: Every connected Cayley graph on a group of order 2p^2 or 4p (p odd prime) contains a cycle of length 4, 8, or 16; hence the Erdős–Gyárfás conjecture holds for these Cayley graphs.
hypotheses: G is a finite group of order 2p^2 or 4p with p an odd prime; X = Cay(G,S) is connected (S generates G, S⁻¹=S).
holds-here: true — these are finite simple min-degree-≥3 graphs, a strict subclass of the conjecture's domain.
status: asserted-by-source (peer-reviewed Mathematicski Vesnik 2021); primary proofs are explicit cycle sequences in the full text.
bearing: adds to the list of settled restricted classes; correctness of the explicit 16-cycles is audit-checkable but not independently re-run here.
anchor: research/summaries/ghasemi-varmazyar-erdos-gyarfas-cayley-2p2.md
```

## Not in the library / caveats
- The quoted Erdős text is from the 1997 Discrete Math. collection; the paper
  cites it as [3]. We hold a citation of the primary text via this paper, not the
  original Discrete Math. pages themselves.
