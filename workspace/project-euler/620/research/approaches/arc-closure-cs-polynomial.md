```approach
idea: Single-monotone integer count via the n_p + n_q = c+s arc-closure identity and a degree-(c+s) unit-circle polynomial
mechanism: The workspace's winning meshing model (pattern_finder, checked: g(16,5,5,6)=9, G(16)=9, G(20)=205) is the toothed-contour integer congruence, NOT the W-invariant. For a type-t planet at upper tangency point P_t(d), with beta_t = angle of P_t about the ring centre O and mu_t = angle about the sun centre S (both of the SAME point), define n_t(d) = [ (c-t)*beta_t + (s+t)*mu_t ]/pi. All four planets mesh simultaneously iff n_p(d) in Z and n_q(d) in Z (the parity condition n_p - n_q == p - q mod 2 is automatic — see below). The decisive structural fact is the IDENTITY n_p(d) + n_q(d) = c + s holding for EVERY d in the admissible interval (numerically exact to 60 digits in code/out/winner_refine.txt), which collapses the model: n_q = (c+s) - n_p, so n_q in Z is automatic once n_p in Z, and n_p - n_q = 2*n_p - (c+s) == c+s == p-q (mod 2) because c = s+p+q. The whole four-planet meshing condition therefore reduces to the single condition n_p(d) in Z on the monotone function n_p (increasing on (d_min, d_max), checked per case in code/pattern/fast_g.py), so g(c,s,p,q) = #{k in Z : n_p(d_min) < k < n_p(d_max)}. The transcendental congruence n_p(d) = k is algebraised exactly: with z = e^{i beta_p}, a_p = (c-p)/(2pi), b_p = (s+p)/(2pi), and the triangle closure b_p e^{i mu_p} = a_p z - d, the condition (c-p)beta_p + (s+p)mu_p = pi*k is equivalent to the unit-circle polynomial z^{c-p} * (a_p z - d)^{s+p} = (-1)^k * b_p^{s+p}, of degree c+s in z. Since n_p is monotone, g is just the number of integer levels k crossed over the d-interval, counted by the endpoint values n_p(d_min), n_p(d_max) — a bound-independent O(1)-per-tuple evaluation with exact (interval/Sturm) floor handling.
status: adopted
first-step: (1) Prove the identity n_p(d)+n_q(d) = c+s (elementary angle-sum / Ptolemy argument on triangle OSP), and prove n_p(d) is strictly increasing on (d_min, d_max). (2) Reduce g to #{k in Z : n_p(d_min) < k < n_p(d_max)} with d_min = max(|c-s-2p|, |c-s-2q|)/(2pi), d_max = (c-s)/(2pi) - 1; at d_min the limiting type's triangle is degenerate so n_p(d_min) is piecewise 0 / (c-p) / (s+p) / etc. by the sign of c-s-2t, and at d_max it is an arctan value at gap = 1 (a 2pi enters, so exact-floor needs interval arithmetic or the unit-circle polynomial). (3) Implement g(c,s,p,q) = floor(n_p(d_max)) - ceil(n_p(d_min)) + 1 with exact floor via high-precision interval arithmetic + escalation to the degree-(c+s) polynomial when a level is within 1e-12 of an endpoint; sum over all (s,p,q) with s+p+q <= 500 and verify 9/9/205 first.
```

## What this is, and how it was reached

This is the synthesis the inventor+research exchange is meant to produce: it is
**neither** of the three originally proposed candidates, but the intersection of
what the literature actually says and what this run's own computation found.

- Research verdict on `number-theoretic-crt` grounded the *reformulation* — the
  discreteness is a toothed-contour integer congruence (Kurasov 2020, eq. 7/8:
  Σ φ·z = πK or 2πK′), valid for **eccentric** systems — while explicitly
  rejecting its *multiplicative/CRT count* half (unsupported, and the
  index↔d identification overcounts because tangency forces positions and the
  free variable is d).
- Meanwhile the run's own winning model (`code/pattern/n_integer_count.py`,
  `winner_refine.py`, `tangency_enum.py`) established the correct discrete
  congruence empirically: `n_t(d) = [(c-t)beta + (s+t)mu]/pi in Z`, with the
  crucial **identity `n_p + n_q = c+s`** that neither the W-invariant nor any
  candidate anticipated.

So the adopted line is exactly "the combination of your reformulation and what
the literature actually says": Kurasov's toothed-contour congruence is the
correct discrete language, but the payoff is **not** a CRT/Smith product — it is
the identity `n_p + n_q = c+s`, which collapses four congruences to one monotone
integer-level count, and the unit-circle polynomial `z^{c-p}(a_p z - d)^{s+p} =
(-1)^k b_p^{s+p}` (degree c+s) turns that into exact root counting.

## Why it beats the alternatives

- **Beats `inversion-coaxial`** (already refuted): no conformal map, no
  metric/tooth-pitch transfer problem; the teeth data live in the original
  geometry via the arc-length closure, which is precisely what survives.
- **Beats `tangent-half-angle`**: the t = tan(E/2) parametrisation was mounted
  on the still-unverified W-invariant and mixed ellipse eccentric anomaly with
  circle angles. The unit-circle z = e^{i beta_p} substitution is cleaner: it
  keeps the actual tangency triangle (a_p, b_p, d) and gives a degree-(c+s)
  polynomial directly, with no square-root clearing or spurious roots.
- **Beats `number-theoretic-crt` as proposed**: it keeps Kurasov's congruence
  but replaces the overcounting CRT product with the exact reduction
  `n_q = (c+s) - n_p`, so there is exactly ONE free integer condition and the
  count is monotone integer-level crossings — no gcd/lcm multiplicative
  conjecture, no four-index overcount.

## Status of each ingredient

- **Checked (this run's computation):** the model reproduces g(16,5,5,6)=9,
  G(16)=9, G(20)=205; n_p increasing on the admissible interval; the identity
  n_p+n_q = c+s at 60-digit precision (including at arbitrary non-valid d);
  mirror symmetry (upper/lower are the two tangency points). Anchors:
  `code/out/n_integer_model.txt`, `code/out/winner_refine.txt`,
  `code/out/tangency_enum.txt`.
- **Sourced:** the toothed-contour congruence shape (Kurasov 2020, MATEC Web
  Conf. 329:03027, eq. 7/8 — eccentric systems), plus the Guo 5.21–5.25 /
  Parker–Lin / Zou / Sun coaxal assembly-condition literature.
  Caveat: Kurasov full text is 403-blocked; eq. 7/8 from search-engine
  extraction, unverified locally.
- **Still to prove (first-step 1):** the exact identity n_p+n_q = c+s and the
  monotonicity of n_p over the whole interval for all (c,s,p,q) — currently
  numerical, needs an elementary geometric proof.
- **Still to derive (first-step 2–3):** the exact endpoint floors n_p(d_min),
  n_p(d_max), and the O(1) g with exact integer-part evaluation.

## Oracle anchors to respect

g(16,5,5,6)=9, G(16)=9, G(20)=205; target G(500). Any closed form must first
reproduce the 22 per-tuple g values in `code/out/n_integer_model.txt` (sum 205).
