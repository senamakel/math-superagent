"""Extract exact state sequences: N1(k), P1(k), S(k), vR value from structure.json."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "out", "structure.json")
def main():
    structure = json.load(open(DATA))
    ks = sorted(int(k) for k in structure)
    N1s=[]; P1s=[]; Ss=[]; vRs=[]
    for k in ks:
        d=structure[str(k)]
        N1s.append(d["N1"]); P1s.append(d["P1"]); Ss.append(sum(d["values"]))
        vRs.append(int(d["R"]))
    import json as j
    print("N1:", j.dumps(N1s))
    print("S:", j.dumps(Ss))
    print("P1:", j.dumps(P1s))
    print("vR(int):", j.dumps(vRs))
if __name__=="__main__":
    main()
