<!-- source: https://thelig.ht/petalnumbers/part2.html | converted from HTML -->

The Number Hiding Inside the Spirograph MathJax = { loader: {load: ['output/svg', 'input/tex']}, tex: { tags: 'ams', } }; -->

# The Number Hiding Inside the Spirograph Part 2

*For more introduction into the problem and a derivation of the Petal Numbers for finite values of b see [Part 1][1].*

After the I published the first article about the Petal Numbers, I received two interesting responses on Reddit. Reddit user *[existentialpenguin][2]*commented that he did a search for the approximate form of p as b → ∞ (`4.603338`) in the OEIS and found [an entry][3] that matched very closely. That entry lists that it is the solution of ( arccos ( 1 p) + π) 2 + 1 = p 2, derived from a different problem completely. Reddit user *[BruhcamoleNibberDick][4]*then sketched out a derivation of p resulting in the same equation, which would in theory prove the two numbers are equal.

In this article we'll go over a derivation of p inspired by *BruhcamoleNibberDick*'s comment, prove that p is indeed transcendental, and finally we'll provide an efficient method to compute p.

## Deriving p as b → ∞

From Part 1 recall the spirograph function and its derivative:

s ( θ) = p e − i b θ + b e i θ d s d θ ( θ) = − i b p e − i b θ + i b e i θ

We want to constrain these equations to the points where the petals of the spirograph are tangent:

[image: The spirograph when all petals are tengent to each other]

The critical thing to observe is that at the points of tangency, θ = ω, both the position and velocity vectors are parallel. This means that the tangent of their arguments (i.e. angle) are equal:

tan ( arg ( s ( ω))) = tan ( arg ( d s d θ ( ω))) tan ( arctan ( I m ( s ( ω)) R e ( s ( ω)))) = tan ( arctan ( I m ( d s d θ ( ω)) R e ( d s d θ ( ω)))) I m ( s ( ω)) R e ( s ( ω)) = I m ( d s d θ ( ω)) R e ( d s d θ ( ω)) I m ( s ( ω)) ⋅ R e ( d s d θ ( ω)) = I m ( d s d θ ( ω)) ⋅ R e ( s ( ω)) (1)

For the sake of space, let's simplify each side separately. First the left side:

I m ( s ( ω)) ⋅ R e ( d s d θ ( ω)) I m ( p e − i b ω + b e i ω) ⋅ R e ( − i b p e − i b ω + i b e i ω) ( p sin ( − b ω) + b sin ω) ⋅ R e ( − b p e i ( π 2 − b ω) + b e i ( π 2 + ω)) ( − p sin ( b ω) + b sin ω) ⋅ ( − b p cos ( π 2 − b ω) + b cos ( π 2 + ω)) ( − p sin ( b ω) + b sin ω) ⋅ ( − b p sin ( b ω) − b sin ω) b p 2 sin 2 ( b ω) + b p sin ( b ω) sin ω − b 2 p sin ω sin ( b ω) − b 2 sin 2 ω b p 2 sin 2 ( b ω) + ( 1 − b) b p sin ( b ω) sin ω − b 2 sin 2 ω (2)

Now let's simplify the right side of (1):

I m ( d s d θ ( ω)) ⋅ R e ( s ( ω)) I m ( − i b p e − i b ω + i b e i ω) ⋅ R e ( p e − i b ω + b e i ω) I m ( − b p e i ( π 2 − b ω) + b e i ( i 2 + ω)) ⋅ ( p cos ( − b ω) + b cos ω) ( − b p sin ( π 2 − b ω) + b sin ( π 2 + ω)) ⋅ ( p cos ( b ω) + b cos ω) ( − b p cos ( b ω) + b cos ω) ⋅ ( p cos ( b ω) + b cos ω) − b p 2 cos 2 ( b ω) − b 2 p cos ( b ω) cos ω + b p cos ω cos ( b ω) + b 2 cos 2 ω − b p 2 cos 2 ( b ω) + ( 1 − b) b p cos ( b ω) cos ω + b 2 cos 2 ω (3)

Now equate (3) and (2) per (1). Group sin 2 ω + cos 2 ω terms:

