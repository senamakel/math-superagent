# Śniady, "Coalescing random walks via the coalescence determinant" — summary

<!-- source: https://arxiv.org/pdf/2602.20043 | Piotr Śniady, arXiv:2602.20043 -->

Full text at `research/sources/sniady_coalescing_determinant_wall_particles.full.md`.

## What the source establishes

Systems of coalescing random walks (on Z and their Brownian scaling limits), where
particles merge on collision: when the number of particles changes, the classical
Karlin–McGregor / Lindström–Gessel–Viennot determinant for non-colliding paths no
longer applies. The paper uses the **ghost-particle method**: when two particles
coalesce, one is the visible heir and the other becomes an *invisible ghost* that
keeps walking, restoring a fixed-particle-count square-matrix structure. Then the
probability of any prescribed coalescence pattern is a **determinant** of a
block matrix of transition probabilities (Theorem 2.2, "coalescence determinant").
Integrating out ghost positions gives a ghost-free closed form for the survivors.

The core new contribution is the **wall-particle system**: starting from every
site occupied, this is the joint system of *survivors* together with the
*walls* (the boundaries between their basins of attraction). Its finite-dimensional
distributions are determinants of block matrices built from transition probabilities
and their cumulative sums (Theorem 1.1, 3.2); a finite block suffices even for an
infinite initial configuration. Applications re-derive the Rayleigh spacing density
and the joint distribution of consecutive gaps (negatively correlated, ρ ≈ −0.163).
Half-line results (Theorem 4.4) concern reflected Brownian motion on [0,∞).

## Why it is in the library (adjacent computational attack, absorbing-wall thread)

This is the closest *coalescing-particle* template to the finish-line-as-absorbing-wall
direction in `research/threads/finish_line_as_absorbing_wall.md`. Its half-line /
wall treatment addresses the boundary the torpids finish line introduces, and its
determinantal machinery is the standard way to get *exact signed* probabilities for a
prescribed coalescence pattern (which parallels the parity statistic: parity is a
signed sum of chain-pairs mod 2). A companion paper (`research/sources/sniady_urban_exact_determinant_coalescing_particles.full.md`) already files the ghost/determinant
construction.

**Restriction (why it does not solve PE597):** the torpids rule is not coalescence.
A bumped rear boat goes *out* immediately and is transparent (a removed obstacle);
the coalescing system merges particles that thereafter move *together* (one cluster).
And PE597's dynamics is continuous ballistic with Exp(1) speeds and a *finite*
finish position per boat, whereas this system is nearest-neighbor lattice walks /
Brownian with every site initially occupied. So the theorems transfer as *technique
leads* (how exact pattern probabilities are organized, ghost-matrix structure) but
not as results. Sourced-claim status: none of its theorems is asserted to hold for
the torpids parity; it is an adjacent exact-signed attack only.
