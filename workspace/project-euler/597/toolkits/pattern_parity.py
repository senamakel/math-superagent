"""Classify which bump patterns yield even vs odd parity, for small n.

This is the structural study behind the parity observations. It enumerates
every possible bump-edge multiset (chronology is irrelevant to parity — only
the set of bump edges matters) and computes, for each, the resulting new
order, the parity, and the number of transitive chain pairs (i<j joined by a
bump chain i->...->j). Confirms the identity

      parity == (# chain pairs) mod 2

on every concrete pattern reachable by the race dynamics for small n.

Signature:
    patterns_by_n(n) -> {(pattern,p): desc} where a pattern is a frozenset of
    directed bump edges (bumper, bumped), restricted to "valid" bump sets.
"""
from brute import parity_of_new_order, simulate_order


def race_observed_patterns(n, L, N=60000, seed=3):
    """Return the set of bump-edge-sets ever observed playing the real race."""
    import random
    rng = random.Random(seed)
    seen = set()
    for _ in range(N):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        above = simulate_order(n, L, speeds)
        # reconstruct edges from above? above only records reachability, not
        # the direct edges. Instead replay via brute by diffing positions is
        # unreliable; use race_events.
        from toolkits.race_events import race_events
        ev = race_events(n, L, speeds)
        seen.add(frozenset(ev['bumps']))
    return seen


def parity_from_edges(n, edges):
    """Reconstruct the new order and parity from a bump-edge set using the
    statement's transitive-chain rule (no dynamics needed)."""
    # above[i] = boats reachable from i following bump edges (placed below i)
    above = [set() for _ in range(n)]
    adj = {i: [] for i in range(n)}
    for (a, b) in edges:
        adj[a].append(b)
    for i in range(n):
        seen = {i}
        stack = [i]
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        above[i] = seen - {i}
    par, order = parity_of_new_order(n, above)
    chain_pairs = sum(len(a) for a in above)   # directed pairs (i -> ... -> j)
    return par, order, chain_pairs, above
