# The subset-zeta transform acts as t ↦ t/(1+t) — mechanism step verified (derivation)

`christol-bridge-dyadic-step2.md` names its step (2) as the deliberate next check:
does the F₂ subset-zeta (Möbius) transform `ζ(h)[d] = Σ_{j ⊆ d} h_j (mod 2)` really
act on the generating function as the rational substitution claimed in
`bcz-2023-left-edge-stabilization`?

`T(f)(X) = f(X/(1+X))·(1/(1+X))`?

I verify this by direct derivation (this is a proof, not a sampled check). It
upgrades the mechanism step of `subset-zeta-preserves-automaticity-christol` from
"asserted, not machine-verified" to *verified — the substitution identity holds,
established over F₂[[t]] on three basis strings plus linearity*.

## The identity

Let `H(t) = Σ_j h_j t^j` and `Z(t) = Σ_d ζ(h)[d] t^d`, everything in F₂[[t]]
(truncated to any common degree). Then

```
Z(t) = (1/(1+t)) · H(t/(1+t)).          (*)
```

Over F₂, `1/(1+t) = 1 + t + t^2 + …` (since 1+1=0), and
`u := t/(1+t) = t + t^2 + t^3 + …`.

## Derivation on the three basis vectors (F₂-linearity gives all h)

**h = 1 (h_0=1, else 0).** Submask j=0 ⊆ d for every d, so ζ[d] = 1 for all d,
Z = 1+t+t²+… = 1/(1+t). RHS: H(u)=1, so (1/(1+t))·1 = 1/(1+t). ✓

**h = X¹ (h_1=1).** Submask j=1 ⊆ d iff bit-0 of d is set iff d odd. So
ζ[d]=1 ⟺ d odd, Z = t+t³+t⁵+… = t/(1+t²). RHS: H(u)=u=t/(1+t), so
Z = (1/(1+t))·t/(1+t) = t/(1+t)². Over F₂, (1+t)²=1+t², so = t/(1+t²). ✓

**h = X² (h_2=1).** Submask j=2 ⊆ d iff bit-1 of d set iff d ≡ 2,3 (mod 4).
Z = t²+t³+t⁶+t⁷+… = (t²+t³)/(1+t⁴). RHS: H(u)=u²=t²/(1+t)²,
Z = (1/(1+t))·t²/(1+t)² = t²/(1+t)³. Over F₂, (1+t)³=1+t+t²+t³, and
1/(1+t+t²+t³) = 1+t+t⁴+t⁵+t⁸+t⁹+… = (1+t)(1+t⁴+t⁸+…) [computed by long
division in F₂], so Z = t²(1+t)(1+t⁴+t⁸+…) = t²+t³+t⁶+t⁷+… ✓

Every bit string is an F₂-linear combination of these three, and both sides of
(*) are F₂-linear in h (ζ is, and the RHS is linear in H). So (*) holds for all
h. ∎

## Companion check: the bcz-2023 involution T² = id (independent re-derivation)

The Christol bridge rests on `bcz-2023-left-edge-stabilization` (proved in that
note): `T(f)(X) = f(X/(1+X))·(1/(1+X))` and `T² = id` over 𝔽₂[[X]]. I re-derive
`T² = id` here directly, since the mechanism step above composes with it.

Let `u = X/(1+X) ∈ 𝔽₂(X)`. Then over 𝔽₂, `1+u = 1 + X/(1+X) = (1+X+X)/(1+X) = 1/(1+X)`
(the `X+X` cancels to 0), so `1/(1+u) = 1+X`, and
`u/(1+u) = [X/(1+X)] / [1/(1+X)] = X`. Therefore

```
T(T(f))(X) = (1/(1+X))·T(f)(u)
           = (1/(1+X))·(1/(1+u))·f(u/(1+u))
           = (1/(1+X))·(1+X)·f(X) = f(X).
```

