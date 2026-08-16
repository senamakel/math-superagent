#!/usr/bin/env python3
"""Map the autocorrelation boundary of the fold.

Two-state Markov chains in switch-density p with switching probability a are a
clean family of balanced, aperiodic, exponentially-decaying-autocorrelation
strings that interpolate between iid (a=p=0.5 -> zero centred autocorrelation)
and nearly-alternating (a close to 1 -> strongly anti-correlated). We locate
where the fold second moment E[S(n)^2]/(n-2) breaks (starts growing ~ n), i.e.
where density-1 SUPPLY stops holding.

The autocorrelation of a two-state Markov chain is rho(delta) = (1-2a)^delta.
So 'bounded autocorrelation of h with finite sum' corresponds to a away from 0.
Anticorrelation (a>0.5), i.e. negative (1-2a), is the regime that must be
priced: the primes have centred lag-1 autocorr ~ -0.04 (a ~ 0.52), so a is
RELEVANT. We find the largest negative correlation (smallest (2a-1)) under
which the fold still gives E[S^2]=O(n).
"""
import sys, random
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos


def markov_h(N, p, a, seed=3):
    """Two-state chain: state 1 with stationary prob p, switching prob a.
    a = P(flip from either state to the other). Autocorr (1-2a)^k."""
    random.seed(seed)
    # stationary dist: P(1) = p requires flip prob a and stay probs adjusted
    # we directly simulate: chain in {0,1}, P(next != cur) = a regardless.
    # stationary P(1)=1/2. For general p keep p=1/2 mostly; allow p too via:
    #   simpler: iid a gives zero autocorr; anti: alternate with prob a.
    out = []
    cur = random.randint(0, 1)
    for _ in range(N):
        out.append(cur)
        if random.random() < a:
            cur = 1 - cur
    return out


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 32768
    print(f"Two-state Markov chain (p=1/2), switching prob a, fold 2nd-moment ratio")
    print(f"prefix-mean of S^2/(n-2), n in [512,{N}] sampled, and whether it stays O(1).")
    print("a       autocorr_step   mean_ratio   max_ratio")
    for a in [0.50, 0.52, 0.54, 0.56, 0.58, 0.60, 0.63, 0.66, 0.70, 0.75, 0.80, 0.90, 0.95]:
        h = markov_h(N + 2, 0.5, a)
        s = 0.0
        mx = 0.0
        c = 0
        for n in range(512, N + 1, 256):
            S, _ = s_sos(n, h[:n])
            r = S * S / (n - 2)
            s += r
            mx = max(mx, r)
            c += 1
        print(f"{a:6.2f}   {1-2*a:14.3f}   {s/c:9.2f}   {mx:9.1f}")


if __name__ == "__main__":
    main()
