<!-- source: https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/ | converted from HTML -->

Math Can, in Theory, Help You Escape a Hungry Bear | Quanta Magazine

[Home][1]

Math Can, in Theory, Help You Escape a Hungry Bear

[Comment][2]

Save Article

Read Later

###### Share

[Facebook][3]

[4]

[Copied! Copy link][5]

[Email][6]

[Pocket][7]

[Reddit][8]

[Ycombinator][9]

[10]

-

-

Comment

Comments

-

Save Article

Read Later

Read Later

[Insights puzzle][11]

# Math Can, in Theory, Help You Escape a Hungry Bear

*By *[Pradeep Mutalik][12]

*August 25, 2021*

How readers used their geometry skills to survive a dangerous puzzle.

Comment

Save Article

Read Later

[James Round][13] for Quanta Magazine

## Introduction

Our [June Insights puzzle][14] added a few twists to a classic puzzle made famous by Martin Gardner in his 1965 *Scientific American*column and later published in the book *The Colossal Book of Short Puzzles and Problems*. In our version, a swimmer at the center of a circular lake of radius 3.5 is attempting to escape a bear hunting him from the shore. The bear doesn’t swim but can run along the circumference at 3.5 times the swimmer’s speed, which is 1 unit of length per unit of time. To survive, the athlete must swim to shore before the bear reaches the same point.

Our first puzzle posed some basic questions about the swimmer’s strategy. For example, what could he learn from the way squirrels spiral up a tree to escape pursuing dogs? The other puzzles explored newer questions, which led to some unexpected mathematical sleuthing.

Before we discuss the solutions, you may have noticed that we did not mention any specific units for distance, time and velocity. The numbers were carefully chosen to avoid the need for conversion factors: First, the swimmer’s velocity is 1, so the swimmer’s time is numerically equal to his swimming distance. Second, the ratio of the bear’s speed to the swimmer’s speed is the same as the lake’s radius, so the bear’s angular velocity is also 1. In other words, the distance traveled by the swimmer over a given time interval has the same numeric value as the angular distance (in radians) traveled by the bear. Clearly, swimming straight for the shore opposite the bear is not an option, since the bear only needs to run π (~3.14) radians while the athlete needs to swim 3.5 distance units. To simplify matters, we’ll mostly dispense with the word “units” and just mention the numeric values. (If this lack of explicit units makes you uncomfortable, you’re welcome to substitute any units you like, so long as your velocity is expressed in terms of the same units you’ve used for distance and time.)

For further convenience, let’s assume that the center of the lake is at the origin (0, 0) of an *x*–*y*coordinate system and the bear starts out at the easternmost edge along the *x*-axis (3.5, 0). We will express angle measurement in radians, giving the degree equivalents only in the final answers. (I loved how [Paolo Abiuso parodied][15] the classic riddle that asks, “What color is the bear?” Paolo’s answer: “I don’t know, but it seems to understand polar coordinates.”)

To start the chase, the swimmer forces the bear to run by making a small movement away from the bear in the opposite direction. If the bear does nothing, the swimmer continues moving away, getting closer to the shore with no gain for the bear. Therefore, the bear’s best strategy is to commit itself and start running in either direction. Let’s assume the bear runs counterclockwise.

## Puzzle 1

1. How can the swimmer apply the squirrel strategy (keeping in a direction diametrically opposite to the bear) to get into the best position to escape?
2. What kind of path does the swimmer trace in doing so?
3. How many full turns will the swimmer make before the squirrel strategy stops being of any further help?
4. How long does it take to reach that point?
5. Can the swimmer finally evade the bear?

We’ll assume the bear continues running counterclockwise. For these particular questions, changing direction either makes no difference or makes things worse for the bear.

