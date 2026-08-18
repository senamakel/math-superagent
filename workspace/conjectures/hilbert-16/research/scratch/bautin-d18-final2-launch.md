Bautin d=18 falsifier run launched 2026-08-18 ~10:47: pid 1645:
  nohup python code/bautin/membership_d18.py 18 > code/out/.d18_final2.tmp.txt 2>&1 &
Falsifier: a_18 (h=16) predicted 2392 by c(h)=(h^2+14h+8)/8; the d=18 monomial
count of L18, plus lex-Groebner membership L18 in <L4,L6,L8> (L10 re-check
same-run).
Earlier d18 runs in flight since ~10:12: pid 594 -> code/out/d18_final.captured.txt,
pid 711/713 -> code/out/d18_run.log; both at degree 15 as of 10:46.
Prior incomplete runs: d18v2 reached deg 15 (1131s), .d18.tmp.txt reached deg 17 (2130s).
Script code/bautin/membership_d18.py: exact sympy rational arithmetic, recurrence
degrees 3..18, gauge c_{k,0}=0, V2=(u^2+v^2)/2, Q1=A u^2+C u v+D v^2,
Q2=E u v+F v^2, rotation linear part.
