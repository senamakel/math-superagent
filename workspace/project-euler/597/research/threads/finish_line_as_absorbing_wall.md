# Thread: the finish line as an absorbing wall

`thread`:
question: Is the finite-finish torpids parity provable from the convex-minorant / record structure of the no-finish race, or is the finish line a genuinely new boundary effect (absorbing wall) with its own region combinatorics?
status: open
rests-on:
- Goldie 2022 "Records, permutations and greatest convex minorants" (`research/sources/goldie_records_permutations_convex_minorants.full.md`): F_n (GCM side count) has independent-Bernoulli representation P(I_j=1)=1/j; face-length partition = cycle-length partition of uniform random permutation, distribution-free in the increment law.
- Alsmeyer–Kabluchko–Marynych–Vysotsky arXiv:2002.07687 (`research/sources/alsmeyer_kabluchko_marynych_vysotsky_convex_minorant_length.full.md`): permutation representation of GCM segment lengths and limit theorems.
- Suidan 2001 TVP via mathnet mirror (`research/sources/suidan_convex_minorants_random_walks_tvp.full.md`): P(GCM has m segments) = (1/(m! N^m)) d^m/dz^m (−ln(1−z))^m |_{z=0^+} = S1(N,m)/N! (unsigned Stirling first kind).
- Abramson thesis (echolarship): F_n d= K_n = sum_{j≤n} I_j, P(I_j=1)=1/j (records construction).
- Menon–Srinivasan arXiv:0909.4036 (`research/sources/menon_srinivasan_shock_clustering_lex.full.md`): half-line Burgers shock-clustering stays Markov for spectrally-negative Lévy data, generator obeys Lax equation (integrable) — the nearest published structure to a wall, but for sticky gas (mass-conserving) not rear-removal, and with Lévy/Brownian not Exp(1) iid speeds, and no parity statistic.
- Bernardi arXiv:1604.06554 (`research/sources/bernardi_deformations_braid_arrangement_trees.full.md`): regions of braid-arrangement deformations counted by decorated plane trees; the run's cell counts (n=3 → 32, n=4 → 1202, L-independent, 17/32 and 595/1202 even) do not match any catalogued transitive deformation sequence found so far.
blocked-by:
- No published treatment found of the finite-finish parity arrangement (hyperplanes (L−p_j)/v_j and (p_i−p_j)/(v_i−v_j) on the simplex).
- `finish-line-breaks-exponential-clock-machinery` claim: finish times are inverse-exponential (non-constant hazard), so Plackett–Luce/order-statistic-spacings machinery does not drive the bump/finish chronology.
next:
- Confirm whether the run's parity cells are regions of a *deformation of a braid-like arrangement* in the variable v_j directly (not the normalized simplex); test the region counts 32, 1202 against known deformation families (Shi, Linial, Catalan, semiorder, graphical).
- If no match: the arrangement is a new object; the exact route stays the run's own (rational functions of m=L/40 — verified n=2,3,4).