"""Universal Euclidean (Chtholly / AtCoder floor_sum generalisation) monoid.

CONVENTION (1-INDEXED).  This module follows the 1-indexed convention of the
canonical fhq / LOJ138 / OI-wiki "universal Euclidean" (万能欧几里得)
templates: over the lattice path y = (p*t + q)/r for t = 1..n,
    dR = n                       (one R step per unit of t)
    dU = floor((p*n + q)/r)      (one U step per unit increase of floor(y))
    S0 = sum_{t=1}^{n} z^{t-1}                                   (mod M)
    S1 = sum_{t=1}^{n} z^{t-1} * floor((p*t+q)/r)                (mod M)
    S2 = sum_{t=1}^{n} z^{t-1} * floor((p*t+q)/r)^2              (mod M)

The t-th R step carries weight z^{t-1} (t = 1..n) and sits after
floor((p*t+q)/r) U's.  This is exactly the convention of OI-wiki
(f(a,b,c,n) = sum_{i=1}^n floor((ai+b)/c), "the number of U before the i-th
R equals floor((ai+b)/c), i = 1..n"), of fhq ("the x-th R has y =
floor((px+r)/q) U's before it"), and of LOJ138's recursion template, and it
is the convention the PE1006 Psi reduction uses.

For a 0-INDEXED sum (i = 0..n-1), use the wrapper ue0(p, q, r, n, z) below:
it returns the same ueuclid node but with S1 = sum_{i=0}^{n-1} z^i *
floor((p*i+q)/r), S2 likewise, via floor((p*i+q)/r) =
floor((p*(i+1) + (q-p))/r), so ue0(p,q,r,n,z) calls ueuclid with intercept
q-p: putting t = i+1 (the 1-indexed variable), floor((p*t + (q-p))/r) equals
floor((p*i + q)/r).
(When p > q the intermediate intercept q-p is lifted by the smallest k*r
with k = ceil((p-q)/r) >= 0 and the k shift is undone on S1/S2/dU.)

where z is a geometric ratio taken mod M.  This is the monoid of directive 4
(universal-Euclidean second-moment primitive) that turns Psi(10^18) for PE1006
into an O(log n) evaluation instead of enumerating n terms.

Node = (dR, dU, w, S0, S1, S2), all integers mod M (dR, dU as plain ints;
w = z^dR).  Compose(left, right) is the directive-4 rule:
    dR = l.dR + r.dR
    dU = l.dU + r.dU
    w  = l.w * r.w
    S0 = l.S0 + l.w * r.S0
    S1 = l.S1 + l.w * (r.S1 + l.dU * r.S0)
    S2 = l.S2 + l.w * (r.S2 + 2*l.dU*r.S1 + l.dU^2*r.S0)
Identity: all zeros with w = 1.  The dU shift carries floor values across a
segment boundary -- the one place this primitive goes wrong, so it is tested
hard below against a direct loop.

Two independent implementations share one interface so each can check the other:
  - ueuclid_direct(p, q, r, n, z):  O(n) literal loop (the oracle), 1-indexed.
  - ueuclid(p, q, r, n, z):         O(log) Euclidean split, the real primitive.
  - ue0(p, q, r, n, z):              0-indexed wrapper (i = 0..n-1).

Mapping to the canonical sources on disk:
  fhq_treap 6-component monoid  (research/sources/universal-euclidean-geometric-weight-fhq.full.md)
  LOJ138 recursive split        (research/sources/loj138-universal-euclidean-floor-moments.full.md)
  OI-wiki universal Euclidean   (research/sources/oi-wiki-universal-euclidean-floor-sum.full.md)
by composing U = (0,1,1,0,0,0) and R = (1,0,z,1,0,0) steps with the recursion
  m = floor((p*n+r)/q);
  if m == 0:              return R^n
  if p >= q:              solve(p%q, q, r, n, U, U^{p//q} * R)
  else: return R^{(q-r-1)//p} * U * solve(q, p, (q-r-1)%p, m-1, R, U) * R^{cnt}
where cnt = n - (q*m - r - 1)//p, and the caller prepends floor(r/q) leading U's.
"""
from __future__ import annotations
from typing import NamedTuple

# PE1006 modulus.
M = 101001001


