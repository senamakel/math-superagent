import re

with open("out/psi_data_1_150.txt") as f:
    text = f.read()

lines = [l for l in text.splitlines() if "True" in l and ":" in l]
vals = []
for l in lines:
    # format: "  3 :  True : n= 5,|S|=  13 : 20302"
    parts = l.split(":")
    # last part is the value
    v = parts[-1].strip()
    k = int(parts[0].strip())
    vals.append((k, int(v)))

with open("out/psi_seq_1_150.txt", "w") as f:
    for k, v in vals:
        f.write(f"{k} {v}\n")

print("count:", len(vals))
print("terms (k, psi mod M):")
for k, v in vals:
    print(k, v % 101001001)
