# Wu, "Non-invariance of the Brauer–Manin obstruction for surfaces"

[[wu-non-invariance-brauer-manin]]

Source: `https://arxiv.org/abs/2103.01784` (arXiv:2103.01784v3, 2021). **The downloaded .full.md file contains only the arXiv landing page — abstract, submission history, references — not the paper body.**

## What it actually establishes

From the abstract alone, the paper's claims are:
- For any nontrivial extension `L/K` of number fields, assuming **a conjecture of M. Stoll**, Wu constructs two kinds of smooth projective geometrically connected surfaces over `K`:
  1. a surface with a `K`-rational point and weak approximation with BM obstruction off `∞_K`, whose base change by `L` **fails** to have that property off `∞_L`;
  2. a **counterexample to the Hasse principle explained by the BM obstruction** whose base change by `L` **cannot be explained** by the BM obstruction.
- The paper illustrates both constructions with explicit unconditional examples ("We illustrate these constructions with explicit unconditional examples" — the abstract does not say whether the unconditional examples are of kind 1, kind 2, or one of each).

**What the local full text actually contains:** the arXiv landing page (HTML conversion), not the paper. No theorem statements, no proofs, no examples beyond the abstract. The run has **no body text** for this source, so any use of its claims must either fetch the PDF (`/pdf/2103.01784`) or treat the abstract as the ceiling of what is established here.

## What it implies here

**Holds-here: unchecked — the abstract's constructions are about base-change non-invariance of the BM obstruction for *surfaces in general*; they neither require nor address K3 surfaces in particular**, and the paper's class (surfaces over number fields, arbitrary Kodaira dimension) is not the magic-square K3 `S`. The direct relevance is **negative caution**: if the BM obstruction's *failure* and *explanatory power* are not invariant under field extension, then the CONTEXT.md "hinge" — MSS exist over Q(√3), conjecture none over Q, hence a BM class vanishing under base change — is the *right shape* only if the class is one whose vanishing over Q(√3) is certified, not assumed. Wu shows the BM obstruction does not behave monotonically under base change; it does not forbid the hinge pattern (the surface here would be over Q, extension Q(√3)).

**Conjecture-of-Stoll dependence:** the abstract states the main constructions assume a conjecture of M. Stoll. Which parts are unconditional is not decidable from the abstract. This is a second reason the source can only be cited as evidence that base-change non-invariance phenomena exist — not that they occur for the magic-square surface.

**Does not help the run's computations:** no data, no local-invariant formula, no example transferable to Bremner II's surface. Flagged so nobody re-reads the empty full text expecting a usable theorem.

```claim
id: wu-bm-noninvariance-under-base-change
statement: Assuming a conjecture of Stoll, for any nontrivial extension L/K
  of number fields there exist smooth projective geometrically connected
  surfaces over K whose Brauer-Manin obstruction behaviour (weak
  approximation off infinity, Hasse principle) is not inherited by the base
  change from K to L; both kinds illustrated with explicit unconditional
  examples.
hypotheses: Stoll's conjecture for the general constructions; surface kind
  not restricted to K3; only the abstract is on disk (no body text)
holds-here: unchecked (no body text; surfaces generic, not the magic-square K3)
status: asserted (abstract only — do not cite the paper's theorems without
  fetching the PDF)
bearing: caution for the Q(√3)-base-change "hinge": BM non-invariance under
  extension is real, so any claim that a BM obstruction vanishing over Q(√3)
  explains Q-vanishing needs the class and its evaluations computed, not
  inferred from the extension-field MSS constructions
anchor: research/sources/wu-non-invariance-brauer-manin.full.md
contradicts: nothing on disk (no recalled claim says BM is base-change invariant)
```

**Gap this leaves:** the open request `exact-reduction-magic-507c` is not touched by these three papers — Bremner's own reduction remains the anchor; nothing here supplies `Br(S)/Br(Q)` for the magic-square K3.