rows = {}
with open("out/psi_state_1_200.txt") as f:
    header = f.readline()
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if len(parts) < 7:
            continue
        k = int(parts[0]); P = int(parts[1]); S = int(parts[2])
        N1 = int(parts[3]); N0 = int(parts[4]); P1 = int(parts[5]); vR = int(parts[6])
        rows[k] = dict(P=P, S=S, N1=N1, N0=N0, P1=P1, vR=vR)

# Print N1 sequence in compact form
n1 = [rows[k]["N1"] for k in sorted(rows)]
print("N1(1..200):", n1)
n0 = [rows[k]["N0"] for k in sorted(rows)]
print("N0(1..200):", n0)
print()
print("k : N1 : N1 mod-it-increments (delta N1) : delta")
prev = 0
deltas = []
for k in sorted(rows):
    d = n1[k-1] - prev
    deltas.append(d)
    prev = n1[k-1]
print("delta N1:", deltas)
