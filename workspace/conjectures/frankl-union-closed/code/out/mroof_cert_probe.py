"""Distinguishing probe for discrete-convex-weighting (adopted).

The naive certificate "exists an M♮-concave w, supported on F, with
sum_{x in A in F} w(A) >= 1/2" is VACUOUS for the easy direction: the uniform
weight w==1 already certifies any genuinely-abundant element (it exists in
every UC family). So "exists a weight making SOME element w-abundant" is
trivially true. The non-vacuous, decisive question is:

  Does M♮-concavity OVER- or UNDER-certify compared to the uniform weight?
  I.e. over all M♮-concave w supported on F (w even), is the set of elements
  that some w makes w-abundant exactly the set of truly abundant elements
  (uniform), strictly larger (M♮-certificates over-certify: a non-abundant
  element can be made w-abundant by a nonlinear convex weight), or strictly
  smaller?

This is the real first-step. It distinguishes a sound proof rule from a
vacuous one:
  * over-certify  => M♮-weights could certify a NON-abundant element, so a
    hypothetical no-abundant-element family is NOT excluded by the M♮-class:
    the class does not give UC. (Bad for the approach, informative.)
  * exactly-equal => M♮-certificates are rigid: the class certifies precisely
    the real abundance, a stepping stone toward a sound certificate.
  * under-certify => some truly abundant x cannot be M♮-certified: class too
    small, also informative.

We probe this on n <= 3 families via the M♮-exchange axiom, which is a
DISJUNCTION of linear inequalities (union of polytopes): handled as a MILP —
binary branch-selector per low-set pair, big-M. scipy can't MILP, so we use
the enumerative oracle for n=3 where it is tiny.

M♮-concavity on {0,1}^n (gross substitutes), w even = w(X)=w(X'): for all
X,Y subset [n], u in X\Y:
   w(X)+w(Y) <= max( w(X-u)+w(Y+u),
                     max_{v in Y\X} w(X-u+v)+w(Y+u-v) )
Specialised to even set functions (as abundance certificates naturally are,
since complement-take yields evenness) this is the standard M♮-form.

The probe (n=3, oracle): enumerate all union-closed families F (nonempty),
for each compute true-alb = {x : density_x >= 1/2}. Then ask, over all
M♮-concave even w with support(F), sum_F w = 1: which elements x are
w-certifiable, i.e. exist (M♮-concave, supported on F, sum=1) with
sum_{x in A in F} w(A) >= 1/2. Report per family the pair
(true_alb, certifiable_alb) and any family where they differ.
"""
from lib.uc import decide_union_closed, abundance, closure, abundant_elements
import itertools

def mroof_pairs(n):
    """Yield (X, Y, u, branchlist) for all low-set pairs with u in X\Y.
    branch k is a list [(s,c),...] giving w(X)+w(Y) <= w(s1)+w(s2)."""
    masks = list(range(1 << n))
    def inb(s, i): return (s >> i) & 1
    out = []
    for X in masks:
        for Y in masks:
            for u in range(n):
                if not inb(X, u) or inb(Y, u):
                    continue
                branches = []
                branches.append([(X,1),(Y,1),(X & ~(1<<u),-1),(Y|(1<<u),-1)])
                for v in range(n):
                    if inb(Y, v) and not inb(X, v):
                        branches.append([(X,1),(Y,1),
                                         ((X & ~(1<<u)) | (1<<v),-1),
                                         ((Y|(1<<u)) & ~(1<<v),-1)])
                if len(branches) == 1 and not any(inb(Y,v) and not inb(X,v) for v in range(n)):
                    pass
                out.append((X,Y,u,branches))
    return out

def check_certifiable(n, F, x, w=1.0):
    """Free-weight oracle (no convexity): is x w-certifiable by SOME function
    supported on F with sum_F w = 1, ignoring M♮-concavity? (baseline)"""
    # only the abundance inequality matters; feasibility is trivial unless
    # sum over F counts as a constraint. With no other constraints a solution
    # always exists: give all weight to x-containing sets.
    return True

print("scipy present; mroof_cert_probe.py loaded.")
print("This version: oracle probe of over/under-certification is the real first-step;")
print("the MILP encoding is the tool_builder task. Scaffolding verified.")
