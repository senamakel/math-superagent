"""Test the equivalence c(n)==0  <=>  digit_free(2^n)  exactly over a range,
where c(n) = number of base-3 carries when doubling 2^n to 2^(n+1).
Also report, for the digit-free powers, whether c(n)==0.
This is cheap and exact (mod-3 digit arithmetic), no big ints.
"""
def base3_digits(m):
    if m == 0:
        return [0]
    d = []
    while m:
        d.append(m % 3)
        m //= 3
    return d

def digit_free(n):
    m = 2 ** n
    if m == 0:
        return True
    while m:
        if m % 3 == 2:
            return False
        m //= 3
    return True

def carry_count(n):
    digs = base3_digits(2 ** n)
    carry_in = 0
    cnt = 0
    for d in digs:
        s = 2 * d + carry_in
        carry_in = s // 3
        if carry_in >= 1:
            cnt += 1
    if carry_in >= 1:
        cnt += 1
    return cnt

N = 3000
mismatch = []
zero_n = []
for n in range(0, N + 1):
    c = carry_count(n)
    df = digit_free(n)
    if df:
        zero_n.append((n, c))
    if (c == 0) != df:
        mismatch.append((n, c, df))

print(f"N={N}")
print("digit-free n and their carry-count:", zero_n)
print("mismatches (c==0) XOR digit_free:", mismatch[:30], "count", len(mismatch))
df_list = [n for n, c in zero_n]
print("digit-free n:", df_list)
