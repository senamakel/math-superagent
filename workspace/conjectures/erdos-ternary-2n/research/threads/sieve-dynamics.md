# Thread: the sieve dynamics of A_k

**status:** open — the central line. The sieve textbook picture is wrong; the exact structure is below.

## Question

The Erdős conjecture says the orbit `{2^n : n ≥ 0}` meets the digit-2-avoiding set only at n ∈ {0,2,8}. What is the exact structure of the sieve sets `A_k`, and what does that structure force any proof to show?

## Exact structure of A_k (derived; elementary, worth formalising)

Key facts:

1. **2 is a primitive root mod 3^k for every k ≥ 1** (order `φ(3^k) = 2·3^(k-1)`) — LAG-1/LAG-2, Saye's Lemma 1.
2. Therefore the map
   `Φ_k : Z/(2·3^(k-1))Z → (Z/3^k Z)^×`,  `n ↦ 2^n mod 3^k`
   is a **bijection** (domain and codomain both have 2·3^(k-1) elements; injectivity by order).
3. `S_k = { r mod 3^k : k low digits in {0,1} }`, `|S_k| = 2^k`; but powers of 2 are never divisible by 3, so the attained part is `S_k ∩ (Z/3^k)^×`, whose members have **low digit 1** and the other k−1 digits in {0,1}: **`|S_k ∩ (Z/3^k)^×| = 2^(k-1)`**.
4. Hence **`|A_k| = 2^(k-1)` exactly, for every k**, with a bijection between the 2^(k-1) digit patterns (low digit 1, rest in {0,1}) and the residue classes of A_k.

**Consequences (each elementary, each decisive):**

- **The naive growth is exact, not approximate.** `|A_k| = 2^(k-1)` forever. Any "the sieve empties" argument is false *by bijection*: at every finite level all 2^(k-1) digit patterns occur, and Narkiewicz's count bound is matched exactly.
- **No class ever dies and no two classes ever collide.** Each class of A_k corresponds to a unique digit pattern; each pattern extends by one new {0,1} bit in exactly 2 ways; each extension is a unit mod 3^(k+1); each unit is hit by exactly one exponent. The map A_{k+1} → A_k (drop the newest digit) is exactly 2-to-1.
- **The survivor tree is a full infinite binary tree.** `A_∞ = ∩_k A_k` (as subsets of Z) = {n : (2^n)_3 avoids digit 2} — the conjecture says this set is {0,2,8}. Every finite check is consistent: for any {0,1} string of length k there is an exponent realising its low k digits. The question is whether a *consistent* choice of exponent exists across all k, i.e. whether the infinite digit string is the 3-adic expansion of some actual 2^n.

**The honest reformulation (this is the real problem):**

Let `Σ_{0,1} ⊂ Z_3` be the 3-adic Cantor set `{λ : all digits ∈ {0,1}}`. Since 2^2 = 4 ≡ 1 (mod 3) generates 1+3Z_3 topologically (LTE: v_3(4^t − 1) = 1 + v_3(t), so ord(4 mod 3^k) = 3^(k-1)), and 2 ≡ −1 (mod 3), the closure of the orbit `{2^n : n ∈ Z}` in `Z_3^×` is **all of `Z_3^×`** (the two cosets ±(1+3Z_3), both dense in their component). So the conjecture is:

> **A dense orbit (the powers of 2 in Z_3^×) meets the Cantor set Σ_{0,1} ∩ Z_3^× in exactly the three integer points 1, 4, 256.**

Every n produces an element 2^n of the dense orbit; the conjecture says that though the orbit is dense, it lands in the thin Cantor set only three times. This is precisely the Furstenberg transversality / "intersections of multiplicative translates of Cantor sets" framework from LAG-3/LAG-4 — the closure is everything, so dimension arguments on the closure cannot decide the orbit's visits; only the arithmetic of the map n ↦ 2^n can.

## What blocks any size-based proof

- `|A_k| = 2^(k-1)` exactly → counting never decays; a proof cannot bound the count of survivors, only *which paths* survive.
- Narkiewicz's `1.62 X^{α_0}` is the count of low-digit survivors integrated over digit lengths; consistent with the exact 2^(k-1) growth, and gives no path information.
- The witnesses 0,2,8 are exactly the three known infinite paths; a claimed obstruction must let these three through (GOAL.md witness check — the falsification oracle).

## What is next

1. **Formalise the bijection** (tool/lean): Φ_k bijective, |A_k| = 2^(k-1), 2-to-1 extension map. This kills the "sieve shrinks" picture permanently and redirects effort to path structure.
2. **Compute the real object:** the set of infinite paths realised by actual 2^n. Algorithmically: maintain for each digit-pattern its realising exponent mod 2·3^(k-1) (unique); a path is realised iff the limit exponent exists in Z (not just Z_3). Reproduce Saye's n ≤ 2·3^45 from the digit data alone (his recursion IS this).
3. **The transfer operator for paths**, not counts: on the tree of digit patterns, the self-consistency constraint for a path to be 2^n is a contraction-type condition on the exponent coordinates. Narkiewicz's argument effectively shows the low-digit data is independent of the exponent; the missing piece is the middle/high-digit coupling.
4. Confirm numerically (small k ≤ 12) the exactness: |A_k| = 2^(k-1) for k = 1..12, and that the extension is exactly 2-to-1. The oracle `digit_free` + a mod-3^k sieve, no big integers.

## Claims to record from this thread

```claim
id: SIEVE-EXACT
statement: |A_k| = 2^(k-1) exactly for all k ≥ 1; Φ_k: n mod 2·3^(k-1) ↦ 2^n mod 3^k is a bijection onto (Z/3^k)^×; the extension map A_{k+1} → A_k is exactly 2-to-1; no class dies and no two classes collide at any finite level.
hypotheses: order of 2 mod 3^k is 2·3^(k-1) (proved; primitive root).
holds-here: yes — this is the exact structure of the sieve set.
status: proved-here (elementary; from LAG-1 bijectivity; to be checked numerically and formalised)
bearing: kills all "sieve shrinks by counting" arguments; redirects to path structure.
anchor: research/threads/sieve-dynamics.md
```

```claim
id: DENSE-ORBIT
statement: The closure of {2^n : n ∈ Z} in Z_3^× is all of Z_3^× (ord(4 mod 3^k) = 3^(k-1), so 4 topologically generates 1+3Z_3; 2 ≡ −1 mod 3 gives the other coset). The Erdős conjecture is equivalent to: the dense orbit {2^n} meets Σ_{0,1} ∩ Z_3^× in exactly {1, 4, 256}.
hypotheses: ord(4 mod 3^k) = 3^(k-1) for all k (LTE).
holds-here: yes.
status: proved-here (derived; closure claim elementary)
bearing: reframes the problem as dense-orbit-vs-Cantor-set; explains why all existing methods stall on the middle digits.
anchor: research/threads/sieve-dynamics.md
```