A. Starting at the center of the lake initially allows the swimmer to keep pace with the bear’s angular velocity. At every point, the athlete can imagine a small “safe circle” around the origin, within which he can always stay opposite the bear. He wants to allocate just enough of his swimming velocity to going around such a circle (in the tangential as opposed to the radial direction) in order to remain opposite the bear while simultaneously moving outward as quickly as he can toward the shore. At a certain distance he reaches the largest possible safe circle, such that he has to swim at full speed along its perimeter just to keep opposite the bear, and he is no longer getting closer to the shore. This occurs when the swimmer reaches a distance of 1 from the center of the lake. The beauty of the squirrel strategy is that the swimmer gains distance from the bear without allowing the bear to reduce any of the angular separation.

As the bear moves from A to B, the swimmer keeps opposite all the time (as shown by the line MN), finally reaching point P. The swimmer’s semicircular path is shown in red, and his outermost safe circle is in green. PQ is his final radial dash.

Samuel Velasco/Quanta Magazine

If the bear changes directions frequently, the swimmer just needs to shuffle in the opposite direction to the bear, following what [Jonathan Barmak][16] described as a path that is “piecewise semicircular (concatenation of arcs of circles of same radius).” This will also take the swimmer the same distance away from the bear in the same time.

B. As several readers pointed out, this strategy results in the swimmer moving along a semicircle (OP in red) with radius 0.5 and center at (0, −0.5), and ending up at point (0, −1) south of the center. [Jonathan Barmak gave a technical reason][17] for why this path is a semicircle.

C. The swimmer thus makes a full half-turn (π radians) along the semicircle, in the same time that the bear has made a quarter turn ($latex \frac{π}{2}$ radians) along the circumference of the lake. By the magic of our automatic interconversions, this will take the bear a time of $latex \frac{π}{2}$ or 1.57, which happens to be the distance the athlete swims along the circumference of the semicircle (π times its radius of 0.5).

D. As we established above, it takes 1.57 time units to reach the safe circle along the red semicircle OP in the figure.

E. It is now obvious that the swimmer can evade the bear. The swimmer only has to swim 2.5 (time or distance units) in the radial direction (PQ) to reach the shore at the south pole of the lake. The bear still needs a time of π to reach the same point. The swimmer’s total time will be 1.57 + 2.5 = 4.07, and he will reach the shore π − 2.5 = 0.64 time units before the bear (with a separation of 0.64 × 3.5 = 2.26 distance units along the circumference from C to Q).

These basic questions were well answered by several readers, including [Arthur Champernowne][18], [Andrew][19], [Jonathan Barmak][17], [Lazar Ilic][20], [Ivan Rygaev][21] and [Paolo Abiuso][15].

For this puzzle and all the others except puzzle 2, it does not make any difference if the bear reverses direction. The swimmer can simply reverse his angular direction to stay opposite the bear while moving outward as before. The relative positions of the bear and swimmer remain the same, with the swimmer opposite the bear at the exact distance he would have been if the bear had not reversed.

Puzzle 2 is more complicated and interesting. Let’s look at the other puzzles first.

## Puzzle 3

Suppose, on the other hand, that the athlete’s goal is to get out of the lake as far ahead of the bear as possible. Which of these strategies is now most efficient, and what is the greatest distance he can put between himself and the bear along the lake circumference?

1. Follow the squirrel strategy until it doesn’t help any longer, and then make a dash for it in the radial direction.
2. Follow the squirrel strategy until it doesn’t help any longer, and then make a dash for it in some other direction.
3. Follow the squirrel strategy for some time, and then make a dash for it in some direction.
4. Follow some other strategy instead of the squirrel strategy.

The answer is **B**, which gives the swimmer a maximum circumferential lead of 3.74.

The swimmer must follow the squirrel strategy as far as it can go, which takes him to a radial distance of 1, and then make a dash for it in the direction that takes him furthest away from the bear. This lies along the tangent away from the bear in the same direction that the swimmer was headed at the instant he joined the safe circle — directly heading east in our scenario.

