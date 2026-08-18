from pathlib import Path
import re, math
ROOT=Path(__file__).resolve().parents[1]/'out'
def data(name):
    out=[]
    for line in (ROOT/name).read_text().splitlines():
        ns=list(map(int,re.findall(r'-?\d+',line)))
        if len(ns)>=2: out.append(ns)
    return out
for name in ['vr_rungaps.txt','r_runs_wythoff.txt']:
    rs=data(name); print(name, len(rs), rs[:3])
rs=data('r_runs_wythoff.txt')
# File has a header-like first row and then records; inspect rows whose first two fields are plausible index/start.
starts=[]
for r in rs:
    if len(r)>=2 and 1<=r[0]<=2000 and 1<=r[1]<=4000: starts.append((r[0],r[1]))
print('candidate pairs',starts[:5], 'count',len(starts))
for offset in range(1,4):
    bad=[]
    for j,(a,b) in enumerate(starts[offset-1:],1):
        s=b if a==j else a
        want=(3*j+math.isqrt(5*j*j))//2
        if s!=want: bad.append((j,a,b,want));break
    print('interpretation',offset,'first bad',bad[:1] or 'none')