class Node(NamedTuple):
    dR: int
    dU: int
    w: int      # z^dR mod M
    S0: int     # sum z^(t-1)      (1-indexed, t = 1..n)
    S1: int     # sum z^(t-1) * floor((p*t+q)/r)
    S2: int     # sum z^(t-1) * floor((p*t+q)/r)^2

    def __str__(self) -> str:
        return (f"Node(dR={self.dR}, dU={self.dU}, w={self.w}, "
                f"S0={self.S0}, S1={self.S1}, S2={self.S2})")


IDENTITY = Node(dR=0, dU=0, w=1, S0=0, S1=0, S2=0)


def compose(l: Node, r: Node) -> Node:
    """Directive-4 composition: segment l followed by segment r."""
    dU = l.dU + r.dU
    dR = l.dR + r.dR
    w = (l.w * r.w) % M
    S0 = (l.S0 + l.w * r.S0) % M
    S1 = (l.S1 + l.w * (r.S1 + l.dU * r.S0)) % M
    S2 = (l.S2 + l.w * (r.S2 + 2 * l.dU * r.S1 + l.dU * l.dU * r.S0)) % M
    return Node(dR=dR, dU=dU, w=w, S0=S0, S1=S1, S2=S2)


def _pow(node: Node, k: int) -> Node:
    """node composed with itself k times (monoid power)."""
    res = IDENTITY
    while k:
        if k & 1:
            res = compose(res, node)
        node = compose(node, node)
        k >>= 1
    return res


def step_R(z: int) -> Node:
    return Node(dR=1, dU=0, w=z % M, S0=1, S1=0, S2=0)


def step_U() -> Node:
    return Node(dR=0, dU=1, w=1, S0=0, S1=0, S2=0)


# ---------------------------------------------------------------------------
# O(n) direct loop -- the oracle that ueuclid must agree with.
# ---------------------------------------------------------------------------

def ueuclid_direct(p: int, q: int, r: int, n: int, z: int) -> Node:
    """Literal loop, 1-INDEXED (t = 1..n), matching the O(log) ueuclid:
    one R step per t, floor((p*t+q)/r) U's before the t-th R, weight z^{t-1}.

    S0 = sum_{t=1}^n z^{t-1}, S1 = sum_{t=1}^n z^{t-1} * floor((p*t+q)/r),
    S2 = sum_{t=1}^n z^{t-1} * floor((p*t+q)/r)^2.
    """
    dR = n
    dU = (p * n + q) // r
    S0 = S1 = S2 = 0
    zp = 1  # z^(t-1), t = 1..n
    z = z % M
    for t in range(1, n + 1):
        fl = (p * t + q) // r
        S0 = (S0 + zp) % M
        S1 = (S1 + zp * (fl % M)) % M
        S2 = (S2 + zp * (fl % M) * (fl % M)) % M
        zp = (zp * z) % M
    w = pow(z, dR, M)
    return Node(dR=dR, dU=dU, w=w, S0=S0, S1=S1, S2=S2)


def ue0(p: int, q: int, r: int, n: int, z: int) -> Node:
    """0-INDEXED wrapper: sums over i = 0..n-1 at weight z^i.

    S0 = sum_{i=0}^{n-1} z^i, S1 = sum_{i=0}^{n-1} z^i * floor((p*i+q)/r),
    S2 likewise; dR = n, dU = floor((p*(n-1)+q)/r) (total U count of the
    0-indexed path), w = z^n.

    Identity used: floor((p*i + q)/r) = floor((p*(i+1) + (q-p))/r), so the
    0-indexed sum equals the 1-indexed ueuclid called with intercept q - p.
    When q - p < 0 the intercept is lifted to q2 = q - p + k*r >= 0 with
    k = ceil((p-q)/r), i.e. floor((p*t + (q-p))/r) = floor((p*t + q2)/r) - k
    for every t.  The intermediate node carries the g_t = f_t + k floors, so
    its moments are undone to the target (f_t = g_t - k):
        S1 = node.S1 - k*S0,  S2 = node.S2 - 2k*node.S1 + k^2*S0,
        dU = node.dU - k.
    Requires q >= 0 (all 0-indexed path floors nonnegative).
    """
    if n == 0:
        return IDENTITY
    if q < 0:
        raise ValueError("ue0 requires q >= 0 (0-indexed floors nonnegative)")
    k = 0 if p <= q else (p - q + r - 1) // r  # ceil((p-q)/r), 0 if p <= q
    q2 = q - p + k * r
    node = ueuclid(p, q2, r, n, z)  # 1-indexed, nonnegative intercept
    if k == 0:
        return Node(dR=node.dR, dU=node.dU, w=node.w,
                    S0=node.S0, S1=node.S1, S2=node.S2)
    S0 = node.S0
    S1 = (node.S1 - k * S0) % M
    S2 = (node.S2 - 2 * k * node.S1 + k * k * S0) % M
    dU = node.dU - k
    return Node(dR=node.dR, dU=dU, w=node.w, S0=S0, S1=S1, S2=S2)