The reason for this is clear: Since the swimmer is seeking to maximize distance, he must milk the squirrel strategy to the hilt, as it gives him separation from the bear for free. Once he reaches the limit of that strategy, he needs to make a dash in the direction as far away from the bear as possible, which happens to be the tangent to the safe circle. Making the angle any larger would result in the swimmer reentering the safe circle, taking him back to square one.

The strategy the swimmer can use to achieve the maximum lead on the bear.

It is not hard to calculate how far ahead of the bear the swimmer will emerge from the lake. In Figure 2, the length of line segment OP is 1, and OQ, the hypotenuse of the triangle, is 3.5. The length of his final dash, by Pythagoras’ theorem, is $latex \sqrt{\left(OQ^{2}-O P^{2}\right)}$ or $latex \sqrt{\left(3.5^{2}-1^{2}\right)}$ = 3.354, during which he covers cos -1 ($latex \frac{1}{3.5}$) = 1.281 radians in addition to his initial lead of π which makes ~4.423 radians. Our numerical magic also tells us how much the bear has covered from B to C during the swimmer’s dash: It’s the same number as PQ in radians, 3.354, which is 1.069 radians short of the swimmer (or a distance of 3.74 along the arc CQ). This is about 67% greater than the lead achieved by the simple strategy described in the solution of puzzle 1.

## Bonus 1

Does the best strategy for puzzles 2 and 3 change if the radius of the lake is 4.5 units and the bear’s running speed is 4.5 times that of the swimmer? (The swimmer’s speed remains the same as before.)

Answer: No, it does not change for puzzle 3. Puzzle 2 is an open question that we will discuss later.

The strategy for puzzle 3 would not change at all for this case. In fact, the simple strategy described in the puzzle 1 solution fails for the case where the lake’s radius and the speed ratio between the bear and the swimmer exceed π + 1 (~4.14). Nevertheless, by following the puzzle 3 strategy, the swimmer can escape quite easily.

Here are the same calculations we made above for this case.

The radius of the safe circle remains 1 unit. In the diagram, line segment OP is 1, and the hypotenuse OQ is now 4.5. The length of the swimmer’s straight dash is $latex \sqrt{\left(4.5^{2}-1^{2}\right)}$ = 4.387 units, covering an additional cos -1 ($latex \frac{1}{4.5}$) = 1.347 radians. The bear would need to run around an arc of π + 1.347 = 4.888 radians to catch up with the swimmer when he reaches the shore. Since the bear only covers 4.387 (same as the length swum by the swimmer), it will fall 4.488 − 4.387 = 0.101 radians short.

[Arthur Champernowne][18], [Lazar Ilic][20] and [Paolo Abiuso][15] recognized that there is life after π + 1 and used this strategy to answer the second bonus question below.

## Bonus 2

What is the highest ratio between the bear’s running speed and the swimmer’s speed that will still allow the swimmer to escape? (Assume that the radius of the lake in units is equal to this ratio, and the swimmer’s speed is unchanged.)

Answer: 4.6033.

We need to do the same calculations as above in reverse. By setting the final distance between the swimmer and the bear to zero and solving numerically for the lake radius and bear speed that would produce this result, we get a value of 4.6033. You can check that this is the limit: $latex \sqrt{\left(4.6033^{2}-1^{2}\right)}$ = 4.4934, cos -1 ($latex \frac{1}{4.6033}$) = 1.3518, and π + 1.3518 (the angle the bear travels) also equals 4.4934 from B to C.

## Puzzle 2

Suppose our goal is not just to evade the bear but to escape as fast as possible (our swimmer’s arms and legs are tired, after all). Which of these strategies is most efficient, and what is the fastest escape time in each case?

This turned out to be an extremely interesting question, whose final answer is still in doubt. The two contending strategies are:

C. Follow the squirrel strategy for some time, and then make a dash for it in some direction.
D. Follow some other strategy instead of the squirrel strategy.

