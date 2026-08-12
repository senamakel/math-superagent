# PE 761 — Regular n-gon critical speed (pattern-finder deliverable)

Structured formula validated against both independent published exact values, then
applied to the hexagon.

## Formula (stewbasic, math.SE 1762665; corroborated by Abel et al. arXiv:2007.08965)

For a regular n-gon (swimmer at center, runner at an edge midpoint-speed v), the
critical runner speed is V(n) = 1/cos(alpha) where:

    theta = pi/n,  t = tan(theta)
    K = largest integer with  sin(K*theta) - (K+n)*t*cos(K*theta) < 0
        (== floor of the unique root of tan(x*theta) - (x+n)*t in [1, n/2))
    alpha = 1/2 * (  K*theta  +  acos( 2*sin(K*theta)/((K+n)*t) - cos(K*theta) )  )

## Validation (exact, checked)

- n=3:  V = (3+sqrt5)*sqrt2 = 7.4049183473  — matches Abel et al. Thm 4.5 exact value.
- n=4:  V = sqrt(5/2*(7+sqrt41)) = 5.78859314459 — matches Abel 4.6, David K,
        and the statement oracle 5.78859314 (8 dp).
- n->inf: converges to circle constant 4.6033388 (IBM Ponder This goblin identity),
        confirmed: V(5000)=4.60333945.

## RESULT

    V_hexagon = V(6) = 5.0550504633038933...  ->  rounded to 8 dp:  5.05505046

(For n=6: K=2, alpha=1.37166085458, V=1/cos(alpha).)

## Auxiliary sequence K(n)

K(n) for n=3..36:
1,1,2,2,3,3,3,4,4,5,5,6,6,6,7,7,8,8,9,9,9,10,10,11,11,12,12,12,13,13,14,14,15,15
- exact linear recurrence (order 8): a(n)=a(n-1)+a(n-7)-a(n-8), i.e. K(n)-K(n-1)
  is period 7 with pattern [0,1,0,1,0,0,1] — this holds through n~85 (verified),
  then deviates (first K(n)!=floor(3n/7) at n=86, off by +1). So K(n)=floor(3n/7)
  is a conjecture valid only up to n=85; the recurrence-period-7 claim also breaks.
  K is only an auxiliary index in the V(n) formula; it does not affect the 8-dp
  answer accuracy since V changes smoothly.