# ---------------------------------------------------------------------------
# O(log) Euclidean recursion -- the real primitive.
# ---------------------------------------------------------------------------

def _solve(p: int, q: int, r: int, n: int, a: Node, b: Node) -> Node:
    """Composed node for the path U^{floor((p*t+q)/r)} R_t, t = 1..n
    (1-indexed: the t-th R sits after floor((p*t+q)/r) U's).

    a = U-type step, b = R-type step (b carries weight z^(t-1) via step_R).
    This mirrors the fhq / LOJ138 solve() recursion.
    """
    if n == 0:
        return IDENTITY
    if p >= q:
        # floor((p i + r)/q) = floor(p/q) + floor(((p%q) i + r)/q):
        # fold the p//q leading U's into the base.
        return _solve(p % q, q, r, n, a, compose(_pow(a, p // q), b))
    m = (p * n + r) // q
    if m == 0:
        return _pow(b, n)
    # cnt = n - floor((q*m - r - 1)/p)  (number of trailing R's after the
    # swapped segment); leading R-block has (q-r-1)//p R's.
    cnt = n - (q * m - r - 1) // p
    return compose(
        _pow(b, (q - r - 1) // p),
        compose(
            a,
            compose(_solve(q, p, (q - r - 1) % p, m - 1, b, a),
                    _pow(b, cnt))))


def ueuclid(p: int, q: int, r: int, n: int, z: int) -> Node:
    """O(log) evaluation of the S0/S1/S2 monoid for y=(p*t+q)/r, t=1..n
    (1-INDEXED; see module docstring).  Matches ueuclid_direct.

    Requires r > 0, n >= 0.  Matches ueuclid_direct.
    """
    if n == 0:
        return IDENTITY
    # floor((p i + q)/r) = floor(q/r) + floor(((q mod r) ... )); prepend the
    # leading floor(q/r) U's (fhq main: pow(nu, r/q) + solve(p,q,r%q,...)).
    leading_u = q // r
    U = step_U()
    R = step_R(z)
    inner = _solve(p, r, q % r, n, U, R)
    return compose(_pow(U, leading_u), inner)


# ---------------------------------------------------------------------------
# Independent plain loop (floor_sum at z=1 style) as a tertiary check.
# ---------------------------------------------------------------------------

def floor_sum_plain(p: int, q: int, r: int, n: int) -> int:
    """sum_{t=1}^{n} floor((p*t+q)/r), plain integers (unweighted),
    1-indexed to match ueuclid's convention."""
    return sum((p * t + q) // r for t in range(1, n + 1))


if __name__ == "__main__":
    import random
    random.seed(1006)

    print(f"Modulus M = {M}")
    print("=" * 70)

    n_fail = 0
    trials = 30
    print(f"\nAcceptance tests 1-3: {trials} random (p,q,r,n,z), "
          f"ueuclid vs ueuclid_direct vs plain loop "
          f"(1-indexed: t=1..n, weight z^(t-1))")
    for _ in range(trials):
        p = random.randint(1, 1_000_000)
        q = random.randint(0, 1_000_000)
        r = random.randint(1, 1_000_000)
        n = random.randint(1, 3000)
        z = random.randint(0, M - 1)

        a = ueuclid(p, q, r, n, z)
        b = ueuclid_direct(p, q, r, n, z)

        ok = (a.dR == b.dR == n
              and a.dU == b.dU == (p * n + q) // r
              and a.S0 == b.S0 and a.S1 == b.S1 and a.S2 == b.S2
              and a.w == pow(z % M, n, M))
        if not ok:
            n_fail += 1
            print(f"FAIL p={p} q={q} r={r} n={n} z={z}")
            print(f"  log   : {a}")
            print(f"  direct: {b}")

        # Acceptance test 2 shown separately below: S1 at z == 1 must equal
        # the unweighted floor sum.

    print(f"\nacceptance 1-3 (random): {trials - n_fail}/{trials} trials passed")

    # Acceptance test 2: S1 at z == 1 versus the plain (unweighted)
    # floor_sum sum_{t=1}^n floor((p*t+q)/r), over the same random parameters.
    nz = 0
    for _ in range(trials):
        p = random.randint(1, 1_000_000)
        q = random.randint(0, 1_000_000)
        r = random.randint(1, 1_000_000)
        n = random.randint(1, 3000)
        c = ueuclid(p, q, r, n, 1)
        plain = floor_sum_plain(p, q, r, n) % M
        if c.S1 != plain:
            nz += 1
            print(f"FAIL floor_sum z=1 S1 p={p} q={q} r={r} n={n}: "
                  f"{c.S1} != {plain}")
    print(f"acceptance 2 (S1 at z=1 vs floor_sum): {trials - nz}/{trials} passed")
    n_fail += nz

    # Deterministic small-case cross-check including the leading-U and
    # boundary (m == 0, p >= q) cases.
    print("\nDeterministic cases:")
    det = [(1, 0, 1, 5, 3), (7, 2, 3, 10, 3), (3, 5, 7, 12, 3),
           (1000, 3, 1346269, 20, 3), (2, 1, 1, 6, 3), (1, 1, 2, 4, 2)]
    for (p, q, r, n, z) in det:
        a = ueuclid(p, q, r, n, z)
        b = ueuclid_direct(p, q, r, n, z)
        match = (a.dR == n and a.dU == (p * n + q) // r
                 and a.S0 == b.S0 and a.S1 == b.S1 and a.S2 == b.S2
                 and a.w == pow(z % M, n, M))
        status = "ok" if match else "MISMATCH"
        if not match:
            n_fail += 1
        print(f"  ({p},{q},{r},{n},z={z}) {status}: "
              f"dU={a.dU} S0={a.S0} S1={a.S1} S2={a.S2}")

    if n_fail == 0:
        print("\nALL MONOID TESTS PASSED (ueuclid == ueuclid_direct on every trial)")
    else:
        print(f"\n{n_fail} FAILURES -- do not trust ueuclid yet")

    # ue0: verify the 0-indexed wrapper against an independent 0-indexed
    # direct loop (S1 = sum_{i=0}^{n-1} z^i * floor((p*i+q)/r)).
    nz0 = 0
    print(f"\nue0 acceptance: {trials} random (p,q,r,n,z) vs 0-indexed direct "
          f"(i=0..n-1)")
    for _ in range(trials):
        p = random.randint(1, 1_000_000)
        q = random.randint(0, 1_000_000)
        r = random.randint(1, 1_000_000)
        n = random.randint(1, 3000)
        z = random.randint(0, M - 1)
        a = ue0(p, q, r, n, z)
        # independent 0-indexed loop
        zz = z % M
        S0 = S1 = S2 = 0
        zp = 1
        for i in range(n):
            fl = (p * i + q) // r
            S0 = (S0 + zp) % M
            S1 = (S1 + zp * (fl % M)) % M
            S2 = (S2 + zp * (fl % M) * (fl % M)) % M
            zp = (zp * zz) % M
        ok0 = (a.dR == n and a.S0 == S0 and a.S1 == S1 and a.S2 == S2
               and a.w == pow(zz, n, M)
               and a.dU == (p * (n - 1) + q) // r)
        if not ok0:
            nz0 += 1
            print(f"FAIL ue0 p={p} q={q} r={r} n={n} z={z}: {a} "
                  f"vs ({S0},{S1},{S2})")
    print(f"ue0 acceptance (vs 0-indexed direct): "
          f"{trials - nz0}/{trials} passed")
    if nz0:
        n_fail += nz0

    # Large-n sanity: O(log) must return instantly and consistently.
    import time
    t0 = time.time()
    big = ueuclid(514229, 3, 1346269, 10**18, pow(10, -1, M))
    dt = (time.time() - t0) * 1000
    print(f"\nlarge-n sanity: ueuclid(514229,3,1346269,10^18,10^-1) "
          f"in {dt:.3f} ms")
    print(f"  {big}")
    print(f"  dR==10^18: {big.dR == 10**18}, "
          f"dU==(p*n+q)//r: {big.dU == (514229*10**18 + 3)//1346269}")
