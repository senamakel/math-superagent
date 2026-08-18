from pathlib import Path

def read(path,col):
 return [int(x.split()[col]) for x in Path(path).read_text().splitlines() if x.strip()]
for fn,col in [('code/out/psi_exact.txt',0),('code/out/psi_residues.txt',0)]:
 a=read(fn,col); print(fn, a[:5], a[-3:])
# exact decimal Psi is first column; residue files are two-column index,value
for fn,col in [('code/out/psi_exact.txt',0),('code/out/psi_residues.txt',1),('code/out/c1_terms.txt',1),('code/out/lmin.txt',1),('code/out/dj_raw.txt',1)]:
 a=read(fn,col)
 print(fn, len(a), a[:8])
 d=[a[i+1]-a[i] for i in range(len(a)-1)]
 print('d=',d[:20])
