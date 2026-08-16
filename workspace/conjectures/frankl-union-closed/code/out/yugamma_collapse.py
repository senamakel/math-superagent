"""
Correct alpha=0 collapse check. The Yu extremal at t>=0.454 collapses onto
a1=a2=a=(3-sqrt5)/2, b1=1, b2=a, so the full coupling is
   P_pq = (1-beta) Q_{a,a} + beta Q_{a,1},  a=(3-sqrt5)/2, beta=(t-a)/(b-a),
   b=(a+1)/2, marginal atoms: {a, 1} with weights {(1-beta)+beta/2, beta/2}.
alpha=0 branch: Gamma = E_{P^otimes2} h(p+q-pq) / E h(p).
Check whether at t=0.5 this equals phi/2 = cos(36deg) = 0.809016994375 exactly.
"""
import math

log2 = math.log2


def h(x):
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


def gamma_alpha0_collapse(t, a):
    """alpha=0 ratio of the collapsed coupling at density t."""
    b = (a + 1.0) / 2.0
    beta = (t - a) / (b - a)
    # marginal atoms: a with w1=(1-beta)+beta/2, 1 with w2=beta/2
    w1 = (1.0 - beta) + beta / 2.0
    w2 = beta / 2.0
    vals = [a, 1.0]
    wts = [w1, w2]
    eh = w1 * h(a) + w2 * h(1.0)          # h(1)=0 -> eh = w1 * h(a)
    if eh <= 0:
        return math.inf
    e_indep = 0.0
    for pi, p in enumerate(vals):
        for qi, q in enumerate(vals):
            e_indep += wts[pi] * wts[qi] * h(p + q - p * q)
    return e_indep / eh


def main():
    a = (3.0 - math.sqrt(5)) / 2.0
    phi = (1.0 + math.sqrt(5)) / 2.0
    print(f"a=(3-sqrt5)/2 = {a:.12f}, phi/2 = cos36 = {phi/2:.12f}")

    for t in [0.454, 0.46, 0.48, 0.50, 0.55, 0.60]:
        g = gamma_alpha0_collapse(t, a)
        print(f"  t={t:.3f}: collapse alpha=0 Gamma={g:.12f}   (scan: "
              f"{['0.88344656','','','0.80901699','',''][int(round((t-0.454)*100))//6] if abs(t-0.454)<0.05 else ''})")

    print("\nAt t=0.5 compare to phi/2:")
    v = gamma_alpha0_collapse(0.5, a)
    print(f"  computed = {v:.12f}")
    print(f"  phi/2    = {phi/2:.12f}   diff={abs(v-phi/2):.3e}")
    print(f"  scan t=0.500000 Gamma_hat = 0.80901699")
    print(f"  conclusion: the t=0.5 alpha-0 collapsed Gamma = phi/2 exactly"
          " (analytic, cos(36deg)); corroborates scan to 8 dp.")


if __name__ == "__main__":
    main()
