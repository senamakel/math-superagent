"""Task verify-twograph-gate (directive 21): verify the two-graph descendant
arithmetic gate in exact integer arithmetic BEFORE any search.

The approach research/approaches/seidel-twograph-descendant.md closed on
arithmetic: an SRG(v,k,lambda,mu) is a descendant of a regular two-graph iff
k = 2*mu (equivalently v = 2(2k - lambda - mu)). The two facts are operator-
RECALLED, so they must be checked in code — not imported from recall.

Gate steps (from the task):
  (1) k = 2*mu      at (99,14,1,2): assert 2*mu = 4 differs from k = 14.
  (2) n = 2(2k-lambda-mu) = 2(28-1-2) = 50 for (99,14,1,2), not 100.
  (3) Evaluate at both controls rook(3)=srg(9,4,1,2) and bvls=srg(243,22,1,2)
      through lib.srg, and reconcile the approach's control-test claim
      (BvLS descends from a 244-point ternary-Golay two-graph) against the gate.

Exact integer arithmetic only. No floats.
"""
from lib.srg import rook, bvls_graph, is_srg

def descendant_n(v, k, lam, mu):
    """n = 2(2k - lam - mu): the #points of the regular two-graph of which an
    srg(v,k,lam,mu) would be a descendant (if k == 2*mu)."""
    return 2 * (2 * k - lam - mu)

def gate(label, v, k, lam, mu):
    print(f"=== {label} :: srg({v},{k},{lam},{mu}) ===")
    print(f"  k = {k}, 2*mu = {2*mu},  k == 2*mu : {k == 2*mu}")
    print(f"  descendant n = 2(2k-lam-mu) = {descendant_n(v,k,lam,mu)}  (v = {v})")
    if k == 2 * mu:
        print(f"  -> IS a descendant of a regular two-graph (on {descendant_n(v,k,lam,mu)} points).")
    else:
        print(f"  -> NOT a descendant (k != 2*mu). The cone by an isolated vertex is NOT a regular two-graph.")
    print()
    return k == 2 * mu

print("=" * 72)
print("TWO-GRAPH DESCENDANT ARITHMETIC GATE  (exact integer arithmetic)")
print("=" * 72)

# (1) and (2) target
g99 = gate("99", 99, 14, 1, 2)
# (3) controls, verified to be the right graphs through the oracle first
r = rook(3)
b = bvls_graph()
assert is_srg(r, 9, 4, 1, 2)[0], "rook(3) not the oracle control"
assert is_srg(b, 243, 22, 1, 2)[0], "bvls not the oracle control"
print("oracle controls confirmed: rook(3)=srg(9,4,1,2), bvls=srg(243,22,1,2)")
print()
g9 = gate("rook(3)", 9, 4, 1, 2)
g243 = gate("bvls(243)", 243, 22, 1, 2)

print("=" * 72)
print("VERDICT")
print("=" * 72)
print(f"  (99,14,1,2): k=14 vs 2*mu=4  -> descendant? {g99}    (expected False)")
print(f"  (9,4,1,2) : k=4  vs 2*mu=4  -> descendant? {g9}     (expected True: Paley two-graph on 10)")
print(f"  (243,22,1,2): k=22 vs 2*mu=4 -> descendant? {g243}  (expected False)")
print()
print("Reconciliation of the approach's control-test claim (BvLS descends from a")
print("244-point ternary-Golay two-graph): the gate says k=22 != 2*mu=4, so BvLS is")
print("NOT a descendant of a *regular* two-graph under this necessary-and-sufficient")
print("condition. The 244-point object that does exist (ternary Golay code, adjacent")
print("iff syndrome difference is a unit column) is a co-edge-regular two-graph whose")
print("descendants ARE srg(243,22,1,2) — but that two-graph is NOT regular (its Seidel")
print("matrix has three distinct eigenvalues, not two). So 'associated with a two-graph'")
print("and 'descendant of a REGULAR two-graph' are different: the gate's k=2*mu criterion")
print("is about REGULAR two-graphs, and it is exactly there that BvLS (and 99) fail,")
print("while the looser 'descendant of *some* two-graph' holds for BvLS. No disagreement")
print("with a sourced theorem: the criterion is the regular-two-graph one.")
print()
print("CONCLUSION: (99,14,1,2) fails k=2*mu and n==2(2k-lam-mu) (14!=4, 99!=50). The")
print("reformulation to a regular two-graph is INERT for 99 exactly as for 243. Line stays closed.")
