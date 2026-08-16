"""
Independent cross-check of the Yu (Entropy 2023) certified point, computed by a
DIFFERENT code path from code/out/yu_optimization.py.

Certified point: alpha=0.035, a1=a2=a=0.3300622, b1=a, b2=1, t=0.38234.
Coupling P_pq = (1-beta) Q_{a,a} + beta Q_{a,1},  Q_{x,y} = 1/2 d_{(x,y)} + 1/2 d_{(y,x)}.

Differences from yu_optimization.py:
  * the independent product coupling E_{P_p^otimes2} is summed explicitly over the
    4 marginal-atom pairs with math.fsum, NOT via the closed form that drops h(1)
    terms (so h(1)=0 behavior is exercised, not assumed);
  * phi(1,p,q) is computed with an explicit 3-element sort, not np.median;
  * all atom weights are built from beta with explicit floats and summed with
    math.fsum.

Only Python's math module is used (no numpy/scipy), so this is a genuinely separate
implementation of the same formula. Agreement to ~1e-9 is the claim being tested.

Output: the same g/E h(p) value, to be compared with yu_optimization.py's
'Gamma_hat(t) >= 1.00000889'.
"""
import math

log2 = math.log2


def h(x):
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


def phi1(p, q):
    """phi(1,p,q) = median{max{p,q}, 1/2, p+q} via explicit 3-sort."""
    return sorted([max(p, q), 0.5, p + q])[1]


def crosscheck():
    alpha = 0.035
    a = 0.3300622
    t = 0.38234
    b1, b2 = a, 1.0

    # --- geometry / beta (explicit, same as paper) ---
    a_mean = (a + a) / 2.0          # = a
    b_mean = (b1 + b2) / 2.0        # = (a+1)/2
    assert 0.0 <= a_mean <= t < b_mean <= 1.0
    beta = (t - a_mean) / (b_mean - a_mean)

    # --- joint atom weights (explicit, summed with fsum) ---
    wa = (1.0 - beta) / 2.0         # each of (a1,a2),(a2,a1) -> here both (a,a)
    wb = beta / 2.0                 # each of (b1,b2),(b2,b1) -> (a,1),(1,a)

    # marginal P_p: p=a1 w=wa, p=a2 w=wa, p=b1 w=wb, p=b2 w=wb
    marg_vals = [a, a, b1, b2]
    marg_wts = [wa, wa, wb, wb]
    Ehr_tot = math.fsum(wi * h(vi) for vi, wi in zip(marg_vals, marg_wts))  # E h(p)

    # --- E_{P_p^otimes2} h(p+q-pq) : independent product coupling ---
    indep_terms = []
    for i in range(4):
        for j in range(4):
            p = marg_vals[i]
            q = marg_vals[j]
            indep_terms.append(marg_wts[i] * marg_wts[j] * h(p + q - p * q))
    e_indep = math.fsum(indep_terms)

    # --- E_{P_pq} h(phi(1,p,q)) : the coupled (dependent) atoms ---
    # atoms: (a1,a2) w=wa, (a2,a1) w=wa, (b1,b2) w=wb, (b2,b1) w=wb
    cry_vals = [a, a, b1, b2]      # first coordinate
    cry_wts = [wa, wa, wb, wb]
    coupled_terms = []
    for k in range(4):
        p = cry_vals[k]
        q = cry_vals[k]            # a1,a2 -> here q = p^* = same equal; for Q_{x,y} pairs
        # For Q_{a,a} both coords are a; for Q_{a,1} the two Diracs are (a,1),(1,a).
        # Reconstruct explicitly rather than assuming symmetry:
    # Explode Q atoms directly:
    #   Q_{a,a} = d_{(a,a)}                       (weight 1-beta over the Q)
    #   Q_{a,1} = 1/2 d_{(a,1)} + 1/2 d_{(1,a)}   (weight beta)
    qatoms = [((a, a), 1.0 - beta), ((a, 1.0), beta/2.0), ((1.0, a), beta/2.0)]
    coupled_terms = [w * h(phi1(p, q)) for (p, q), w in qatoms]
    e_coupled = math.fsum(coupled_terms)

    g = (1.0 - alpha) * e_indep + alpha * e_coupled
    ratio = g / Ehr_tot

    print("INDEPENDENT cross-check (math.fsum, explicit 3-sort phi, explicit Q-atoms)")
    print(f"  a={a} t={t} alpha={alpha} b1={b1} b2={b2}")
    print(f"  beta        = {beta:.9f}   (expect 0.1560676)")
    print(f"  E h(p)      = {Ehr_tot:.12f}")
    print(f"  E[P^2] h    = {e_indep:.12f}")
    print(f"  E[P_pq] h   = {e_coupled:.12f}")
    print(f"  g           = {g:.12f}")
    print(f"  g / E h(p)  = {ratio:.11f}")
    return ratio


if __name__ == "__main__":
    v = crosscheck()
    ref = 1.00000889
    print(f"\nReference (yu_optimization.py): >= 1.00000889")
    print(f"Cross-check value:               {v:.8f}")
    print(f"Abs diff from 1.00000889:        {abs(v - ref):.3e}")