b p 2 sin 2 ( b ω) + ( 1 − b) b p sin ( b ω) sin ω − b 2 sin 2 ω = − b p 2 cos 2 ( b ω) + ( 1 − b) b p cos ( b ω) cos ω + b 2 cos 2 ω b p 2 sin 2 ( b ω) + b p 2 cos 2 ( b ω) − b 2 sin 2 ω − b 2 cos 2 ω = ( 1 − b) b p cos ( b ω) cos ω − ( 1 − b) b p sin ( b ω) sin ω b p 2 − b 2 = ( 1 − b) b p ⋅ ( cos ( b ω) cos ω − sin ( b ω) sin ω)

Replace cos ( b ω) cos ω with cos ( ( b + 1) ω) + sin ( b ω) sin ω per cosine angle sum formula:

b ⋅ ( p 2 − b) = ( 1 − b) b p ⋅ ( ( cos ( ( b + 1) ω) + sin ( b ω) sin ω) − sin ( b ω) sin ω) ( p 2 − b) = ( 1 − b) p cos ( ( b + 1) ω) ( p 2 − b) ( 1 − b) p = cos ( ( b + 1) ω) (4)

With (4) we have an expression that puts ω in terms of b and p. Since we are interested in solving for p as b → ∞, let's take the limit. Important to note that we assume p exists as b → ∞ during these steps:

lim b → ∞ cos ( ( b + 1) ω) = lim b → ∞ ( p 2 − b) ( 1 − b) p lim b → ∞ cos ( ( b + 1) ω) = lim b → ∞ ( p 2 ( 1 − b) p − b ( 1 − b) p) lim b → ∞ cos ( ( b + 1) ω) = lim b → ∞ p ( 1 − b) + lim b → ∞ b ( b − 1) p lim b → ∞ cos ( ( b + 1) ω) = 1 p lim b → ∞ ( b + 1) ω = arccos ( 1 p) lim b → ∞ ω = lim b → ∞ arccos ( 1 p) b + 1 (5)

Since we have assumed that p exists as b → ∞ it should be clear that lim b → ∞ ω = 0 but we keep it in this form because it will be necessary to evaluate another limit.

The second major thing to observe is that at the points of tangency, π n ( b + 1) = arg ( s ( ω)), where n ∈ Z:

π n ( b + 1) = arg ( s ( ω)) π n ( b + 1) = arctan ( I m ( s ( ω)) R e ( s ( ω))) tan ( π n ( b + 1)) = I m ( s ( ω)) R e ( s ( ω)) tan ( π n ( b + 1)) = I m ( p e − i b ω + b e i ω) R e ( p e − i b ω + b e i ω) tan ( π n ( b + 1)) = p sin ( − b ω) + b sin ω p cos ( − b ω) + b cos ω tan ( π n ( b + 1)) = − p sin ( b ω) + b sin ω p cos ( b ω) + b cos ω (6)

Now take the limit of (6) as b → ∞ and replace ω with (5):

lim b → ∞ tan ( π n ( b + 1)) = lim b → ∞ − p sin ( b arccos ( 1 p) b + 1) + b sin ( arccos ( 1 p) b + 1) p cos ( b arccos ( 1 p) b + 1) + b cos ( arccos ( 1 p) b + 1) lim b → ∞ tan ( π n ( b + 1)) = lim b → ∞ − p sin ( arccos ( 1 p)) + b sin ( arccos ( 1 p) b + 1) p cos ( arccos ( 1 p)) + b cos ( arccos ( 1 p) b + 1)

Use the identities cos ( arccos x) = x and sin ( arccos x) = √ 1 − x 2:

lim b → ∞ tan ( π n ( b + 1)) = lim b → ∞ − p √ 1 − ( 1 p) 2 + b sin ( arccos ( 1 p) b + 1) p ( 1 p) + b cos ( arccos ( 1 p) b + 1) lim b → ∞ tan ( π n ( b + 1)) = lim b → ∞ − √ p 2 − 1 + b sin ( arccos ( 1 p) b + 1) 1 + b cos ( arccos ( 1 p) b + 1)

Use the [small-angle approximations][5] for tan, sin, and cos:

