<!-- source: https://web.archive.org/web/2023/https://math.stackexchange.com/questions/1555855/prove-that-the-boy-cannot-escape-the-teacher | converted from HTML -->

geometry - Prove that the boy cannot escape the teacher - Mathematics Stack Exchange

**Teams**

Q&A for work

Connect and share knowledge within a single location that is structured and easy to search.

[Learn more about Teams][1]

# [Prove that the boy cannot escape the teacher][2]

[Ask Question][3]

Asked 8 years, 3 months ago

Modified [8 years, 2 months ago][4]

Viewed 1k times

22

[5]

$\begingroup$

I'm struggling with the following problem from Terence Tao's "Solving Mathematical Problems":

Suppose the teacher can run six times as fast as the boy can swim. Now show that the boy cannot escape. (Hint: Draw an imaginary square of sidelength 1/6 unit centred at $O$. Once the boy leaves that square, the teacher gains the upper hand.)

Here $O$ is the center of the swimming pool. This question is a follow up on the previous one, **which is solved in the affirmative in the text**

(Taylor 1989, p. 34, Q2). In the centre of a square swimming pool is a boy, while his teacher (who cannot swim) is at one corner of the pool. The teacher can run three times faster than the boy can swim, but the boy can run faster than the teacher can. Can the boy escape from the teacher? (Assume both persons are infinitely manoeuvrable.)

---

**My attempt:**

Since the boy can always swim back into the small square of sidelength 1/6 centered at $O$, I can't see how to apply the hint properly. Also, since the student's path need not even be smooth (it was taken as a polygonal chain in the previous question) I'm having difficulties writing data down clearly.

Any help would be appreciated. Thanks.

- [geometry][6]
- [analytic-geometry][7]
- [curves][8]

[Share][9]

Cite

Follow

asked Dec 2, 2015 at 2:40

