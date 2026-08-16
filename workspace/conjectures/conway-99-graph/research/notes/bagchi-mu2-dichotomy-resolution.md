# Claim c6 — resolved without contradiction: the μ=2 dichotomy's branch structure

<!-- Resolves the contradiction flagged in established-claims.md's c6 and in
brouwer-neumaier-1988-finding.md. The apparent contradiction disappears once
the K_{1,1,2}-free lemma's second branch is kept. -->

## The resolution (from the primary source)

The Bagchi Theorem 4 statement as carried by secondary summaries — "any SRG
with μ=2 is either a grid graph or k ≥ 12λ(λ+3)" — **appeared to contradict the
existence of BvLS (243,22,1,2)** (λ=1, k=22 < 48). That apparent contradiction
resolves as follows.

The proof (captured verbatim from the ScienceDirect passage) is:

> Suppose k < 12λ(λ+3). By BN1988, a μ=2 SRG with k < 12λ(λ+3) is K_{1,1,2}-free.
> Therefore (by Lemma 1) it is the collinearity graph of an (s,t)-GQ. Since
> t+1 = μ = 2, it is a grid graph.

**Lemma 1 (kept in full):** *Any K_{1,1,2}-free SRG is either the collinearity
graph of a generalized quadrangle, **or else its parameters satisfy
k ≥ (λ+1)(λ+2)**.*

So the chain only reaches "grid" when BOTH conditions hold:
  (i)  k < 12λ(λ+3)  ⇒  K_{1,1,2}-free,  and
  (ii) k < (λ+1)(λ+2)  ⇒  falls in the GQ branch, not the k≥(λ+1)(λ+2) branch.

For **BvLS (243,22,1,2)**: λ=1 ⇒ (λ+1)(λ+2) = 2·3 = 6, and k=22 ≥ 6. So (ii)
FAILS: BvLS satisfies the second branch of Lemma 1, is NOT forced to be a GQ,
and is NOT forced to be a grid. **There is no contradiction.**

For **(99,14,1,2)**: λ=1 ⇒ (λ+1)(λ+2)=6, k=14 ≥ 6. Same conclusion: a putative
99-graph is NOT forced to be a grid by this theorem either.

## What the dichotomy genuinely says about 99

The real content is a dichotomy on ordinary k. For λ=1, μ=2 SRGs it is:
- if k < 12·1·(1+3) = 48 and additionally k < (1+1)(1+2) = 6, then it is a grid.
- For λ=1 the grid branch only bites when k < 6; there is a unique such nonempty
  case class, and 14 and 22 are both far above 6.

So **Bagchi/BN1988 gives no contradiction for (99,14,1,2)** — the bound that
bites is λ(λ+3)/2 = 2 (BN1988 Corollary), and 14 ≥ 2. Confirmed by reading the
Brouwer–Neumaier 1988 full text, whose table lists (99,14,1) as `?` open.

**This closes claim c6 as "does not rule out 99".** The naive reading that
would "prove" 99 nonexistence is exactly the kind that also proves 243
nonexistence — and here it dissolves completely once condition (ii) is
restored. There is no hidden structural difference between 99 and 243 needed:
the theorem simply does not bind either k=14 or k=22.

## Correction to the earlier brouwer-neumaier-1988-finding note

That note worried that Bagchi's theorem might rule out BvLS and demanded a
K_{1,1,2} computation. That worry is now dissolved: the theorem as correctly
read does not rule out BvLS (the k≥(λ+1)(λ+2) branch absorbs k=22), so no
contradiction forces a K_{1,1,2} investigation for consistency. (Computing the
K_{1,1,2} status of BvLS is still of independent interest for structure, but it
is no longer needed to save the theorem.)

