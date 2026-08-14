"""Diagnose where pattern_pass2 hangs: run each stage with timing."""
import numpy as np, time, sys

N = 200_000
t0 = time.time()
H = np.loadtxt("code/out/seq_H.txt", dtype=np.int64)
A = np.loadtxt("code/out/seq_A063985.txt", dtype=np.int64)
Phi = np.loadtxt("code/out/seq_Phi.txt", dtype=np.int64)
c = np.loadtxt("code/out/seq_cototient.txt", dtype=np.int64)
n = np.arange(1, N + 1, dtype=np.int64)
print("load:", time.time() - t0, flush=True)

t0 = time.time()
print("id H:", bool(np.array_equal(H, 3*n*(n+1) - 6*Phi)), time.time()-t0, flush=True)
print("dH:", bool(np.array_equal(np.diff(H, prepend=0), 6*c)), flush=True)
print("dA:", bool(np.array_equal(np.diff(A, prepend=0), c)), flush=True)

t0 = time.time()
spf = np.zeros(N + 1, dtype=np.int64)
for p in range(2, N + 1):
    if spf[p] == 0:
        spf[p::p] = p
print("spf:", time.time() - t0, flush=True)

t0 = time.time()
am = A % 2
viol = int(np.sum(am[1:N-4] != am[4:N-1]))
print("period4:", viol, time.time()-t0, flush=True)
pred = np.isin(n % 4, [1, 2])
print("A odd iff:", bool(np.array_equal((A % 2).astype(bool)[1:], pred[1:])), flush=True)

t0 = time.time()
predH = np.zeros(N, dtype=np.int64)
predH[1:] = 6 * (((n[1:] + 1) // 2) % 2)
print("H mod12 law:", bool(np.array_equal(H % 12, predH)), time.time()-t0, flush=True)

t0 = time.time()
periods = [p for p in range(1, 401) if np.array_equal(am[1:N-p-1], am[1+p:N-1])]
print("periods:", periods[:10], "...", time.time()-t0, flush=True)

t0 = time.time()
k = np.arange(1, N + 1, dtype=np.int64)
p0 = spf[1:]
m = k.copy()
active = np.ones(N, dtype=bool)
tval = np.zeros(N, dtype=np.int64)
for _ in range(20):
    with np.errstate(divide="ignore", invalid="ignore"):
        div = active & (m % p0 == 0)
        tval = tval + div
        m = np.where(div, m // p0, m)
        active = div
    if not active.any():
        break
print("valuation:", time.time() - t0, flush=True)

t0 = time.time()
is_pp = (p0 ** tval == k)
print("is_pp:", int(is_pp.sum()), time.time()-t0, flush=True)
