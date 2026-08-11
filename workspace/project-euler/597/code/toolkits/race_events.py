"""Record the full bump/finish outcome of a PE 597 race.

Single callable that replays the exact chronological dynamics over iid
Exp(1) speeds (same engine family as toolkits.race_outcome) and returns a
complete description of what happened: the parity of the new order, every
bump edge, every finish, and the chain-inversion count.

Signature:
    race_events(n, L, speeds) -> dict with keys
        parity      int 0=even 1=odd
        bumps       list of (bumper, bumped) edges in chronological order
        finishes    list of boat indices that reached the finish line
        num_chains  int, number of pairs (i<j) joined by a bump chain
                    i->...->j (direct or transitive)
        order       list, new ascending listing (lowest place first)
"""
from brute import simulate_order, parity_of_new_order


def race_events(n, L, speeds):
    above = simulate_order(n, L, speeds)
    par, order = parity_of_new_order(n, above)
    # Bump edges and finishes are re-derived from the same dynamics; to keep
    # this independent of brute's internal state we recompute them via a
    # direct replay mirroring brute.simulate_order.
    state = [0] * n            # 0 ROWING, 1 FINISHED, 2 OUT
    pos = [40.0 * j for j in range(n)]
    bumps = []
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            vj = speeds[j]
            ft = (L - pos[j]) / vj
            k = None
            for kk in range(j + 1, n):
                if state[kk] == 0:
                    k = kk
                    break
            cands = [(ft, 'F', j, None)]
            if k is not None:
                vk = speeds[k]
                if vj > vk:
                    cands.append(((pos[k] - pos[j]) / (vj - vk), 'C', j, k))
            for c in cands:
                if c[0] == float('inf'):
                    continue
                if best is None or c[0] < best[0] - 1e-15:
                    best = c
        t, kind, j, k = best
        if kind == 'F':
            state[j] = 1
            pos[j] = L
        else:
            state[j] = 2
            pos[j] = pos[k]
            bumps.append((j, k))
    finishes = [j for j in range(n) if state[j] == 1]
    # chain count independent of the parity permutation: recompute above sets
    num_chains = sum(len(a) for a in above)
    return {
        'parity': par,
        'bumps': bumps,
        'finishes': finishes,
        'num_chains': num_chains,
        'order': order,
    }