Amazingly, they are equally efficient to the third decimal place!

Strategy C gives an optimized solution of **3.5041**that cannot be improved further, while strategy D gives a solution of **3.5038**that can possibly be improved.

(Update: Further analysis shows that this latter solution can be disrupted by two reversals by the bear, so the strategy C solution is the true shortest path.)

We are considering this problem last because of a fundamental complication: The bear can reverse direction! If the bear chose to do so in any of the previous situations, it wouldn’t affect the final result. But if the swimmer is trying to minimize his swimming time, the situation changes. A reversal of direction can literally bend the swimmer’s path out of shape, adding a significant amount of time to the originally intended path. As [Jonathan Barmak][22] rightly pointed out, this must be factored in when we’re determining the quickest path. When I originally prepared this puzzle, I thought the answer was obviously C, but Barmak’s construction forced me to revisit D.

As an example, consider an obvious strategy that would be fastest if the bear did not change direction. Once the bear has committed to running in a particular direction, the swimmer can just aim radially at a point slightly ahead of where the bear would get to in a time of 3.5, which in our coordinate system also has an angular distance of 3.5 radians. Since a straight line is the shortest distance between two points, this is without a doubt the shortest possible path for the swimmer, taking 3.5 time units.

This shows how the bear’s reversal of direction bends the swimmer’s path. Here initial leg OD is 0.12 and the long leg DC’ is 3.395, giving a combined path of 3.515 for the swimmer.

That sounds great in principle, but the bear can allow the swimmer to commit himself to this path and then change directions after running an angular distance of about 0.12 (from A to B in Figure 3, which is about a third of 3.5 − π). This forces the swimmer to alter his intended target C (which is at an angle of 3.5 from A), aiming just ahead of the point C’, which is where the bear will reach running clockwise from B. C’ is at an angular coordinate of π − 0.13 (~3.01) from A resulting in a new path time of 3.515.

In evaluating the time of a path, we have to use the worst-case scenario. Let’s look at each of the possible strategies mentioned.

A. Follow the squirrel strategy until it doesn’t help any longer, and then make a dash for it in the radial direction.

The squirrel strategy, as we saw above, is impervious to a reversal of direction. Hence the fastest path time for this strategy remains 4.07 as we determined in puzzle 1.

B. Follow the squirrel strategy until it doesn’t help any longer, and then make a dash for it in some other direction.

The fastest time is at least 4.07, since the shortest distance to shore from the edge of the safe circle is radial. Heading in another direction simply adds more distance and time.

C. Follow the squirrel strategy for some time, and then make a dash for it in some direction.

The swimmer can follow the squirrel strategy until he is exactly π units away from shore radially, and then make a straight dash radially. This strategy was suggested by some readers, and it is impervious to disruption, because the bear will require a time of π to catch the swimmer regardless of which direction it runs. The time required for this is π + arcsin(3.5 − π) = 3.50815.

[Lazar Ilic][20] and [Paolo Abiuso][15] suggested the swimmer should start following the squirrel strategy and at the optimal moment take off on the tangent to his semicircular path that reaches the shore just ahead of the bear. We can call this the arc-tangent strategy. In principle this seems to be an optimal strategy because it involves no change in direction and as Abiuso mentioned, this kind of smooth transition will save time compared to a sharp change in angle. The shortest arc-tangent combination that just eludes the bear requires spending 0.1861 following the squirrel strategy, followed by a tangential straight-line dash of 3.318, giving a total path time of 3.5041. Unlike in the straight-line case discussed above, the bear cannot increase the swimmer’s time by reversing course, even though the straight-line segment is greater than π.

The squirrel arc-tangent strategy. As described in the text, this strategy is impervious to the bear’s reversals.

