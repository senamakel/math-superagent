# An–Dai–Hu 2025 — Chebyshev property of three classes of complete hyperelliptic integrals

Full text: [[an-dai-hu-chebyshev-hyperelliptic-2025.html.full]] (Qual. Theory Dyn.
Syst. 24 (2025), art. 172, DOI 10.1007/s12346-025-01330-x).

## What the source establishes (held full text, abstract verbatim)

**Main result:** three classes of complete hyperelliptic integrals of the first kind
are **Chebyshev**, and the exact bound on the number of zeros of these Abelian
integrals is **one**. Method: the criterion function (recent advancement) plus
techniques from symbolic computation. The result shows "there exist other subfamilies
of ovals of the hyperelliptic Hamiltonian which are not exceptional, but the
corresponding complete hyperelliptic integrals of the first kind still satisfy the
Chebyshev property."

**Scope:** the three classes' explicit hypotheses (the Hamiltonians/oval families) are
in the paywalled body; the held capture is the Springer landing page with abstract and
figures only.

## What it lets this run conclude

- A Lean-friendly special-family Abelian-integral target exists: Chebyshev property
  (ECT with rank 1 ⇒ at most one zero, sharp) for three named hyperelliptic
  first-kind families — the exact shape of the run's
  `h16-sharp-abelian-named-family` goal and its G-ect-apply pipeline. But the class
  hypotheses are NOT held (body paywalled), so the target cannot be instantiated
  without the paper body or the underlying "On the Chebyshev Property of Degenerate
  Complete Hyperelliptic Integrals" companion.
- It does not bound arbitrary Abelian integrals or displacement functions and does not
  affect H16.2 status.

```claim
id: h16-an-dai-hu-2025-chebyshev-hyperelliptic
statement: An–Dai–Hu (2025, QTDS 24 art. 172): three classes of complete hyperelliptic integrals of the first kind are Chebyshev with exact zero bound one. The explicit class hypotheses are in the paywalled body (abstract + figures held only).
hypotheses: three named classes of complete hyperelliptic first-kind integrals (body not held); criterion-function method.
holds-here: yes — a potential Lean-friendly sharp-abelian validation target, but not instantiable until the class hypotheses are obtained.
status: asserted
evidence: held Springer landing page with abstract verbatim (research/sources/an-dai-hu-chebyshev-hyperelliptic-2025.html.full.md lines 20-45).
falsifier: a member of one of the three classes with two zeros (contradicting the Chebyshev/one-zero claim), or an error in the criterion-function application.
sources: https://doi.org/10.1007/s12346-025-01330-x
anchor: research/sources/an-dai-hu-chebyshev-hyperelliptic-2025.html.full.md
follows-from:
answers:
```
