rows = {}
with open("out/psi_state_1_200.txt") as f:
    header = f.readline()
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split(",")
        if len(parts) < 7: continue
        k = int(parts[0]); P = int(parts[1]); S = int(parts[2])
        N1 = int(parts[3]); N0 = int(parts[4]); P1 = int(parts[5]); vR = int(parts[6])
        rows[k] = dict(P=P, S=S, N1=N1, N0=N0, P1=P1, vR=vR)

ks = sorted(rows)
print("v_R mod M (1..200):")
print([rows[k]["vR"] for k in ks])
print()
print("P1 mod M (1..200):")
print([rows[k]["P1"] for k in ks])
print()
print("S (plain sum, 1..200):")
print([rows[k]["S"] for k in ks])
