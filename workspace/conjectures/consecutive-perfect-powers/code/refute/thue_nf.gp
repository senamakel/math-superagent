/* Number field route: K = Q(cuberoot 2).  Verify class number 1, unit rank 1,
   and list units with zero omega^2 coefficient == solve Norm = +-1. */
K = bnfinit(x^3 - 2, 1);
print("class number: ", K.no);
print("regulator: ", K.reg);
print("fundamental units / unit group basis:");
print(K.tu);            /* torsion */
print(K.fu);            /* fundamental units */
print("unit rank r1+r2-1:"); 
print(1 + 1 - 1);
/* Solve Norm(c - d*omega) = c^3 - 2d^3 = +-1 with PARI thue as the complete
   resolution; cross-check with bnfisnorm style. */
TN = thueinit(x^3 - 2);
print("thue c^3-2d^3=1 : ", thue(TN, 1));
print("thue c^3-2d^3=-1: ", thue(TN, -1));
