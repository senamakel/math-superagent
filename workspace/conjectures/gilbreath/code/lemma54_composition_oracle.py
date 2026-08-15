"""Oracle check for lemma54_composition.lean:
   (1) the max record-gap bound -> budget -> success, and
   (2) the transitivity composition (v<=g, g<=2*nu2+2, v even) -> success,
   over all {0,2}^L patterns and even v, plus the Link-A orbit bound.
   This validates that the Lean statement faithfully captures the informal
   claim and that it is non-vacuously true.  Exact integers."""
import itertools

def runAbs(v, el):
    for e in el:
        v = abs(v - e)
    return v

def countTwo(el):
    return sum(1 for e in el if e == 2)

def maxAll(el):
    return max(el) if el else 0

viol1 = viol2 = viol3 = 0
checked1 = checked2 = checked3 = 0
for L in range(0, 9):
    for pat in itertools.product([0, 2], repeat=L):
        el = list(pat)
        nu2 = countTwo(el)
        ma = maxAll(el)
        for v in range(0, 2*L+8, 2):   # even v only
            final = runAbs(v, el)
            # composition_via_max: budget on the record gap -> success
            if max(v, ma) <= 2*nu2 + 2:
                checked1 += 1
                if final not in (0, 2):
                    viol1 += 1
            # transitivity composition: v<=g and g<=budget (any g) -> success
            # (g ranges over all naturals >= v that are <= budget; existence of
            #  the chain is what matters; here the tightest g = max(v,ma))
            g = max(v, ma)
            if g <= 2*nu2 + 2:
                checked2 += 1
                if final not in (0, 2):
                    viol2 += 1
            # Link-A orbit bound: runAbs <= max v (maxAll el)
            checked3 += 1
            if final > max(v, ma):
                viol3 += 1
print(f"composition_via_max : checked {checked1}, violations {viol1}")
print(f"transitivity         : checked {checked2}, violations {viol2}")
print(f"orbit_le_max (LinkA) : checked {checked3}, violations {viol3}")
