```approach
idea: Number-theoretic / CRT-based formula for g(c,s,p,q) from discrete contact-point phase bookkeeping
mechanism: Label ring teeth 0..c-1 and sun teeth 0..s-1. A planet of t teeth meshing ring tooth i_C and sun tooth i_S imposes i_S == i_C + delta_t (mod gcd structure). Four planets give four constraints; global sun/ring orientations absorb two; two congruences remain, counted by CRT / Smith normal form. Conjectured: g depends on c,s,p,q only through gcd/lcm structures, hence is multiplicative, giving a sub-cubic sieve for G(500).
status: refuted
killed-by: the congruence reformulation is right (Kurasov 2020 toothed contours, off-centre) but the CRT/multiplicativity half is unsupported and self-undermining — tangency forces positions (free variable is d, not four independent tooth indices), so a four-index CRT product overcounts; superseded by the single monotone integer condition n_p in Z via the identity n_p + n_q = c+s
precedent: https://www.matec-conferences.org/articles/matecconf/abs/2020/25/matecconf_icmtmte2020_03027/matecconf_icmtmte2020_03027.html (Kurasov 2020, gear eccentric systems, toothed-contours integer congruences, eq. 7/8); thread `offcentre-mesh-phase-model`; Guo 2011 eq. 5.21-5.25; Simionescu 1998; Xue 2020; Zou 2015; Sun 2017
first-step: (superseded — see research/approaches/arc-closure-cs-polynomial.md; the surviving part, the toothed-contour congruence, is carried there, while the CRT/multiplicative count is dropped)
```

## Research verdict — split, and why it closes as refuted

**Grounded half (kept elsewhere).** The *reformulation* — discreteness as a
toothed-contour integer congruence Σ φ·z = πK / 2πK′ — is directly supported by
Kurasov 2020 (gear **eccentric** systems, eq. 7/8), structurally the same object
as the run's winning congruence `n_t = [(c-t)beta + (s+t)mu]/pi in Z`. This half
survives and is carried by `arc-closure-cs-polynomial`.

**Refuted half (dropped).** The payoff claim — g multiplicative in c,s,p,q via
gcd/lcm, counted by CRT/Smith normal form — has no source support, and the
candidate's own mechanism ("counting tooth-index assignments is equivalent to
counting d values") is wrong for the off-centre geometry: exact tangency forces
each planet's position (two mirror points per type), so the free variable is the
single centre-distance d, and a product over four Z_c indices massively
overcounts a one-dimensional discreteness. The run's winning model confirms this:
the correct count is NOT a CRT product but the single monotone condition
`n_p in Z`, with `n_q = (c+s) - n_p` making the second congruence automatic.

**Source caveat:** Kurasov 2020 is 403-blocked to the downloader; eq. 7/8 taken
from search-engine extraction of the open-access MATEC PDF, unverified locally.
