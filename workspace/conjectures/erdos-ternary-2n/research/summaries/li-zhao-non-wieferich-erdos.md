# Li–Zhao: Non-Wieferich property of prime ideals and a conjecture of Erdős

**Source:** arXiv:2601.12753 (Jan 2026). Full text at `research/sources/li-zhao-non-wieferich-erdos.full.md`.

## What it establishes

1. **Dupuy–Weirich theorem (stated precisely, source [3] = JNT 158 (2016) 268–280):** For distinct primes p,q and digit b, the Cesàro average over n of the frequency of digit b in the first m digits of (p^n)_q converges, as m → ∞, to 1/q. That is, `lim_{m→∞} f_{p,m}(b) = 1/q` where `f_{p,m}(b) = lim_{N→∞} (1/N) Σ_{n=1}^N f_{p,n,m}(b)`. This is the *average-over-n* analogue of digit equidistribution; Conjecture 1.2 (Dupuy–Weirich) asserts the stronger pointwise limit for each n.
2. **Theorem 1.1 (the Wieferich-tower structure, the crucial one for this run):** For a prime ideal 𝔭 of a number field's ring of integers and α not a root of unity, the kernel of the reduction map `⟨α⟩_{𝔭^r} → ⟨α⟩_{𝔭^{r-1}}` has size 1 for all r > v except when `r − v ≡ 1 (mod e)`, where it has size p (the rational prime below 𝔭); e = ramification index. **In particular, if 𝔭 is unramified, 𝔭 is never α-Wieferich for r > v.** Applied to α = 2, 𝔭 = (3) in ℚ (ramification index e = 1): the kernel `⟨2⟩_{3^r} → ⟨2⟩_{3^{r-1}}` has size 3 for all sufficiently large r. That is the full growth: the 3-adic tower has **no Wieferich obstruction** — the kernel is always as large as possible.
3. **Theorem 1.2:** the generalized Dupuy–Weirich theorem for number fields: if (β) has only unramified prime-ideal factors of residue degree 1, digits are asymptotically equidistributed on average.
4. **Theorem 1.3:** block complexity of β-adic expansions of α^n when ramified factors appear: `C(α) = (Σ g_j e_j^{-1} log p_j)/(Σ g_j f_j log p_j)`.
5. **Proof of Theorem 1.2** is a neat induction: `D_m(b) = N(β) D_{m-1}(b) + h_{m-1}`, iterated to get `f_{α,m}(b) → 1/#D`.

## What it implies for this run

- The 3-adic tower `2 mod 3^r` has kernel size 3 at every level (unramified, e=1): the reduction `⟨2⟩_{3^r} → ⟨2⟩_{3^{r-1}}` is exactly 3-to-1 for r > v — consistent with SIEVE-EXACT / |A_k| = 2^{k-1}, where each class splits into exactly 2 digit-children (the digit map between consecutive levels is 3-to-1, and among the 3 lifts exactly 2 avoid the digit 2 in the new position).
- The Wieferich obstruction that plagues the binary digits of 3^n (Dupuy–Weirich, Conrad notes) is **absent** on the 3-adic side for powers of 2. This asymmetry is significant: for (2^n)_3, the low-digit block is fully "generic" at every level — no 3-adic obstruction limits the digit structure. What limits the *pointwise* behaviour is not the tower's kernel but the arithmetic of the specific exponent n.
- Theorem 1.3 gives block complexity log C_m(α)/(m log N(β)) → (Σ g_j e_j^{-1} log p_j)/(Σ g_j f_j log p_j) for ramified bases — for β = 3 ramified?? no, for β=3 in ℚ, 𝔭=(3) has e=2 (since 3 = p^1·unit, ramified with e = ... for ℚ, (3) over 3: e = 1 for the only prime above 3 in ℚ — ℚ has no ramified primes below; the ramified case is in number fields). Keep as context.

## Claims
```claim
id: LZ-1
statement: Dupuy–Weirich theorem: for distinct primes p,q, limit over m of the Cesàro average over n of digit-b frequency in the first m digits of (p^n)_q equals 1/q.
hypotheses: p,q distinct primes, b a digit, m → ∞ before n.
holds-here: yes for p=2,q=3.
status: proved (as stated in Li–Zhao, citing JNT 2016; theorem 1.2 here is a generalization)
bearing: the strongest average digit-uniformity result on the low digits; says nothing pointwise, matching GOAL.md's heuristic caveat.
anchor: research/sources/li-zhao-non-wieferich-erdos.full.md
```
```claim
id: LZ-2
statement: For α=2, the kernel of ⟨2⟩_{3^r} → ⟨2⟩_{3^{r-1}} has size p=3 for all r > v (unramified prime ideal (3) over 3 in ℚ, e=1). Equivalently, the order of 2 modulo 3^r is exactly 3 times the order modulo 3^{r-1} for all large r, and the reduction is 3-to-1: no Wieferich obstruction in the 3-adic tower.
hypotheses: α not a root of unity; 𝔭 unramified; e=1.
holds-here: yes; matches the primitive-root order 2·3^{r-1} exactly (LAG-2, SAYE-2).
status: proved (Theorem 1.1 in Li–Zhao)
bearing: the low-digit block of (2^n)_3 is generic at every level — the obstruction to the conjecture is not a 3-adic Wieferich phenomenon.
anchor: research/sources/li-zhao-non-wieferich-erdos.full.md
```