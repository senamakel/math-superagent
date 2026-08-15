# Kummer descent + local symbols — the divisibility conditions as cohomology

```approach
idea: Recast the ideal→element lift (x − ζ_p^i) = u·α^q in Z[ζ_p] as an explicit Kummer class in K^×/(K^×)^q ≅ H^1(K, μ_q), and derive the Cassels/double-Wieferich divisibility conditions as local triviality of that class via the Hilbert symbol and Hensel lifting — no analytic class-number table.
mechanism: factors pairwise coprime off (1−ζ_p) → each ideal (x−ζ_p^i) a q-th power ideal up to the ramified prime. Obstruction to the element-lift is a class in Cl(K)/qCl(K); via the Kummer map K^×/(K^×)^q ≅ H^1(K,μ_q) this is the Kummer class of x−ζ_p. "A class in K^×/(K^×)^q is trivial iff a local q-th power at every place (Hilbert symbol local-global)"; evaluating at primes above q by Hensel lifting gives the q^2-Wieferich congruence, valuation at (1−ζ_p) gives Cassels p|y. Would convert check_conditions from numerically-calibrated to proved, including the crossprime-q-hminus-not-sourced forcing step.
status: refuted
killed-by: local-global-does-not-detect-class-group (the Cl/qCl obstruction is the non-local part; local Hilbert symbols cannot force q|h^-(Q(ζ_p)))
precedent: Kummer theory/Hilbert symbol local-global (standard; Påsztor–Adachi, "On norm residue symbols and conductors", https://www.sciencedirect.com/science/article/pii/S0022314X00925605); cohomological characterisation of the Hilbert symbol on Q_p^×, https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/cohomological-characterization-of-the-hilbert-symbol-over-qp/2859498F443527AF5CC4B822D8DBFAC5; Kummer descent in Z[ζ_p] for generalized Fermat (Stickelberger/reflection on the ω-component), https://hal.science/hal-00578783v2/document
```

**Literature verdict: REFUTED — the local-symbol reformulation cannot deliver the class-group half it promises.**

## What the technique actually is, and whether it is real

The Kummer part is completely standard and sourced:
- Kummer map `K^×/(K^×)^q ↪ H^1(K, μ_q)` (Kummer theory); for K containing μ_q, Hilbert-symbol local-global: an element α ∈ K^× is a global q-th power iff it is a q-th power in every completion. Sources: standard; the local-symbol/conductors literature is Påsztor–Adachi, "On norm residue symbols and conductors" (https://www.sciencedirect.com/science/article/pii/S0022314X00925605), and the cohomological characterisation of the Hilbert symbol on Q_p^× (https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/cohomological-characterization-of-the-hilbert-symbol-over-qp/2859498F443527AF5CC4B822D8DBFAC5).
- Kummer descent in Z[ζ_p] applied to generalized-Fermat-type equations is published: the hal-00578783 exposition (Stickelberger/reflection killing the ω-component of the p-class group, Furtwängler-type congruences) does exactly this *for the same-prime / conjugate-part situation*.

## The fatal defect: local triviality is about elements, and the q|h^- forcing is non-local

The candidate's central promise is that local symbols re-derive **both** the Wieferich congruence **and** the class-group forcing `q | h^-(Q(ζ_p))` (the load-bearing `crossprime-q-hminus-not-sourced`), converting check_conditions to proved.

The local-global principle is a statement about **elements**: "α is a global q-th power iff locally a q-th power." The obstacles to "x−ζ_p^i is a q-th power element" are (1) the unit/root-of-unity part and (2) the ideal class of the q-th-power ideal being trivial. Obstacle (2) — `Cl/qCl` — is **exactly the non-local part**: it is a genuinely global arithmetic invariant that no fixed set of local Hilbert symbols can detect. The whole reason the classical descent is blocked by the class group is precisely that local triviality does NOT imply global principality.

So the mechanism's claimed equivalence "globally trivial ⇔ q|h^-(Q(ζ_p)) and Wieferich holds" is wrong: the local-symbol machinery reproduces at most the *congruence* half (the Wieferich/Cassels-q^2 congruence, which is genuinely a local q-th-power condition at the mirror prime), and **cannot** produce the `q|h^-(Q(ζ_p))` forcing, which is global. The candidate even states the obstruction to the element-lift as a class in `Cl(K)/qCl(K)` and then proposes to detect it locally — that is the one thing local symbols cannot do.

## Honest residue

- **What survives**: the Wieferich congruence `q^{p-1} ≡ 1 (mod p^2)` (and the Cassels valuation `p|y`) are plausibly re-derivable as local q-th-power / valuation conditions via the Hilbert symbol and Hensel lifting. That half of the approach is grounded and would be a genuine strengthening of check_conditions' calibration. It also gives a clean *cohomological* explanation of the "double" (q-th-power-residue at both mirror primes).
- **What is killed**: the claim that local triviality of the Kummer class of x−ζ_p is *equivalent* to the full divisibility conditions *including* `q|h^-`. That forcing step remains exactly as open as before (`crossprime-q-hminus-not-sourced`); local symbols cannot close it because it is non-local.

## What to do next

If this line is reopened, it should be reopened as a *partial* mechanism: derive the Wieferich-congruence half from Kummer descent + Hilbert symbol (grounded, standard), and state plainly that the class-group half is untouched, requiring the Mihăilescu/Cassels forcing that this run has not sourced. Do not reopen it as a route to `q|h^-`.

precedent: Kummer theory/Hilbert symbol local-global (standard; Påsztor–Adachi, "On norm residue symbols and conductors", https://www.sciencedirect.com/science/article/pii/S0022314X00925605); "(a,b)_p" characterisation https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/cohomological-characterization-of-the-hilbert-symbol-over-qp/2859498F443527AF5CC4B822D8DBFAC5; Kummer descent in Z[ζ_p] for generalized Fermat (Stickelberger/reflection on the ω-component), https://hal.science/hal-00578783v2/document .
killed-by: local-global-does-not-detect-class-group (the Cl/qCl obstruction is the non-local part; local Hilbert symbols cannot force q|h^-(Q(ζ_p))).