[image: user1337's user avatar]

[10]

[user1337][10] user1337

24.3k 7 7 gold badges 62 62 silver badges 152 152 bronze badges

$\endgroup$

18

-

$\begingroup$ Indeed the boy can stay in the pool indefinitely, but this doesn't amount to an "escape" in the sense of the earlier problem. $\endgroup$

– [hardmath][11]

Dec 2, 2015 at 2:47

-

$\begingroup$ @hardmath I understand what you're saying, but the hint implies that teacher should watch for the time where the student leaves the small square, and my problem is that he (the teacher) can never know when the student leaves that square for the last time. $\endgroup$

– [user1337][10]

Dec 2, 2015 at 2:49

-

1

$\begingroup$ @SamWeatherhog Even in the "3 times faster" case, swimming to the opposite corner is too slow for the student. $\endgroup$

– [user1337][10]

Dec 2, 2015 at 3:01

-

7

$\begingroup$*Suppose the teacher can run six times as fast as the boy can swim. Now show that the boy cannot escape.*Is that really all the information? What shape does the swimming pool have? What are their starting positions? $\endgroup$

– [Eric S.][12]

Dec 18, 2015 at 8:16

-

1

$\begingroup$ @EricS. As I've written above, this question is a follow up question on the one where the shape of the pool and the initial positions are defined. $\endgroup$

– [user1337][10]

Dec 18, 2015 at 8:26

| Show **13**more comments

## 4 Answers 4

Sorted by: [Reset to default][13]

Highest score (default) Date modified (newest first) Date created (oldest first)

8

+200

[14]

$\begingroup$

# Definitions and assumptions (without loss of generality)

-

Without loss of generality, we can consider the teacher is on the bottom half corner (we know the teacher is in a corner and the problem is symmetrical).

-

Lets call **the inner square**the square of 1/6 unit of side, centered at the origin.

-

It takes at least $6\times \frac{1}{12} = \frac{1}{2}$ unit of time for the kid to reach the side of the inner square.

**In that time, the teacher goes to the center of the bottom side of the pool, no matter where the boy goes.**

When the kid leaves the inner square, teacher always go as close as possible to the kid. If the kid goes back inside the inner square, the teacher goes back to his original position.

# Solving the problem

We will now show that in this situation, the boy cannot escape.

## Case 1 : The boy exits the inner square at its bottom square

-

Obviously, the boy can't escape by the bottom side of the pool, since the teacher is here.

-

If he tries to escape by one side, it will take at least $6\times 5/12 = 2.5$ units of time. The teacher can be anywhere on the side in 1.5 unit of time.

-

If he tries to escape by the top, it will take at least $6\times 7/12 = 3.5$ units of time. The teacher can be anywhere on the top in 2.5 units of time.

## Case 2 : The boy exits the inner square by one side (for example, the right side).

-

Again, the boy can't escape by the bottom because the teacher is here.

-

If the boy tries to escape on the right side, it will take at least $6\times 5/12 = 2.5$ units of time. The teacher can be anywhere on the side in 1.5 unit of time.

-

If the boy tries to escape on the left side, it will take at least $6\times 7/12 = 3.5$ units of time. The teacher can be anywhere on the side in 3.5 unit of time, even if he start by going through the right.

-

If the boy tries to escape on the top side , it will take at least $6\times 5/12 = 2.5$ units of time. The teacher can be anywhere on the side in 2.5 unit of time.

## Case 3 : The boy exits on the top side

If the boy exits the inner square on the right half of the top, then, the teacher goes right. If the boy exits on the left half, the teacher goes left.

For the sake of the argument, let's say the boy exits the inner square on the right side (the situation is symmetric if he exits on the left).

-

The boy can't escape by the bottom (obvious).

-

If the boy tries to escape on the right side, it will take at least $6\times 5/12 = 2.5$ units of time. The teacher can be anywhere on the side in 1.5 unit of time.

-

If the boy tries to escape on the top side, it will take at least $6\times 5/12 = 2.5$ units of time. The teacher can be anywhere on the side in 2.5 unit of time.

-

If the boy tries to escape on the top half of the left side, it will take him at least $6\times 1/2 = 3$ units of time. The teacher can be on the top half of the left side in 3 units of time, even if he starts going on the right.

-

If the boy tries to escape on the bottom half of the left side of the pool. (this one is a bit more tricky)

Let $x$ be the distance between the escape point and the middle of the left side. The minimum time the kid takes to go there is :

$$T_{kid} = 6\times \sqrt{0.5^2 + (\frac{1}{12}+x)^2}$$

The time the teacher takes to get there, if he starts by going right is :

$$T_{teacher} = 3+x$$

We can show that $T_{kid}\geq T_{teacher}$, or

$$f(x) = T_{kid}- T_{teacher} = 6\times \sqrt{0.5^2 + (\frac{1}{12}+x)^2} - 3- x \geq 0$$

It could be done analytically, but I used wolfram alpha [here][15] to show it.

# Conclusion

Since wherever the kid exits the inner square, he loses, the proof is complete.

[Share][16]

Cite

Follow

[edited Dec 25, 2015 at 14:44][17]

[image: Mike's user avatar]

[18]

[Mike][18]

533 1 1 gold badge 4 4 silver badges 12 12 bronze badges

answered Dec 24, 2015 at 5:45

[image: fredq's user avatar]

[19]

[fredq][19] fredq

950 5 5 silver badges 9 9 bronze badges

$\endgroup$

2

-

1

$\begingroup$ This is excellent, very well done, and a great first answer on the site! $\endgroup$

– [Stella Biderman][20]

Dec 24, 2015 at 7:03

-

$\begingroup$ it was not so clear in the context, but he considered the swimming pool an unit square. $\endgroup$

– [Mike][18]

Dec 25, 2015 at 14:26

Add a comment |

2

[21]

$\begingroup$

The boy has no incentive to change direction since he loses time.

Which direction should he pick?

- In the 6×speed case, no matter which direction the boy chooses, the teacher can get there faster.
- In the 3×speed case, there are numerous directions where the boy can escape... just not the opposite diagonal corner.

[image: enter image description here][image: enter image description here]

[Share][22]

Cite

Follow

answered Dec 24, 2015 at 23:38

[image: cactus314's user avatar]

[23]

[cactus314][23] cactus314

24.4k 4 4 gold badges 40 40 silver badges 113 113 bronze badges

$\endgroup$

1

-

$\begingroup$ in the 3x speed, the boy can't escape if he goes straight to the opposite diagonal corner. It takes him $3\times \sqrt{0.5^2 + 0.5 ^2} \approx 2.1$ unit of time. The teacher gets there in 2 $\endgroup$

– [fredq][19]

Dec 25, 2015 at 7:37

Add a comment |

0

[24]

$\begingroup$

Consider a square centred at $(0,0)$ in the Cartesian plane. Without loss of generality let the square have a side length of 2 units.

Suppose that the teacher is at vertex $(1,1)$.

Assume that there exists some point on the perimeter of the square with coordinates $(x,y)$ such that the student will arrive here before the teacher and so will escape. Due to the symmetry of the square, we can assume without loss of generality that $y=-1$. And so our point becomes $(x,-1)$.

Let the boy swim at $k$ $unit/s$ and let the teacher run at $6k$ $unit/s$

Then we have,

Distance from teacher= $2+(1-x)$ (distance travelled vertically down +distance travelled horizontally left towards point).

Distance from the student=$\sqrt{x^{2}+1}$

Time taken for teacher to reach this point $(t_{1})= \frac{3-x}{6k}$.

Time taken for student to reach this point $(t_{2})= \frac{\sqrt{x^{2}+1}}{k}$.

In order for the student to escape $(t_{1})>(t_{2})$,

hence, $\frac{3-x}{6k}>\frac{\sqrt{x^{2}+1}}{k}$.

Noting that $-1<x<0$ (i.e. the point we are looking for is in the third quadrant) reveals that this inequality does not hold in this interval.

[Share][25]

Cite

Follow

[edited Dec 24, 2015 at 5:32][26]

answered Dec 24, 2015 at 5:14

[image: J.Gudal's user avatar]

[27]

[J.Gudal][27] J.Gudal

1,313 10 10 silver badges 18 18 bronze badges

$\endgroup$

1

-

$\begingroup$ It would work, in that case we would require $\frac{3-x}{3k}>\frac{\sqrt{x^{2}+1}}{k}$ which is satisfied at $(-0.5,-1)$. $\endgroup$

– [J.Gudal][27]

Dec 24, 2015 at 5:47

Add a comment |

0

[28]

$\begingroup$

Consider a square of side length 1 unit. Consider 2 cases:

Case 1. Boy is at centre. Teacher is at corner. Boy swims to opposite corner. Distance for boy is 2/sqrt2 = 0.71 Distance for teacher is 1 + 1 = 2 But teacher is 6x faster. Therefore teacher beats boy.

Case 2. Boy is at centre. Teacher is at middle of a side. Boy swims to opposite side. Distance for boy is 1/2 = 0.5 Distance for teacher is 1/2 + 1 + 1/2 = 2 But teacher is 6x faster. Therefore teacher beats boy.

Boy can never escape.

[Share][29]

Cite

Follow

answered Dec 24, 2015 at 19:53

[image: A.Prof Bill Walter's user avatar]

[30]

[A.Prof Bill Walter][30] A.Prof Bill Walter

26 3 3 bronze badges

$\endgroup$

Add a comment |

## You must [log in][31] to answer this question.

##

Not the answer you're looking for? Browse other questions tagged

- [geometry][6]
- [analytic-geometry][7]
- [curves][8]

.

- The Overflow Blog
-

[Defining socially responsible AI: How we select partners][32]

- Featured on Meta
-

[Upcoming privacy updates: removal of the Activity data section and Google...][33]

-

[Changing how community leadership works on Stack Exchange: a proposal and...][34]

#### Linked

[1][35] [Will the boy outwit the teacher in this way?][36]

[14][37] [Can the boy escape the teacher for a regular $n$-gon?][38]

#### Related

[3][39] [Constructing a square whose sides contain 4 given points][40]

[0][41] [prove that the quadrilateral $ABCD$ is a square][42]

[14][37] [Can the boy escape the teacher for a regular $n$-gon?][43]

[3][44] [Prove that the perpendicular from the origin upon the straight line][45]

[0][46] [Find the tangent line that passes through the point that doesn't lie on the given line][47]

[1][48] [Given $3$ lines, prove that $3$ points cannot be collinear][49]

[4][50] [Calculate the angle of Escape][51]

#### [Hot Network Questions][52]

-

[How to paint a window in my house yellow? [image processing with Mathematica]][53]
-

[Reading tips on longitudinal mixed models and mediation][54]
-

[Leetcode 3sum problem solution][55]
-

[Why did so many Ks change into Js and Qs?][56]
-

[Who was Bilbo's / Frodo's mithril chain mail made for?][57]
-

[Solving PDEs as ODEs under certain conditions][58]
-

[How can current phase shift be 90 degrees behind voltage just "inside the capacitor" on an RC series circuit but be in phase in the resistor?][59]
-

[Geonodes: How to Set Material for every material in this remeshed mesh?][60]
-

[Any negative effects of using audio ADC for instrumentation use][61]
-

[Which city is on the pic][62]
-

[Determine whether the counterfeit coin is heavier or lighter in two weighings on a standard balance][63]
-

[Proof of the put-call parity formula][64]
-

[Is all this modal theory for guitarists truly necessary?][65]
-

[Why doesn't Washington want to enact a law to punish all currency manipulators, including China?][66]
-

[Energy of Transmit Pulses in Digital Communication][67]
-

[Why do electromagnets have itty bitty wires?][68]
-

[Hilbert's sixth problem and QFT description][69]
-

[How to calculate advantage/disadvantage with multiple dice (e.g. 3d6, 2d10, etc.)][70]
-

[Cite an article from an old journal][71]
-

[What's the translation of "ratcheting" in French to designate a sequencing technique used in music production?][72]
-

[How can I union two lists in the given way?][73]
-

[Book about a young girl with a special necklace who time travels to England during the reign of Henry VIII][74]
-

[Can I use healing on a construct?][75]
-

[What is the lady saying between 0:45 and 0:47 in this radio episode by SRF?][76]

more hot questions

[Question feed][77]


## Links

[1]: https://web.archive.org/web/20240304035301/https://stackoverflow.co/teams/
[2]: /web/20240304035301/https://math.stackexchange.com/questions/1555855/prove-that-the-boy-cannot-escape-the-teacher
[3]: /web/20240304035301/https://math.stackexchange.com/questions/ask
[4]: ?lastactivity
[5]: /web/20240304035301/https://math.stackexchange.com/posts/1555855/timeline
[6]: /web/20240304035301/https://math.stackexchange.com/questions/tagged/geometry
[7]: /web/20240304035301/https://math.stackexchange.com/questions/tagged/analytic-geometry
[8]: /web/20240304035301/https://math.stackexchange.com/questions/tagged/curves
[9]: /web/20240304035301/https://math.stackexchange.com/q/1555855
[10]: /web/20240304035301/https://math.stackexchange.com/users/62839/user1337
[11]: /web/20240304035301/https://math.stackexchange.com/users/3111/hardmath
[12]: /web/20240304035301/https://math.stackexchange.com/users/263514/eric-s
[13]: /web/20240304035301/https://math.stackexchange.com/questions/1555855/prove-that-the-boy-cannot-escape-the-teacher?answertab=scoredesc#tab-top
[14]: /web/20240304035301/https://math.stackexchange.com/posts/1587471/timeline
[15]: https://web.archive.org/web/20240304035301/http://www.wolframalpha.com/input/?i=plot%206*%28%20sqrt%280.25%20%2B%20%28x%2B1%2F12%29%5E2%29%29%20-3-x%20from%200%20to%200.5
[16]: /web/20240304035301/https://math.stackexchange.com/a/1587471
[17]: /web/20240304035301/https://math.stackexchange.com/posts/1587471/revisions
[18]: /web/20240304035301/https://math.stackexchange.com/users/23412/mike
[19]: /web/20240304035301/https://math.stackexchange.com/users/297080/fredq
[20]: /web/20240304035301/https://math.stackexchange.com/users/123230/stella-biderman
[21]: /web/20240304035301/https://math.stackexchange.com/posts/1588216/timeline
[22]: /web/20240304035301/https://math.stackexchange.com/a/1588216
[23]: /web/20240304035301/https://math.stackexchange.com/users/4997/cactus314
[24]: /web/20240304035301/https://math.stackexchange.com/posts/1587453/timeline
[25]: /web/20240304035301/https://math.stackexchange.com/a/1587453
[26]: /web/20240304035301/https://math.stackexchange.com/posts/1587453/revisions
[27]: /web/20240304035301/https://math.stackexchange.com/users/225386/j-gudal
[28]: /web/20240304035301/https://math.stackexchange.com/posts/1588095/timeline
[29]: /web/20240304035301/https://math.stackexchange.com/a/1588095
[30]: /web/20240304035301/https://math.stackexchange.com/users/300677/a-prof-bill-walter
[31]: /web/20240304035301/https://math.stackexchange.com/users/login?ssrc=question_page&amp;returnurl=https%3a%2f%2fmath.stackexchange.com%2fquestions%2f1555855
[32]: https://web.archive.org/web/20240304035301/https://stackoverflow.blog/2024/02/29/defining-socially-responsible-ai-how-we-select-api-partners/
[33]: https://web.archive.org/web/20240304035301/https://meta.stackexchange.com/questions/396794/upcoming-privacy-updates-removal-of-the-activity-data-section-and-google-conver
[34]: https://web.archive.org/web/20240304035301/https://meta.stackexchange.com/questions/396924/changing-how-community-leadership-works-on-stack-exchange-a-proposal-and-rough
[35]: /web/20240304035301/https://math.stackexchange.com/q/1762499
[36]: /web/20240304035301/https://math.stackexchange.com/questions/1762499/will-the-boy-outwit-the-teacher-in-this-way?noredirect=1
[37]: /web/20240304035301/https://math.stackexchange.com/q/1762665
[38]: /web/20240304035301/https://math.stackexchange.com/questions/1762665/can-the-boy-escape-the-teacher-for-a-regular-n-gon?noredirect=1
[39]: /web/20240304035301/https://math.stackexchange.com/q/1512824
[40]: /web/20240304035301/https://math.stackexchange.com/questions/1512824/constructing-a-square-whose-sides-contain-4-given-points
[41]: /web/20240304035301/https://math.stackexchange.com/q/1650388
[42]: /web/20240304035301/https://math.stackexchange.com/questions/1650388/prove-that-the-quadrilateral-abcd-is-a-square
[43]: /web/20240304035301/https://math.stackexchange.com/questions/1762665/can-the-boy-escape-the-teacher-for-a-regular-n-gon
[44]: /web/20240304035301/https://math.stackexchange.com/q/2437182
[45]: /web/20240304035301/https://math.stackexchange.com/questions/2437182/prove-that-the-perpendicular-from-the-origin-upon-the-straight-line
[46]: /web/20240304035301/https://math.stackexchange.com/q/3716507
[47]: /web/20240304035301/https://math.stackexchange.com/questions/3716507/find-the-tangent-line-that-passes-through-the-point-that-doesnt-lie-on-the-give
[48]: /web/20240304035301/https://math.stackexchange.com/q/4065862
[49]: /web/20240304035301/https://math.stackexchange.com/questions/4065862/given-3-lines-prove-that-3-points-cannot-be-collinear
[50]: /web/20240304035301/https://math.stackexchange.com/q/4653882
[51]: /web/20240304035301/https://math.stackexchange.com/questions/4653882/calculate-the-angle-of-escape
[52]: https://web.archive.org/web/20240304035301/https://stackexchange.com/questions?tab=hot
[53]: https://web.archive.org/web/20240304035301/https://mathematica.stackexchange.com/questions/299926/how-to-paint-a-window-in-my-house-yellow-image-processing-with-mathematica
[54]: https://web.archive.org/web/20240304035301/https://stats.stackexchange.com/questions/641681/reading-tips-on-longitudinal-mixed-models-and-mediation
[55]: https://web.archive.org/web/20240304035301/https://codereview.stackexchange.com/questions/290842/leetcode-3sum-problem-solution
[56]: https://web.archive.org/web/20240304035301/https://chinese.stackexchange.com/questions/57775/why-did-so-many-ks-change-into-js-and-qs
[57]: https://web.archive.org/web/20240304035301/https://scifi.stackexchange.com/questions/285841/who-was-bilbos-frodos-mithril-chain-mail-made-for
[58]: https://web.archive.org/web/20240304035301/https://math.stackexchange.com/questions/4874573/solving-pdes-as-odes-under-certain-conditions
[59]: https://web.archive.org/web/20240304035301/https://electronics.stackexchange.com/questions/704699/how-can-current-phase-shift-be-90-degrees-behind-voltage-just-inside-the-capaci
[60]: https://web.archive.org/web/20240304035301/https://blender.stackexchange.com/questions/314021/geonodes-how-to-set-material-for-every-material-in-this-remeshed-mesh
[61]: https://web.archive.org/web/20240304035301/https://electronics.stackexchange.com/questions/704651/any-negative-effects-of-using-audio-adc-for-instrumentation-use
[62]: https://web.archive.org/web/20240304035301/https://travel.stackexchange.com/questions/187686/which-city-is-on-the-pic
[63]: https://web.archive.org/web/20240304035301/https://puzzling.stackexchange.com/questions/125809/determine-whether-the-counterfeit-coin-is-heavier-or-lighter-in-two-weighings-on
[64]: https://web.archive.org/web/20240304035301/https://quant.stackexchange.com/questions/78553/proof-of-the-put-call-parity-formula
[65]: https://web.archive.org/web/20240304035301/https://music.stackexchange.com/questions/135093/is-all-this-modal-theory-for-guitarists-truly-necessary
[66]: https://web.archive.org/web/20240304035301/https://politics.stackexchange.com/questions/86096/why-doesnt-washington-want-to-enact-a-law-to-punish-all-currency-manipulators
[67]: https://web.archive.org/web/20240304035301/https://dsp.stackexchange.com/questions/93167/energy-of-transmit-pulses-in-digital-communication
[68]: https://web.archive.org/web/20240304035301/https://electronics.stackexchange.com/questions/704591/why-do-electromagnets-have-itty-bitty-wires
[69]: https://web.archive.org/web/20240304035301/https://mathoverflow.net/questions/466243/hilberts-sixth-problem-and-qft-description
[70]: https://web.archive.org/web/20240304035301/https://rpg.stackexchange.com/questions/210704/how-to-calculate-advantage-disadvantage-with-multiple-dice-e-g-3d6-2d10-etc
[71]: https://web.archive.org/web/20240304035301/https://academia.stackexchange.com/questions/208195/cite-an-article-from-an-old-journal
[72]: https://web.archive.org/web/20240304035301/https://french.stackexchange.com/questions/54282/whats-the-translation-of-ratcheting-in-french-to-designate-a-sequencing-techn
[73]: https://web.archive.org/web/20240304035301/https://mathematica.stackexchange.com/questions/299865/how-can-i-union-two-lists-in-the-given-way
[74]: https://web.archive.org/web/20240304035301/https://scifi.stackexchange.com/questions/285913/book-about-a-young-girl-with-a-special-necklace-who-time-travels-to-england-duri
[75]: https://web.archive.org/web/20240304035301/https://rpg.stackexchange.com/questions/210695/can-i-use-healing-on-a-construct
[76]: https://web.archive.org/web/20240304035301/https://german.stackexchange.com/questions/76611/what-is-the-lady-saying-between-045-and-047-in-this-radio-episode-by-srf
[77]: /web/20240304035301/https://math.stackexchange.com/feeds/question/1555855
