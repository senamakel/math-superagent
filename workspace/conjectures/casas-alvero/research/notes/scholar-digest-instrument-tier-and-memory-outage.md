# Scholar digest — instrument tier, CLO, Yakubovich, and the memory outage

This file records what the scholar concluded from the reference library,
including what could not be stored durably because the Cognee memory server
is down (16 consecutive `remember_memory` failures this run; the librarian's
cycle note also flagged the outage). The claim blocks below are written into
notes that feed `derived/CLAIMS.md`.

## What was digested (this cycle)

The library was already strong on the CA-specific tier. The newly-gathered
set added the instrument tier (the named tools) plus one new primary. Status
of each:

1. **Cox–Little–O'Shea, *Using Algebraic Geometry* (GTM 185, 2e, 2005)** —
   was a BROKEN STUB (raw PDF fragments). **FIXED**: rewrote
   `research/summaries/clo2005_using-algebraic-geometry.md` with the real
   content (Thm 2.3 resultants; Prop 5.8 / eq (5.9) u-resultant
   factorisation; Elimination/Extension Theorems). Load-bearing: Prop 5.8 is
   the classical statement behind the run's ADOPTED
   `uresultant-one-var-eliminant` approach, corroborating
   `uresultant-theorem-held-source` from a second canonical source. Claim
   `clo-uresultant-factorization` written.

2. **EoM "Resultant"** — already a proper note. Univariate Poisson product
   formula R(f,g)=a^m b^n ∏(αᵢ−βⱼ), Sylvester determinant, discriminant.
   Bearing: R_i = Res_x(f,H_i f) weighted-homogeneity, the leading-coeff
   clause's char-p degeneracy (R_{n−1}=(−1)^n n^n a_n vanishes when p|n).

3. **EoM "Gröbner basis"** — already a proper note. Buchberger, elimination
   ideals, weighted orders. Bearing: the scheme picture and the
   over-ℚ-vs-over-F_p distinction.

4. **EoM "Newton diagram"** — already a proper note. The one-variable
   eliminant instrument (Newton polygon of the eliminant in t under
   a_j↦t^j a_j, ord₀(Rᵢ)=n(n−i)).

5. **Wikipedia "Hasse derivative"** — already a proper note. The char-free
   derivative convention the bad-prime lists use; resolves
   `hasse-vs-ordinary`.

6. **Wikipedia "Newton polytope"** — already a proper note. Minkowski-sum
   under multiplication, toric link, Bernstein–Kushnirenko.

7. **Yakubovich v2 (arXiv:1504.00274v2, "Towards the CA conjecture", via Porto
   repository)** — already a proper note with claim
   `yakubovich-2015-towards-1504.00274v2`. Same paper as the already-held v1;
   both held and cross-linked. Claimed-proof-family preprint; nothing changes
   the standing status (CA open, smallest open degree 20). Real-rooted
   ≥5-distinct-roots result corroborates Laterveer–Ounaïes (which needs no
   real-root hypothesis).

## Conclusions

- Every newly-gathered source is now a usable claim-bearing note except where
  noted; the one defective stub (CLO) is fixed.
- The instrument tier gives the run **second-source grounding for its adopted
  approach**: CLO Prop 5.8 independently confirms the u-resultant factorisation
  that `uresultant-one-var-eliminant` and thread `uresultant-converge` rely on.
  The recorded caveat (multiplicities — CA's V(I) is one point of multiplicity
  B=∏ ord₀(Rᵢ), and the equality is Valabrega–Valla, strictly stronger than
  CA) stands and is now anchored in the note.
- No source contradicts recalled memory. The EoM/CLO instrument facts agree
  with the run's already-established `ord0-resultant-weighted-order-proved-all-n`
  and `uresultant-theorem-held-source`.

## Storage failure (per GOAL/AGENTS: state plainly)

The Cognee memory server is unhealthy: 16 consecutive `remember_memory`
calls failed with the health check not answering within 8 s, the same failure
the librarian's cycle note (`research/notes/librarian-cycle-2026-instrument-tier.md`)
recorded as unresolved. This means **durable Cognee memory was NOT updated
this cycle.** The findings are preserved in workspace notes, which feed the
ledgers (claims/threads) that every role reads; the cross-run Cognee store is
stale until the server recovers. A later cycle with a healthy memory server
should re-run: the CLO u-resultant finding
(`clo-uresultant-factorization`) and the Yakubovich v1/v2 reconciliation.
The two failed `remember_memory` texts are included below so they are not
lost; re-store them verbatim when memory recovers.

### To re-store when memory recovers (1) — CLO u-resultant

Cox-Little-O'Shea GTM 185 (2e, 2005), Prop 5.8 / eq (5.9): for a
well-constrained square system f1=...=fn=0 with bounded degrees, no solutions
at infinity, all multiplicities one, the van der Waerden u-resultant
Res_{1,d1..dn}(u0+u1x1+...+unxn, f1,...,fn) = C * prod_{p in V}(u0+a_{i1}u1+...+a_{in}un):
it factors over C into linear factors whose coefficient vectors are EXACTLY
the common roots, computed as a Macaulay-matrix determinant quotient. This is
the classical statement (second independent source after
Emiris-Pan-Tsigaridas §4.3) backing the run's ADOPTED
uresultant-one-var-eliminant approach: for I=(R1..Rn-1) in Q[a], CA in degree
n is V(I)={0}, equivalent to Res_u(I)=c*u^B (single power). CAVEAT: Prop 5.8
as stated assumes all multiplicities one and no solutions at infinity; CA's
V(I) is one point of multiplicity B=prod ord_0(R_i) (Samuel multiplicity,
Valabrega-Valla equality), STRICTLY STRONGER than CA; a mismatch is gr_m0
evidence, NOT a counterexample. Source:
research/summaries/clo2005_using-algebraic-geometry.md, full text
research/sources/clo2005_using-algebraic-geometry.full.md (Prop 5.8 lines
~7860-7990, Thm 2.3, Elimination/Extension Thms lines ~1942-1994).

### To re-store when memory recovers (2) — Yakubovich v1/v2

Yakubovich "Towards the Casas-Alvero conjecture" (arXiv:1504.00274) v1=1 Apr
2015, v2=14 Aug 2015 (titled differently "The validity of the Casas-Alvero
conjecture" vs "Towards the Casas-Alvero conjecture"; same paper). The v2 is
definitive and is what later records cite; both full texts now held and
cross-linked (note research/notes/yakubovich-1504-00274-v1-v2.md). It is in
the claimed-proof family (preprint, not peer-reviewed for its full-CA
implications); nothing changes CA's standing status of open. Real-rooted
results corroborate Laterveer-Ounaies' >=5-distinct-roots bound (which needs
no real-root hypothesis). Claim id yakubovich-2015-towards-1504.00274v2.
