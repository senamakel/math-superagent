# Thread: the sieve dynamics of A_k

**status:** open — this is the central line.

## Question

Does the survival tree of classes `A_k ⊂ Z/(2·3^(k-1))Z` eventually die outside the three witnesses {0,2,8}, and can its splitting be captured by a transfer operator whose spectral radius is strictly below the naive 2 (i.e. below Narkiewicz's growth)? What exactly is the splitting distribution of a class `j ∈ A_k` into children at `A_{k+1}`?

## What it rests on (claim ids)

- `SAYE-2`: the digit split rule `d_{k+1}(2^(i u_k + j)) ≡ d_{k+1}(2^j) + i·d_1(2^j) (mod 3)`.
- `LAG-2`: |A_k| ≤ 2^(k-1) uniformly (Narkiewicz bound in 3-adic form).
- `DH-1`: the low-ones tail is settled; residuals have ≥ 26 ones.
- `SAYE-3`: the recursion enumerates A_k in Θ(2^k) work, mirroring the fastest known sieve.

## The exact split rule (derived from SAYE-2, elementary)

Fix class j at level k. Its children at level k+1 are i ∈ {0,1,2} with the (k+1)-st digit not equal to 2:

`d_{k+1}(2^(i u_k + j)) = (d_{k+1}(2^j) + i·ε) mod 3`, ε = d_1(2^j) ∈ {1,2}.

- If ε = 1: children i with `d + i ≢ 2 (mod 3)`. One i is forbidden; the other two survive.
- If ε = 2: children i with `d + 2i ≢ 2 (mod 3)`. Since 2 = −1 mod 3, `d − i ≢ 2`, i.e. i ≠ d − 2 = d + 1 (mod 3). One i is forbidden; two survive.

So **every class splits into exactly two children at every level** (the forbidden child is unique because ε is a unit). This is the crucial structural fact: `|A_{k+1}| = 2·|A_k|` exactly, if every class contributes two distinct children. The growth is exactly 2^k — matching Narkiewicz's bound — and there is no death.

Wait — check the case d + i·ε ≡ 2 mod 3 for both i = a and i = b, a ≠ b: that would need (a−b)·ε ≡ 0 mod 3, impossible since ε is a unit. So exactly one i is forbidden. **Every class in A_k has exactly two children in A_{k+1}.** Therefore |A_{k+1}| = 2·|A_k| for all k, unless two different classes produce the same child (a collision).

**Collisions are the only way survival can decay.** |A_k| = 2^k · (1 − collision effects). The witnesses {0,2,8} survive forever; Narkiewicz's 2^k growth is exactly this doubling, and the sieve can only close by showing collisions eventually wipe out every class that is not one of the three witnesses. This reframes the whole problem:

> **Size never decays. The classes can only merge, not die. A proof of the conjecture must show that the infinite binary tree of survivors (2 children per node, no death) has only three infinite paths.**

## What blocks it / what is next

- Narkiewicz's bound says nothing about collisions; the count 2^k is attained (or near-attained) for all k, and there is no death, so any "the sieve empties" argument is false by SAYE-2's splitting lemma.
- The next concrete step: compute |A_k| exactly and count collisions C_k = 2|A_k| − |A_{k+1}| for small k. If C_k is 0 for all small k, the tree is exactly binary for a long time and collision structure is very sparse; if C_k > 0, examine where collisions come from (a class merging with a sibling of another class).
- Likely refinement: track not just the class but the pair (last digit of representative power, pending carry structure) to detect when two classes land on the same residue mod 3^(k+1).

## Refined question (the one to attack)

For n ≥ 9, the class of n at level k is a node in a full binary tree of survivors. The witnesses 0,2,8 give three infinite paths. Since every node has exactly 2 children, the tree is a binary tree with ~2^k nodes at depth k. The conjecture is that the paths {0,2,8} are the only three *infinite* paths that extend (no other infinite branch). Finitary version: for each witness w ∈ {0,2,8} and each n > 8, there is some k with n ∉ A_k. That is, each non-witness dies. But death never happens at a node — it happens on a *path*: eventually, for each n, the path of n must *collide* (become equal as residues mod 3^k ... no, n is fixed; rather for each n its own path must, at some level k, be excluded).

Actually hold on: death never happens means EVERY path survives at every k! That can't be right. If |A_{k+1}| = 2|A_k| at every step with no collisions, then every path in the full binary tree of survivors continues, so the limit set A_∞ has |A_∞| = continuum-many-integers? No — A_∞ ⊆ Z, the actual integer n's. The issue: A_k contains the *residue class of n mod 2·3^(k-1)*, not the exponent n itself. The path of a *fixed integer* n is the sequence of its residue classes; if every residue class at every level survives, then n ∈ A_k for all k, so n ∈ A_∞. So if there were truly no collisions, A_∞ would contain every n — but the three witnesses + n=1,3,9 etc. all have 2s eventually... clearly collisions must happen and must exclude most n. So the growth 2^k with no collisions *cannot* continue forever: the universe of residue classes mod 2·3^(k-1) has size 2·3^(k-1) which grows like 3^k > 2^k, so there's room; the including map A_k → A_{k+1} is 2-to-1 and injective on residue classes as long as collisions are absent... but |A_k| = 2^k means A_k fills... it fills 2^k of 2·3^(k-1) classes = (2/3)^k fraction, going to 0. So no contradiction: A_k can genuinely be a 2^k-element subset forever.

But then the conjecture says A_∞ = {0,2,8}, i.e. of the continuum of infinite binary paths, only three correspond to integers that are powers of 2. The path set is the limit of the binary tree; membership of integer n requires the residue sequence to match the actual n mod 2·3^(k-1). So the question is genuinely about *which infinite paths are realizable*.

## Next concrete computations (small, decisive)

1. Reproduce the three witnesses through digit_free and the sieve for k=1..12; check |A_k| recurrence.
2. Count collisions C_k = 2|A_k| − |A_{k+1}| for small k; check whether |A_k| = 2^k · (1−o(1)).
3. Track the last-digit ε = d_1(2^j) of each survivor class; see if the set of ε's is uniformly 1/2,1/2.
4. Formulate the conjecture "only three infinite paths" as a finite automaton question: the transition is a permutation on (j mod u_k, digit-histo) — this is a finitely-generated dynamics on Z/2·3^(k-1)Z that a small program can explore to k≈46 without materialising 2^n.