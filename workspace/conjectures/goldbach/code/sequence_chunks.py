from pathlib import Path
for name in ['seq_rn_50000.txt','seq_gn.txt']:
 a=[int(x) for x in Path('code/out/'+name).read_text().split()]
 for i in range(0,len(a),512):
  b=a[i:i+512]
  print(name,i+1,i+len(b),b[:6],b[-6:])
