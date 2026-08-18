# G4 thesis attack — TPTP encoding

# Statement under attack (hypotheses of the mechanical-word model):
#   a = p/q in (0,1), rational; k < q; digits
#     d_j(x) = floor(x + (j+1)a) - floor(x + ja);
#   factor values v_m over the k+1 intercepts x_m = -m*a mod 1 (m = 0..k);
#   Psi(k) = sum_m v_m^2.
# The *thesis* is that no fixed-dimensional O(log k) aggregation of Psi(k)
# over all k+1 intercepts is known/available.  This file encodes only the
# *tempting single-intercept replacement*: the claim that a single intercept
# suffices, i.e. that Psi(k) is determined by the m=0 factor alone.
# A model where v_0 is the same but Psi(k) differs refutes that replacement.

# k = 1.  Intercepts m = 0, 1.  Values: v_0 = d_0(-0) = 1 - 0 = 1
# (binary "1" at the m=0 arc); v_1 = d_0(-a).  Hypothesis d0 = 0 or 1,
# and the word is not the all-zero word.  Claim: v_1 = v_0 (single intercept
# determines the sum).  A model with d0 = 0 gives v_1 = 0 != 1.

fof(h_digit_binary, axiom, d0 = 0 | d0 = 1).
fof(h_not_all_zero, axiom, d0 = 1 | v1 = 1).
fof(h_factor_values, axiom,
    (v1 = d0) & (v0 = 1)).
fof(goal, conjecture, v0 = v1).
