"""Verify every equation claimed in the two source texts (Ponder This circle,
stewbasic n-gon) before writing the digest notes. All values from mpmath at
dps=50; each printed line is a check of a quoted source equation."""
import mpmath as mp

mp.mp.dps = 50

# ---------- 1. Circle (Ponder This May 2001) ----------
# cos(B) = 1/T ; sin(B) = (1/T)*(pi + B)  =>  tan(B) = pi + B,  T = 1/cos(B)
B = mp.findroot(lambda x: mp.tan(x) - (mp.pi + x), 1.35)
T = 1 / mp.cos(B)
print("B_circle      =", B, "(source: 1.3518168)")
print("T             =", T, "(oracle: 4.60333885)")
print("cosB*T-1      =", mp.cos(B) * T - 1, "-> 0 means cos(B)=1/T holds")
print("sinB*T-(pi+B) =", mp.sin(B) * T - (mp.pi + B), "-> 0 means sin(B)=(pi+B)/T holds")
print("tanB-(pi+B)   =", mp.tan(B) - (mp.pi + B), "-> 0 means tan(B)=pi+B holds")
# x = B + pi solves tan(x) = x (memory's alternative characterisation)
x = B + mp.pi
print("x=B+pi        =", x, "; tan(x)-x =", mp.tan(x) - x)
# stage radius R/v at swimmer speed 1 : angular speed check
R = mp.mpf(1)
v = T
rho = R / v          # stage radius
print("stage rho=R/v =", rho, "; swimmer ang.speed rho*1/rho vs runner v/R:",
      max(abs(1 / rho - v / R), 0))
# dash distance R*sin(B); runner arc R*(pi+B); equality of times at critical v
print("swim-chord R sinB =", R*mp.sin(B), "; runner arc R(pi+B) =", R*(mp.pi+B),
      "; ratio =", mp.sin(B)*v/(mp.pi+B), "(should be 1)")

# ---------- 2. stewbasic n-gon general formula ----------
def stewbasic(n):
    th = mp.pi / n
    t = mp.tan(th)
    K = None
    for k in range(0, n + 1):
        if mp.sin(k*th) - (k + n)*t*mp.cos(k*th) < 0:
            K = k
    # K is largest with the inequality < 0 (loop ends leaving the last good)
    inner = (mp.mpf(2)*mp.sin(K*th)) / ((K + n)*t) - mp.cos(K*th)
    al = (mp.mpf(1)/2) * (K*th + mp.acos(inner))
    lam = 1 / mp.cos(al)
    s = mp.cos(al) / mp.cos(al - K*th)
    return K, al, lam, s

for n in (3, 4, 6, 1000):
    K, al, lam, s = stewbasic(n)
    print(f"n={n}: K={K}  alpha={al}  V={lam}  s=cos a/cos(a-Kth)={s}")
print("n=4 V should equal 5.78859314; n=6 = 5.05505046; n=1000 -> 4.6033")

# hexagon detail (CONTEXT.md claims): K=2, alpha = 1/2(pi/3 + arccos(-1/8))
th = mp.pi/6
inner = (2*mp.sin(2*th)) / (8*mp.tan(th)) - mp.cos(2*th)
print("hexagon inner 2sin(Kth)/((K+n)t)-cos(Kth) =", inner, "(CONTEXT: -1/8)")
al6 = (mp.mpf(1)/2)*(mp.pi/3 + mp.acos(mp.mpf(-1)/8))
print("alpha_hexagon =", al6, " V =", 1/mp.cos(al6))
print("exact closed form 2+2*sqrt(21)/3 =", 2 + 2*mp.sqrt(21)/3)

# ---------- 3. David K square closed form (independent second route) ----------
V4_dk = mp.sqrt(mp.mpf(5)/2 * (7 + mp.sqrt(41)))
print("DavidK V_square =", V4_dk, "(oracle 5.78859314)")
tau_relation = 0  # d2 = v*d1 at limit per David K: v = sqrt(5/2(7+sqrt41))
print("cl