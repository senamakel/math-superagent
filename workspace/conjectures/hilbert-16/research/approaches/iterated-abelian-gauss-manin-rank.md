```approach
idea: Iterated-Abelian Gauss–Manin rank — treat the nonlinear displacement in perturbed integrable systems as iterated Abelian integrals forming a finite-rank module over C[h] via the Gauss–Manin connection, with rank μ^k at order k, and bound zeros by the finite differential system.
mechanism: ordinary Abelian integrals are a finite C[t]-module (Novikov–Yakovenko); higher Melnikov functions are iterated integrals in integrable holomorphic foliations (Gavrilov, IMPA survey). A finite-rank module at fixed order gives a Picard–Fuchs-type system and access to argument-principle/zero-counting methods.
status: narrowed
survives: Hamiltonian/near-Hamiltonian perturbations where the displacement variation is a finite-order Melnikov function represented by iterated Abelian integrals; it does not cover the full nonlinear displacement of the open DRR four-Dulac graphics. On this restriction it yields a finite differential system and zero-counting tools for a fixed variation order.
precedent: https://w3.impa.br/~hossein/myarticles/namo-2006.pdf; https://doi.org/10.1006/jdeq.2000.3967; https://ar5iv.labs.arxiv.org/html/math/0110126; https://numdam.org/articles/10.5802/aif.1684/; claim:h16-bny-abelian-bound; claim:gmv-ect-does-not-cover-i6b-four-dulac
```

Failed in general (the full non-Hamiltonian, non-hyperbolic displacement is not a period integral), live on the Hamiltonian restriction. The general-position insight — locate the finite core that carries the rank — is preserved by the adopted `dulac-cochain-stokes-consistency` line, which replaces μ^k with the resonance data (k, a) plus the Stokes cocycle.
