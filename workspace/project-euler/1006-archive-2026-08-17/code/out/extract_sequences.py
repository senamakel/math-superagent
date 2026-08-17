"""Extract integer sequences from the state / psi data files for pattern analysis."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

def load_state():
    """Return dict k -> dict(N1,N0,P1_mod,vR_mod,S_mod) from psi_state_1_200.txt."""
    data = {}
    path = os.path.join(HERE, "psi_state_1_200.txt")
    with open(path) as f:
        header = f.readline()
        for line in f:
            parts = line.split(",")
            k = int(parts[0])
            data[k] = dict(
                S_mod=int(parts[1]),
                S_val=0,  # not available here
                N1=int(parts[2]),
                N0=int(parts[3]),
                P1_mod=int(parts[4]),
                vR_mod=int(parts[5]),
            )
    return data

def main():
    st = load_state()
    ks = sorted(st)
    print("k,S_mod,N1,N0,P1_mod,vR_mod")
    for k in ks:
        d = st[k]
        print(f"{k},{d['S_mod']},{d['N1']},{d['N0']},{d['P1_mod']},{d['vR_mod']}")

if __name__ == "__main__":
    main()
