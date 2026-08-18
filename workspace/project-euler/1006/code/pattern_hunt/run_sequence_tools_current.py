from pathlib import Path


def values(path, limit=None):
    out=[]
    for line in Path(path).read_text().splitlines():
        parts=line.split()
        if not parts: continue
        if len(parts)==2 and parts[0].lstrip('-').isdigit() and parts[1].lstrip('-').isdigit():
            out.append(int(parts[1]))
        elif len(parts)==1 and parts[0].lstrip('-').isdigit():
            out.append(int(parts[0]))
        if limit and len(out)>=limit: break
    return out

for p in ['code/out/psi_exact.txt','code/out/psi_residues.txt','code/out/c1_terms.txt','code/out/lmin.txt','code/out/counts.txt']:
    print(p, values(p, 30))
