```approach
idea: Attack Ψ through the Rauzy graph (de Bruijn graph of factors) of the
Sturmian word instead of through window/floor-sum representations. For a
Sturmian word, exactly ONE length-k factor is right-special (both 0- and 1-
extensions occur) — call it R_k — and every other factor has a unique right
extension, so the factor set of length k+1 is obtained from that of length k by
replacing R_k by R_k 0 and R_k 1. This gives the exact, already-verified
recurrence Psi(k+1) = 100*Psi(k) + 100*V(R_k)^2 + 20*S1(k) + J(k), where V(R_k)
is R_k's decimal value and heavier S1(k)=sum of V(w) over the factors w with
w*'1' a factor. Named mathematics: Rauzy graph / right-special factors,
the extension-recurrence for factor complexity (Cassaigne), Sturmian balance.

mechanism: The recurrence is an exact step in k, but its driving terms are
governed by the Wythoff / Beatty block structure of the Fibonacci word: V(R_k)
is constant on runs [s_j, s_{j+1}-1] with s_j = floor(j*phi^2) (upper Wythoff
A001950), run lengths in {1,2,3}, and J(k) = 1+floor((k+1)/phi^2) exactly. So the
normalised recurrence advances k by whole Wythoff blocks, and the block-jump can
be collapsed by the same continued-fraction / Beatty summation (Ostrowski) used
for S1(k) and the run skeleton, giving O(log). This is a genuinely different
recursion in k from the adopted floor-sum monoid, and it is the run's own
verified-pattern ground (exact for k=1..3000 in the pattern hunt), so it doubles
as a second independent route at sizes brute cannot reach.

status: adopted
scope: Adopted AS THE RUN'S SECOND INDEPENDENT ROUTE at moderate k (10^4, 10^6),
reproducing the valid general-k anchors independently of the Toeplitz or
universal-Euclidean machinery. The primary 10^18 method remains the adopted
floor-sum/Ostrowski monoid (pe1006-ostrowski-sawtooth-closed-form); this
candidate is its independent verifier, not a replacement. The structural
ingredients are all literature-backed and the recurrence itself is the run's own
verified ground (exact k=1..3000). The mechanism's "giving O(log)" for the
Wythoff-block jump at k=10^18 is NOT a literature result: no source collapses a
base-10 value-sum recurrence by Wythoff/Beatty blocks, and the candidate's own
flag (a) names exactly this as open. So the O(log) claim is a derivation task,
not a citable fact, and the recurrence is stepwise-in-k unless that collapse is
derived. At k=10^6 the stepwise form costs O(#runs) = O(k/phi^2) ~ 4e5 run
updates with the pattern-hunt within-run S1 structure (S1(k)=A_j+d_j*10^{s_j} on
[s_j+1, s_{j+1}-1]), which is a feasible independent verifier; it is not a
10^18 method yet.
precedent: (a) unique right-special factor per length for Sturmian words —
Cassaigne, "Complexité des facteurs spéciaux" (Bull. Belg. Math. Soc. 4 (1997)
67-88) / special-factor-complexity-difference claim: p(n+1)-p(n) = #right-special
length-n factors, so exactly one for Sturmian; Du, Mousavi, Schaeffer & Shallit,
arXiv:1406.0670 (RAIRO-ITA), Thm 18: the unique right-special length-n factor of
the Fibonacci word is the reverse of the n-prefix f[0..n-1]^R (library claim
fibonacci-unique-special-factor-reverse); Masáková & Pelantová, arXiv:0809.0603
(factor complexity via Rauzy graphs, unique left/right special factors); a
straight proof in hal-01829175 / Wojcik formal-intercept notes. (b) Wythoff /
Beatty run structure — upper Wythoff A001950 (s_j = floor(j*phi^2)), run starts
verified in-container k=1..3000; J(k)=c1(k+1)=1+floor((k+1)/phi^2) matches OEIS
A189663 (c1(k)=ceil(k/phi^2)) — catalogue cross-check + in-container verification
(research/summaries/oeis_a189663.md, oeis_a001950.md). (c) the exact recurrence
itself is the run's own pattern-hunt ground (code/pattern_hunt/check_ext_recurrence.py,
pattern_verify_full.py, pattern_verify_runs.py: exact k=1..3000, mod M k=1..199/400);
no literature source applies an extension-recurrence to decimal factor values —
it is run-verified computation, appropriately claimed as such. (d) O(log)
collapse of the run-skeleton / S1(k) sums: NOT sourced; candidate's flag (a).
first-step: Build codework that runs the forward extension recurrence
Psi(k+1)=100*Psi(k)+100*V(R_k)^2+20*S1(k)+J(k) stepwise but run-compressed
(within-run S1(k)=A_j+d_j*10^{s_j} on [s_j+1,s_{j+1}-1], run starts s_j=floor(j*phi^2),
J(k)=1+floor((k+1)/phi^2)), and at k=10^4 and k=10^6 reproduce the valid
general-k residues INDEPENDENTLY of the Toeplitz and monoid machinery — i.e.
agree with brute/mech_psi where reachable and with the universal-Euclidean
monoid's output once that monoid is built. This discharges the adopted promise
and gives the primary route its second-method verifier. The Wythoff-block O(log)
jump is a separate derivation task, out of scope for this adopted role.
```

