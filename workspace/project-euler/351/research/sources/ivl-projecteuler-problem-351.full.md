<!-- source: https://www.ivl-projecteuler.com/overview-of-problems/25-difficulty/problem-351 | converted from HTML -->

IVL - Project Euler Solutions - Problem 351

Search this site

Embedded Files

Skip to main content

Skip to navigation

#

Project Euler 35 1 - Hexagonal Orchards

Official link: [https://projecteuler.net/problem=351][1]

#

Thought Process

Clearly we only need to consider one sixth of the hexagon and then we can multiply the final answer by 6.

Lets focus on the top right triangle

I include a diagram to help readers understand.

Lets denote the angle between P0-P1 and P0-P2 as Angle 1. Then the angle between P0-P1 and P0-P3 is clearly 1/2 of Angle 1, lets call it Angle 1/2. Now clearly the angle between P0-P1 and P0-P4 is also Angle 1, we've already seen this angle before, hence the point will be hidden. Similarly we can see that between P0-P1 and P0-P5 we have Angle 1/3. In short each point, x, on the n -th layer represents Angle x/n.

For example on the 4-th layer we have the 3rd point, P6, will have Angle 2/4 = Angle 1/2

Now the problem is simple.

We just need to find all of the points which have an angle x/n such that gcd(x, n) > 1. We know that on the n -th layer there are gonna be φ (n), where φ (n) is [Euler's Totient Function][2], numbers, x, such that gcd(x, n) = 1, therefore there are n - φ (n) numbers such that gcd(x, n) > 1.

Then we have a nice formula for H(n). Take note of the [Totient Summatory Function][3]

Originally just using the wiki page and my [mobius sieve][4] I could get the answer in ~85 seconds.

After solving the problem you have access to the [PDF overview][5] of the problem, which shows you how to implement the Totient Summatory Function efficiently. I implemented algorithm 6 detailed on the PDF, then runtime has dropped to ~1 second!

This new algorithm has been added to my python package [mathslib][6]

#

Interactive Code

Input an Integer ( yourinput)

Code will output H(n)

Google Sites

Report abuse

Page details

Page updated

Google Sites

Report abuse


## Links

[1]: https://projecteuler.net/problem=351
[2]: https://en.wikipedia.org/wiki/Euler%27s_totient_function
[3]: https://en.wikipedia.org/wiki/Totient_summatory_function
[4]: https://mathslib.readthedocs.io/en/latest/mathslib.html#mathslib.numtheory.mobius_k_sieve
[5]: https://projecteuler.net/overview=0351
[6]: https://mathslib.readthedocs.io/en/latest/index.html
