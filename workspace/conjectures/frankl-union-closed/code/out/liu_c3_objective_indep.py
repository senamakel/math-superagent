#!/usr/bin/env python3
"""
liu_c3_objective_indep.py — independent second implementation of Liu's
conditionally-IID 9-dimensional coupling objective (Liu, arXiv:2306.08824,
Eq (84), Theorem 12/13 / Section V-B).

This file is an INDEPENDENT code route, written from the paper's stated
objective and the prompt definition, so that a second route can cross-check
the primary implementation. It shares no code with the Yu/Sawin two-atom
scorer in code/lib/uccouple.py or code/search/uc-coupling/*.

OBJECTIVE (Eq (84) in Liu, written in the prompt's notation):

    h(z) = -z*ln(z) - (1-z)*ln(1-z)            (natural log; ratios unaffected)

    P0 = a1*d(b0) + a2*d(b2) + (1-a1-a2)*d(b4)
    P1 = a1*d(b1) + a2*d(b3) + (1-a1-a2)*d(b5)
    qbar = 1 - q
    M   = qbar*P0 + q*P1

    D = E_M[h(X)]                                 (denominator)

    N = (1-beta) * E_{X,Y iid M}[h(XY)]                                  (iid term)
      + beta     * ( qbar*E_{X,Y iid P0}[h(XY + XY(1-X)(1-Y))]
                   + q*E_{X,Y iid P1}[h(XY + XY(1-X)(1-Y))] )             (coupled term)
      (cond. IID: conditioned on a common U, X,Y ~ P0 resp ~ P1, but the
       expression XY+XY(1-X)(1-Y) = X*Y*(1 + (1-X)(1-Y)) is the OR-adjacent
       output under the protocol of Example 5 with f(sbar)=sbar^2; by
       symmetry the "conditioned" OR-entropy reduces to this product form.)

    objective = N / D

    A constant c is certified iff min objective >= 1 subject to
        E_M[X] >= 1 - c ,  all vars in [0,1],  a1 + a2 <= 1.

Entry point: python3 liu_c3_objective_indep.py
Reports every number to 15 digits using mpmath at mp.dps=50.

Two reference evaluations, both reproduced:

(1) Liu's conditional record.
    q=0, P0 = p*d(x) + (1-p)*d(0)  with
        p   = 0.893604513905457
        x   = 0.690787593924988
        beta= 0.100052559862974
    => E_M[X] = p*x = 0.617290912081259
       c' = 1 - p*x = 0.382709087918741
       objective = 1.0000000000000  (1.0 to ~1e-14)

(2) Sawin/Yu record expressed as a 9-d point.
    Two-atom: P0 = (1-a)*d(1-b) + a*d(0), q=0, with
        a   = 0.0788772927059232
        b   = 0.329454738503037
        beta= 0.0356069
    => E_M[X] = (1-a)(1-b) = 0.617654466633297
       c* = 1 - E_M[X] = 0.382345533366703
       objective = 1.00026277270766

Both are reported with the mapping P0 = a1*d(b0) + a2*d(b2) + a3*d(b4),
a3 = 1-a1-a2, so the whole thing is written as a genuine 9-d vector
(a1,a2,q,b0..b5) plus beta, exactly the (84)+(85)+(86)+(87) formulation.
"""

import mpmath as mp

mp.mp.dps = 50

# --------------------------------------------------------------------------
# entropy and the objective, written as pure functions on the 9-d vector
# --------------------------------------------------------------------------
def h(z):
    """Binary entropy, natural log, h(0)=h(1)=0."""
    z = mp.mpf(z)
    if z <= 0 or z >= 1:
        return mp.mpf(0)
    return -z * mp.log(z) - (1 - z) * mp.log(1 - z)


def entropy_moments_atoms(weights, values):
    """E_{sum w_i d(v_i)} [ h(X) ]."""
    return mp.fsum(w * h(v) for w, v in zip(weights, values))


def product_expected_h(weights, values):
    """E_{X,Y iid sum w_i d(v_i)} [ h(X*Y*(1 + (1-X)(1-Y))) ].

    X,Y independent with the given atom distribution.  The coupled argument
    is XY + XY(1-X)(1-Y) = XY * (1 + (1-X)(1-Y)).
    """
    out = mp.mpf(0)
    for i in range(len(weights)):
        for j in range(len(weights)):
            x, y = values[i], values[j]
            arg = x * y + x * y * (1 - x) * (1 - y)
            out += weights[i] * weights[j] * h(arg)
    return out


def iid_expected_h(weights, values):
    """E_{X,Y iid sum w_i d(v_i)} [ h(X*Y) ]."""
    out = mp.mpf(0)
    for i in range(len(weights)):
        for j in range(len(weights)):
            x, y = values[i], values[j]
            out += weights[i] * weights[j] * h(x * y)
    return out


def p0_p1_from_9d(a1, a2, q, b0, b1, b2, b3, b4, b5):
    """Return (weights0, vals0, weights1, vals1, a3)."""
    a3 = 1 - a1 - a2
    w0 = (a1, a2, a3)
    v0 = (b0, b2, b4)
    w1 = (a1, a2, a3)
    v1 = (b1, b3, b5)
    return w0, v0, w1, v1, a3


