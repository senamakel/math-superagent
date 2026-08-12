<!-- source: https://research.ibm.com/blog/ponder-this-may-2001 | converted from HTML -->

Ponder This Challenge - May 2001 - Goblin chase in a pool - IBM Research

Ponder This Challenge:

This month's puzzle, like many others, traces its sources to Martin Gardner (Mathematical Carnival).

**PART A:**
We are in a rowing boat on a circular lake, starting at the center. At the edge of the lake is a mean goblin who wants to eat us; and if he catches us, he will do so. The goblin can't swim and won't go into the lake (and doesn't have a boat!) but he can run k times as fast as we can row.
(We'll discuss the parameter k later.)

We, however, can run significantly faster than the goblin can, so if we are able to reach a point at the edge of the lake without the goblin being there, then we will be able to escape.

Will we be able to escape or are our only options to be marooned forever on the lake or to be eaten by the goblin?

The answer depends on the parameter k.
There is a threshold T, such that if k<T then we can escape, and if k>T the goblin will eat us. Find the threshold T to six digits.

**PART B:**
Why is the goblin called Jimmy?

**Posted May 8th: Clarifications and Hints:**

The correct answer is not PI=3.14159..., nor is it PI+1.

Even if it were, PI to six digits is not 3.142857. (That's the six-digit approximation to 22/7, but PI is not quite 22/7.)

Part B is there mostly for fun, but its answer relates to the correct answer to Part A.

---

We will post the names of those who submit a correct, original solution! If you don't want your name posted then please include such a statement in your submission!

We invite visitors to our website to submit an elegant solution. Send your submission to the [ponder@il.ibm.com][1].

*If you have any problems you think we might enjoy, please send them in. All replies should be sent to:*[ponder@il.ibm.com][2]

## Solution

-

Click here to view the solution

**PART A:**

The threshold is T=4.6033388, gotten as the solution to the pair of equations
cos(B) = 1/T,
sin(B) = (1/T)*(pi + B).

For any value of k, we define the angle B=arccos(1/k), that is, cos(B)=1/k. We measure B in radians, so that a central angle of B corresponds to a circumferential distance of R*B, where R is the radius of the lake.

Assume first that the goblin starts out at the northern edge of the lake and moves counterclockwise throughout the chase. We start at the center.

Our path has two phases.

In the first phase, we trace out a semicircular arc, whose radius is (1/(2k)) times the radius of the lake. We start out heading due south, away from the goblin. We are moving at (1/k) times the speed of the goblin. When he reaches the point due west of center, we will be due east of center, (R/k) away from the center. Moreover, we will have kept diametrically opposite the goblin at all times: the center of the circle lies directly between me and the goblin.

In the second phase, we continue in a straight line, due north, towards shore. (Notice that when we ended our semicircular arc, we were heading north; we just continue in that direction.) We aim to hit the shore at an angle B away from the normal.

Still assuming that the goblin never changes direction, from the time that we finish the semicircular arc, we will travel distance R*sin(B), while the goblin will travel distance R*( pi + B). Namely, he travels R*pi to get halfway around the lake, and another R*B to cover the extra distance to our landing point.

The goblin will exactly catch up to us if R*sin(B) = (1/k)*R*(pi+B). Together with cos(B)=1/k, we solve for B=1.3518168 radians (or 77.453398 degrees) and k=T=4.6033388.

If the goblin never changes direction, then from the time we leave the semicircle, he is always slowly catching up to us in the angular sense. If he changes direction, he is only loses some of this advantage. We wait until he is once again diametrically opposite us, and then we zig back left on another chord, which will also get us to shore at an angle B.

To show that this is optimal (for both parties), consider this function of our two positions. For each of the two chords through our point which hit the shore at angle B, consider the end of the chord closer to us. Of those two ends, select the one further from the goblin's current position. Call that point P.

The function "GA" or "goblin's advantage", is the time it will take us to reach P, minus the time it will take the goblin to reach P. If we head towards P, no matter what the goblin does, the GA does not increase.

If the goblin heads towards our current position, no matter what we do, his GA does not decrease. (This is a special property of angle B, and takes a bit of calculus to verify.)

So if we both play optimally, GA does not change. For the special value k=4.6033388, the GA starts out at 0 (for our initial position (R/k,0) and his position (-R,0)), and so ends up at 0: dead heat racing for P. If k<4.6..., the GA starts out negative, and is still negative when we reach the shore, so we escape.

**Al Zimmermann gives us the following answer for Part A:**
I am reminded of the old physics problem in which you are asked to use a
barometer to determine the height of an apartment building. My favorite
solution is to offer the barometer to the building's superintendent in
exchange for his telling you how tall the building is. And so I wonder if
the goblin would grant us safe passage in exchange for our boat. We could
pursue this strategy by reminding the goblin of the old saying, "Give a
goblin a human and he'll eat for a day. Give a goblin a boat and he'll eat
forever."

**PART B:**
Why is the goblin called "Jimmy"?
The rowboat traces out a letter J (small semicircle, leading smoothly into a chord).

Those of you who answered "Because that's his name" have been with us too long.

---

*If you have any problems you think we might enjoy, please send them in. All replies should be sent to:*[ponder@il.ibm.com][2]

## Solvers

- **Krishna Kumar**(05.01.2001 @ 3:38 PM EDT)
- **Saibal Mitra**(05.01.2001 @ 5:26 PM EDT)
- **Henry Bottomley**(05.01.2001 @ 7:27 PM EDT)
- **Bill Schwennicke**(05.01.2001 @ 8:53 PM EDT)
- **Alexey Vorobyov**(05.02.2001 @ 4:17 PM EDT)
- **Colin Bown**(05.02.2001 @ 5:32 PM EDT)
- **Vince Lynch**(05.06.2001 @ 9:07 AM EDT)
- **Sunil Srivastava**(05.07.2001 @ 5:47 PM EDT)
- **Michel Jacquemin**(05.08.2001 @ 8:16 AM EDT)
- **Arjun Viswanathan**(05.08.2001 @ 9:53 AM EDT)
- **Amit Elazari**(05.08.2001 @ 11:18 AM EDT)
- **Steve Walter**(05.08.2001 @ 1:12 PM EDT)
- **Marian Olteanu**(05.08.2001 @ 2:10 PM EDT)
- **Sriram Thiagarajan**(05.08.2001 @ 2:18 PM EDT)
- **Derek Kisman**(05.08.2001 @ 5:43 PM EDT)
- **Jacques Willekens**(05.09.2001 @ 9:42 AM EDT)
- **Douglas Schrag**(05.10.2001 @ 9:15 AM EDT)
- **Michael Malak**(05.11.2001 @ 10:46 AM EDT)
- **Tjinder Singh Manku**(05.10.2001 @11:10 AM EDT)
- **Ionel Santa**(05.11.2001 @ 8:57 AM EDT)
- **Jean**(05.11.2001 @ 11:23 AM EDT)
- **Flies**(05.11.2001 @ 11:23 AM EDT)
- **Bednarik Jozef**(05.14.2001 @ 10:05 AM EDT)
- **Sridhar Srinivasan**(05.14.2001 @ 6:44 PM EDT)
- **Ether Jones**(05.14.2001 @ 9:08 PM EDT)
- **Jeff Little**(05.17.2001 @11:55 AM EDT)
- **Shankar Venkataramani**(05.17.2001 @ 1:41 PM EDT)
- **Dharmashankar Subramanian**(05.17.2001 @ 3:36 PM EDT)
- **Victor Chang**(05.17.2001 @ 8:48 PM EDT)
- **Prithu**(05.19.2001 @ 1:11 PM EDT)
- **Paul Kahler**(05.22.2001 @ 9:56 AM EDT)
- **Adam Daire**(05.23.2001 @ 2:44 AM EDT)
- **Andoni Alexandr**(05.25.2001 @ 5:34 AM EDT)
- **Walter Isidro**(05.27.2001 @ 2:38 AM EDT)
- **Dave Biggar**(05.27.2001 @ 8:53 PM EDT)
- **Holiday's Cafe**(05.29.2001 @ 1:29 PM EDT)
- **Ross Millikan**(05.29.2001 @ 2:33 PM EDT)
- **Alan Skelley**(05.30.2001 @ 5:58 PM EDT)
- **Yuriy Groysman**(05.31.2001 @ 8:08 PM EDT)

## Related posts

-

### [Ponder This Challenge - August 2026 - The Wheel of Buttons][3]

Puzzle

Gadi Aleksandrowicz

31 Jul 2026

  -

Ponder This

-

### [Ponder This Challenge - July 2026 - Return of the Superheroes][4]

Puzzle

Gadi Aleksandrowicz

01 Jul 2026

  -

Ponder This

-

### [Ponder This Challenge - June 2026 - The Superhero Team Movies][5]

Puzzle

Gadi Aleksandrowicz

01 Jun 2026

  -

Ponder This

-

### [Ponder This Challenge - May 2026 - The Powers of a Binary Matrix][6]

Puzzle

Gadi Aleksandrowicz

01 May 2026

  -

Ponder This


## Links

[1]: mailto:ponder@il.ibm.com?subject=ANSWER%3A%20May%202001%20Ponder%20This
[2]: mailto:ponder@il.ibm.com?Subject=PUZZLE%20SUGGESTION%3A&amp;Body=Please%20include%20the%20answer%20with%20your%20submission.
[3]: /blog/ponder-this-august-2026
[4]: /blog/ponder-this-july-2026
[5]: /blog/ponder-this-june-2026
[6]: /blog/ponder-this-may-2026
