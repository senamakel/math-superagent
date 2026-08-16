import numpy as np

def fold(h):
    return np.array([h[i] ^ h[(i+1) % len(h)] for i in range(len(h))], dtype=int)

def wt(h):
    return int(h.sum())

def fourier_rhs(h, power):
    N = len(h)
    omega = np.arange(N) / N
    hh = np.fft.fft(h)
    mult = np.abs(1 + np.exp(2j*np.pi*omega)) ** (2*power)
    total = np.real(np.sum(mult * np.abs(hh)**2))
    return total / N

np.random.seed(1)
for N in [8, 16, 32]:
    h = np.random.randint(0, 2, N).astype(int)
    f1 = fold(h)
    hn = h.copy()
    for _ in range(3):
        hn = fold(hn)
    print(f"N={N}  wt(1+s h)={wt(f1):2d} ParsevalPow1={fourier_rhs(h,1):6.3f}  "
          f"wt(1+s)^3(h)={wt(hn):2d} ParsevalPow3={fourier_rhs(h,3):6.3f} ParsevalPow1(wrong)={fourier_rhs(h,1):6.3f}")
