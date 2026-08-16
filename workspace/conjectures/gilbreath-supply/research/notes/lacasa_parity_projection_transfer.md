# Transfer check — do Lacasa's unconditional forbidden gap-blocks survive to the fold's parity string?

Question: The reopened pass (GOAL priority 2) asks for a K>1 functional of the fold controlled by an
arithmetic input strictly weaker than pointwise mod-4 switch density. Lacasa et al. (arXiv:1802.08349,
in library) proved **unconditional** forbidden blocks in the prime gap sequence *mod 6*. The fold's
input is the **parity** string `h[j] = ((q_{j+1} − q_j)/2) mod 2`. Does the mod-6 forbidden structure
survive projection to this binary parity string?

## The projection (the key observation)

Let gap `g`, write `g = 6a + c` with `c ∈ {0,2,4}` (mod-6 class). Then

```
h = (g/2) mod 2 = (3a + c/2) mod 2 = (a mod 2) ⊕ (c/2 mod 2).
```

`a` is a free parameter ranging over all non-negative integers (any gap `6a+c ≥ 2` is possible in
the abstract residue sense), so `a mod 2` takes both values 0 and 1 regardless of `c`.

**Consequence: the parity bit `h[j]` carries NO mod-6 information.** Given any mod-6 block
`(c_1,…,c_m)`, the parity block `(h_1,…,h_m)` can be *any* binary block, by choosing the parities of
the `a_i` freely — the `(c_i/2 mod 2)` term is an additive constant that is swamped by the free
`(a_i mod 2)`.

## Verified by hand, m = 2 (the first forbidden block)

Forbidden `(4,4)`: `g1 = 6a1+4, g2 = 6a2+4`. Then `h1 = (a1 mod 2) ⊕ 0`, `h2 = (a2 mod 2) ⊕ 0`.
So every `(h1,h2) ∈ {0,1}²` is realisable from this *forbidden* mod-6 block (take a1,a2 parities to
match). Likewise every `(h1,h2)` is realisable from an *admissible* block. So at m=2 the parity string
has **no forbidden block** — the unconditional Lacasa constraint `(4,4)` is invisible to the fold.

## General statement (by the free-parity argument above)

For every `m`, every binary parity block `(b_1,…,b_m)` is realisable from *both* an admissible and a
forbidden mod-6 block of size `m` (where forbidden blocks exist). Hence the parity string `h` carries
**no forbidden-block constraint from the mod-6 enumeration at any order**.

**Status of this note's claim:** the m=2 case is verified by hand here (argument above). The general m
case follows by the same free-parity reasoning but is **recorded as a conjecture pending mechanical
check** — `code/librarian/lacasa_projection_check.py` is written to confirm it for m=1..4 and should
be run by the coder/refuter. Do not cite the general-m statement as verified until that check runs.

## Consequence

This is a **negative for the naive transfer**: Lacasa's unconditional K>1 structure is a property of
the **mod-6 residue** sequence, and the fold sees only **mod-4 parity**. The projection destroys the
constraint. A K>1 functional claim *cannot* be built directly on the Lacasa forbidden-block
enumeration. The punchline of the reopened pass stands: the primes' unconditional K>1 correlations,
while real (this source), are not readable by the fold's parity input — so the sought
"K>1 functional controlled by a strictly-weaker-than-switch-density input" is not supplied by this
source. It remains open.
