# Ellis–Ivan–Leader, "Small Sets in Union-Closed Families" (arXiv:2201.11484, 2022)

**Full text:** [[ellis-ivan-leader-small-sets-2022.full]] · **Source URL:**
https://arxiv.org/html/2201.11484 — resolves the 3-set fault line.

<!-- source: https://arxiv.org/html/2201.11484 | converted from HTML -->

## What is in it

- SMALL SETS IN UNION-CLOSED FAMILIES
        - Abstract
  - 1 Introduction
        - Theorem 1.
  - 2 Proof of main result
        - Lemma 2.
        - Proof.
        - Proof of Theorem 1.
  - 3 An open problem
        - Question 3.
  - References


## What it claims

Our aim in this note is to show that, for any ϵ > 0 \epsilon>0, there exists a union-closed family ℱ \mathcal{F} with (unique) smallest set S S such that no element of S S belongs to more than a fraction ϵ \epsilon of the sets in ℱ \mathcal{F}. More precisely, we give an example of a union-closed family with smallest set of size k k such that no element of this set belongs to more than a fraction ( 1 + o ⁡ ( 1)) ​ log 2 ⁡ k 2 ​ k (1+o(1))\frac{\log_{2}k}{2k} of the sets in ℱ \mathcal{F}.

We also give explicit examples of union-closed families containing ‘small’ sets for which we have been unable to verify the Union-Closed Conjecture.

## Statements it makes

###### Theorem 1.

Theorem 1 is asymptotically sharp, in view of results of Wójcik [12] and Balla [2]: Wójcik showed that if S S is a set of size k ≥ 1 k\geq 1 in a finite union-closed family, then the average frequency of the elements in S S is at least c k c_{k}, where k ⋅ c k k\cdot c_{k} is defined to be the minimum average set-size over all union-closed families on the ground-set [k] [k], and Balla showed that c k = ( 1 + o ⁡ ( 1)) ​ log ⁡ k 2 ​ k c_{k}=(1+o(1))\frac{\log k}{2k}, confirming a conjecture of Wójcik from [12].

## Status
The digest above is complete. Theorem 1 (stated in full in the digest and
confirmed in the body at lines 36–40) is proved by explicit construction.

```claim
id: ellis-ivan-leader-smallest-set-frequency
statement: For any k >= 3 there is a union-closed family whose unique smallest
  set S has size k, with every element of S having frequency
  (1+o(1))·(log2 k)/(2k). For k=3 this is below the conjecture's Sarvate-Renaud
  2-set behaviour and shows the 3-set analogue of the singleton/doublet results
  FAILS: a smallest 3-set does not force an abundant element in it.
hypotheses: family union-closed, (unique) smallest set of size k
holds-here: yes
status: proved (Theorem 1, explicit construction)
bearing: resolves the "3-set question" negatively -- a containing-family of
  radius-3 needs the LP/weight machinery (Pulaj), not the trivial
  smallest-set argument; and singles out which small-size-set results force UC
  (singleton, doublet) vs which do not (3-set+)
anchor: research/sources/ellis-ivan-leader-small-sets-2022.full.md (Theorem 1)
contradicts: none (it confirms Sarvate-Renaud's 3-set example is not an accident)
```
