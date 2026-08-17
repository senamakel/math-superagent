from fractions import Fraction

def S(k):
    return Fraction(4**(k-1)) * (Fraction(k) - Fraction(13,6)) + Fraction(2*k-1,3)

# Theorem to verify:  S_k is an integer  <=>  3 | k.
# Proof (exact integers only):
#   6 S_k = 4^{k-1}(6k - 13) + 2(2k-1) = 4^{k-1}(6k-13) + 4k - 2.
#   4^m mod 6:  4^0=1, 4^1=4, 4^2=16=4 -> for m>=1, 4^m = 4 mod 6.
#   Three cases mod 6:
#     m = k-1 = 0  (k=1):      6S = 1*(6-13) + 2 = -5 -> S = -5/6, not integer
#                                        (6·S ≡ 1·(-13) + 4·1 - 2 = -11 ≡ 1 mod 6? )
#     m >= 1:  6S ≡ 4*(6k-13) + 4k - 2 (mod 6)
#                     = 24k - 52 + 4k - 2 = 28k - 54 ≡ 28k ≡ 4k (mod 6)
#     so  6S ≡ 4k (mod 6);  if 3|k then 4k ≡ 0 → 6S ≡ 0 → S integer.
#     if 3 ∤ k then k ≡1,2 mod 3 → 4k ≡ 4, 2 ≠ 0 → 6S not ≡ 0 mod 6 → not integer.
# Verify against exact fractions over k=1..400 (and separately k=1 edge).
for k in range(1, 401):
    is_int = S(k).denominator == 1
    want = (k % 3 == 0)
    if is_int != want:
        print("MISMATCH at k =", k, S(k))
        break
else:
    print("Verified for k=1..400:  S_k integer  <=>  3 | k  (exact arithmetic).")

# And the guaranteed-count integer sequence at k ≡ 0 mod 3:
seq = [int(S(k)) for k in range(3, 45, 3)]
print("S_{3,6,9,...} (exact integers, k=3..42):")
print(seq)