#!/usr/bin/env python3
"""High-precision parallel Monte Carlo for p(n,L) using the verified brute.py
engine. Each worker runs its own independent RNG stream and a contiguous chunk
of samples; results are pooled with the standard error of a binomial mean.

p_hat = mean of N Bernoulli draws (parity even). SE = sqrt(p(1-p)/N).

Usage:
    python3 high_precision_mc.py n L total_samples [chunk_per_worker]
separate ranges (n, L) by the total-samples argument; run per-(n,L) process.
"""
import multiprocessing as mp
import random
import sys
import time


def _worker(params):
    n, L, total, seed = params
    rng = random.Random(seed)
    even = 0
    for _ in range(total):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        # parity 0 == even
        if _engine(n, L, speeds) == 0:
            even += 1
    return even


_engine = None


def _init_engine(module_name):
    global _engine
    import importlib
    brute = importlib.import_module(module_name)
    _engine = brute.outcome_parity


def run(n, L, total_samples, chunk=None, seed0=12345):
    nprocs = mp.cpu_count()
    if chunk is None:
        chunk = 200000
    nchunks = (total_samples + chunk - 1) // chunk
    nprocs = min(nprocs, nchunks)
    pool = mp.Pool(nprocs, initializer=_init_engine, initargs=("brute",))
    jobs = []
    t0 = time.time()
    for i in range(nchunks):
        c = min(chunk, total_samples - i * chunk)
        jobs.append((n, L, c, seed0 + i))
    results = pool.map(_worker, jobs)
    pool.close(); pool.join()
    even = sum(results)
    N = sum(min(chunk, total_samples - i * chunk) for i in range(nchunks))
    p = even / N
    se = (p * (1 - p) / N) ** 0.5
    dt = time.time() - t0
    print(f"n={n} L={L}: N={N} even={even} p={p:.6f} SE={se:.6f} "
          f"({N/dt:.0f} samp/s, {dt:.1f}s, {nprocs} procs)")
    return p, se


if __name__ == "__main__":
    n = int(sys.argv[1]); L = float(sys.argv[2])
    total = int(sys.argv[3])
    run(n, L, total)
