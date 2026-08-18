"""Requested pattern extension with correct table parsing and conventions."""
from decimal import Decimal,getcontext
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from lib.fibword import fib_prefix,next_fib
getcontext().prec=100
alpha=(Decimal(3)-Decimal(5).sqrt())/2
phi2=((Decimal(1)+Decimal(5).sqrt())/2)**2

def load(path):
 d={}
 for line in Path(path).read_text().splitlines():
  q=line.replace(',',' ').split(); nums=[int(x) for x in q if x.lstrip('-').isdigit()]
  if len(nums)>=2:d[nums[0]]=nums[-1]
 return d

def main():
 c=load('code/out/c1_terms.txt');p=load('code/out/psi_residues.txt')
 cb=next(((k,c[k],1+int(Decimal(k)*alpha)) for k in c if c[k]!=1+int(Decimal(k)*alpha)),None)
 # p values are residues, compare only modulo 100
 pb=next(((k,p[k]%100,c[k]%100) for k in p if p[k]%100!=c[k]%100),None)
 lb=None
 for k in range(1,401):
  pred=k+next_fib(k)-1;w=fib_prefix(pred)
  if len({w[i:i+k] for i in range(pred-k+1)})!=k+1:lb=(k,pred);break
 w=fib_prefix(10000);starts=[i for i in range(1,len(w)) if w[i-1:i+1]=='01']
 # Statement's floor(j phi^2) uses j=1 and positions counted from zero.
 rb=next(((j,x,int(Decimal(j)*phi2)) for j,x in enumerate(starts) if x!=int(Decimal(j)*phi2)),None)
 print('c1 range',min(c),max(c),'first falsifier',cb)
 print('Psi mod100 range',min(p),max(p),'first falsifier',pb)
 print('Lmin range 1..400 first falsifier',lb)
 print('V starts zero-based j=1..%d word=%d first falsifier=%r last=%d'%(len(starts),len(w),rb,starts[-1]))
 print('samples',[(k,c[k],p[k]%100,next_fib(k),k+next_fib(k)-1) for k in [1,2,3,5,8,13,21,34,55,89,144,233,377]])
if __name__=='__main__':main()
