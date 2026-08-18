from pathlib import Path
import re,math
p=Path(__file__).resolve().parents[1]/'out/r_runs_wythoff.txt'
for line in p.read_text().splitlines():
 ns=list(map(int,re.findall(r'-?\d+',line)))
 if len(ns)>30:
  starts=ns
  bad=[]
  for j,s in enumerate(starts,1):
   # exact floor(j*(3+sqrt(5))/2), with floor((3j+sqrt(5j^2))/2)
   want=(3*j+math.isqrt(5*j*j))//2
   if s!=want: bad.append((j,s,want));break
  print(f'starts={len(starts)} first_bad={bad[:1] or "none"}')
  print('gaps=',{d:sum(b-a==d for a,b in zip(starts,starts[1:])) for d in sorted(set(b-a for a,b in zip(starts,starts[1:])))})
  break