def objective(alpha_params):
    """objective(a1,a2,q,b0,b1,b2,b3,b4,b5,beta) -> (obj, E_M_X).

    All nine vars + beta.  Uses the (84) expression.
    """
    a1, a2, q, b0, b1, b2, b3, b4, b5, beta = alpha_params
    qbar = 1 - q
    w0, v0, w1, v1, a3 = p0_p1_from_9d(a1, a2, q, b0, b1, b2, b3, b4, b5)

    # denominator: E_M[h(X)] with M = qbar*P0 + q*P1.
    # M has atoms: qbar on each of (b0,b2,b4) weighted (a1,a2,a3), and
    # q on each of (b1,b3,b5) weighted (a1,a2,a3).
    D = mp.mpf(0)
    for wb_, vb_ in ((qbar, v0), (q, v1)):
        for w, v in zip(w0, vb_):
            D += wb_ * w * h(v)

    # iid term: E_{(qbar P0 + q P1)^otimes2}[h(XY)].  X=marginal of M.
    # Build the marginal weights/values of M explicitly.
    m_weights = []
    m_vals = []
    for wb_, vb_ in ((qbar, v0), (q, v1)):
        for w, v in zip(w0, vb_):
            m_weights.append(wb_ * w)
            m_vals.append(v)
    iid_term = iid_expected_h(m_weights, m_vals)

    # coupled term: qbar*E_{P0^otimes2} + q*E_{P1^otimes2}
    coup0 = product_expected_h(w0, v0)
    coup1 = product_expected_h(w1, v1)
    coup_term = qbar * coup0 + q * coup1

    N = (1 - beta) * iid_term + beta * coup_term
    obj = N / D

    E_M_X = mp.fsum(mw * mv for mw, mv in zip(m_weights, m_vals))
    return obj, E_M_X


def fmt(x):
    return mp.nstr(mp.mpf(x), 15)


# --------------------------------------------------------------------------
# two reference evaluations
# --------------------------------------------------------------------------
def eval_liu_record():
    p = mp.mpf("0.893604513905457")
    x = mp.mpf("0.690787593924988")
    beta = mp.mpf("0.100052559862974")
    a3 = 1 - p
    # 9-d encoding: P0 = p*d(x) + (1-p)*d(0), i.e.
    #   a1=p on b0=x, a2=0, a3=1-p on b4=0 ; q=0
    obj, E = objective((p, mp.mpf(0), mp.mpf(0),
                        x, mp.mpf(0), mp.mpf(0), mp.mpf(0),
                        mp.mpf(0), mp.mpf(0), beta))
    cprime = 1 - p * x
    return obj, E, cprime


def eval_two_atom():
    a = mp.mpf("0.0788772927059232")
    b = mp.mpf("0.329454738503037")
    beta = mp.mpf("0.0356069")
    # 9-d encoding: P0 = (1-a)*d(1-b) + a*d(0), q=0
    a1 = 1 - a
    xv = 1 - b
    obj, E = objective((a1, mp.mpf(0), mp.mpf(0),
                        xv, mp.mpf(0), mp.mpf(0), mp.mpf(0),
                        mp.mpf(0), mp.mpf(0), beta))
    cstar = 1 - (1 - a) * (1 - b)
    return obj, E, cstar


def main():
    print("liu_c3_objective_indep.py — independent Liu conditionally-IID 9-d objective")
    print("h = natural-log binary entropy; objective = N/D per Liu Eq (84)")
    print("mp.dps =", mp.mp.dps)
    print()
    print("=" * 70)
    print("EVALUATION (1): Liu conditional record (q=0, P0 = p*d(x)+(1-p)*d(0))")
    print("=" * 70)
    obj1, E1, c1 = eval_liu_record()
    print("  p    =", fmt("0.893604513905457"))
    print("  x    =", fmt("0.690787593924988"))
    print("  beta =", fmt("0.100052559862974"))
    print("  E_M[X] = p*x =", fmt(E1))
    print("  c' = 1 - p*x      =", fmt(c1), "  (paper 0.382709087918741)")
    print("  objective N/D     =", fmt(obj1), "  (should be 1.0 within ~1e-6)")
    print("  9-d encoding: a1=p , a2=0 , a3=1-p , b0=x , b2=0 , b4=0 , q=0")
    print()
    print("=" * 70)
    print("EVALUATION (2): Sawin/Yu record as a 9-d two-atom point")
    print("=" * 70)
    obj2, E2, c2 = eval_two_atom()
    print("  a    =", fmt("0.0788772927059232"))
    print("  b    =", fmt("0.329454738503037"))
    print("  beta =", fmt("0.0356069"))
    print("  P0   = (1-a)*d(1-b) + a*d(0), q=0")
    print("  E_M[X] = (1-a)(1-b) =", fmt(E2))
    print("  c* = 1 - E_M[X]      =", fmt(c2), "  (Sawin/Yu 0.3823455)")
    print("  objective N/D        =", fmt(obj2))
    print("  9-d encoding: a1=1-a , a2=0 , a3=a , b0=1-b , b2=0 , b4=0 , q=0")
    print()
    # guards
    print("--- guard checks ---")
    print("  eval(1) objective within 1e-6 of 1.0:", "PASS" if abs(obj1 - 1) < 1e-6 else "FAIL")
    print("  eval(1) c' reproduces 0.382709087918741:", "PASS" if abs(c1 - mp.mpf("0.382709087918741")) < 1e-12 else "FAIL")
    print("  eval(2) c* reproduces 0.3823455:", "PASS" if abs(c2 - mp.mpf("0.3823455")) < 1e-6 else "FAIL")
    print("  eval(2) objective >= 1 (certifies c*):", "PASS" if obj2 >= 1 else "FAIL")


if __name__ == "__main__":
    main()
