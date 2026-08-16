# Arithmetic check — Pirzada 2-power unicyclic orders

The paper (EJGTA 10(1):337–344) states, in Table 1, the recurrence
`|G_i| = |G_{i-1}| + 2^{i+4}` alongside the computed orders
|G1| = 94, |G2| = 222, |G3| = 478. **These do not agree**: with that recurrence
|G2| = 94 + 2^6 = 158, not 222; |G3| = 158 + 2^7 = 286, not 478.

Deriving the closed form from the paper's own construction (Section 2, Proof of
Theorem 2.1): each half X_i has order
|X_i| = 2|P_i| + 8 + 3 + 4, where |P_i| = 8·Σ_{j=1}^{i} 2^j = 8(2^{i+1} − 2).
So |X_i| = 2·8(2^{i+1}−2) + 15 = 16·(2^{i+1}−2) + 15 = 32·2^i − 32 + 15 = 32·2^i − 17.
G_i = X_i ∪ X_i' ∪ {bridge}, so |G_i| = 2|X_i| = 64·2^i − 34 = **2^{i+6} − 34**.

Check: i=1: 2^7−34 = 128−34 = 94 ✓; i=2: 2^8−34 = 256−34 = 222 ✓;
i=3: 2^9−34 = 512−34 = 478 ✓. The three stated orders are all consistent with
`|G_i| = 2^{i+6} − 34`, not with the table's recurrence.

The largest possible cycle lies within one half, ≤ |X_i| = 32·2^i − 17 < 32·2^i = 2^{i+5}.
So no cycle of length 2^{i+5} or larger can exist. By construction all of
4, 8, …, 2^{i+3} are avoided and a 2^{i+4}-cycle exists, so **the unique 2-power
cycle length is exactly 2^{i+4}**. This part is sound.

**Conclusion:** the paper's *orders* (94, 222, 478, …) and the *unique-2-power*
*length 2^{i+4}* claim are verified. The paper's stated recurrence
`|G_i| = |G_{i-1}| + 2^{i+4}` is a typo (off by a factor of two); the correct
closed form is `|G_i| = 2^{i+6} − 34` and the correct transition into G_i is
`+ 2^{i+5}`. Do not repeat the paper's table recurrence.
