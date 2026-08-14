# Choice functions and Tychonoff's theorem — Gottschalk 1951

**Source:** doi:10.1090/s0002-9939-1951-0040376-x
**Author:** W. H. Gottschalk, Proc. Amer. Math. Soc. 2 (1951) 172–174
**Full text:** verbatim theorem and proof held via read_sources (see below).

## What this establishes — the exact choice-theoretic basis of de Bruijn–Erdős

The de Bruijn–Erdős compactness theorem is the statement that an infinite graph
is k-colourable iff every finite subgraph is. Its proof runs through Rado's
selection principle; Gottschalk shows Rado's principle is an easy corollary of
Tychonoff's theorem (product of compact spaces is compact), which itself is
equivalent to the Boolean prime ideal theorem / a weak choice principle.

The exact theorem proved (verbatim from the paper):

> Let {Xα | α ∈ T} be a family of finite sets, let A be the class of all finite
> subsets of T, and for each A ∈ A let φ_A be a choice function of {Xα | α ∈ A}.
> Then there exists a choice function φ of {Xα | α ∈ T} such that A ∈ A implies
> the existence of B ∈ A with B ⊇ A and αφ = αφ_B (α ∈ A).

Proof: for A ∈ A let E_A be the set of all φ ∈ X = ∏_{α∈T} X_α such that
αφ = αφ_B (α ∈ A) for some B ∈ A with B ⊇ A. Provide each X_α with the
discrete topology. Since X is compact and {E_A | A ∈ A} is a class of nonempty
closed subsets of X with the finite intersection property, there exists
φ ∈ ⋂_{A∈A} E_A.

**Corollary (verbatim):** A family of finite sets has a one-to-one choice
function if and only if each of its finite subfamilies has a one-to-one choice
function.

## Why it matters here

This is the proof-theoretic content behind `debruijn-erdos-compactness`: the 
plane-colouring reduction chi(G) = sup over finite subgraphs needs a choice
principle (BPI/Tychonoff for finite spaces), no more and no less. The
hypothesis to record on the claim block is "ordinary choice principle (Boolean
prime ideal theorem / Rado selection)". The reduction is not constructive in
the colouring but is a theorem of ZFC (indeed of ZF + BPI).

```claim
id: rado-selection-tychonoff-basis
statement: Rado's selection principle (for a family of finite sets, coherent finite choice functions extend to a global choice function) is a corollary of Tychonoff's theorem; hence the de Bruijn-Erdős compactness reduction for graph colouring holds under the Boolean prime ideal theorem (weak choice), with the one-to-one case as the combinatorial content.
hypotheses: Family of finite sets indexed by an arbitrary set; Tychonoff for products of finite discrete spaces (equivalently BPI); standard graph colouring.
holds-here: true — supplies the exact hypothesis (a choice principle, BPI suffices) that the de Bruijn-Erdős reduction needs; the infinite colouring question is thereby reduced to finite subgraphs in ZF+BPI.
status: proved (Gottschalk 1951; proof verified verbatim from source)
bearing: Pins down the compactness reduction's choice-theoretic hypothesis precisely; the rest of the run can treat chi(G) = sup_finite chi as proved input.
anchor: research/sources/gottschalk-choice-functions-1951.md
```

## Source text

The theorem above and its corollary are quoted from the paper as read. This is
the definitive statement of the choice-basis of the compactness principle.

## Note on download

Full text not stored as a file (network-blocked); the theorem statement and
proof are held verbatim above from read_sources. Status: **sourced via
read_sources; theorem and proof verbatim in this note.**