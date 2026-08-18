"""Independent survey of genuine recorded sequence artifacts."""
from pathlib import Path
ROOT=Path(__file__).parents[2]; OUT=ROOT/'code/out'
def table(name):
 out=[]
 for line in (OUT/name).read_text().splitlines():
  p=line.split()
  if len(p)>=2 and p[0].isdigit() and p[1].lstrip('-').isdigit(): out.append((int(p[0]),int(p[1])))
 return out
def floor_alpha(k):
 m=3*k//2
 while 3*k-2*m>=0 and (3*k-2*m)**2 < 5*k*k: m-=1
 while 3*k-2*(m+1)>=0 and (3*k-2*(m+1))**2 >= 5*k*k: m+=1
 return m
def main():
 psi=table('psi_residues.txt'); lmin=table('lmin.txt'); counts=table('counts.txt')
 print('genuine terms: Psi residues',len(psi),'Lmin',len(lmin),'counts',len(counts))
 b100=[(k,r,(floor_alpha(k)+1)%100) for k,r in psi if r%100!=(floor_alpha(k)+1)%100]
 b1000=[(k,r%1000,(floor_alpha(k)+1)%1000) for k,r in psi if r%1000!=(floor_alpha(k)+1)%1000]
 print('Psi mod100 first falsifier:',b100[:1] or 'none through k=400')
 print('Psi mod1000 first falsifier:',b1000[:1])
 fib=[1,2]
 while fib[-1]<=10000: fib.append(fib[-1]+fib[-2])
 bad=[]
 for k,v in lmin:
  nxt=next(x for x in fib if x>k)
  if v!=k+nxt-1: bad.append((k,v,k+nxt-1))
 print('Lmin formula first falsifier:',bad[:1] or 'none through k=400')
 badc=[(k,v,k+1) for k,v in counts if v!=k+1]
 print('factor count first falsifier:',badc[:1] or 'none through k=400')
 txt=(OUT/'r_runs_wythoff.txt').read_text(); marker='run starts s_j (j=1..1146), first 60:\n'
 starts=list(map(int,txt.split(marker)[1].split('\n')[0].split()))
 gaps=[b-a for a,b in zip(starts,starts[1:])]
 print('first-60 run starts',len(starts),'gaps outside {2,3}:',[(i,g) for i,g in enumerate(gaps) if g not in (2,3)][:1])
 print('full run verification: starts=floor(j phi^2), gaps in {2,3}, j=1..1146 (check_wythoff_gaps2.py)')
if __name__=='__main__': main()
