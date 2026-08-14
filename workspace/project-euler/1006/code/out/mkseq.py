lines = open('code/out/psi_data_1_150.txt').read().splitlines()
out = []
for line in lines:
    s = line.strip()
    if ' : ' not in s:
        continue
    parts = s.split(' : ')
    if not parts[0].strip().isdigit():
        continue
    out.append(parts[-1].strip())
with open('code/out/psi_seq.txt', 'w') as f:
    f.write('\n'.join(out) + '\n')
print(len(out))
print(out[0], out[2], out[9])
