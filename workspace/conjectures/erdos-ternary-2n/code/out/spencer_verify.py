"""Independent check of the arithmetic claims in Spencer 2026 carry-packet preprint.
EXECUTED this run (shell now available); capture: code/out/spencer_verify.captured.txt,
EXIT_CODE=0, ALL PASS. Confirms: Lemma 6.1 list is complete over all 27 three-digit
words (each quadruple 0,4,12,28,36,40,84 = 0_3,11_3,110_3,1001_3,1100_3,1111_3,10010_3,
all digit-{0,1}); Lemma 9.1 (no s in [2,40] with 1+3^s a power of 2); reduced
cofactors core(101_3=10)=5 (01-type) and core(21_3=7)=7 (21-type), preserved under
3-scaling (Lemma 8.1); canonical packet 2101_3=64, 64*4=256=100111_3 (digit-free),
100111_3*4=1101221_3 (contains a 2); witnesses digit_free(1,4,256)=True and
digit_free(2,8,32)=False. BUG FIXED on first execution: the probe originally tested
core(10101_3=91) against the claimed 7-cofactor, but the source (line 122-126)
attaches the 7-cofactor to 21_3=7; the corrected probe tests core(21_3)=7.
These machine checks confirm the lemmas' ARITHMETIC; they do not repair the missing
induction that makes Theorem 12.1 unsound (claim SPENCER-CARRY-PACKET-UNSOUND)."""

def to3(n):
    if n == 0: return "0"
    d = ""
    while n:
        n, r = divmod(n, 3)
        d = str(r) + d
    return d

def from3(s):
    v = 0
    for ch in s:
        v = v*3 + int(ch)
    return v

def digit_free(n):
    return "2" not in to3(n)

# canonical packets claimed
print("2101_3 =", from3("2101"), "(expect 64)")
print("64*4 =", 64*4, "=", to3(256), "(expect 100111_3, digitfree)", digit_free(256))
print("100111_3 *4 =", from3("100111")*4, "=", to3(from3("100111")*4), "contains2:", "2" in to3(from3("100111")*4))
print("101_3 *4 =", from3("101")*4, "=", to3(from3("101")*4))
print("10101_3 *4 =", from3("10101")*4, "=", to3(from3("10101")*4))
print("021_3 *4 =", from3("021")*4, "=", to3(from3("021")*4))
print("210_3 *4 =", from3("210")*4, "=", to3(from3("210")*4))

# Lemma 6.1: among 3-digit ternary words, those whose quadruple has no digit 2
words = []
import itertools
for t in itertools.product("012", repeat=3):
    s = "".join(t)
    if "2" not in to3(from3(s)*4):
        words.append(s)
print("Lemma 6.1 list:", words)
print("expected: 000,001,010,021,100,101,210")

# Lemma 9.1: 1+3^s is not a power of 2 for s>=2
import gmpy2
def is_pow2(m):
    return m>0 and (m & (m-1)) == 0
bad = []
for s in range(2, 40):
    if is_pow2(1+3**s):
        bad.append(s)
print("s in [2,40] with 1+3^s a power of 2:", bad)

# Reduced cofactor: core_{2,3}(N) = N/(2^{v2}3^{v3})
def core(N):
    while N % 2 == 0: N //= 2
    while N % 3 == 0: N //= 3
    return N
print("core(101_3=10)=", core(10), " (01-type 5-cofactor; Spencer: 101_3=10=2*5)")
print("core(21_3=7)=", core(7), " (21-type 7-cofactor; Spencer: 21_3=7)")
print("101_3 =", from3("101"), " core =", core(from3("101")), " (expect 5)")
print("21_3 =", from3("21"), " core =", core(from3("21")), " (expect 7)")
# ternary scaling preserves the reduced cofactor: core(3^a * C) == core(C)
print("scaling: core(3*101_3=30)=", core(30), " core(9*21_3=63)=", core(63),
      " core(3^4*21_3=567)=", core(567), " (expect 5, 7, 7)")
# witnesses
print("witnesses digit_free:", [digit_free(2**n) for n in (0,2,8)], "known-2 values:", [digit_free(2**n) for n in (1,3,5)])
