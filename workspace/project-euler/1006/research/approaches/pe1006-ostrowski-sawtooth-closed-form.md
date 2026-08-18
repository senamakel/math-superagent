# Approach: Ostrowski / Beatty numeration closed form for the second moment

```approach
idea: The mechanical/floor-sum reduction writes Ψ(k) as the second moment of
      v(x) = Σ_j digit_j(x) 10^{k-1-j} over the k+1 representatives x_m =
      frac(−m·a), a = F(n−2)/F(n). The run's current primitive for this is the
      universal-Euclidean monoid. The genuinely different route: the
      representatives x_m are equally spaced with step a on the circle, so the
      k+1 floor-sum values are the *sorted values of a Beatty-type sequence*,
      and the second moment over them can be evaluated directly from the
      continued fraction of α = 1/φ² by Ostrowski numeration — a number-theory
      closed form (sawtooth/summed-digit style, like the classic evaluation of
      Σ floor(iα) or Ostrowski's theorem on Σ {iα}), giving O(log k) with no
      matrix monoid and providing an independent check on the floor-sum.

mechanism: The gap between k+1 equally-spaced points on the circle is governed
      by the three-distance theorem; the multiset of values { floor(x_m + ja) }
      over m = 0..k is, for fixed j, countable in closed form from the
      continued fraction expansions of a (rational convergent to 1/φ²) and of
      the fractional parts. Summing the squares of the geometric-weighted
      combinations then reduces to signed sums of the "interval" measure of
      these Beatty sequences — the object Ostrowski's theory evaluates in
      O(log). This reuses the mechanical representation (so it inherits the
      verified slope/intercept work) but replaces the Euclidean monoid with an
      Ostrowski/Beatty closed form, an independent line and an independent
      verification target.

status: adopted

adopted-reason: The only grounded candidate that is also a genuinely
      independent evaluation of the SAME Psi(k) (three-gap/Ostrowski closed form
      instead of the universal-Euclidean monoid) — exactly what step-5
      verification needs. It inherits the verified mechanical slope/intercept
      work and replaces the single hard primitive with the three-gap exact
      counts, giving a second route to one number. Reaffirmed by the follow-up
      round: the three alternative engines (transfer-operator spectral,
      weighted-language diagonal, Fourier orbit correlation) were closed or
      narrowed by the literature, and the Fourier candidate's needed engine —
      continued-fraction renormalisation of fractional-part sums (J. Number
      Theory 1985; Ralston arXiv:1105.5810) — is exactly this route, so the
      synthesis folds into Ostrowski rather than creating a fourth engine.

mechanism-checked: Every ingredient is standard and cited.
      (i) The k+1 points frac(−m·a) are exactly N points of a circle rotation
      x ↦ x+a mod 1. The **Three Distance / Gap Theorem** (Sós) states their
      consecutive gaps take at most three lengths, with **exact counts**
      N1,N2,N3 and lengths L1,L2,L3 given in terms of the Ostrowski/continued-
      fraction data of a — see Weiß, arXiv:1807.11273 (explicit statement with
      counts) and van Ravenstein, J. Austral. Math. Soc. A 45 (1988). This is
      the machinery that turns the "multiset count" into a closed form.
      (ii) Sums Σ floor(iα) and Σ({iα}−1/2) have explicit OU—closed forms in
      the continued fraction of α / Ostrowski expansions: Rockett & Szüsz
      treat the full theory; "Sums of fractional parts of integer multiples of
      an irrational", J. Number Theory 1985 (0022314X85710128) gives explicit
      formulas for C(m,α,γ)=Σ({iα+γ}−1/2) via continued-fraction numerators.
      Bugeaud–Reutenauer, "On the conjugates of Christoffel words", DMT
      (dmtcs.15140), parametrise via Ostrowski numeration.
      (iii) The geometrically-weighted floor sum Σ_i x^i floor((a i+b)/c) — the
      exact object the second moment reduces to — is the universal-Euclidean /
      'Chtholly' primitive evaluated in O(log): AtCoder floor_sum, luogu P5170
      (template 类欧几里得算法), cnblogs mizu164 LOJ138 (万能欧几里得). This is the
      run's committed primitive; Ostrowski is an *alternative closed form* for
      the same sums, which is precisely what makes it an independent check.

independent-check: Because this route reaches the SAME Ψ(k) by a different
      closed-form reduction (three-gap/Ostrowski counts instead of the
      Euclidean monoid), it is the natural second, independent route for step 5
      — not a separate claim, but a separate way of computing the same number,
      which is exactly what independent verification needs.

precedent:
      - Weiß, "Deducing Three Gap Theorem from Rauzy-Veech induction",
        arXiv:1807.11273.
      - van Ravenstein, "The Three Gap Theorem (Steinhaus Conjecture)",
        J. Austral. Math. Soc. A 45 (1988) (or doi:10.1017/s1446788700031062).
      - Rockett & Szüsz, "Continued Fractions" / and the J. Number Theory note
        "Sums of fractional parts of integer multiples of an irrational"
        (0022314X85710128).
      - Bugeaud & Reutenauer, "On the conjugates of Christoffel words",
        Discrete Math. Theor. Comput. Sci., dmtcs.15140 (Ostrowski
        parametrisation).
      - Floor-sum with geometric weight: luogu P5170; cnblogs mizu164 "LOJ138
        类欧几里得算法【万能欧几里得】" (the universal-Euclidean primitive).

first-step: Implement the three-distance count function directly and verify it
      against the mechanical multiset before any O(log) claim. Concretely: for
      fixed k and rational slope a = F(n-2)/F(n) (F(n) > k, strict), compute
      the k+1 sorted points frac(-m·a), m = 0..k; get their gap multiset via
      the exact three-distance theorem (gap lengths and counts N1,N2,N3 from
      the continued fraction of a — Weiß arXiv:1807.11273, van Ravenstein);
      and for each digit position j confirm that the count of ones
      #{m : floor(x_m + j·a) - floor(x_m + (j-1)·a) = 1} equals the value the
      three-gap counts predict, for k = 1..60 against code/mech/mech_psi.py.
      The acceptance anchors are already corrected (Psi(10^4)=34432237,
      Psi(10^6)=20938836, claim directive6-anchors-verified-incontainer), so
      this route's gate is: reproduce Psi(k) for k=1..150, then Psi(10)=10699667,
      then the two corrected anchors, by a three-gap/Ostrowski closed form —
      no universal-Euclidean monoid, no Toeplitz collapse. Only then is it the
      independent step-5 route for the committed method.
```

## Assessment for the run

**Grounded.** The three-distance theorem gives exact gap counts of the
representative set, and sums of floors of multiples of an irrational have
explicit continued-fraction closed forms — together they make the second moment
an `O(log)` number, independent of the Euclidean monoid. This is the strongest
of the three proposals as an *independent verification* route for step 5: same
object, different reduction.
