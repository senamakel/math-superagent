Convergence-round decision, inventor. All three proposed candidates were
correctly refuted by research — one on its own run-collected falsifier
(boolean-influence, the `nu2 = #{zeta=1}` conflation), two on literature
grounds. Rather than salvage any of the three, I adopted the third option that
the refutations jointly point at but did not name.

Adopted: `overshoot-corrected-supply-weight`
(`research/approaches/overshoot-corrected-supply-weight.md`, status: adopted).

The synthesis: the F2 fold/parity structure is right, but every parity approach
drops the exact-value correction. The exact lift is

    nu2 = F_diag - O,
    F_diag = #{k in [2, n-1] : delta_k == 2 (mod 4)}   (actual-diagonal parity)
    O      = #{k in [2, tau-1] : delta_k == 2 (mod 4)} (outside the maximal
                                                        {0,2} suffix)

O splits into stray 2s outside the suffix and overshoot (delta_k >= 6, excess
t >= 2). The overshoot component is governed by the run's PROVED descent/excess
machinery (step-law drain, excess renormalization max-principle), not by new
parity theory. So the open supply bound splits into (i) the named-open ABGS
switch bound (parity side) and (ii) a NEW overshoot bound O <= (c'-c)n — the
attackable half.

Also corrected this round: the previously-adopted `dyadic-linear-complexity-supply`
carried the same broken identity `nu2 = #{zeta=1}`; it is now marked refuted,
with a pointer to the corrected decomposition.

First concrete step (tool_builder, today): write `code/out/overshoot_decomposition.py`
and measure, on ONE diagonal per n under ONE convention, nu2, F_diag, F_fold,
O, O_a, O_b on the primes / Thue-Morse / period-3 / consecutive-odds. The
decisive question is whether O = o(F_diag) (parity is approximately exact, ABGS
suffices up to a provable small error) or O carries real density (the magnitude
term is the whole problem). This is a measurement, never a proof; the exact
identity is immediate but the overshoot bound is conjectured.
