<!-- source: https://web.archive.org/web/2023/https://math.stackexchange.com/questions/47477/number-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n | converted from HTML -->

sequences and series - Number of occurrences of the digit 1 in the numbers from 0 to n - Mathematics Stack Exchange

### [current community][1]

-

[blog][2] [chat][3]

[Mathematics][1]
-

[Mathematics Meta][4]

### your communities

[Sign up][5] or [log in][6] to customize your list.

### [more stack exchange communities][7]

[company blog][8]

[Stack Exchange][9] Inbox Reputation and Badges

[sign up][10] [log in][11] [tour][12] help

- [Tour Start here for a quick overview of the site][12]
- [Help Center Detailed answers to any questions you might have][13]
- [Meta Discuss the workings and policies of this site][14]
- [About Us Learn more about Stack Overflow the company][15]
- [Business Learn more about hiring developers or posting ads with us][16]

[Mathematics][17]

- [Questions][18]
- [Tags][19]
- [Users][20]
- [Badges][21]
- [Unanswered][22]

- [Ask Question][23]

_

Mathematics Stack Exchange is a question and answer site for people studying math at any level and professionals in related fields. Join them; it only takes a minute:

[Sign up][24]

**Here's how it works:**

1. Anybody can ask a question
2. Anybody can answer
3. The best answers are voted up and rise to the top

# [Number of occurrences of the digit 1 in the numbers from 0 to n][25]

up vote 10 down vote favorite

**2**

 |

We have a function:

$f(n)$ = number of occurrences of the digit $1$ in the numbers from $0$ to $n$.

Example: $f(12) = 5$

It is obvious that $f(1)=1.$

Question: Which is the next number for which $f(n) = n$?

[sequences-and-series][26]

[share][27] | cite | [improve this question][28]

 |