lim b → ∞ π n ( b + 1) = lim b → ∞ − √ p 2 − 1 + b ( arccos ( 1 p) b + 1) 1 + b π n = − √ p 2 − 1 + arccos ( 1 p) √ p 2 − 1 = arccos ( 1 p) − π n p 2 − 1 = ( arccos ( 1 p) − π n) 2 p 2 = 1 + ( arccos ( 1 p) − π n) 2 (7)

If we set n = − 1 then (7) is exactly equal to the equation characterizing entry A328227 in the OEIS. Important to note that only the negative solutions of p when 0"> n > 0 are valid and only the positive solutions of p when n ≤ 0 are valid.

As we mentioned in the previous article, different values of n result in different solutions for p. This is because the tangency condition is satisfied by multiple shapes of the spirograph. The number of distinct values of p that result in unique shapes is ⌊ b / 2 ⌋ and when b → ∞, there are an infinite number of values for p. To capture the fact that this is a family of numbers, we'll rename p to P P b n and rephrase (7) given the domain considerations in the previous paragraph. P P ∞ n are the positive solutions of the following equation, for n ∈ Z ∗:

( P P ∞ n) 2 = 1 + ( arccos ( 1 P P ∞ n) + π n) 2 (8)

## Proof That P P ∞ n ≠ 0 is Transcendental

Our original proof that P P ∞ n ≠ 0 is transcendental had an incorrect step. Reddit user **[existentialpenguin][6] suggested a variation on the original proof which the following proof incorporates. This proof relies on the [Lindemann–Weierstrass theorem][7] which for our purposes implies that if x is a algebraic number then cos x must be a transcendental number or x = 0. Before engaging in the main proof, we first want to show that when P P ∞ n = 1 then n = 0:

( P P ∞ n) 2 = 1 + ( arccos ( 1 P P ∞ n) + π n) 2 1 2 = 1 + ( arccos ( 1 1) + π n) 2 1 = 1 + ( arccos ( 1) + π n) 2 0 = π n 0 = n (9)

Now for the main proof, we'll put (8) into a more convenient form:

( P P ∞ n ≠ 0) 2 = 1 + ( arccos ( 1 P P ∞ n ≠ 0) + π n) 2 + √ ( P P ∞ n ≠ 0) 2 − 1 = arccos ( 1 P P ∞ n ≠ 0) + π n cos ( + √ ( P P ∞ n ≠ 0) 2 − 1) = cos ( arccos ( 1 P P ∞ n ≠ 0) + π n) cos ( + √ ( P P ∞ n ≠ 0) 2 − 1) = ( 1 P P ∞ n ≠ 0) cos ( π n) − ( 1 P P ∞ n ≠ 0) sin ( π n) ( − 1) n cos ( + √ ( P P ∞ n ≠ 0) 2 − 1) = ( 1 P P ∞ n ≠ 0) ( − 1) n cos ( + √ ( P P ∞ n ≠ 0) 2 − 1) = P P ∞ n ≠ 0 (10)

(9) shows that when P P ∞ n = 1 then it is implied that n = 0. By the contrapositive that means that when n ≠ 0 then P P ∞ n ≠ 1. Now let's use (10) and proceed by contradiction:

- Assume that P P ∞ n ≠ 0 ≠ 1 is algebraic.
- Then ( P P ∞ n ≠ 0) 2 must be algebraic.
- Then ( P P ∞ n ≠ 0) 2 − 1 must be algebraic.
- Then ( P P ∞ n ≠ 0) 2 − 1 must be algebraic.
- Then + √ ( P P ∞ n ≠ 0) 2 − 1 must be algebraic.
- Then cos ( + √ ( P P ∞ n ≠ 0) 2 − 1) must be transcendental.
- Then ( − 1) n cos ( + √ ( P P ∞ n ≠ 0) 2 − 1) must be transcendental.
- Yet, P P ∞ n ≠ 0 = ( − 1) n cos ( + √ ( P P ∞ n ≠ 0) 2 − 1) which we assumed was algebraic, a contradiction.

Therefore P P ∞ n ≠ 0 must be transcendental. □

## Computing P P ∞ n

Given our equation for P P ∞ n there is no algebraically straightforward way to compute P P ∞ n. Though maybe with a simple change of variables we can simplify the problem. Let's set P P ∞ n = 1 cos ( q n − π n):

