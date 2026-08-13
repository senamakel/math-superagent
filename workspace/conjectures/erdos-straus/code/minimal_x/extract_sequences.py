"""Extract per-class sequences from open_class_minimal_x.json for the sequence tools.

For each open class r in {1,121,169,289,361,529} and k = 0..KMAX:
    n = 840*k + r, all n = 1 (mod 4) so n = 4m+1 with m = 210k + (r-1)/4,
    and minimal x satisfies x >= m+1.
Sequences per class:
    x(k)       minimal x
    e(k)       excess = x - (m+1) = x - (210k + (r+3)/4)
    y(k), z(k) accompanying minimal-x solution
Also the divisor parameter d(k) = 4x - n = 4e(k) + 3  (since 4x - n = 4(m+1+e) - (4m+1) = 4e+3).
"""
import json

rows = json.load(open('code/out/open_class_minimal_x.json'))['rows']
KMAX = json.load(open('code/out/open_class_minimal_x.json'))['KMAX']

by_r = {}
for row in rows:
    by_r.setdefault(row['r'], []).append(row)
for r, arr in by_r.items():
    arr.sort(key=lambda t: t['k'])

out = {}
for r in [1, 121, 169, 289, 361, 529]:
    arr = by_r[r]
    ks = [t['k'] for t in arr]
    assert ks == list(range(min(ks), KMAX + 1)), (r, ks[0], ks[-1], len(ks))
    m0 = (r - 1) // 4
    X = [t['x'] for t in arr]
    E = [t['x'] - (210 * t['k'] + m0 + 1) for t in arr]
    Y = [t['y'] for t in arr]
    Z = [t['z'] for t in arr]
    D = [4 * t['x'] - t['n'] for t in arr]
    out[r] = {'k0': ks[0], 'x': X, 'excess': E, 'd': D, 'y': Y, 'z': Z}
    print(f"r={r}: x(k) = {X}")
    print(f"r={r}: excess e(k) = {E}")
    print(f"r={r}: d(k)=4x-n = {D}")

json.dump(out, open('code/out/open_class_sequences.json', 'w'), indent=1)
print("\nsaved code/out/open_class_sequences.json")