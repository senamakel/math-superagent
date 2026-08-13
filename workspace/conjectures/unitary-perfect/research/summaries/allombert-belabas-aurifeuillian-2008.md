# Practical Aurifeuillian factorization — Allombert & Belabas (2008)

Source: https://www.numdam.org/item/10.5802/jtnb.641.pdf, J. Th. Nombres Bordeaux 20 (2008) 543-553. Full text at `[[allombert-belabas-aurifeuillian-2008.full]]`. The theory of the Aurifeuillean split that underlies `2^{2p}+1 = L_p·M_p`.

## Granville–Pleasants existence criterion (Prop 1.1)

Let a ∈ Q*, a* the squarefree representative of a in Q*/(Q*)^2. Then `a·ζ_d` is a square in Q(ζ_d) — equivalently `Φ_d(a)` has an Aurifeuillean factorization — iff `a* | d` and (exactly) one holds:
- a* ≡ 1 (mod 4) and d odd; or
- a* ≡ 3 (mod 4) and v2(d) = 1; or
- a* even and v2(d) = 2.

Reduction `Φ_d(a) = Φ_{D}(A)` with D = 2^{v2(d)} Π_{p|d,p≠2} p, A = a^{d/D}; the criterion reduces to (D,A).

## Product formula (Prop 2.1)

For (d,a) satisfying the criterion, `Π_{j∈(Z/dZ)*} (χ(j)G − ζ^j_d)` is an Aurifeuillian divisor of `Φ_d(a)`, where `G(a) = f·Π_{p|a*} g(p)` ∈ Q(ζ_d), χ(j) a Legendre-Jakobi character (with an i factor when a* even, j ≡ 3 mod 4).

## Algorithm (Alg 3.1) and complexity (Thm 3.4, Cor 3.5)

Computes an Aurifeuillian factor in deterministic time `Õ(d^2 L)` (L = log(|a|+1)) assuming a prime ℓ ≡ 1 (mod d) with ℓ ≤ D·d^C, C<8 (Linnik best C=5.5, Heath-Brown; under GRH ℓ ≤ 2(d log d)^2 ⇒ the Õ(d^2 L) claim is unconditional-ish by Linnik too). O(dL) space.

## Relevance to this problem

For `Φ_{4p}(2)`: d = 4p, a = 2. Then a* = 2 even, v2(d) = v2(4p) = 2 ⇒ criterion satisfied. This is the *reason* `2^{2p}+1 = Φ_2(2)·Φ_4(2)·Φ_{4p}(2)... ` splits Aurifeuilleanly, and the same machinery gives the explicit `L_p, M_p` halves already used in the thread. So this source *explains/justifies* the split `2^{2p}+1 = L_p·M_p` and gives a deterministic algorithm to produce and factor the halves — relevant to any future factoring campaign or closed-form manipulation of L_p, M_p as algebraic numbers (they are norms from Q(ζ_{4p}) of `G ± ζ_{4p}`).

**Caveat / does not settle:** the paper gives the *algorithm* to find factors, not a closed algebraic identity for `(2/(2^p+i))_4`; the Aurifeuillean norm structure alone does not fix the biquadratic-character distribution. It supports the "Aurifeuillean split" claim already on disk (`aurifeuillean-split`) with the existence criterion.

```claim
id: aurifeuillean-existence
statement: Φ_d(a) has an Aurifeuillean factorization iff, with a* the squarefree
  part of a (a*|d and one of:) a*≡1 mod 4 & d odd; a*≡3 mod 4 & v2(d)=1;
  or a* even & v2(d)=2. For Φ_{4p}(2) with a=2: a*=2 even, v2(4p)=2, so the
  criterion holds — the split 2^{2p}+1 = L_p·M_p is justified, and each factor
  is a norm from Q(ζ_{4p}), ≈ half the bit length.
hypotheses: a ∈ Q*, a*|d, the three-case condition; d>2, |a|>4 for nontriviality
holds-here: yes (a=2, d=4p satisfies the even-d v2=2 case)
status: sourced
bearing: grounds the Aurifeuillean split (claim aurifeuillean-split) in a stated
  existence criterion, and ties L_p, M_p to norms G±ζ_{4p} — the algebraic
  objects the adopted quartic-character route works with
anchor: research/sources/allombert-belabas-aurifeuillian-2008.full.md
```
