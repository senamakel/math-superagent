from pathlib import Path
R=Path('code/out')
# Read run-position table from the actual two-column file if present.
for name in ['r_runs_wythoff.txt','vr_runvals.txt','vr_r_runs_wythoff.txt']:
 p=R/name
 if not p.exists(): continue
 a=[]
 for l in p.read_text().splitlines():
  z=l.split()
  try:
   if len(z)>=2:a.append((int(z[0]),int(z[1])))
  except:pass
 if not a: continue
 pos=[x[0] for x in a]
 gaps=[pos[i+1]-pos[i] for i in range(len(pos)-1)]
 print(name,'rows',len(a),'first',a[:8],'gaps',sorted(set(gaps)), 'gap-prefix',gaps[:30])
