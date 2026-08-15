/* Complete resolution: c^3 - 2 d^3 = +-1.
   thueinit/tthue require a univariate binary form f(x) = c^3 - 2.
   The binary form P(c,d) = c^3 - 2 d^3 corresponds to f(x) = x^3 - 2.
   thue(f,a) lists ALL primitive integer solutions. */
TN = thueinit(x^3 - 2);
print("c^3-2d^3 =  1 : ", thue(TN, 1));
print("c^3-2d^3 = -1 : ", thue(TN, -1));
