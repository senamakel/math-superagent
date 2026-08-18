# Library cycle — 2026-08-18

## Sources held or confirmed

- [Torregrosa, *Cubic planar vector fields with high local cyclicity*](https://doi.org/10.1007/s40863-024-00486-9), full text: `research/sources/torregrosa-cubic-high-local-cyclicity-2024.full.md`.
- [Tian–Yu, *Bifurcation of ten small-amplitude limit cycles by perturbing a quadratic Hamiltonian system*](https://doi.org/10.48550/arxiv.1311.3381), full text: `research/sources/tian-yu-ten-small-amplitude-2013.full.md`.
- [Prohens–Torregrosa, *New lower bounds for the Hilbert numbers using reversible centers*](https://ddd.uab.cat/pub/artpub/2019/204392/newlowbou_a2019v32n1p331.pdf), full text: `research/sources/prohens-torregrosa-lower-bounds-reversible-centers-2019.full.md`.
- [Malev–Novikov, *Linear estimate for the number of zeros of Abelian integrals*](https://doi.org/10.48550/arxiv.0903.5056), full text: `research/sources/malev-novikov-linear-abelian-2009.full.md`.
- [Christopher–Lloyd, *Polynomial systems: a lower bound for the Hilbert numbers*](https://doi.org/10.1098/rspa.1995.0081), Crossref record: `research/sources/christopher-lloyd-lower-bound-1995-crossref.full.md`; publisher full text was blocked by HTTP 403.

## Claim blocks

### Local cyclicity and the analytic input

**Evidence:** asserted-by-source (Torregrosa 2024; full text, Introduction).

**Claim:** For polynomial/analytic vector fields, the return map is analytic locally, so small-amplitude limit cycles are zeros of an analytic displacement map. Torregrosa states the cubic-family local cyclicity problem remains unresolved and that the paper supplies families with twelve small-amplitude cycles. The paper also explains that Zoladek's original eleven-cycle proof had gaps and later work supplied higher-order analyses.

**Hypotheses:** polynomial or analytic field; local monodromic equilibrium; perturbation family as specified by the source.

**Falsifier:** a certified counterexample showing the stated return-map analyticity or the paper's explicit twelve-cycle construction fails.

### Global lower bounds

**Evidence:** asserted-by-source (Prohens–Torregrosa 2019, Theorem 1; full text lines 1–45).

**Claim:** H(4)≥28, H(5)≥37, H(6)≥53, H(7)≥74, H(8)≥96, H(9)≥120, H(10)≥142. The introduction records H(2)≥4 and H(3)≥13.

**Hypotheses:** polynomial planar systems of the corresponding degree; constructions use simultaneous degenerate Hopf bifurcations of reversible/Darboux centers. These are source claims, not independently certified here.

**Falsifier:** an error in the displayed systems, bifurcation hypotheses, or a rigorous/certified construction with a smaller count; numerical plots do not falsify or establish them.

### Special Abelian-integral bound

**Evidence:** asserted-by-source (Malev–Novikov 2009, Theorem 1.1).

**Claim:** For the oval family x²y(1−x−y)=t and polynomial 1-form ω of degree n, the number of isolated zeros of the Abelian integral on (0,1/64) is at most 7n/4+9.

**Hypotheses:** exactly the displayed oval family, polynomial 1-form degree n, interval (0,1/64), zeros counted as in the theorem.

**Falsifier:** a source-exact counterexample or a proof audit finding an invalid reduction.

## Negative result / source gap

The Royal Society publisher page for Christopher–Lloyd 1995 was blocked with HTTP 403. The Crossref metadata is held, while the n² log n lower-growth statement is already represented by other held sources in ROOT/CONTEXT. No claim is upgraded beyond asserted-by-source.