{
for(p_ = 1, 5,
  p = [83,911,2903,4871,18787][p_];
  idx = List();
  for(k=1, (p-3)\2,
    m = 2*k;
    if (numerator(bernfrac(m)) % p == 0, listput(idx, m));
  );
  print("p=", p, "  irregular=", #idx>0, "  indices=", Vec(idx));
)
}
