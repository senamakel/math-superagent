#!/usr/bin/env python3
"""Extract exact passages from Elsholtz-Tao full text for the library notes."""
src = '/workspace/research/sources/pomerance-erdos-straus.full.md'
txt = open(src, encoding='utf-8').read()
out = []

def grab(label, start, stop, n=3000):
    i = txt.find(start)
    if i < 0:
        out.append(f"\n===== {label} =====\n[NOT FOUND {start[:70]!r}]")
        return
    j = txt.find(stop, i)
    if j < 0:
        j = min(len(txt), i + n)
    out.append(f"\n===== {label} =====\n{txt[i:j]}")

grab("Type-I/II general definition", "Type I", "Type II")
grab("Prop 1.6 (Vanishing)", "Proposition 1.6", "Remark 1.8")
grab("Prop 1.9 (Solvable congruences)", "Proposition 1.9", "Remark 1.10")
grab("Prop 2.2 (Description of Type I solutions)", "Proposition 2.2", "Proposition 2.3")
grab("Prop 2.6 (Description of Type II solutions)", "Proposition 2.6", "Proposition 2.7")

open('/workspace/code/out/et-excerpts.txt', 'w', encoding='utf-8').write('\n'.join(out))
print(len('\n'.join(out)), 'chars written')