As [Paolo Abiuso][23] pointed out in rebutting the claims of strategy D, a reversal by the bear does force the swimmer to alter his path, but this decreases the swimmer’s time because the swimmer can take a path that’s closer to the shore than his original destination. In Figure 4, the swimmer remains on his initial squirrel path as the bear moves from A to B. When the bear reaches B, the swimmer, at T, takes off on a tangent. The destination is C if the bear keeps moving counterclockwise or C’ if it changes direction. The two paths are of equal length as OC’ is the mirror image of OC across the radial line from B. Let’s assume the bear continues counterclockwise. At R, the bear switches direction. Notice that there exists a path DF (shown in red) that mirrors the swimmer’s original target across the radial line DR’ to F, which is again of equal length. The swimmer has a wedge-shape area of the circle CDF within which every point on shore is closer to him than his original target. The swimmer can therefore escape in a shorter time as explained below.

Recall that the swimmer was diametrically opposite the bear at point T before starting on his straight-line dash. Thereafter, the bear steadily gains in angular distance on the swimmer counterclockwise. So, the length of arc RR’ counterclockwise (let’s call this RR’*cc*) is less than π, but its clockwise length is more than π (let’s call this RR’*c*, making RR’*c*> RR’*cc)*. The counterclockwise reach of the bear is the length of arc RC in the original time, which is equal to the clockwise arc RC’’ where C’’ is the point the bear would expect to end up clockwise. Let’s call this distance *x*. Therefore, arc R’C, which is *x*− RR’*cc,*is longer than arc R’C’’ which is *x *− RR’*c*— the bear has a longer “reach” past R’ in its original direction compared to the reverse direction. But arc R’C is equal to arc R’F (as DF is a radial mirror of DC). Therefore, the bear cannot quite reach F clockwise in the same time as it would reach C counterclockwise. Thus, the swimmer could swim to any point within arc C’’F, all of which are closer to the shore than his original target.

D. Follow some other strategy instead of the squirrel strategy.

[Jonathan Barmak][22] suggested and diagrammed a fast disruption-free path that he called the “squirrel + two segments” strategy:

1. Follow the squirrel strategy for 0.3 units of time. …
2. Then move radially for 0.07 units.
3. Check where the bear is and move straight to its antipodal point.

This results in a straight-line dash of 3.1355 units. Since this is smaller than π, it cannot be disrupted because the reverse distance the bear will need to cover to reach the same point will be longer. Barmak also showed that reversal by the bear during the second segment does not increase the path duration. The time required by this path is 3.5055.

Barmak’s innovative construction is explicitly designed to ensure that path reversals do not increase the stated maximum time. Nevertheless, it involves not just one, but two sharp changes in direction, which seems to indicate that the time can probably be improved by smoothing out the transitions between the three parts.

There is one other path we can explore. We saw that any change in the bear’s direction shortened the backward time in the arc-tangent path. What if we chose a path such that the swimmer pulls as far away as needed from the backward path to keep its length at the allowable maximum at all points? In other words, the swimmer swims at the edge of what he can get away with, equalizing his forward and backward path lengths at all points (except in the beginning and the end).

My calculations indicate that such a path indeed exists. It consists of a straight dash at the beginning, and another at the end, joined by a smooth curve that keeps the length of the projected backward path the same as what the forward path finally ends up being. Specifically, the swimmer aims at an angle of 3.2453 radians for a distance of 0.079 initially and makes a straight dash of length 3.3168 to the shore at an angle of 3.5038 radians at the end. These two straight line segments are joined by a smooth curve until about time 0.187, during which the distance from the moving reverse target is kept such that the projected backward path time remains constant. As the destination reveals, the path time is 3.5038, slightly better than that of the arc-tangent strategy. (Disclaimer: This is a new solution that has not been time-tested. It could have some unapparent flaw or need some modifications.)

(Update: The above disclaimer turns out to have been warranted. Two reversals by the bear, the first at the end of the initial straight-line segment and the second 0.19 units later, lengthen the path length to more than 3.5041.)

