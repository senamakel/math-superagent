from pathlib import Path
R=Path('code/out')
def rows(name):
 out=[]
 for l in (R/name).read_text().splitlines():
  z=l.split()
  if len(z)>=2:
   try:out.append(tuple(map(int,z)))
   except:pass
 return out
for name in ['dj_raw.txt','dj_mod.txt','vr_runvals.txt','vr_r_runs_wythoff.txt']:
 p=R/name
 if not p.exists():continue
 a=rows(name);print(name,'rows',len(a),'first',a[:5])
 print('last',a[-3:])
 print('widths',sorted(set(map(len,a))))
