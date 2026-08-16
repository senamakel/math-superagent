# Approach: Abel–Gontcharoff root-difference representation, with pinned-centroid descent (adopted, primary line)

Change representation from the coefficient ideal to the root multiset, using the
**exact** per-root factorization of the Hasse derivatives, and — the synthesis
this round's convergence names — use its `e_1` case to pin the last scenario
coordinate and obtain an explicit descent. This is the single line the run
executes; the other four `adopted` files (centroid-recursion,
deformation-obstruction-bad-points, osculating-curve-wronski,
arithmetic-jet-lift) are folded into it, not running beside it.

```approach
idea: Abel–Gontcharoff / root-difference factorization of the resultants,
      sharpened by the pinned centroid. Write f = ∏_{j=1}^n (x − β_j) (monic).
      The Hasse derivative is the Taylor coefficient:
          f(x+t) = ∏_j ((x−β_j) + t) = Σ_i e_{n−i}(x−β_1,…,x−β_n) t^i,
      hence — exactly, over every field, with no char-0 hypothesis —
          H_i(f)(x) = e_{n−i}(x−β_1, …, x−β_n),
      the (n−i)-th elementary symmetric function of the differences from x to
      the roots. Therefore, up to the (unit) leading coefficient,
          R_i := Res_x(f, H_i(f)) = ∏_{β root of f} e_{n−i}(β−β_1,…,β−β_n).
      For the witness root β = β_j the difference β_j−β_j = 0 drops out, so
          H_i(f)(β_j) = e_{n−i}(β_j−β_1, …, [j removed], …, β_j−β_n),
      the (n−i)-th elementary symmetric function of the n−1 differences from β_j
      to the *other* roots. CA ⟺ for each i = 1..n−1 there is a root β_{j_i}
      with this e_{n−i} = 0, i.e. an Abel–Gontcharoff vanishing pattern.

      The synthesis (the "neither side named it" move): the i = n−1 case is
          H_{n−1}(f)(β_j) = e_1(β_j−β_1,…,[j],…,β_j−β_n)
                          = Σ_{k≠j}(β_j−β_k) = nβ_j + a_1 = n(β_j − c),
      where c = −a_1/n = (Σ_j β_j)/n is the centroid. So the hypothesis at
      i = n−1 (derivative n−1 shares a root with f) FORCES c to be a root of f,
      and forces the root witnessing color n−1 to be β = c: the last coordinate
      j_{n−1} of every Ghosh scenario tuple T = (j_1,…,j_{n−1}) is pinned. The
      tuple space shrinks from n^{n−1} to n^{n−2} (a factor-n reduction — the
      only measured lever against the n=20 minors infeasibility, where
      C = binom(190,18) ≈ 1e20). Writing f = (x−c)·g (deg g = n−1), the
      remaining colors i = 1..n−2 become conditions on g; the unproved
      induction (the load-bearing bet, exactly Ghosh's claimed downward
      induction, restated algebraically with no Brouwer-degree step) is that
      these force g to be CA of degree n−1. That induction is what the run
      attacks next, on paper at small n and against the char-p witness.
mechanism: This is the explicit form of Ghosh's reformulation. Ghosh (2024/25)
      reduces CA to: for every index tuple T = (j_1,…,j_{n−1}) the homogeneous
      forms G_{T,i} = Φ_{j_i}(σ_i(x_1,…,x_{n−1})) form a regular sequence. The
      per-root identity identifies σ_i with e_{n−i} and the variables x_ℓ with
      the differences β_{j_i}−β_{k(ℓ)}: the scenario equation "derivative i
      shares root β_{j_i}" is *literally* e_{n−i}(differences from β_{j_i}) = 0.
      So the scenario/regular-sequence machinery the run already owns gets an
      explicit closed form, and Newton's identities convert each e_{n−i} = 0
      into power-sum conditions p_m(β_{j_i}) = Σ_{k≠j_i} (β_{j_i}−β_k)^m = 0
      — and those power sums are themselves Hasse-derivative evaluations of f
      at β_{j_i}, closing the loop. The named engines are Abel–Gontcharoff
      interpolation, Newton's identities, the Jacobi–Trudi / Giambelli
      determinantal forms of the e's, and the pinned centroid (e_1 case) as the
      descent device. The collapse step is the Gauss–Lucas/Polstra fact
      (sourced, held): every root a vertex of the convex hull ⟺ f is a pure
      power, so a counterexample has a non-vertex root — the ordering that the
      e_{n−i}-equations must propagate to a contradiction.
status: adopted
first-step: (tool_builder/coder, exact sympy, oracle-guarded via
      lib.casas_alvero — NO code-execution role has run this yet; the capture
      code/out/rootdiff_identity.captured.txt does not exist.)
      Stage 1 (already scripted, run as-is): execute
      code/rootdiff/verify_rootdiff_identity.py, capture to
      code/out/rootdiff_identity.captured.txt, and report the verdict against
      the script's own failure criterion on both identities (A) H_i(f)(x) =
      e_{n−i}(x−β_*) and (B) R_i = ∏_β H_i(f)(β), over QQ n=4,5,6 and F_p
      n=p+1, p=2,3,5.
      Stage 2 (the synthesis's first arithmetic check, new this round): for
      n = 5,6,8 verify (a) H_{n−1}(f) = nx + a_1 exactly; (b) gcd(f,H_{n−1}f)≠1
      ⟹ f(c)=0, c=−a_1/n, on random monic f; (c) COUNT scenario tuples: among
      all n^{n−1} tuples T only n^{n−2} can satisfy G_{T,n−1}=0 because j_{n−1}
      is pinned to the centroid root — report the concrete saving; (d) the
      induction core on the guard set: for f=(x−c)·g with f CA of degree n,
      check whether g shares a root with each of its first n−2 Hasse
      derivatives (this is the statement the whole descent rests on — verify it
      does NOT follow vacuously, and on which small examples it holds); (e) the
      char-p witness x^{p+1}−x^p (p=2,3,5,7): confirm step (i) SURVIVES
      (c=−a_1/n=1 is a root, n=p+1 invertible) while the descent step (ii)
      FAILS (n−1=p≡0, so centroid(g)=c is undefined) — the named char-p break.
charp-break: The factorization H_i(f)(β) = e_{n−i}(β−β_1,…) is valid over every
      field (Hasse derivatives), so the identity itself has no char-p break. The
      break is per-color degeneracy plus the loss of the convex-hull ordering.
      For the witness x^{p+1}−x^p over F_p (roots 0,1) the Hasse derivatives are
      H_1 = x^p, H_i = 0 for 2 ≤ i ≤ p−1 (Lucas: C(p,i)=C(p+1,i)=0 mod p), and
      H_p = x−1. So root 0 witnesses every color 1..p−1, root 1 witnesses color
      p, and the two-root coloring survives because the vanishing colors impose
      no constraint while the Gauss–Lucas/convex-hull propagation has no F_p
      analogue. Separately, the pinned-centroid descent breaks at p | n−1: the
      centroid c is still a root (step (i) survives since n = p+1 is invertible)
      but centroid(g) = c requires dividing by n−1 ≡ 0 — the witness sits
      exactly on that break. Verified by hand via Lucas for p = 2,3,5 in
      research/notes/root-difference-identity-verified.md.
first-step-status: identity SETTLED by proof (char-free tautology over any commutative
      ring, research/notes/root-difference-identity-verified.md). The Stage 1
      symbolic capture is DELIBERATELY SUPERSEDED (directive 10 option 2): the
      zero-byte capture was a failed redirection and must not be re-run;
      code/rootdiff/verify_rootdiff_identity.py is not load-bearing. The only
      live question is the char-p break (rdc-charp-break), located on paper as
      per-color vacuity {2..p-1} + no F_p convex-hull ordering + the p|n-1
      descent break. Stage 2 (pinned-centroid pinning + descent induction core)
      remains the concrete arithmetic work once the break is named.
precedent: gvb-lift, bad-prime-criterion (Schaub–Spivakovsky Cor 8),
      bad-prime-minors-criterion (arXiv:2411.13967 Thm 3.1), ghosh-complete-
      intersection (the G_{T,i}/regular-sequence reformulation), polstra-convex
      hull (every root a vertex ⟺ pure power), and Castryck–Laterveer–Ounaïes
      2012 (the centroid/root of f^{(d−1)} is already used as a distinguished
      point — Prop 15/16 — so the pinning is the literature's own distinguished
      point, not new; what is new is pinning the scenario coordinate and the
      explicit descent). The per-root identity H_i(f)(x) = e_{n−i}(x−β_1,…) is
      elementary and exact (f(x+t) Taylor expansion); verified on paper as a
      char-free tautology in research/notes/root-difference-identity-verified.md.
speculative: the collapse step "the e_{n−i} = 0 colorings force all n roots to
      coincide" — equivalently "g inherits the CA property under f=(x−c)·g" —
      is the conjecture to establish (provable-for-small-n first). The identity
      and the pinning are not speculative; the induction is, and it is stated
      here as the attack target rather than asserted.
```

## Decision record (convergence this round)

The proposing call timed out, so there were no fresh candidates. Research's
return re-derived the standard Hasse/derivative-tower model and added no new
engine. The existing convergence therefore stands, and this round's decision is
to make it single and executable: **root-difference-coloring is the adopted
line**, sharpened by the pinned-centroid descent (its `e_1` case). The other
four `adopted` files are folded into it as its engines, each closed with a
`killed-by` line in its own file:

- `centroid-recursion` — the `i = n−1` case of this identity; absorbed here.
- `arithmetic-jet-lift` — the determinant (`J_T` minor) form of the same Ghosh
  scenario machinery; kept as this line's engine and provenance, not a separate
  attack.
- `deformation-obstruction-bad-points` — the fiberwise rank reading of the same
  `M_T`; blocked by the same measured wall, not a cheaper route.
- `osculating-curve-wronski` — the same incidence data in projective form; no
  new inference.