To address the bonus 1 question, there is no reason to think that the arc-tangent strategy and this new solution will not apply if the radius of the lake were 4.5 units with the bear’s running speed 4.5 times that of the swimmer.

After the safety-first, squirrel-assisted time of over 4, these improved strategies get the swimmer unbelievably close to the minimum possible time of 3.5!

It is possible that this straight line-curve-straight line path can be optimized a little further. These kinds of path-length calculations are tricky to do, and it is even trickier to prove that the path can withstand all kinds of disruptions by the bear reversing its direction.

What if the bear reverses a second time? This is not as disruptive as it might seem for two reasons. First, notice that a reversal is costly for the bear: In every reversal, it gives up any gain on the swimmer that it has already achieved, so the reversal has a penalty of reducing the reach of the reverse path by twice the length of the reversed segment. Second, the bear is running out of time: The closer the swimmer gets to shore, the less effective the reversal is in increasing path length, until it completely ceases to be effective when the swimmer’s distance from the bear’s antipode reaches π.

(Update: While a second reversal by the bear has smaller effects on the swimmer’s path length as stated above, it can nevertheless increase the path length enough to disqualify some solutions, as described above in case of the straight line-curve-straight line path.)

Thank you to all who dived into this puzzle. If you come up with a better time for puzzle 2, please post it here. I will also post further details of the solution presented here. Please let me know if I’ve made a mistake in any of these calculations, or if you can think of a way that allows the bear to lengthen the swimmer’s path that I may have missed. The prize for this puzzle goes to Paolo Abiuso and Jonathan Barmak, who argued eloquently for their two competing strategies. Congratulations to the winners and see you next time for new Insights!

***Updates: October 4, 2021**

Further analysis of the straight line-curve-straight line path based on a discussion initiated by [Michel][24] shows that this path can be lengthened by the bear beyond the length of the arc-tangent solution by performing two reversals of direction at strategic points in the path. Therefore, the arc-tangent path of 3.5041 is indeed the shortest path: It cannot be disrupted by multiple reversals for the reason detailed in the original solution. The straight line-curve-straight line path remains the shortest path if the bear is allowed only one reversal, but that is an arbitrary restriction.*

The Quanta Newsletter

*Get highlights of the most important news delivered to your email inbox*

## Also in Mathematics

[Graduate Student Proves a Quantum Uncertainty Principle for Fractals][25]

[chaos theory][26]

###

[Graduate Student Proves a Quantum Uncertainty Principle for Fractals][25]

*By *[Shalma Wegsman][27]

August 12, 2026

[Comment][28]

Save Article

Read Later

[image: A collage that superimposes various images and depictions of rivers over a sketch of a river network. A hand holds a rotating image of deltas over where the sketched river meets the sea.]

[Why Are Rivers So Mathematical?][29]

[Qualia][30]

###

[Why Are Rivers So Mathematical?][29]

*By *[Natalie Wolchover][31]

August 10, 2026

[Comment][32]

Save Article

Read Later

[Why the Legendary Erdős Problems Are Falling to AI][33]

[artificial intelligence][34]

###

[Why the Legendary Erdős Problems Are Falling to AI][33]

*By *[Konstantin Kakaes][35]

August 3, 2026

[Comment][36]

Save Article

Read Later

## Comment on this article

*Quanta Magazine moderates comments to facilitate an informed, substantive, civil conversation. Abusive, profane, self-promotional, misleading, incoherent or off-topic comments will be rejected. Moderators are staffed during regular business hours (New York time) and can only accept comments written in English. *

Show comments

[image: An artist’s conception of the ways that functional capacities have been mapped to regions of the brain.]

## Next article

The Brain Doesn’t Think the Way You Think It Does

[37]

Close

Log in to Quanta

## Use your social network

[Facebook Connect with Facebook][38]

[Connect with Google][39]

or

