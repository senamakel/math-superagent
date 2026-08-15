#!/usr/bin/env python3
"""Benchmark the throughput of the n=11 kernel filter.

Streams geng 11 -d4 and runs graph6_to_edges + check_kernel on every graph,
timing how many graphs/second pure Python can process, and how many kernel
members are found in a bounded prefix. Extrapolates to the full 187M.
"""
import subprocess, time, sys
sys.path.insert(0, "/workspace/code")
from census_kernel import graph6_to_edges, check_kernel

n = 11
cmd = ["nauty-geng", str(n), "-d4"]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        text=True, bufsize=1)

LIMIT = 3_000_000
start = time.time()
count = 0
members = 0
try:
    for ln in proc.stdout:
        ln = ln.rstrip("\n")
        if not ln or ln[0] in ">#":
            continue
        m, edges = graph6_to_edges(ln)
        ok, reason = check_kernel(n, edges)
        count += 1
        if ok:
            members += 1
        if count >= LIMIT:
            break
finally:
    proc.kill()

el = time.time() - start
rate = count / el
print(f"processed {count} graphs in {el:.1f}s, rate={rate:.0f} graphs/s")
print(f"kernel members in prefix: {members}")
print(f"projected full 187095840 graphs at {rate:.0f}/s: {187095840/rate:.0f}s")