[edited Jun 24 '11 at 22:24][29]

[30]

[Nana][30]

4,193 2 18 34

 |

asked Jun 24 '11 at 21:49

[31]

[Mark Zimmers][31]

78 1 2 6

 |

 |

 |

 |  |

 |

11111111111111111111111111111111111287981 – [The Chaz 2.0][32] Jun 24 '11 at 21:57

 |

 |  |

 |

Can I write a program to solve it? – [usul][33] Jun 24 '11 at 21:58

 |

1 |  |

 |

@S4M: count the 1 in 12 as well. – [Isaac][34] Jun 24 '11 at 22:05

 |

1 |  |

 |

@Mark: The number in my first comment was meant to stir the pot; I don't think there is another solution. – [The Chaz 2.0][32] Jun 24 '11 at 22:16

 |

1 |  |

 |

Wouldn't potential solutions to this be more likely/frequent, say, in base 2? ;-) – [amWhy][35] Jun 24 '11 at 23:22

 |

| show **14**more comments

 |

## 3 Answers 3

[active][36] [oldest][37] [votes][38]

up vote 8 down vote accepted

 |

So I dug up my notes on this problem (for those interested this is [project euler][39] problem [# 156][40]) There is an analytical form for the solution to this problem (but alas, even the analytical form is too slow to solve the *big*problem, which requires finding ALL numbers that satisfy this condition for ALL digits 1-9). I will state my result first (to avoid hiding it in the text) and provide explanation for it after.

**SOLUTION**

Define a *list representation*of a number $n$ to be (following a notation I borrowed from continued fractions)

$$n = r_k*10^k + r_{k-1}*10^{k-1} + ... + r_0*10^0 \equiv [r_k,r_{k-1},...,r_0]$$ The function $f(d,n)$ which gives the number of occurances of a digit $d$ up to the number $n$ is given by $$ f(d,n) = \sum_{j=0}^k\left(\sum_{i=0}^{r_j} (10^j\delta_{i-1,d})+ r_jE(j) +\delta_{r_j,d}(n[j:]+1)\right)$$

where the notation $n[j:]$ is used to signify the number formed by the last $j$ digits (e.g. for $n=1234=[1,2,3,4]$, $n[1] = 4$, $n[3] = 234$) and $E(j) = j*10^{j-1}$

Typing this into mathematica (and checking ($f(1,n) = n$ gives the next result of $\mathbf{199981}$).

*NOTE*: This can be generalized even further to any base $B$ by replacing occurrences of $10^k$ with $B^k$

**MOTIVATION**

First observe that in the number 0-9 any digit appears only 1 time.

In the numbers 0-99 any digit appears 10 + 10 times (10 times as the ones digit and 10 times in the range x0-x9)

In the numbers 0-999 any digit appears 20*10+100 = 300 times (20 times in each range of 100+ plus 100 in the range x00-x99)

It is not difficult to prove that this pattern continues, for any number given as $10^k-1$ there are $k*10^{k-1}$ appearances of *any*digit in that range.

This motivates my definition of the function

$$E(j) = j*10^{j-1}$$

However, the number given is unlikely to be as nice as $10^k-1$ we have to learn a clever way to add up the parts of that range. For a number (given in the above notation) like $[4,0,0,0]$. We see that the range $0-999$ occurs 4 times ($0-999$,$1000-1999$,$2000-2999$,$3000-3999$. So we are left with $4*E(3) = 1200$ occurrences of the digit $1$ (this motivates the $r_jE(j)$ term). However, in the range 1000-1999 the digit one occurs an extra 1000 (or $10^j$) times, this extra term only happens if $r_j$ is greater then the digit we are summing over (e.g. if we are adding occurrences of the digit $9$ the answer would be 1200 and not 2200), the best way I could think of to express this conditional statement analytically was with the sum $\sum_{i=1}^{r_j}(10^j\delta_{i-1,d})$

Calculating a number like $[4,1,2,4]$ is not much more difficult, we simply iterate over the sequence $[4,0,0,0]$, $[3,0,0]$, $[2,0]$,$[4]$ following the formula in the previous paragraph. However, the method above will miscount because it ignores the extra occurrence of the digit $1$ in the range $4100-4124$. So at every step of the iteration we have to make sure there aren't any tails that we are forgetting to count, which motivates the $\delta_{r_j,d}(n[j:]+1)$ term.

[share][41] | cite | [improve this answer][42]

 |

[edited Jun 27 '11 at 17:04][43]

 |

answered Jun 27 '11 at 16:54

[44]

[crasic][44]

1,678 2 15 26

 |

 |

 |

 |  |

 |

Hi ! I was working over this problem 156, and came up with a similar solution (wrote a program) - but i have been struggling to find out HOW to know when to stop.. How does one know that we've exhausted all possible solutions for [f(d,n) - n = 0] ?? My program almost ran out of memory trying to figure out a pattern !! – [trinity][45] Aug 1 '13 at 12:56

 |

add a comment |

 |

up vote 6 down vote

 |

Ok this is simple to do with Mathematica.

```
For[i = 0; j = 0, i <= 200000,
 i++, j += (Plus @@ Cases[IntegerDigits[i], 1]); If[j == i, Print[i]]]
```

The result is

```
0,1,199981,199982,199983,...,199990,200000
```

Therefore the number you search has to be 199981.

[share][46] | cite | [improve this answer][47]

 |

[edited Jun 25 '11 at 20:18][48]

 |

answered Jun 24 '11 at 22:27

[49]

[Listing][49]

10.3k 3 25 55

 |

 |

 |

 |  |

 |

While this is a correct way to approach this particular question, the *actual*problem in question (which is a project Euler problem) requires the sum total of **all**numbers that satisfy this condition for all digits 1-10. Not so easy (or fast) do with this brute force method (where do you set the upper search limit for instance?). – [crasic][44] Jun 24 '11 at 23:26

 |

 |  |

 |

You can easily make it stop after it finds the first wanted number. I leave this modification to you. I agree that with some thoughts you could still fasten up the calculation a lot (factor 100 at least). – [Listing][49] Jun 25 '11 at 7:21

 |

 |  |

 |

I dont see why 199984, 199985,...,199990 are not solutions as well as we have $f(199984)=f(199983)+1=199984$ and same for every number until 199991. – [S4M][50] Jun 25 '11 at 19:53

 |

 |  |

 |

You are right I didn't mark properly that I left out the other solutions, now its correct. – [Listing][49] Jun 25 '11 at 20:19

 |

1 |  |

 |

*fasten up the calculation*I like it. How about *slowen down the calculation*? – [GEdgar][51] Jun 25 '11 at 20:23

 |

| show **1**more comment

 |

up vote 1 down vote

 |

I think I have the beginning of an idea to solve this. We can start by noticing that $f(10^{n+1}-1)= 1+10^n+10\times f(10^n-1)$ because when you list all the numbers from 1 to $10^{n+1}$ you get: 1... $10^n-1$, $10^n$,..., 1999...99, 20...00,...$10^{n+1}-1$. from $10^n$ to 1999...99 you can see $10^n+f(n)+1$ the digit '1', and from 20...00 to $10^{n+1}-1$ you get $9\times f(10^n-1)$ the digity '1'. So let's call $u_n=10^n-1$ and $v_n=f(u_n)$.

I can see that $u_9 >v_9$ and $u_{10} < v_{10}$, so the anwswer should be in beetween (or at least smaller than $10^{10}-1$.

[share][52] | cite | [improve this answer][53]

 |

answered Jun 24 '11 at 23:09

[50]

[S4M][50]

708 3 9

 |

 |

 |

 |  |

 |

$f(10^{n+1})=(n+1)10^n$. – [André Nicolas][54] Jun 25 '11 at 5:20

 |

 |  |

 |

hmm that's true. So $10^{9+1}$ is also a solution. This problem keeps fascinating me, I want to find ALL the solutions to $f(n)=n$ ! – [S4M][50] Jun 26 '11 at 8:53

 |

 |  |

 |

How many solutions are there to $f(n) = n!$ ?? $$$$ :) – [The Chaz 2.0][32] Jun 27 '11 at 17:25

 |

add a comment |

 |

## Not the answer you're looking for? Browse other questions tagged [sequences-and-series][26] or [ask your own question][23].

asked

 |

**5 years ago**

 |

viewed

 |

**8994 times**

 |

active

 |

**[4 years ago][55]**

 |

[image: Computational Science at Stack Exchange] [56]

15 votes · [comment][57] · [stats][58]

#### Related

[5][59] [$n$-th digit in the sequence of natural numbers][60]

[5][61] [Formula for the sequence formed by the digits of the natural numbers][62]

[1][63] [How many $a$-nary sequences of length $b$ never have $c$ consecutive occurrences of a digit?][64]

[0][65] [how many variables are there from 9 digits excluding repeat numbers][66]

[2][67] [Counts and skips the numbers that have digits divisible by 3 (change in base method)][68]

[0][69] [Definition of co-occurrence for sequences?][70]

[3][71] [Number of natural numbers made from the digits 1, 2 and 3 wherein the sum of their digits is equal to n.][72]

[0][73] [Mathematical notation for a number to contain all of the digits from a set][74]

[0][75] [With pen and paper, digits that follow the first occurrence of a sequence in pi][76]

[2][77] [How can it be proven that a certain number of integers has a certain number of digits?][78]

#### [Hot Network Questions][79]

-

[I need to know how to approach replacing md5 for transporting Unity game data to a remote server][80]
-

[Finite surjective morphism of normal varieties and Galois coverings][81]
-

[Would a suit that acts as extra-cardiovascular system allow you to run indefinitely?][82]
-

[Equivalent of the Dutch phrase "take someone down a notch"][83]
-

[Is there a single-word replacement for the phrase "friendly verbal duel"?][84]
-

[Should we kill the features that users are not using frequently, to improve performance?][85]
-

[What's really meant by context-free in the term context-free grammar?][86]
-

[How to show blank (black) screen via command line (SSH conenction)?][87]
-

[Smallest Prime with a Twist (A068103)][88]
-

[Is there a proper name for this kind of toothed disk?][89]
-

[Can a company charge you for services never requested or received?][90]
-

[Is this pie graph describing US government spending accurate?][91]
-

[Are CVE counts a good indicator of a software's security?][92]
-

[Physically, how do dragons grasp and *transport* the contents of their hoards?][93]
-

[Taking my mate (tea) on the plane?][94]
-

[Why does stacking polarizers of the same angle still block more and more light?][95]
-

[Is there a "Reina-Valera" only movement?][96]
-

[OD&D said it could be played with 20-50 players and one referee. How was that expected to work and still be fun?][97]
-

[How to enter the OGL into my work][98]
-

[Why is this vector field curl-free?][99]
-

[\underline rule position][100]
-

[How is an Elastic IP address different from a static IP address?][101]
-

[Should Failed Login Attempts Be Logged][102]
-

[2016 Time Capsule String: How Versatile Is Your Language?][103]

more hot questions

[question feed][104]

[about us][15] [tour][12] [help][13] [blog][105] [chat][3] [data][106] [legal][107] [privacy policy][108] [work here][109] [advertising info][110] mobile**[contact us][111]****[feedback][4]**

Technology  | Life / Arts  | Culture / Recreation  | Science  | Other  |

1. [Stack Overflow][112]
2. [Server Fault][113]
3. [Super User][114]
4. [Web Applications][115]
5. [Ask Ubuntu][116]
6. [Webmasters][117]
7. [Game Development][118]
8. [TeX - LaTeX][119]

 |

1. [Software Engineering][120]
2. [Unix & Linux][121]
3. [Ask Different (Apple)][122]
4. [WordPress Development][123]
5. [Geographic Information Systems][124]
6. [Electrical Engineering][125]
7. [Android Enthusiasts][126]
8. [Information Security][127]

 |

1. [Database Administrators][128]
2. [Drupal Answers][129]
3. [SharePoint][130]
4. [User Experience][131]
5. [Mathematica][132]
6. [Salesforce][133]
7. [ExpressionEngine® Answers][134]
8. [Cryptography][135]

 |

1. [Code Review][136]
2. [Magento][137]
3. [Signal Processing][138]
4. [Raspberry Pi][139]
5. [Programming Puzzles & Code Golf][140]
6. [more (7)][141]

 |

1. [Photography][142]
2. [Science Fiction & Fantasy][143]
3. [Graphic Design][144]
4. [Movies & TV][145]
5. [Music: Practice & Theory][146]
6. [Seasoned Advice (cooking)][147]
7. [Home Improvement][148]
8. [Personal Finance & Money][149]

 |

1. [Academia][150]
2. [more (8)][151]

 |

1. [English Language & Usage][152]
2. [Skeptics][153]
3. [Mi Yodeya (Judaism)][154]
4. [Travel][155]
5. [Christianity][156]
6. [English Language Learners][157]
7. [Japanese Language][158]
8. [Arqade (gaming)][159]

 |

1. [Bicycles][160]
2. [Role-playing Games][161]
3. [Anime & Manga][162]
4. [Motor Vehicle Maintenance & Repair][163]
5. [more (17)][164]

 |

1. [MathOverflow][165]
2. [Mathematics][1]
3. [Cross Validated (stats)][166]
4. [Theoretical Computer Science][167]
5. [Physics][168]
6. [Chemistry][169]
7. [Biology][170]
8. [Computer Science][171]

 |

1. [Philosophy][172]
2. [more (3)][173]

 |

1. [Meta Stack Exchange][174]
2. [Stack Apps][175]
3. [Area 51][176]
4. [Stack Overflow Talent][177]

 |

site design / logo © 2017 Stack Exchange Inc; user contributions licensed under [cc by-sa 3.0][178] with [attribution required][179]

rev 2017.1.3.1


## Links

[1]: //web.archive.org/web/20170104201629/http://math.stackexchange.com/
[2]: https://web.archive.org/web/20170104201629/http://math.blogoverflow.com/
[3]: https://web.archive.org/web/20170104201629/http://chat.stackexchange.com/?tab=site&amp;host=math.stackexchange.com
[4]: https://web.archive.org/web/20170104201629/http://meta.math.stackexchange.com/
[5]: https://web.archive.org/web/20170104201629/https://math.stackexchange.com/users/signup?ssrc=site_switcher&amp;returnurl=http%3a%2f%2fmath.stackexchange.com%2fquestions%2f47477%2fnumber-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n
[6]: https://web.archive.org/web/20170104201629/https://math.stackexchange.com/users/login?ssrc=site_switcher&amp;returnurl=http%3a%2f%2fmath.stackexchange.com%2fquestions%2f47477%2fnumber-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n
[7]: //web.archive.org/web/20170104201629/http://stackexchange.com/sites
[8]: https://web.archive.org/web/20170104201629/http://stackoverflow.blog/
[9]: //web.archive.org/web/20170104201629/http://stackexchange.com/
[10]: https://web.archive.org/web/20170104201629/https://math.stackexchange.com/users/signup?ssrc=head&amp;returnurl=http%3a%2f%2fmath.stackexchange.com%2fquestions%2f47477%2fnumber-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n
[11]: https://web.archive.org/web/20170104201629/https://math.stackexchange.com/users/login?ssrc=head&amp;returnurl=http%3a%2f%2fmath.stackexchange.com%2fquestions%2f47477%2fnumber-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n
[12]: /web/20170104201629/http://math.stackexchange.com/tour
[13]: /web/20170104201629/http://math.stackexchange.com/help
[14]: //web.archive.org/web/20170104201629/http://meta.math.stackexchange.com/
[15]: https://web.archive.org/web/20170104201629/http://stackoverflow.com/company/about
[16]: https://web.archive.org/web/20170104201629/https://www.stackoverflowbusiness.com/?ref=topbar_help
[17]: /web/20170104201629/http://math.stackexchange.com/
[18]: /web/20170104201629/http://math.stackexchange.com/questions
[19]: /web/20170104201629/http://math.stackexchange.com/tags
[20]: /web/20170104201629/http://math.stackexchange.com/users
[21]: /web/20170104201629/http://math.stackexchange.com/help/badges
[22]: /web/20170104201629/http://math.stackexchange.com/unanswered
[23]: /web/20170104201629/http://math.stackexchange.com/questions/ask
[24]: /web/20170104201629/http://math.stackexchange.com/users/signup?ssrc=hero&amp;returnurl=http%3a%2f%2fmath.stackexchange.com%2fquestions%2f47477%2fnumber-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n
[25]: /web/20170104201629/http://math.stackexchange.com/questions/47477/number-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n
[26]: /web/20170104201629/http://math.stackexchange.com/questions/tagged/sequences-and-series
[27]: /web/20170104201629/http://math.stackexchange.com/q/47477
[28]: /web/20170104201629/http://math.stackexchange.com/posts/47477/edit
[29]: /web/20170104201629/http://math.stackexchange.com/posts/47477/revisions
[30]: /web/20170104201629/http://math.stackexchange.com/users/4426/nana
[31]: /web/20170104201629/http://math.stackexchange.com/users/12545/mark-zimmers
[32]: /web/20170104201629/http://math.stackexchange.com/users/7850/the-chaz-2-0
[33]: /web/20170104201629/http://math.stackexchange.com/users/9759/usul
[34]: /web/20170104201629/http://math.stackexchange.com/users/72/isaac
[35]: /web/20170104201629/http://math.stackexchange.com/users/9003/amwhy
[36]: /web/20170104201629/http://math.stackexchange.com/questions/47477/number-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n?answertab=active#tab-top
[37]: /web/20170104201629/http://math.stackexchange.com/questions/47477/number-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n?answertab=oldest#tab-top
[38]: /web/20170104201629/http://math.stackexchange.com/questions/47477/number-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n?answertab=votes#tab-top
[39]: https://web.archive.org/web/20170104201629/http://projecteuler.net/
[40]: https://web.archive.org/web/20170104201629/http://projecteuler.net/index.php?section=problems&amp;id=156
[41]: /web/20170104201629/http://math.stackexchange.com/a/48016
[42]: /web/20170104201629/http://math.stackexchange.com/posts/48016/edit
[43]: /web/20170104201629/http://math.stackexchange.com/posts/48016/revisions
[44]: /web/20170104201629/http://math.stackexchange.com/users/1906/crasic
[45]: /web/20170104201629/http://math.stackexchange.com/users/88606/trinity
[46]: /web/20170104201629/http://math.stackexchange.com/a/47485
[47]: /web/20170104201629/http://math.stackexchange.com/posts/47485/edit
[48]: /web/20170104201629/http://math.stackexchange.com/posts/47485/revisions
[49]: /web/20170104201629/http://math.stackexchange.com/users/3123/listing
[50]: /web/20170104201629/http://math.stackexchange.com/users/12122/s4m
[51]: /web/20170104201629/http://math.stackexchange.com/users/442/gedgar
[52]: /web/20170104201629/http://math.stackexchange.com/a/47493
[53]: /web/20170104201629/http://math.stackexchange.com/posts/47493/edit
[54]: /web/20170104201629/http://math.stackexchange.com/users/6312/andr%c3%a9-nicolas
[55]: ?lastactivity
[56]: https://web.archive.org/web/20170104201629/http://meta.math.stackexchange.com/ads/ct/22452?url=http%3a%2f%2fscicomp.stackexchange.com&amp;s=98e90ec6b462429987a33cf045df2137063595353c906f69da4bd478120d193f
[57]: https://web.archive.org/web/20170104201629/http://meta.math.stackexchange.com/questions/22419#22452
[58]: https://web.archive.org/web/20170104201629/http://meta.math.stackexchange.com/ads/display/22419
[59]: /web/20170104201629/http://math.stackexchange.com/q/188812
[60]: /web/20170104201629/http://math.stackexchange.com/questions/188812/n-th-digit-in-the-sequence-of-natural-numbers
[61]: /web/20170104201629/http://math.stackexchange.com/q/309675
[62]: /web/20170104201629/http://math.stackexchange.com/questions/309675/formula-for-the-sequence-formed-by-the-digits-of-the-natural-numbers
[63]: /web/20170104201629/http://math.stackexchange.com/q/775863
[64]: /web/20170104201629/http://math.stackexchange.com/questions/775863/how-many-a-nary-sequences-of-length-b-never-have-c-consecutive-occurrences
[65]: /web/20170104201629/http://math.stackexchange.com/q/903305
[66]: /web/20170104201629/http://math.stackexchange.com/questions/903305/how-many-variables-are-there-from-9-digits-excluding-repeat-numbers
[67]: /web/20170104201629/http://math.stackexchange.com/q/1159969
[68]: /web/20170104201629/http://math.stackexchange.com/questions/1159969/counts-and-skips-the-numbers-that-have-digits-divisible-by-3-change-in-base-met
[69]: /web/20170104201629/http://math.stackexchange.com/q/1554737
[70]: /web/20170104201629/http://math.stackexchange.com/questions/1554737/definition-of-co-occurrence-for-sequences
[71]: /web/20170104201629/http://math.stackexchange.com/q/1594410
[72]: /web/20170104201629/http://math.stackexchange.com/questions/1594410/number-of-natural-numbers-made-from-the-digits-1-2-and-3-wherein-the-sum-of-the
[73]: /web/20170104201629/http://math.stackexchange.com/q/1783122
[74]: /web/20170104201629/http://math.stackexchange.com/questions/1783122/mathematical-notation-for-a-number-to-contain-all-of-the-digits-from-a-set
[75]: /web/20170104201629/http://math.stackexchange.com/q/2027142
[76]: /web/20170104201629/http://math.stackexchange.com/questions/2027142/with-pen-and-paper-digits-that-follow-the-first-occurrence-of-a-sequence-in-pi
[77]: /web/20170104201629/http://math.stackexchange.com/q/2027185
[78]: /web/20170104201629/http://math.stackexchange.com/questions/2027185/how-can-it-be-proven-that-a-certain-number-of-integers-has-a-certain-number-of-d
[79]: //web.archive.org/web/20170104201629/http://stackexchange.com/questions?tab=hot
[80]: https://web.archive.org/web/20170104201629/http://security.stackexchange.com/questions/147043/i-need-to-know-how-to-approach-replacing-md5-for-transporting-unity-game-data-to
[81]: https://web.archive.org/web/20170104201629/http://mathoverflow.net/questions/258747/finite-surjective-morphism-of-normal-varieties-and-galois-coverings
[82]: https://web.archive.org/web/20170104201629/http://worldbuilding.stackexchange.com/questions/66648/would-a-suit-that-acts-as-extra-cardiovascular-system-allow-you-to-run-indefinit
[83]: https://web.archive.org/web/20170104201629/http://english.stackexchange.com/questions/366388/equivalent-of-the-dutch-phrase-take-someone-down-a-notch
[84]: https://web.archive.org/web/20170104201629/http://english.stackexchange.com/questions/366244/is-there-a-single-word-replacement-for-the-phrase-friendly-verbal-duel
[85]: https://web.archive.org/web/20170104201629/http://ux.stackexchange.com/questions/103163/should-we-kill-the-features-that-users-are-not-using-frequently-to-improve-perf
[86]: https://web.archive.org/web/20170104201629/http://cs.stackexchange.com/questions/68231/whats-really-meant-by-context-free-in-the-term-context-free-grammar
[87]: https://web.archive.org/web/20170104201629/http://askubuntu.com/questions/868000/how-to-show-blank-black-screen-via-command-line-ssh-conenction
[88]: https://web.archive.org/web/20170104201629/http://codegolf.stackexchange.com/questions/105651/smallest-prime-with-a-twist-a068103
[89]: https://web.archive.org/web/20170104201629/http://diy.stackexchange.com/questions/105652/is-there-a-proper-name-for-this-kind-of-toothed-disk
[90]: https://web.archive.org/web/20170104201629/http://money.stackexchange.com/questions/74336/can-a-company-charge-you-for-services-never-requested-or-received
[91]: https://web.archive.org/web/20170104201629/http://skeptics.stackexchange.com/questions/36519/is-this-pie-graph-describing-us-government-spending-accurate
[92]: https://web.archive.org/web/20170104201629/http://security.stackexchange.com/questions/147111/are-cve-counts-a-good-indicator-of-a-softwares-security
[93]: https://web.archive.org/web/20170104201629/http://worldbuilding.stackexchange.com/questions/66667/physically-how-do-dragons-grasp-and-transport-the-contents-of-their-hoards
[94]: https://web.archive.org/web/20170104201629/http://travel.stackexchange.com/questions/85538/taking-my-mate-tea-on-the-plane
[95]: https://web.archive.org/web/20170104201629/http://physics.stackexchange.com/questions/302795/why-does-stacking-polarizers-of-the-same-angle-still-block-more-and-more-light
[96]: https://web.archive.org/web/20170104201629/http://christianity.stackexchange.com/questions/54432/is-there-a-reina-valera-only-movement
[97]: https://web.archive.org/web/20170104201629/http://rpg.stackexchange.com/questions/92584/odd-said-it-could-be-played-with-20-50-players-and-one-referee-how-was-that-ex
[98]: https://web.archive.org/web/20170104201629/http://rpg.stackexchange.com/questions/92640/how-to-enter-the-ogl-into-my-work
[99]: https://web.archive.org/web/20170104201629/http://physics.stackexchange.com/questions/302811/why-is-this-vector-field-curl-free
[100]: https://web.archive.org/web/20170104201629/http://tex.stackexchange.com/questions/347051/underline-rule-position
[101]: https://web.archive.org/web/20170104201629/http://unix.stackexchange.com/questions/334821/how-is-an-elastic-ip-address-different-from-a-static-ip-address
[102]: https://web.archive.org/web/20170104201629/http://security.stackexchange.com/questions/147255/should-failed-login-attempts-be-logged
[103]: https://web.archive.org/web/20170104201629/http://codegolf.stackexchange.com/questions/105398/2016-time-capsule-string-how-versatile-is-your-language
[104]: /web/20170104201629/http://math.stackexchange.com/feeds/question/47477
[105]: https://web.archive.org/web/20170104201629/http://math.blogoverflow.com/?blb=1
[106]: https://web.archive.org/web/20170104201629/http://data.stackexchange.com/
[107]: https://web.archive.org/web/20170104201629/http://stackexchange.com/legal
[108]: https://web.archive.org/web/20170104201629/http://stackexchange.com/legal/privacy-policy
[109]: https://web.archive.org/web/20170104201629/http://stackoverflow.com/company/work-here
[110]: https://web.archive.org/web/20170104201629/http://stackexchange.com/mediakit
[111]: /web/20170104201629/http://math.stackexchange.com/contact
[112]: //web.archive.org/web/20170104201629/http://stackoverflow.com/
[113]: //web.archive.org/web/20170104201629/http://serverfault.com/
[114]: //web.archive.org/web/20170104201629/http://superuser.com/
[115]: //web.archive.org/web/20170104201629/http://webapps.stackexchange.com/
[116]: //web.archive.org/web/20170104201629/http://askubuntu.com/
[117]: //web.archive.org/web/20170104201629/http://webmasters.stackexchange.com/
[118]: //web.archive.org/web/20170104201629/http://gamedev.stackexchange.com/
[119]: //web.archive.org/web/20170104201629/http://tex.stackexchange.com/
[120]: //web.archive.org/web/20170104201629/http://softwareengineering.stackexchange.com/
[121]: //web.archive.org/web/20170104201629/http://unix.stackexchange.com/
[122]: //web.archive.org/web/20170104201629/http://apple.stackexchange.com/
[123]: //web.archive.org/web/20170104201629/http://wordpress.stackexchange.com/
[124]: //web.archive.org/web/20170104201629/http://gis.stackexchange.com/
[125]: //web.archive.org/web/20170104201629/http://electronics.stackexchange.com/
[126]: //web.archive.org/web/20170104201629/http://android.stackexchange.com/
[127]: //web.archive.org/web/20170104201629/http://security.stackexchange.com/
[128]: //web.archive.org/web/20170104201629/http://dba.stackexchange.com/
[129]: //web.archive.org/web/20170104201629/http://drupal.stackexchange.com/
[130]: //web.archive.org/web/20170104201629/http://sharepoint.stackexchange.com/
[131]: //web.archive.org/web/20170104201629/http://ux.stackexchange.com/
[132]: //web.archive.org/web/20170104201629/http://mathematica.stackexchange.com/
[133]: //web.archive.org/web/20170104201629/http://salesforce.stackexchange.com/
[134]: //web.archive.org/web/20170104201629/http://expressionengine.stackexchange.com/
[135]: //web.archive.org/web/20170104201629/http://crypto.stackexchange.com/
[136]: //web.archive.org/web/20170104201629/http://codereview.stackexchange.com/
[137]: //web.archive.org/web/20170104201629/http://magento.stackexchange.com/
[138]: //web.archive.org/web/20170104201629/http://dsp.stackexchange.com/
[139]: //web.archive.org/web/20170104201629/http://raspberrypi.stackexchange.com/
[140]: //web.archive.org/web/20170104201629/http://codegolf.stackexchange.com/
[141]: https://web.archive.org/web/20170104201629/http://stackexchange.com/sites#technology
[142]: //web.archive.org/web/20170104201629/http://photo.stackexchange.com/
[143]: //web.archive.org/web/20170104201629/http://scifi.stackexchange.com/
[144]: //web.archive.org/web/20170104201629/http://graphicdesign.stackexchange.com/
[145]: //web.archive.org/web/20170104201629/http://movies.stackexchange.com/
[146]: //web.archive.org/web/20170104201629/http://music.stackexchange.com/
[147]: //web.archive.org/web/20170104201629/http://cooking.stackexchange.com/
[148]: //web.archive.org/web/20170104201629/http://diy.stackexchange.com/
[149]: //web.archive.org/web/20170104201629/http://money.stackexchange.com/
[150]: //web.archive.org/web/20170104201629/http://academia.stackexchange.com/
[151]: https://web.archive.org/web/20170104201629/http://stackexchange.com/sites#lifearts
[152]: //web.archive.org/web/20170104201629/http://english.stackexchange.com/
[153]: //web.archive.org/web/20170104201629/http://skeptics.stackexchange.com/
[154]: //web.archive.org/web/20170104201629/http://judaism.stackexchange.com/
[155]: //web.archive.org/web/20170104201629/http://travel.stackexchange.com/
[156]: //web.archive.org/web/20170104201629/http://christianity.stackexchange.com/
[157]: //web.archive.org/web/20170104201629/http://ell.stackexchange.com/
[158]: //web.archive.org/web/20170104201629/http://japanese.stackexchange.com/
[159]: //web.archive.org/web/20170104201629/http://gaming.stackexchange.com/
[160]: //web.archive.org/web/20170104201629/http://bicycles.stackexchange.com/
[161]: //web.archive.org/web/20170104201629/http://rpg.stackexchange.com/
[162]: //web.archive.org/web/20170104201629/http://anime.stackexchange.com/
[163]: //web.archive.org/web/20170104201629/http://mechanics.stackexchange.com/
[164]: https://web.archive.org/web/20170104201629/http://stackexchange.com/sites#culturerecreation
[165]: //web.archive.org/web/20170104201629/http://mathoverflow.net/
[166]: //web.archive.org/web/20170104201629/http://stats.stackexchange.com/
[167]: //web.archive.org/web/20170104201629/http://cstheory.stackexchange.com/
[168]: //web.archive.org/web/20170104201629/http://physics.stackexchange.com/
[169]: //web.archive.org/web/20170104201629/http://chemistry.stackexchange.com/
[170]: //web.archive.org/web/20170104201629/http://biology.stackexchange.com/
[171]: //web.archive.org/web/20170104201629/http://cs.stackexchange.com/
[172]: //web.archive.org/web/20170104201629/http://philosophy.stackexchange.com/
[173]: https://web.archive.org/web/20170104201629/http://stackexchange.com/sites#science
[174]: //web.archive.org/web/20170104201629/http://meta.stackexchange.com/
[175]: //web.archive.org/web/20170104201629/http://stackapps.com/
[176]: //web.archive.org/web/20170104201629/http://area51.stackexchange.com/
[177]: https://web.archive.org/web/20170104201629/https://www.stackoverflowbusiness.com/talent
[178]: https://web.archive.org/web/20170104201629/https://creativecommons.org/licenses/by-sa/3.0/
[179]: https://web.archive.org/web/20170104201629/http://blog.stackoverflow.com/2009/06/attribution-required/