Don't have an account yet? Sign up

Close

Forgot your password?

We’ll email you instructions to reset your password

Close

Change your password

Enter your new password

Close

Sign Up

Creating an account means you accept Quanta Magazine's
[Terms & Conditions][40] and [Privacy Policy][41]


## Links

[1]: /
[2]: https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/#comments
[3]: http://www.facebook.com/sharer.php?u=https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/
[4]: https://twitter.com/share?url=https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/&text=Math+Can%2C+in+Theory%2C+Help+You+Escape+a+Hungry+Bear&via=QuantaMagazine
[5]: 
[6]: /cdn-cgi/l/email-protection#c9f6babcaba3acaabdf484a8bda1e28aa8a7ecfb8ae2a0a7e29da1aca6bbb0ecfb8ae281aca5b9e290a6bce28cbaaaa8b9ace2a8e281bca7aebbb0e28baca8bbefaba6adb0f481a6beecfbf9bbaca8adacbbbaecfbf9bcbaacadecfbf9bda1aca0bbecfbf9aeaca6a4acbdbbb0ecfbf9baa2a0a5a5baecfbf9bda6ecfbf9babcbbbfa0bfacecfbf9a8ecfbf9ada8a7aeacbba6bcbaecfbf9b9bcb3b3a5ace7ecf988ecf988a1bdbdb9baecfa88ecfb8fecfb8fbebebee7b8bca8a7bda8a4a8aea8b3a0a7ace7a6bbaeecfb8fa4a8bda1e4aaa8a7e4a0a7e4bda1aca6bbb0e4a1aca5b9e4b0a6bce4acbaaaa8b9ace4a8e4a1bca7aebbb0e4abaca8bbe4fbf9fbf8f9f1fbfcecfb8f
[7]: https://getpocket.com/save?url=https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/&title=Math+Can%2C+in+Theory%2C+Help+You+Escape+a+Hungry+Bear
[8]: https://www.reddit.com/submit?url=https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/
[9]: https://news.ycombinator.com/submitlink?u=https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/&t=Math+Can%2C+in+Theory%2C+Help+You+Escape+a+Hungry+Bear
[10]: https://bsky.app/intent/compose?text=https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/
[11]: /tag/insights-puzzle/
[12]: https://www.quantamagazine.org/authors/pradeep/
[13]: https://www.jamesrounddesign.com/
[14]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/
[15]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/#comment-5445837237
[16]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/#comment-5481198793
[17]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/#comment-5439765885
[18]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/#comment-5438212458
[19]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/#comment-5438859199
[20]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/#comment-5442087087
[21]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/#comment-5443974257
[22]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/#comment-5463587970
[23]: https://www.quantamagazine.org/can-math-help-you-escape-a-hungry-bear-20210629/#comment-5487553416
[24]: https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/#comment-5513097972
[25]: https://www.quantamagazine.org/graduate-student-proves-the-fractal-uncertainty-principle-20260812/
[26]: /tag/chaos-theory/
[27]: https://www.quantamagazine.org/authors/shalmawegsman/
[28]: https://www.quantamagazine.org/graduate-student-proves-the-fractal-uncertainty-principle-20260812/#comments
[29]: https://www.quantamagazine.org/why-are-rivers-so-mathematical-20260810/
[30]: /tag/qualia/
[31]: https://www.quantamagazine.org/authors/natalie/
[32]: https://www.quantamagazine.org/why-are-rivers-so-mathematical-20260810/#comments
[33]: https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/
[34]: /tag/artificial-intelligence/
[35]: https://www.quantamagazine.org/authors/konstantin-kakaes/
[36]: https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/#comments
[37]: /mental-phenomena-dont-map-into-the-brain-as-expected-20210824/
[38]: /mechanix?loginSocial=facebook
[39]: /mechanix?loginSocial=google
[40]: /terms-conditions
[41]: /privacy-policy