## Precedent pass (against the literature)

### Grounded
- **Unique right-special factor per length.** For a Sturmian word p(n) = n+1,
  so p(n+1) − p(n) = 1 = number of right-special length-n factors (Cassaigne's
  special-factor complexity difference, library claim
  `special-factor-complexity-difference`; also Masáková–Pelantová
  arXiv:0809.0603, "the unique left- and right-special factors of each length
  drive the cycle structure of the Rauzy graph Γn"). Du–Mousavi–Schaeffer–Shallit
  (arXiv:1406.0670, Thm 18) state it for the Fibonacci word itself: the unique
  right-special length-n factor is the **reverse of the n-prefix** (library
  claim `fibonacci-unique-special-factor-reverse`). This is exactly the
  structural fact the recurrence's R_k replacement rule needs.
- **Wythoff/Beatty block structure.** The run's own exact ground
  (code/pattern_hunt, verified k=1..3000): V(R_k) constant on runs whose starts
  are s_j = ⌊j·φ²⌋ = upper Wythoff A001950; run lengths ∈ {2,3}; and
  J(k) = c1(k+1) = 1 + ⌊(k+1)/φ²⌋, which matches OEIS A189663 (c1(k) = ⌈k/φ²⌉,
  Shallit's closed form) as a catalogue cross-check
  (research/summaries/oeis_a189663.md, oeis_a001950.md). Dekking's "Morphic
  words, Beatty sequences and integer images of the Fibonacci language" (TCS
  2020) and "The structure of Zeckendorf expansions" (arXiv:2006.06970) provide
  the surrounding Beatty/Zeckendorf theory of such block structures.
- **The recurrence is run-verified, not literature.** Ψ(k+1) = 100Ψ(k) +
  100V(R_k)² + 20S1(k) + J(k) is the run's own verified pattern (exact k=1..3000,
  per check_ext_recurrence.py / pattern_verify_full.py / pattern_verify_runs.py).
  No paper sums decimal values of Fibonacci factors via an extension recurrence;
  the correct status is "run-verified computation from a literature-grounded
  structural fact", not "literature theorem".

### Not sourced (candidate's own open question, flag (a))
- **O(log) collapse of S1(k) and the Wythoff-block jump at k=10^18.** No located
  source (including the spectral trace-map literature, which handles 2x2
  Schrödinger transfer matrices, and the Ostrowski/Beatty summation literature,
  which sums unweighted or φ-weighted quantities) gives a closed form for the
  run-skeleton sum that would jump the recurrence by whole Wythoff blocks in
  O(log). The within-run structure S1(k) = A_j + d_j·10^{s_j} on
  [s_j+1, s_{j+1}−1] (pattern-hunt ground) makes the stepwise recurrence
  O(#runs) per run-group, feasible to 10^6 but not 10^18. The O(log) claim is a
  derivation task, explicitly so flagged by the candidate.

### Verdict
**Grounded** for the role it actually claims: an independent second route at
10^4/10^6 and a genuinely different recursion in k (right-extension structure
vs mechanical floor sums), with every structural ingredient sourced and the
recurrence itself the run's own exact ground. **Not** a 10^18 method until the
run derives the Wythoff-block jump — a gap the candidate itself names, and which
the precedent pass confirms has no literature backing.