import math
# Side-by-side: at fixed phase (powers of 2, frac=1.0) compare residuals for E=0.5568 vs E=0.58496
data = [(256,16),(512,24),(1024,35),(2048,52),(4096,77),(8192,112),(16384,164),(32768,239),(65536,349)]
E1=0.5568; E2=math.log(3)/math.log(2)-1  # 0.58496
print("n        w   w/n^0.5568   w/n^0.58496")
print("-"*60)
for n,w in data:
    print(f"{n:6d} {w:4d}   {w/n**E1:8.4f}     {w/n**E2:8.4f}")

# residual RANGE at each phase for both exponents
def resid_range(E):
    vals=[w/n**E for n,w in data]
    return max(vals)-min(vals), min(vals), max(vals)
r1,mn1,mx1 = resid_range(E1)
r2,mn2,mx2 = resid_range(E2)
print()
print(f"E=0.5568:  w/n^E range [{mn1:.4f},{mx1:.4f}]  spread={r1:.4f}")
print(f"E=0.58496: w/n^E range [{mn2:.4f},{mx2:.4f}]  spread={r2:.4f}")
print()
print("VERDICT comment:")
print(" At fixed phase, E=0.5568 has bounded periodic residual (spread~0.024, no trend).")
print(" E=0.58496 monotone-DRIFTS downward (0.624->0.531), so it is ruled out as an exponent.")
