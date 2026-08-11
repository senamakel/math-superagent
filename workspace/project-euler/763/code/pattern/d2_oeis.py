# Check d=2 D2(N) against OEIS A007902 (computed_agent values 0..21)
# A007902 terms (n=1..40 from the filed note): compare D2(n-1).
a007902 = [1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668,87426,
           202961,471150,1093819,2539348,5895408,13686805,31775756,73771474]
D2 = [1, 1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668,
      87426, 202961, 471150, 1093819, 2539348, 5895408, 13686805]
# D2(N) for N=0..21 has 22 terms; A007902(n) for n=1..22 should equal D2(n-1)
match = all(D2[i] == a007902[i] for i in range(len(D2)))
print("D2(N) == A007902(N+1) for N=0..21:", match)

# Growth ratio
for i in range(1, len(D2)):
    pass
print("\nLast ratios:", [round(D2[i]/D2[i-1],6) for i in range(len(D2)-4, len(D2))])
print("A007902 asymptotic d=2.3216 (Knessl 2006).")