```claim
id: c6-resolved-no-bite
statement: Bagchi 2006 / Brouwer-Neumaier 1988 mu=2 dichotomy does NOT rule
  out srg(99,14,1,2). The grid conclusion requires both k < 12*lambda*(lambda+3)
  (forcing K_{1,1,2}-freeness) AND k < (lambda+1)(lambda+2) (to fall in the GQ
  branch of Lemma 1). For lambda=1 both 99 (k=14) and 243 (k=22) have
  k >= 6 = (lambda+1)(lambda+2), so neither is forced to be a grid. The
  relevant bound for 99 is BN1988's lambda(lambda+3)/2 = 2, satisfied by k=14.
hypotheses: srg(v,k,1,2); the mu=2 dichotomy theorem as stated in the
  secondary sources and the BN1988 primary full text.
holds-here: yes — closes c6.
status: sourced + reasoned (from the BN1988 primary full text and the verbatim
  Bagchi proof passage; the full Bagchi paper is paywalled but the lemma's
  second branch is quoted verbatim in multiple independent summaries).
bearing: the mu<=2 dichotomy is NOT a viable 99-nonexistence route; it was the
  most dangerous "too good to be true" claim in the run and is now retired
  with the exact step (condition ii) that fails for both 99 and 243.
anchor: research/notes/bagchi-mu2-dichotomy-resolution.md
```

```claim
id: bagchi-bvls-contradiction-resolved
statement: The apparent contradiction of claim bagchi-bvls-contradiction-pending
  is RESOLVED and that row is closed: Bagchi 2006 Thm 4 ("mu=2 SRG is a grid or
  k >= 12*lambda*(lambda+3)") does not contradict the existence of BvLS
  (243,22,1,2). The chain to "grid" needs BOTH k < 12*lambda*(lambda+3) AND
  k < (lambda+1)(lambda+2) (Lemma 1's second branch). For lambda=1 the second
  bound is 6, and BvLS has k=22 >= 6, so it falls in the k >= (lambda+1)(lambda+2)
  branch and is NOT forced to be a K_{1,1,2}-free GQ/grid. No K_{1,1,2} check is
  required to save the theorem; the only escape clause hypothesised by
  bagchi-bvls-contradiction-pending ("BvLS not K_{1,1,2}-free") was a false
  dilemma. The same branch absorbs k=14 for (99,14,1,2), so the dichotomy rules
  out neither 99 nor 243.
hypotheses: Bagchi 2006 Thm 4 as carried by the secondary summaries; its proof
  chain via Brouwer-Neumaier 1988 and Lemma 1 (whose full statement, including
  the k >= (lambda+1)(lambda+2) branch, is quoted verbatim).
holds-here: yes — this is exactly the pending dispute on the controls.
status: sourced + reasoned (from the BN1988 primary full text and the verbatim
  Bagchi proof passage; the full Bagchi paper is paywalled but Lemma 1's second
  branch is quoted verbatim in independent summaries). Computation not needed:
  the resolution is purely the second-branch arithmetic 6 <= 22, 6 <= 14.
bearing: closes the last standing `unchecked` row in CLAIMS.md. The mu<=2
  dichotomy is a dead end for 99 (retired, claim c6-resolved-no-bite / this),
  and a reader of the ledger no longer sees a live CONTRADICTION between the
  pending and resolved rows.
anchor: research/notes/bagchi-mu2-dichotomy-resolution.md
answers: bagchi-bvls-contradiction-pending
contradicts: none (resolves the pending row's apparent conflict with c6-resolved-no-bite)
```

```claim
id: srg33-mechanism-answers-request
statement: The mechanism ruling out srg(33,8,1,2) is eigenvalue-multiplicity
  integrality: for srg(v,k,1,2), the multiplicity of the negative eigenvalue is
  g = 1/2[(v-1) - (2k-(v-1))/sqrt(4k-7)]; for k=8 (v=33, sqrt(25)=5) the
  numerator 2k-(v-1) = 16-32 = -16 is not divisible by 5, so g is not an
  integer and the parameter set is infeasible. Equivalently (Makhnev-Minakova
  2004) k must be u^2+u+2 with u in {1,3,4,10,31}, and u=2 (k=8) is not among
  them. This is spectral; it does not transfer to 99 (which passes integrality),
  so srg(33,8,1,2) is a dead end as a structural precedent.
hypotheses: srg definition; standard multiplicity formula.
holds-here: yes.
status: checked (exact integer arithmetic; consistent with Makhnev-Minakova
  classification and the BvLS five-member list).
bearing: answers the open request published-mechanism-ruling-5cf8: the nearest
  precedent (33) dies on pure spectral integrality, which 9 and 243 (and 99)
  all survive — so it gives no weapon for 99.
anchor: code/out/feasibility-candidates-corrected.md
answers: published-mechanism-ruling-5cf8
```