( P P ∞ n) 2 = 1 + ( arccos ( 1 P P ∞ n) + π n) 2 ( 1 cos ( q n − π n)) 2 = 1 + ( arccos ( 1 1 cos ( q n − π n)) + π n) 2 1 cos 2 ( q n − π n) = 1 + ( arccos ( cos ( q n − π n)) + π n) 2 1 cos 2 ( q n − π n) = 1 + q 2 n cos 2 ( q n − π n) = 1 1 + q 2 n cos ( q n − π n) = 1 ± √ 1 + q 2 n (11)

Now let's replace cos ( q n − π n) using the identity cos ( q n − π n) = 1 ± √ 1 + tan 2 ( q − π n):

1 ± √ 1 + tan 2 ( q n − π n) = 1 ± √ 1 + q 2 n tan ( q n − π n) = q n tan q n = q n tan q n − q n = 0

We have reduced our original problem to the problem of finding the roots of tan x − x, i.e. the fixed points of tan x. The specific root we need for P P ∞ n is the smallest root ≥ π n, which we call q n, because otherwise arccos ( cos ( x − π n)) ≠ x − π n. The fixed points of tan x are well-known numbers in themselves that have applications in many areas of math, science, and engineering. There are a few known methods for computing them already (you'll find one in the addendum to this article). You can find more info at [MathWorld][8], including the first 6 roots. For our purposes it suffices to show the connections between the n th fixed point of tan x and P P ∞ n.

The first connection is from our original change of variables:

P P ∞ n = 1 cos ( q n − π n) P P ∞ n = 1 cos q n cos ( π n) + sin q n sin ( π n) P P ∞ n = 1 ( − 1) n cos q n P P ∞ n = ( − 1) n sec q n (12)

We can derive the other connection by combining (11) and (12):

1 cos 2 ( q n − π n) = 1 + q 2 n ( P P ∞ n) 2 = 1 + q 2 n P P ∞ n = + √ 1 + q 2 n

The two different methods of converting between the fixed points of tan x and P P ∞ n is incredible and is a direct result of q n 's nature as both an argument and a result of tan x.

## Conclusion

So what is P P ∞ n? On a physical and geometrical basis, we can say that it's the secant of the right triangle whose tangent is equivalent in radians to the angle to which these ratios are relative. P P ∞ n and the fixed points of tan x are the shadows of these special triangles, of which there are an infinite amount. I have to imagine that the angles and ratios which characterize these special triangles show up in various problems. The spirograph just happened to be my window to them. P P ∞ 1 shows up as the solution to this [IBM challenge problem][9], about which Numberphile also [made a video][10]. May there be other problems where the other ratios of this special triangle are relevant, i.e. the sine, cosine, cosecant, or cotangent?

Given that P P ∞ n have a well-understood connection to the fixed points of tan x, I now think that the values of P P b n which correspond to finite values of b that we derived in Part 1 are more enigmatic and interesting. In a way they could be understood as "intermediate solutions" toward the fixed points of tan x. I find this fascinating and in a future article I may derive a series expansion for directly computing those intermediate solutions. They may reveal more structure and properties of the fixed points of tan x.

[Rian Hunter][11], 6/16/21

## Addendum: Computing the Fixed Points of tan x

To compute the roots of tan x − x, we can apply its [series reversion][12], f ( x), to 0 to solve for x. Unfortunately for the series reversion algorithm to work, we need the first-order term to be non-zero. The series expansion of tan x is x + x 3 3 + 2 x 5 15 + …, so the expansion of tan x − x is x 3 3 + 2 x 5 15 + … which is no good. To fix this, make a change of variables that takes advantage of the fact that tan ( π 2 − x) = cot x and cot ( x + π n) = cot x, i.e. q n = π n + π 2 − r, where n ∈ Z ∗ results in a solution for the n th fixed point of tan x:

tan q n − q n = 0 tan ( π n + π 2 − r) − ( π n + π 2 − r) = 0 tan ( π 2 − ( r − π n)) + r = π n + π 2 cot ( r − π n) + r = π n + π 2 cot ( r) + r = π n + π 2

Yet there is another snag. Ideally we would use the Taylor series of cot r + r about r = 0 to derive the forward series coefficients but cot r + r is not defined at r = 0. On the other hand 1 cot r + r is, so we'll use that instead:

1 cot ( r) + r = 1 π n + π 2 (13)

At this stage the next step would be to find the derivatives of g ( x) = 1 cot ( r) + r to get a formula for the series coefficients parameterized by a series index, e.g. k, but unfortunately there is no easily discernable pattern of the value of the derivatives of 1 cot x + x at x = 0. The series reversion algorithm is also not very amenable to a compact notation. A Python script to compute the series reversion coefficients will be provided at the end of this section. Additionally the OEIS provides the [numerators][13] and the [denominators][14]. For the sake of simplicity we'll assume we have the series reversion coefficients readily available as d k and we'll define the reversion polynomial as f ( x):

f ( x) = ∞ ∑ k = 0 d k x k

We can then apply f ( x) to (13):

f ( 1 cot r + r) = f ( 1 π n + π 2) r = f ( 1 π n + π 2) π n + π 2 − q n = f ( 1 π n + π 2) q n = π n + π 2 − f ( 1 π n + π 2) q n = π n + π 2 − ∞ ∑ k = 0 d k ⋅ ( 1 π n + π 2) k

Now back to the detail of computing d k, the following Python script shows how to compute d k and using them to compute q n:

```
import sympy as sp

import sys

try:
    num_terms = int(sys.argv[1])
except IndexError:
    num_terms = 10

try:
    num_fixed_points = int(sys.argv[2])
except IndexError:
    num_fixed_points = 10

x = sp.symbols('x', real=True)
y = 1 / (sp.cot(x) + x)
s = sp.series(y, x, 0, num_terms)

# this is necessary for the series reversion
# algorithm to work
assert not s.coeff(x, 0)
assert s.coeff(x, 1)

s = s.removeO()

y2 = sp.symbols('y', real=True)
coeffs = sp.symbols('a1:' + str(num_terms), real=True)
finv = sum(sym * y2 ** (i + 1) for (i, sym) in enumerate(coeffs))

newy = s.subs(x, finv).expand()

eqs = []
for i in range(0, num_terms - 1):
    val = newy.coeff(y2 ** (i+1))

    if not i:
        expected = 1
    else:
        expected = 0

    eqs.append(sp.Eq(val, expected))

sols = sp.solve(eqs)
if isinstance(sols, list):
    sols = sols[0]

print("Here are the first %d coefficients for the series reversion of 1/(cot(x) + x)" % (num_terms,))
print(0, 0)
for (k, sym) in enumerate(coeffs):
    print(k+1, sols[sym])

print()

finv_real = sum(sols[sym] * y2 ** (i + 1) for (i, sym) in enumerate(coeffs))
print("Here are approximations for the first %d fixed points of tan(x)" % (num_fixed_points,))
for k in range(num_fixed_points):
    q = (2 * k + 1) * sp.pi/2
    print(k, (q - finv_real.subs(y2, 1/q)).evalf())

```

Copyright © 2021 Rian Hunter


## Links

[1]: index.html
[2]: https://www.reddit.com/r/math/comments/nyi17n/the_number_hiding_inside_the_spirograph/h1ki0rr/
[3]: https://oeis.org/A328227
[4]: https://www.reddit.com/r/math/comments/nyi17n/the_number_hiding_inside_the_spirograph/h1m69bf/
[5]: https://en.wikipedia.org/wiki/Small-angle_approximation
[6]: https://www.reddit.com/r/math/comments/o1frlx/the_number_hiding_inside_the_spirograph_part_2/h248bvt/
[7]: https://en.wikipedia.org/wiki/Lindemann%E2%80%93Weierstrass_theorem
[8]: https://mathworld.wolfram.com/TancFunction.html
[9]: https://www.research.ibm.com/haifa/ponderthis/challenges/May2001.html
[10]: https://www.youtube.com/watch?v=vF_-ob9vseM
[11]: https://twitter.com/cejetvole
[12]: https://mathworld.wolfram.com/SeriesReversion.html
[13]: http://oeis.org/A079330
[14]: http://oeis.org/A088989