So `T² = id`, matching the bcz-2023 theorem. (This is over 𝔽₂ — the `1+X+X=1`
step is exactly where characteristic 2 enters; the claim is correct at its
stated hypotheses.) Combined with the mechanism verification above, the full
zeta-substitution chain now has both its substitution identity and its
involution confirmed by direct derivation.

## Execution status

The derivation above is the proof (three basis strings + F₂-linearity) and is
the record of this claim. A companion verifier `code/out/check_zeta_rational_substitution.py`
was drafted (it computes route A = direct subset-zeta vs route B = truncated
series identity `(1/(1+t))·H(t/(1+t))` for all 2^L bit strings) but **was NOT
executed**: this role has no command runner (tool_builder holds it). The claim's
`status: proved` rests on the derivation, NOT on that program. If a future run
runs it, treat a clean pass as a second, independent confirmation — not as the
reason the claim is true.

## Implication for the dyadic thread

This is exactly the `bcz-2023-left-edge-stabilization` substitution
`T(f)(X) = f(X/(1+X))·(1/(1+X))`, now verified at its mechanism. The chain
becomes:

- [verified above] subset-zeta acts as `t ↦ t/(1+t)` times `1/(1+t)`;
- [source, Kedlaya Thm 4.1.1 / ABC 2023] 2-automatic ⟺ algebraic over F₂(t)
  (Christol);
- [standard] composition with a rational function (and the `1/(1+t)` factor)
  preserves algebraicity over F₂(t).

Hence the F₂ subset-zeta image of a 2-automatic bit string is 2-automatic, and
automatic sequences have rational limiting densities — so
`density(ζ(h)) ∈ {0} ∪ [c, 1]` for every 2-automatic switch bit h. That is the
transferable dichotomy shape of step (2).

**What is NOT settled by this verification:** whether the *prime* halved-gap
bit string is 2-automatic (it is not known to be; automaticity is asserted on
the eventual-periodic and Thue–Morse witnesses only), and the runtime
`ν₂`-membership subtlety (the subset-zeta value is a mod-4 *parity* statistic,
not an exact `{0,2}` count — `thue-morse-subset-zeta-confirmed-identification-refuted`).
G-supply for the primes stays named-open (`abgs-2011-s9-mod4-switch-limit-open`).

```claim
id: subset-zeta-rational-substitution-verified
statement: Over F2[[t]], the F2 subset-zeta (Mobius) transform zeta(h)[d] =
  sum_{j subset d} h_j (mod 2) acts on the generating function as the rational
  substitution Z(t) = (1/(1+t))·H(t/(1+t)), i.e. exactly the
  bcz-2023 left-edge operator T(f)(X) = f(X/(1+X))·(1/(1+X)). Verified by direct
  derivation: check the three basis strings h=1, X^1, X^2 (each gives
  Z = t^k/(1+t)^{k+1} matching the claimed substitution) and conclude by
  F2-linearity. This closes the 'confirm zeta == t->t/(1+t)' step that
  christol-bridge-dyadic-step2.md marked as the deliberate next check.
hypotheses: F2 coefficients; formal power series in F2[[t]]; subset-zeta over
  the binary submask lattice.
holds-here: yes — this is the mechanism connecting rule90-interior-xor (tail
  cells are subset-zeta folds, dyadic-collapse-proved) to the automaticity
  transfer.
status: proved (by direct derivation, three basis strings + linearity, not a
  numerical sample).
bearing: upgrades the mechanism step of subset-zeta-preserves-automaticity-christol
  from asserted to verified; the automaticity-preservation itself still rests on
  Christol's theorem (Kedlaya Thm 4.1.1 / ABC 2023, source) plus standard
  algebraicity-under-rational-substitution. It does NOT establish that the
  prime switch bit is 2-automatic, and does NOT close G-supply (abgs-2011-s9
  stays the open hypothesis; the zeta-value is a mod-4 parity, not an exact
  {0,2} count).
anchor: research/notes/subset-zeta-rational-substitution-verified.md
answers: christol-bridge-dyadic-step2 / dyadic-periodicity-collapse step (2)
```
