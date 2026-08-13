# Avart — A characterization of converging Ducci sequences over Z₂

**Full text:** `research/sources/avart-converging-ducci-sequences-z2.full.md`
**Source URL:** https://www.fq.math.ca/Papers1/49-2/Avart.pdf
**Published:** Fibonacci Quarterly 49.2 (2011) 155–157.

The sharp converse to the classical power-of-2 nilpotence theorem, for the cyclic Ducci map over Z₂.

**Setup.** Over Z₂ the Ducci map is linear: `T(x0,…,x_{k−1}) = (x0+x1, x1+x2, …, x_{k−1}+x0)`, i.e. `T = I + r` (r = cyclic shift). Key identity (proof by induction):
`Tⁿ(x) = Σ_{i=0}^{n} C(n,i)·rⁱ(x)`,
exactly the Pascal-mod-2 / Rule-90 evolution the run proved as `rule90-interior-xor`, but over the cyclic vector.

**Main theorem.**
> **Theorem 4.1.** A vector `x ∈ Z₂ᵏ` is nilpotent (some iterate is the zero vector) **iff** it is the concatenation of several copies of a vector of length a power of 2: `x = ∨(m) y` for some m and some `y ∈ Z₂^{2^ℓ}`.

**Proof mechanism (Proposition 2.1):** if `Tⁿ(x) = 0` then (taking 2^ℓ ≥ n and using `C(2^ℓ, i) ≡ 0 (mod 2)` for 0<i<2^ℓ) `T^{2^ℓ}(x) = x + r^{2^ℓ}(x) = 0`, so `x = r^{2^ℓ}(x)`, i.e. x is `2^ℓ`-periodic; with `2^ℓ = mk + r`, x is r-periodic, hence d-periodic for `d = gcd(k, r)`, and `d | 2^ℓ` forces `d = 2^{ℓ'}` — so x is a concatenation of copies of a length-2^{ℓ'} vector. The converse is the classical nilpotence of length-2^ℓ vectors plus `Tⁿ(∨(m)x) = ∨(m)Tⁿ(x)`.

**Consequence for integer vectors (stated in the paper):** if an integer vector x is nilpotent, its reduction mod 2 must be a concatenation of power-of-2-length copies — a necessary parity condition for convergence to zero.

**What this establishes for this run:**
- The complete characterization of convergence-to-zero for the **cyclic** binary Ducci map: nilpotence is exactly "period 2^ℓ with 2^ℓ | k" (concatenation structure). This is a much sharper statement than "k must be a power of 2" — it says even for power-of-2-length vectors, only the *periodic* ones converge.
- The 2-adic/Pascal structure (`Tⁿ = Σ C(n,i) rⁱ`) is again proved as an identity — one more independent primary anchor for the run's Rule-90 interior and for the `p-adic-valuation-carry-dynamics` approach's claim that the mod-2/Pascal map is the exact linear core.
- **The cyclic/non-cyclic boundary is now well documented.** The classical theorems (Ciamberlini–Marengoni, Glaser–Schöffl, Avart) all characterize the *cyclic* map. The Gilbreath triangle is the non-cyclic half-infinite iteration; the mod-2 local law transfers, but the global conclusions (nilpotence structure, cycle lengths) are cyclic-object facts. Eppstein's anti-Gilbreath (this run's library) is exactly the demonstration that the half-infinite object does **not** satisfy the cyclic convergence conclusions.

**Status:** sourced (peer-reviewed primary).