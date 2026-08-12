<!-- source: https://strauss.hosted.uark.edu/mathfactor_site/mathfactor.uark.edu/2007/10/follow-up-escaping-the-beast/trackback/index.html | converted from HTML -->

The Math Factor Podcast &raquo; Follow Up: Escaping the Beast

#

# [The Math Factor Podcast][1]

-->

## [Follow Up: Escaping the Beast][2]

October 9, 2007 · [answers][3], [calculusey stuff][4], [Follow Up][5], [The Mathcast][6] · [Permalink][2] -->

&laquo;&laquo; [CX. The Princess and A Beast][7] · · · [CY. Number Sleuths][8] &raquo;&raquo;

We can say a bit more about [the Princess’s escape][9].

Amazingly, an optimal path for the Princess is to swim in a half circle of radius 1/8 that of the lake, then dash out to the edge.
We’ll give an analytic proof, but we could give a totally synthetic (geometric) proof as well.

**An Analytic, Calculussey Proof**

First of all, we should ask:

**At a given moment, how fast can the Princess swim towards the edge of the lake? **

Let’s not worry about our actors changing directions— this doesn’t really affect our thinking (remember we assumed they could change directions instantly). So the Beast will be dashing around the lake and the princess taking some route to get away.

Let’s scale things so that the lake has radius 1, and the Beast’s speed is 1. At time *t*then, he will have travelled a distance of *t*, and the Princess will have traveled one-fourth as far, &frac14;*t*.

*At a given moment, how fast can the Princess swim towards the edge of the lake? *

Consider what happens over a very very small interval of time, of size &Delta;t, when the Princess is *r*away from the center of the lake.

The Beast travels &Delta;*t*along the shore. The Princess has to keep the beast on the opposite side of the lake, and so has to swim proportionally less,
*r*&Delta;*t *around.

How much can she increase *r*, if she is travelling a total of &frac14; &Delta;*t*, and needs only to go around a distance of *r*&Delta;*t*? It is well worth learning how to think like an 18th Century Mathematician: essentially we have a right triangle, and can use the Pythagorean Theorem. (We don’t really have exactly a right triangle, but the difference is negligible, and as &Delta;*t*decreases, is less and less important, until irrelevant in the limit.)

By the Pythagorean Theorem, an increment of change of radius &Delta; *r*is &radic;( (&frac14; &Delta; t) 2 – (*r*&Delta; t) 2)

(In the limit, this is good enough; all the differences are vanishingly small compared to &Delta;, as &Delta; decreases.)

In other words, in the limit,

*dr *= &radic; (&frac14; 2 –*r*2) *dt *

Using a little calculus, and remembering that at *t*= 0, we have *r *= 0 as well, we can check that

*r*= &frac14; sin 4*t*

Remember that *t *is not only measuring time, but also the monster’s distance around the lake; the lake is radius 1, so this is also the radian measure around the lake. In other words, the initial part of the Princess’ path, in polar coordinates is:

*r(&theta;)*= &frac14; sin 4&theta;

a circle as promised!

Permalink -->

## 3 Comments [&raquo;][10]

1.

### [strauss][11] said,

December 31, 2007 at [10:04 am][12]

Actually, this is only the optimal path of the form: curve out 1/4 of the way, then make a straight dash. Perhaps one can do better by starting to dash sooner…

2.

### stevestyle said,

January 9, 2008 at [7:56 am][13]

I believe I can describe the solution.

The key points are:

1. The princess will never go inside the spiral/circle.

2. Wherever she ends up, she will have taken the shortest possible route.

Imagine tying one end of a piece of string to the centre of the lake (you can do that with this lake). Now hoop it around the circle and stretch it out to the edge of the lake, keeping it taught.

The path of the string is the shortest route the princess can take to reach that part of the shore.

The path is:

curve outwards for a bit;

continue in the same direction, but in a straight line, until reaching shore.

This is Chaim’s suggested path. He asks if we can improve by heading for shore earlier.

We can reach shore at the same point faster by cutting out the corner. Note that this is not the best route for the princess; it’s just a faster route for reaching the same point on shore.

We can give a range for where the optimal route lies.
If we travel a quarter circle and then head horizontally for shore then it’s easy to show this still beats the beast.
As the princess must travel at least 1, then the beast must travel at least four.
Calculating exactly where the best route lies is complex. I’ve have worked out some equations for it but not solved them. We don’t really need to know do we?

If the princess wants to land as far from the beast as possible, so she has the best safety margin, then she should swim out to _ radius then head to shore in the same direction.
The beast has to cover _ of a circle after the princess starts heading for shore, and an entire circle in total. When the princess lands the beast is still about 0.5 away.
She lands at angle theta, which has cosine _.
If we start the princess from any point on this path then this must still be the best path for her to take.
Note that this does not depend on exactly where the beast it, only on the direction from which he is coming.

Suppose we put the princess and the beast at random points, and the princess want to land as far from the beast as possible. Also assume it is best for her to head straight for shore, rather than retreat to the centre and start out from there.
She will lie on exactly one path of the type we have described, given the direction of the beast. This is her best path.
She should calculate how to land at an angle of theta while also heading away from the beast. This is her best path.

3.

### jay ha said,

March 24, 2014 at [4:55 pm][14]

what about this variation?

An escaped prisoner finds himself in the middle of a square swimming pool. The guard that is chasing him is at one of the corners of the pool. The guard can run faster than the prisoner can swim. The prisoner can run faster than the guard can run. The guard does not swim. Which direction should the prisoner swim in in order to maximize the likelihood that he will get away?

[RSS feed for comments on this post][15] · [TrackBack URL][2]

## Leave a Comment

You must be [logged in][16] to post a comment.

&laquo; [CX. The Princess and A Beast][17]

[CY. Number Sleuths][18] &raquo;

-->

#

###

###

[The Math Factor Podcast Website Quality Math Talk Since 2004, on the web and on KUAF 91.3 FM A production of the University of Arkansas, Fayetteville, Ark USA][1]
NOTE: WE ARE EXPERIENCING SOME SORT OF TECHNICAL PROBLEM WITH LINKS ON THE SITE. Please bear with us while we fix this issue.

--> We're doing a little site maintenance this morning: apologies if the page goes haywire! We'll be done by about 16:00 GMT (12 pm EDT)

--> July 21, 2008: Chaim is traveling and we're taking a couple of weeks off... But more Math Factor is coming soon! (including our very interesting morning at the Fayetteville Farmers' Market soliciting math questions...)

--> July 8, 2008: This has to be the nicest time of year! In a couple of weeks, we're going to be setting up our Math Table at the Farmers' Market, soliciting questions... not quite sure what to expect...

--> June 8, 2008: [The Firefly Festival][19] is coming up quick! Join us in a [amazing woven performance space][20] for an evening of summer fun!

--> May 14, 2008: We are very pleased to announce that we are now a regular column on [the Mathematical Association of America's][21] MAAonline!

--> May 5, 2008: Spring is beautiful here in the Ozarks and we are excited about all the terrific interviews we have slated for the next few weeks!

--> April 14, 2008: Thanks to all our listeners! We really appreciate all of the comments and emails we recieve! We have a terrific slate of interviews lined up (several months worth!) which we are looking forward to sharing...

--> April 4, 2008: Just back from the Gathering for Gardner, with an amazing bunch of interviews. My [sculpture][22] came out great! On the 10th, Frank Morgan will be on the UA campus, 7:30pm POSC 211, speaking on the Double Bubble Theorem. See you there!

--> March 26, 2008: For those in the area, two great talks are coming up: John H. Conway will be giving an April Fool's Day Address, April 1, and Frank Morgan will be speaking on the Double Bubble Conjecture, April 10; both talks are here at the University of Arkansas, in POSC 211, at 7:30 pm

I'm at the Gathering For Gardner this week and should have plenty to report when I return.

--> March 12, 2008: More great fun coming up! Woodchucks! Bubbles! Liars! And, of course, Plenty o' Paradoxes!

--> February 19, 2008: More great interviews and puzzles coming up, and then a discussion about the limits of computation, and why there are true, but unprovable, mathematical theorems! (And this can be *proven!!*)

--> Did you know: you can *search*from the box below? --> Want us to discuss something on the show? Let us know!

--> NOTE: WE ARE EXPERIENCING SOME SORT OF TECHNICAL PROBLEM WITH LINKS ON THE SITE. Please bear with us while we fix this issue.

--> [#mathfactor is now on twitter][23]

-->

Download a great math factor poster to print and share!

Got an idea? Want to do a guest post? Tell us about it!

Heya! Do us a favor and link here from your site!

let us know about interesting stuff for us to link to as well. -->

-

## Search

-

## Contributors to The Math Factor

  - [Chaim Goodman-Strauss and Kyle Kellams][24]
  - [Edmund Harriss][25]
  - [Stephen Morris][26]
  - [Jeff Yoak][27]

-

## Meta

  - [Home][1]
  - [Log in][28]
  - Contact the Math Factor
  - [The Math Factor in iTunes][29]
  - [RSS feed][30]
  - [Comments RSS][31]
  - mathbun.com

-

## Pages

  - [Who We Are][24]
  - [We’d love to hear from you!][32]
  - [Mathfactor Goodies][33]
  - [Products We Like][34]
  - [Books We Highly Recommend!][35]

-

## Categories

  - [art][36]
  - [Authors][37]

    - [Harriss][38]
    - [Morris][39]
    - [Yoak][40]

  - [Favorites][41]
  - [Follow Up][5]
  - [Podcasts][42]
  - [Q&A][43]
  - [The Mathcast][6]

    - [calculusey stuff][4]
    - [errata][44]
    - [game theory][45]
    - [guests][46]
    - [infinity][47]
    - [logic][48]
    - [math puzzles][49]

      - [answers][3]

    - [Mathfactor Events][50]
    - [numbers][51]
    - [paradoxes][52]
    - [Topology and geometry][53]
    - [toys and math products][54]

  - [Uncategorized][55]

-

## Links

  -

## math info

    - [>> More or Less Radio Program][56]
    - [>> Plus Magazine][57]
    - [Brian Hayes’ Bit Player][58]
    - [Calculus On the Web (COW)][59]
    - [Cut the Knot][60]
    - [Dimensions: beautiful math videos][61]
    - [Encyclopedia of earliest uses of mathematical terms][62]
    - [Equalis Online Math Community][63]
    - [Geometry Junkyard][64]
    - [Lots of Math-Art resources][65]
    - [MAA.org][21]
    - [Math For Primates][66]
    - [Math Recreation Blog][67]
    - [Mathematical Moments][68]
    - [Mathematics Illuminated][69]
    - [Mathworld][70]
    - [Maxwell’s Demon][71]
    - [Mudd Fun Facts][72]
    - [Online Encyclopedia of Integer Sequences][73]
    - [Opinions of Doron Zielberger][74]
    - [Outside In][75]
    - [Robert Munafo's Large Numbers Page][76]
    - [Strongly Connected Components Podcast][77]
    - [Terrance Tao’s Blog][78]
    - [The Math Forum][79]

  -

## math podcasts

    - [Strongly Connected Components Podcast][77]

  -

## math products

    - [>> Plus Magazine][57]
    - [Binary Arts Puzzles][80]
    - [Equalis Online Math Community][63]
    - [Math Art Fun][81]
    - [Mathematics Illuminated][69]
    - [The Art of Problem Solving][82]
    - [Zomes][83]

  -

## math puzzles

    - [>> Nick’s Mathematical Puzzles][84]
    - [Binary Arts Puzzles][80]
    - [Blaine's Puzzle Blog][85]
    - [Macalester Problem of the Week][86]
    - [Math Art Fun][81]
    - [Math Puzzle . Com][87]
    - [Math Recreation Blog][67]
    - [Nikoli Puzzle Co.][88]
    - [Perplexus][89]
    - [Puzzles, Brain Teasers and Headbreakers][90]
    - [Spacetime Math Games][91]

  -

## math weirdness

    - [Encyclopedia of earliest uses of mathematical terms][62]
    - [Geometry Games][92]
    - [Lots of Math-Art resources][65]
    - [Math For Primates][66]
    - [Mathbun][93]
    - [Maxwell’s Demon][71]
    - [Outside In][75]
    - [Robert Munafo's Large Numbers Page][76]
    - [xkcd Webcomic][94]

-

## [Our Favorite Segments][41]

  - [Favorites Archive][41]

-

## Archives

  - [2012][95]
  - [2011][96]
  - [2010][97]
  - [2009][98]
  - [2008][99]
  - [2007][100]
  - [2006][101]
  - [2005][102]
  - [A Quick Puzzle From OSCON][103]
  - [Yoak: Denominations of money][104]
  - [HR. CardColm][105]
  - [Pictures from the Gathering][106]
  - [HQ. Newton v Leibnitz][107]
  - [HP. Happy Root 10 Day!][108]
  - [HO. Crazies on the Plane][109]
  - [HN. Barbette][110]
  - [HM. Five Cards][111]
  - [HL. Bear Hunt][112]
  - [HK. Spiders and Fly][113]
  - [HJ. Strange Suitor][114]
  - [Hi! Getting Closer][115]
  - [HH. Corpuscle Candies][116]
  - [HG. Two Love][117]
  - [HF. True Love][118]
  - [HE. On Cake and Coffee][119]
  - [HD. The Math Factor Returns!][120]
  - [Strauss: The coffee pot question][121]
  - [Math Factor Update And Q To Listeners][122]
  - [Yoak: Garbled Marbles][123]
  - [HC. Strongly Connected Components][124]
  - [Morris: A Day at the Races][125]
  - [HB. Puzzlers Pegg and Stephens!][126]
  - [The Nth Day of Christmas][127]
  - [2011!][128]
  - [Mathfactor Update][129]
  - [Morris: Finding Fibonacci][130]
  - [Morris: Fractal Thoughts about Mandelbrot][131]
  - [Morris: Follow Up: Golden Earring – Radar Love][132]
  - [Morris: Futurama – Prisoner of Benda][133]
  - [Morris: Golden Earring – Radar Love][134]
  - [Morris: The Crack that Lets the Light In][135]
  - [HA! Conway on Gardner][136]
  - [Morris: RIP Martin Gardner: 1914 – 2010][137]
  - [GY. Chaitin on the Ubiquity of Undecidability][138]
  - [Update: The Math Factor Podcast][139]
  - [GW. Wolfram’s Principle of Computational Equivalence][140]
  - [G4G9: Report From the Festivities!][141]
  - [GV. Three Quick G4G9 Puzzles From Ed Pegg][142]
  - [Polygonous Party Games][143]
  - [Puzzles and Comments!][144]
  - [GW/GV Math Factor Hits The Road!][145]
  - [Morris: The Meaning of LIFE is …..][146]
  - [GU. Number Freak!][147]
  - [GT. The Largest Escher Exhibit Ever][148]
  - [GP, GQ, GR, GS: The Math Factor Catches Up (For Now)][149]
  - [Yoak: Wheel Whepair][150]
  - [Yoak: Pirate Treasure Map][151]
  - [GO. More Coin Fraud][152]
  - [GN. Benford’s Law][153]
  - [Morris: Follow Up: Triel/Truel/Whatever][154]
  - [Yoak: Miles, Kilometers and Fibonacci Numbers][155]
  - [Morris: How Many Boys? On a Tuesday?][156]
  - [Morris: Trial/Trual/Whatever][157]
  - [GM. What’s the Big Deal Anyway?][158]
  - [Yoak: More Goings On At The ‘Crazy Buttocks’ Party][159]
  - [Follow Up: Yoak: Batteries, and the Problem of the Week][160]
  - [Harris: Myers Game][161]
  - [GL. Math 2033][162]
  - [Morris: Follow Up: Living With Crazy Buttocks][163]
  - [GK. Mythematics][164]
  - [Yoak: Batteries, and the Problem of the Week][165]
  - [GJ. Mathletics!][166]
  - [Yoak: Average Salary][167]
  - [Morris: Living with Crazy Buttocks][168]
  - [GI. Mrs Perkins’ Electric Quilt][169]
  - [Yoak: Foxy!][170]
  - [GH. The Math Book][171]
  - [Yoak: Simple Arithmetic][172]
  - [GG. More on OLD IDAHO USUAL HERE][173]
  - [GF. More Clock Crazies][174]
  - [Yoak: Lewis Carroll – Some Chance I’m Being Obtuse][175]
  - [GE. Clock Confusion Redux][176]
  - [Yoak: More Lewis Carroll – The Square Window][177]
  - [GD. The Math Circus is Coming To Town!][178]
  - [Morris: OLD IDAHO USUAL HERE][179]
  - [Yoak: Lewis Carroll – Passing Shillings][180]
  - [Yoak: Lewis Carroll, Colored Stones][181]
  - [Temporary Post: What is Symmetrical][182]
  - [Yoak: Answer on GC: Another Buncha Prisoners][183]
  - [GC. Another Buncha Prisoners][184]
  - [GB. Hat Strategy][185]
  - [GA. Stacking the Chips][186]
  - [FZ. Find the Coin!][187]
  - [Morris: World of Britain 2: Proof and Paradox][188]
  - [Yoak: Cut The Cube][189]
  - [Morris: …and the clocks struck thirteen][190]
  - [FY. Weights in a Row][191]
  - [FW. Walk Around the Clock][192]
  - [FV. Singmastery!][193]
  - [Morris: Infinite Products][194]
  - [Yoak: Face Up][195]
  - [Morris: World Of Britain][196]
  - [Morris: The Kate Bush Conjecture][197]
  - [FU. Arp and Bif Shake Hands][198]
  - [FT. Sum and Double, Double and Sum][199]
  - [Yoak: Labelous][200]
  - [FS. The Portuguese Waiter Trick!][201]
  - [Yoak: Pick a ball! Any Ball!][202]
  - [Yoak: Followup to A Rather Odd Car Trip][203]
  - [FR. Who Wants To Be A Mathematician?][204]
  - [Harriss: Mathematical Sculpture][205]
  - [Yoak: A Rather Odd Car Trip][206]
  - [Morris: Turning Tables][207]
  - [Yoak: A Fun Math Trick – Guess the Polynomial][208]
  - [Harriss: Rabbit Sequence][209]
  - [Yoak: Will A Real Gold Coin Please Stand Up?][210]
  - [FM. Bamboopalooza One][211]
  - [FL. Algebra on the Radio][212]
  - [Yoak: Mountain Climbing][213]
  - [Harriss: Algebraic Surfaces][214]
  - [A question for our listeners][215]
  - [FK. Twiddling Screws][216]
  - [FJ. Loyd’s Atomic Easter Eggs][217]
  - [FI. Paranoia][218]
  - [FH. Girdling the Earth][219]
  - [FG. Mr. Fled][220]
  - [FF. Hostile Flowers][221]
  - [FE. Burn The Rope][222]
  - [FD. Space Walkers][223]
  - [FC. Cool Clear Water][224]
  - [FB. The Legendary Monte Hall Problem][225]
  - [FA. The Johnsons][226]
  - [EZ. Google, Flutes and Monopoly][227]
  - [Morris: How to Win Your Bonus][228]
  - [EY. Our Vth Anniversary Special!][229]
  - [Follow Up: Sequences of Averages][230]
  - [Morris: Inside Every Hexagram …][231]
  - [Q & A: When Two Spheres Touch…][232]
  - [EX. Gambler’s Ruin!][233]
  - [Follow Up: Differences][234]
  - [Morris: Christmas = Halloween?!?][235]
  - [Morris: Sequences and Scrabble][236]
  - [Harriss: First post][237]
  - [EV. What’s the Difference?][238]
  - [EU. Stacking Cannonballs][239]
  - [ET. Your Holiday Shopping Guide][240]
  - [ES. The Ishango Bone][241]
  - [Follow Up: The Mersenne Primes][242]
  - [ER. The Great Internet Mersenne Prime Search][243]
  - [EQ. Ed Pegg Returns][244]
  - [EP. HIPE][245]
  - [Follow Up: Loops and the Harmonic Series.][246]
  - [Paperdolls!][247]
  - [EO. Spaghetti Loops][248]
  - [EN. Plinko][249]
  - [EM. Awash in Billiard Balls][250]
  - [EL. Math Dance with Dr Schaffer and Mr Stern][251]
  - [EK. The Law of Small Numbers][252]
  - [EJ. Math Factor at the Farmer’s Market][253]
  - [EI. How to Pass a Cube Through Itself!][254]
  - [Follow Up: The Harmonic Series][255]
  - [EH. The Worm Makes It!][256]
  - [EG. The Colossal Book of Short Puzzles and Problems][257]
  - [EF. Visions of Symmetry][258]
  - [EE. Tossem Beaver][259]
  - [ED. Mathemagican Art Benjamin][260]
  - [Follow Up: The Busy Beaver Function][261]
  - [EC. Skyrocketing Functions!][262]
  - [EB. Busy Beavers and Dumb Robots][263]
  - [EA. The Limits of Computation][264]
  - [DZ. Mind Control Across Time and Space!][265]
  - [DY. The Symmetries of Things][266]
  - [DX. Dumb Robots][267]
  - [DW. The Online Encyclopedia of Integer Sequences!][268]
  - [DV. Dealing with Chaos][269]
  - [DU. Chaos at the Card Table][270]
  - [Follow Up: Smullyan’s Paradoxes!][271]
  - [DT. Speaking of Self-reference][272]
  - [DS. Math Chat With Frank Morgan][273]
  - [DR. Double Bubble][274]
  - [DQ. We Are Not Liars][275]
  - [DP. Would Chuck Wood][276]
  - [DO. Proofs Puzzles and Conundra!][277]
  - [DN. Ed Burger’s Trouser Puzzle][278]
  - [DM. On Codes, Primes and Kings][279]
  - [DL. The Wicked King Problem][280]
  - [Greetings From The Math Factor][281]
  - [DK. Flipping the Mattress][282]
  - [DJ. Pegg on Numb3rs][283]
  - [Follow Up: Prime Dice][284]
  - [DI. Dice Games][285]
  - [DH. Ice Cream Cake][286]
  - [Q&A: Deal or No Deal][287]
  - [Q & A: A little puzzle][288]
  - [DG. Ants on a Rod][289]
  - [DF. The Best Full House][290]
  - [DE. The Apples In Stereo][291]
  - [Q and A: Deal or No Deal][292]
  - [DD. Should We Teach College Algebra?][293]
  - [DC. Psychology Matters][294]
  - [DB. Envelope Mystery][295]
  - [DA. A Cake Conundrum][296]
  - [CZ. A Parlour Trick][297]
  - [CY. Number Sleuths][8]
  - [Follow Up: Escaping the Beast][2]
  - [CX. The Princess and A Beast][7]
  - [CW. The Surreal Numbers][298]
  - [CV. Dividing the Loot][299]
  - [CU. Eminently Logical Pirates][300]
  - [CT. Odd People][301]
  - [Follow-up: Weird sums][302]
  - [CS. Perfect Sums][303]
  - [CR. Clock Confusion][304]
  - [CQ. Dollar Auction][305]
  - [CP. The Prisoners Dilemma][306]
  - [Follow-up: Mismatched Pennies][307]
  - [Q&A: Numerous Numbers][308]
  - [CO. Mismatched Pennies][309]
  - [CN. Name That Date][310]
  - [CM. Crossing the Bridge][311]
  - [CL. Some Number of Numbers Sum][312]
  - [CK. The Third Tree][313]
  - [Follow-up: The Stork and The Frog][314]
  - [CJ. The Stork and the Frog][315]
  - [CI. The Royal Order of the Garter][316]
  - [CH. Rayo’s Number!][317]
  - [Follow-up: Graham’s Number][318]
  - [CG. Graham’s Number][319]
  - [Q&A: The Race][320]
  - [CF. Mind Boggling!][321]
  - [CE. Big Numbers][322]
  - [Q&A: Why is 0! = 1?][323]
  - [CD. Alas, Up To A Million Dollars Might Have Been Given Away.][324]
  - [CC. Fair Division][325]
  - [CB. Pi Day][326]
  - [CA. Cut the Cake!][327]
  - [BZ. Two Teams][328]
  - [BY. Guests at a Party][329]
  - [BW. The Math Factor Million Dollar Give Away!!!][330]
  - [BV. 9’s Strike Again][331]
  - [BU. The Online Mind Reader][332]
  - [BT. A Runcinated Dodecaplex][333]
  - [BS. Aha! Escape!][334]
  - [BR. We Don’t Know the Way Out!][335]
  - [BQ. The Smuggler is Paid][336]
  - [BP. The Smuggler’s Fee][337]
  - [BO. When did you say?][338]
  - [BN. Puzzling Panelists][339]
  - [BM. An astronomical cost!][340]
  - [BL. Eternally diminishing returns][341]
  - [BK. Bananas and Rockets][342]
  - [BJ. The Most Powerful Force][343]
  - [BI. The Shape of the Universe][344]
  - [BH. The Poincar&eacute; Conjecture][345]
  - [BG. Bamboopalooza!][346]
  - [BF. Catching Errors][347]
  - [BE. Trap door encryption][348]
  - [BD. Magic Numbers][349]
  - [BC. Casting Out Nines][350]
  - [BA. The Ring is Exchanged][351]
  - [AZ. Another puzzle from Peter Winkler][352]
  - [AY. Dollar Cost Averaging][353]
  - [AX. Averages are not what they seem!][354]
  - [AW. Will we run out of Social Security Numbers?][355]
  - [AV. Dennis Shasha Answers][356]
  - [AU. Dennis Shasha asks about Polish Multiplication][357]
  - [AT. Peter Winkler Answers][358]
  - [AS. A Puzzle From Peter Winkler][359]
  - [AR. A Quick Game][360]
  - [AQ. The Principle of Indifference Redux][361]
  - [AO. Choosing Balls from A Bag][362]
  - [AN. More Sucker Bets][363]
  - [AM. Arrow's Theorem][364]
  - [AL. Rumors and suckers][365]
  - [AK. Paradoxes and Liars][366]
  - [AJ. The Pop Quiz][367]
  - [AI. Census Taker's Puzzle][368]
  - [AH. QED][369]
  - [AG. The Eagle][370]
  - [AF. Counting All Rationals][371]
  - [AE. The Jalopy][372]
  - [AD. Bigger and Smaller Infinities][373]
  - [AC. No Vacancy][374]
  - [AB. The Rational Ruler][375]
  - [AA. The Way Out of the Forest][376]

## Meta

  - [Log in][377]
  - [RSS feed][378]
  - [Comments RSS][379]
  - [WordPress][380]

-->

Beccary and [Weblogs.us][381] ·--> The Math Factor Podcast is brought to you by: [C Goodman-Strauss][11] &#183· [KUAF 91.3 FM][382] &#183· [Math Dept][383] &#183· [Univ. Ark][384] &#183· [XHTML][385] &#183· [CSS][386]

Podcast powered by [podPress v8.8.10.17][387]


## Links

[1]: ../../../../podpress_trac/web/239/0/106%20Busy%20Beavers%20and%20Dumb%20Robots%20_Math_Factor_2008_06_19.mp3.html
[2]: index.html
[3]: ../../../../category/the-mathfactor-podcast/math-puzzles/answers/index.html
[4]: ../../../../category/the-mathfactor-podcast/continua/index.html
[5]: ../../../../category/follow-up/index.html
[6]: ../../../../category/the-mathfactor-podcast/index.html
[7]: ../../cx-the-princess-and-a-beast/trackback/index.html
[8]: ../../cy-number-sleuths/trackback/index.html
[9]: ../../09/cx-the-princess-and-a-beast/index.html
[10]: index.html#respond
[11]: http://comp.uark.edu/~strauss
[12]: index.html#comment-181
[13]: index.html#comment-207
[14]: index.html#comment-1188
[15]: ../feed/index.html
[16]: ../../../../wp-login.php%3Fredirect_to=http:%252F%252Fmathfactor.uark.edu%252F2007%252F10%252Ffollow-up-escaping-the-beast%252F.html
[17]: http://mathfactor.uark.edu/2007/10/cx-the-princess-and-a-beast/
[18]: http://mathfactor.uark.edu/2007/10/cy-number-sleuths/
[19]: http:fireflyfestival.blogger.com
[20]: http://mathbun.com/v/greenweave
[21]: http://www.maa.org
[22]: http://www.mathbun.com/v/sculpture/final+assembly.jpg.html
[23]: http://twitter.com/#search?q=%23mathfactor
[24]: ../../../../about.html
[25]: http://maxwelldemon.wordpress.com/
[26]: ../../../../about.html#morris
[27]: ../../../../about.html#yoak
[28]: ../../../../wp-login.php.html
[29]: http://phobos.apple.com/WebObjects/MZStore.woa/wa/viewPodcast?id=81854832
[30]: ../../../../feed/index.html
[31]: ../../../../comments/feed/index.html
[32]: ../../../../wed-love-to-hear-from-you/index.html
[33]: ../../../../mathfactor-goodies/index.html
[34]: ../../../../products-we-like/index.html
[35]: ../../../../books-we-highly-recommend/index.html
[36]: ../../../../category/art/index.html
[37]: ../../../../category/authors/index.html
[38]: ../../../../category/authors/harriss/index.html
[39]: ../../../../category/authors/morris/index.html
[40]: ../../../../category/authors/yoak/index.html
[41]: ../../../../category/favorites/index.html
[42]: ../../../../category/podcasts/index.html
[43]: ../../../../category/qa/index.html
[44]: ../../../../category/the-mathfactor-podcast/corrections/index.html
[45]: ../../../../category/the-mathfactor-podcast/game-theory/index.html
[46]: ../../../../category/the-mathfactor-podcast/guests/index.html
[47]: ../../../../category/the-mathfactor-podcast/infinity/index.html
[48]: ../../../../category/the-mathfactor-podcast/logic/index.html
[49]: ../../../../category/the-mathfactor-podcast/math-puzzles/index.html
[50]: ../../../../category/the-mathfactor-podcast/events/index.html
[51]: ../../../../category/the-mathfactor-podcast/numbers/index.html
[52]: ../../../../category/the-mathfactor-podcast/paradoxes/index.html
[53]: ../../../../category/the-mathfactor-podcast/topology-and-geometry/index.html
[54]: ../../../../category/the-mathfactor-podcast/toys-and-math-products/index.html
[55]: ../../../../category/uncategorized/index.html
[56]: http://news.bbc.co.uk/2/hi/programmes/more_or_less/default.stm
[57]: http://plus.maths.org
[58]: http://bit-player.org/
[59]: http://cow.temple.edu/
[60]: http://www.cut-the-knot.org/index.shtml
[61]: http://www.dimensions-math.org/
[62]: http://jeff560.tripod.com/mathword.html
[63]: http://www.equalis.com/
[64]: http://www.ics.uci.edu/~eppstein/junkyard/
[65]: http://www.guidetoonlineschools.com/library/math-art
[66]: http://www.mathforprimates.com
[67]: http://mathrecreation.blogspot.com/
[68]: http://www.ams.org/mathmoments/
[69]: http://www.learner.org/courses/mathilluminated/coursematerials/
[70]: http://mathworld.wolfram.com/
[71]: http://maxwelldemon.wordpress.com
[72]: http://www.math.hmc.edu/funfacts/
[73]: http://www.research.att.com/~njas/sequences/
[74]: http://www.math.rutgers.edu/~zeilberg/OPINIONS.html
[75]: http://video.google.com/videoplay?docid=-6626464599825291409
[76]: http://www.mrob.com/pub/math/largenum.html
[77]: http://acmescience.com/shows/scc-shows
[78]: http://terrytao.wordpress.com/
[79]: http://mathforum.org
[80]: http://www.puzzles.com/
[81]: http://mathartfun.com/shopsite_sc/store/html/index.html
[82]: http://www.artofproblemsolving.com
[83]: http://www.zometool.com/
[84]: http://www.qbyte.org/puzzles/
[85]: http://puzzles.blainesville.com/search/label/puzzles
[86]: http://mathforum.org/wagon/
[87]: http://www.mathpuzzle.com/
[88]: http://www.nikoli.com/en/
[89]: http://perplexus.info/
[90]: http://puzzlelot.blogspot.com/
[91]: http://www.spacetime.us/arcade/
[92]: http://www.geometrygames.org/
[93]: http://mathbun.com
[94]: http://www.xkcd.com/
[95]: ../../../../2012/index.html
[96]: ../../../../2011/index.html
[97]: ../../../../2010/index.html
[98]: ../../../../2009/index.html
[99]: ../../../../2008/index.html
[100]: ../../../index.html
[101]: ../../../../2006/index.html
[102]: ../../../../2005/index.html
[103]: ../../../../2012/07/a-quick-puzzle-from-oscon/trackback/index.html
[104]: ../../../../2012/07/yoak-denominations-of-money/trackback/index.html
[105]: ../../../../2012/04/hr-cardcolm/trackback/index.html
[106]: ../../../../2012/04/pictures-from-the-gathering/trackback/index.html
[107]: ../../../../2012/03/hq-newton-v-leibnitz/trackback/index.html
[108]: ../../../../2012/03/hp-happy-root-10-day/trackback/index.html
[109]: ../../../../2012/03/ho-crazies-on-the-plane/trackback/index.html
[110]: ../../../../2012/02/hn-barbette/trackback/index.html
[111]: ../../../../2012/02/hm-five-cards/trackback/index.html
[112]: ../../../../2012/02/hl-bear-hunt/trackback/index.html
[113]: ../../../../2012/02/hk-spiders-and-fly/trackback/index.html
[114]: ../../../../2012/01/hj-strange-suitor/trackback/index.html
[115]: ../../../../2012/01/hi-getting-closer/trackback/index.html
[116]: ../../../../2012/01/hh-corpuscle-candies/trackback/index.html
[117]: ../../../../2012/01/hg-two-love/trackback/index.html
[118]: ../../../../2011/12/hf-true-love/trackback/index.html
[119]: ../../../../2011/12/he-on-cake-and-coffee/trackback/index.html
[120]: ../../../../2011/12/hd-the-math-factor-returns/trackback/index.html
[121]: ../../../../2011/11/strauss-the-coffee-pot-question/trackback/index.html
[122]: ../../../../2011/11/math-factor-update/trackback/index.html
[123]: ../../../../2011/11/yoak-garbled-marbles/trackback/index.html
[124]: ../../../../2011/07/hc-strongly-connected-components/trackback/index.html
[125]: ../../../../2011/07/morris-a-day-at-the-races/trackback/index.html
[126]: ../../../../2011/04/hb-puzzlers-pegg-and-stephens/trackback/index.html
[127]: ../../../../2011/01/the-nth-day-of-christmas/trackback/index.html
[128]: ../../../../2011/01/2011/trackback/index.html
[129]: ../../../../2010/11/mathfactor-update/trackback/index.html
[130]: ../../../../2010/11/morris-finding-fibonacci/trackback/index.html
[131]: ../../../../2010/10/morris-fractal-thoughts-about-mandelbrot/trackback/index.html
[132]: ../../../../2010/10/morris-follow-up-golden-earring-radar-love/trackback/index.html
[133]: ../../../../2010/10/morris-futurama-prisoner-of-benda/trackback/index.html
[134]: ../../../../2010/09/golden-earring-radar-love/trackback/index.html
[135]: ../../../../2010/07/the-crack-that-lets-the-light-in/trackback/index.html
[136]: ../../../../2010/06/ha-conway-on-gardner/trackback/index.html
[137]: ../../../../2010/05/morris-rip-martin-gardner-1914-2010/trackback/index.html
[138]: ../../../../2010/05/gy-chaitin-on-the-ubiquity-of-undecidability/trackback/index.html
[139]: ../../../../2010/05/update-podcast-goes-on-vacation/trackback/index.html
[140]: ../../../../2010/03/gw-wolframs-principle-of-computational-equivalence/trackback/index.html
[141]: ../../../../2010/03/g4g9-report-from-the-festivities/trackback/index.html
[142]: ../../../../2010/03/gv-three-quick-g4g9-puzzles-from-ed-pegg/trackback/index.html
[143]: ../../../../2010/03/polygonous-party-games/trackback/index.html
[144]: ../../../../2010/03/puzzles-and-comments/trackback/index.html
[145]: ../../../../2010/03/gwgv-math-factor-hits-the-road/trackback/index.html
[146]: ../../../../2010/03/the-meaning-of-life-is/trackback/index.html
[147]: ../../../../2010/03/gu-number-freak/trackback/index.html
[148]: ../../../../2010/02/gt-the-largest-escher-exhibit-ever/trackback/index.html
[149]: ../../../../2010/02/gp-gq-gr-gs-the-math-factor-catches-up-for-now/trackback/index.html
[150]: ../../../../2010/02/yoak-wheel-whepair/trackback/index.html
[151]: ../../../../2010/01/yoak-pirate-treasure-map/trackback/index.html
[152]: ../../../../2009/12/go-more-coin-fraud/trackback/index.html
[153]: ../../../../2009/12/gn-benfords-law/trackback/index.html
[154]: ../../../../2009/12/morris-follow-up-trieltruelwhatever/trackback/index.html
[155]: ../../../../2009/12/yoak-miles-kilometers-and-fibonacci-numbers/trackback/index.html
[156]: ../../../../2009/11/how-many-boys-on-a-tuesday/trackback/index.html
[157]: ../../../../2009/11/morris-trialtrualwhatever/trackback/index.html
[158]: ../../../../2009/11/gm-whats-the-big-deal-anyway/trackback/index.html
[159]: ../../../../2009/11/yoak-more-goings-on-at-the-crazy-buttocks-party/trackback/index.html
[160]: ../../../../2009/11/follow-up-yoak-batteries-and-the-problem-of-the-week/trackback/index.html
[161]: ../../../../2009/11/900/trackback/index.html
[162]: ../../../../2009/11/gl-math-2033/trackback/index.html
[163]: ../../../../2009/11/morris-follow-up-living-with-crazy-buttocks/trackback/index.html
[164]: ../../../../2009/11/gk-mythematics/trackback/index.html
[165]: ../../../../2009/11/yoak-batteries-and-the-problem-of-the-week/trackback/index.html
[166]: ../../../../2009/11/gj-mathletics/trackback/index.html
[167]: ../../../../2009/10/yoak-average-salary/trackback/index.html
[168]: ../../../../2009/10/morris-living-with-crazy-buttocks/trackback/index.html
[169]: ../../../../2009/10/gi-mrs-perkins-electric-quilt/trackback/index.html
[170]: ../../../../2009/10/yoak-foxy/trackback/index.html
[171]: ../../../../2009/10/gh-the-math-book/trackback/index.html
[172]: ../../../../2009/10/yoak-simple-arithmetic/trackback/index.html
[173]: ../../../../2009/10/gf-more-on-old-idaho-usual-here/trackback/index.html
[174]: ../../../../2009/10/gf-more-clock-crazies/trackback/index.html
[175]: ../../../../2009/09/yoak-lewis-carroll/trackback/index.html
[176]: ../../../../2009/09/ge-clock-confusion-redux/trackback/index.html
[177]: ../../../../2009/09/yoak-more-lewis-carroll-the-square-window/trackback/index.html
[178]: ../../../../2009/09/gd-the-math-circus-is-coming-to-town/trackback/index.html
[179]: ../../../../2009/08/old-idaho-usual-here/trackback/index.html
[180]: ../../../../2009/08/yoak-lewis-carroll-passing-shillings/trackback/index.html
[181]: ../../../../2009/08/yoak-lewis-carroll-colored-stones/trackback/index.html
[182]: ../../../../2009/08/temporary-post-what-is-symmetry/trackback/index.html
[183]: ../../../../2009/07/yoak-answer-on-gc-another-buncha-prisoners/trackback/index.html
[184]: ../../../../2009/07/gc-another-buncha-prisoners/trackback/index.html
[185]: ../../../../2009/07/gb-hat-strategy/trackback/index.html
[186]: ../../../../2009/07/ga-stacking-the-chips/index.html
[187]: ../../../../2009/07/fz-find-the-coin/trackback/index.html
[188]: ../../../../2009/07/morris-world-of-britain-2-proof-and-paradox/trackback/index.html
[189]: ../../../../2009/07/yoak-cut-the-cube/trackback/index.html
[190]: ../../../../2009/07/morris-and-the-clocks-struck-thirteen/trackback/index.html
[191]: ../../../../2009/07/fy-weights-in-a-row/trackback/index.html
[192]: ../../../../2009/07/fw-walk-around-the-clock/trackback/index.html
[193]: ../../../../2009/06/fv-singmastery/trackback/index.html
[194]: ../../../../2009/06/infinite-products/trackback/index.html
[195]: ../../../../2009/05/yoak-face-up/trackback/index.html
[196]: ../../../../2009/05/world-of-britain/trackback/index.html
[197]: ../../../../2009/05/the-kate-bush-conjecture/trackback/index.html
[198]: ../../../../2009/05/fu-arp-and-bif-shake-hands/trackback/index.html
[199]: ../../../../2009/05/ft-sum-and-double-double-and-sum/index.html
[200]: ../../../../2009/05/yoak-labelous/trackback/index.html
[201]: ../../../../2009/05/fs-the-portuguese-waiter-trick/trackback/index.html
[202]: ../../../../2009/05/yoak-pick-a-ball-any-ball/trackback/index.html
[203]: ../../../../2009/05/04/yoak-followup-to-a-rather-odd-car-trip/index.html
[204]: ../../../../2009/04/fr-who-wants-to-be-a-mathematician/index.html
[205]: ../../../../2009/04/harriss-mathematical-sculpture/trackback/index.html
[206]: ../../../../2009/04/a-rather-odd-car-trip/trackback/index.html
[207]: ../../../../2009/04/turning-tables/trackback/index.html
[208]: ../../../../2009/04/yoak-a-fun-math-trick-guess-the-polynomial/trackback/index.html
[209]: ../../../../2009/04/harriss-rabbit-sequence/trackback/index.html
[210]: ../../../../2009/03/yoak-will-a-real-gold-coin-please-stand-up/trackback/index.html
[211]: ../../../../2009/03/fm-bamboopalooza-one/index.html
[212]: ../../../../2009/03/fl-algebra-on-the-radio/trackback/index.html
[213]: ../../../../2009/03/yoak-mountain-climbing/trackback/index.html
[214]: ../../../../2009/03/harriss-algebraic-surfaces/trackback/index.html
[215]: ../../../../2009/03/a-question-for-our-listeners/trackback/index.html
[216]: ../../../../2009/03/fk-twiddling-screws/trackback/index.html
[217]: ../../../../2009/03/fj-loyds-atomic-easter-eggs/trackback/index.html
[218]: ../../../../2009/03/fi-paranoia/trackback/index.html
[219]: ../../../../2009/03/fh-girdling-the-earth/trackback/index.html
[220]: ../../../../2009/03/fg-mr-fled/trackback/index.html
[221]: ../../../../2009/03/ff-hostile-flowers/trackback/index.html
[222]: ../../../../2009/02/fe-burn-the-rope/trackback/index.html
[223]: ../../../../2009/02/fd-space-walkers/trackback/index.html
[224]: ../../../../2009/02/fc-cool-clear-water/trackback/index.html
[225]: ../../../../2009/02/fb-the-legendary-monte-hall-problem/trackback/index.html
[226]: ../../../../2009/02/fa-the-johnsons/trackback/index.html
[227]: ../../../../2009/02/ez-google-flutes-and-monopoly/trackback/index.html
[228]: ../../../../2009/01/morris-i-want-my-big-bonus/trackback/index.html
[229]: ../../../../2009/01/ey-our-vth-anniversary-special/trackback/index.html
[230]: ../../../../2009/01/follow-up-sequences-of-averages/trackback/index.html
[231]: ../../../../2009/01/inside-every-hexagram/trackback/index.html
[232]: ../../../../2009/01/q-a-when-two-spheres-touch/trackback/index.html
[233]: ../../../../2009/01/ex-gamblers-ruin/trackback/index.html
[234]: ../../../../2009/01/follow-up-differences/trackback/index.html
[235]: ../../../../2009/01/morris-christmas-halloween/trackback/index.html
[236]: ../../../../2009/01/morris-sequences-and-scrabble/trackback/index.html
[237]: ../../../../2008/12/harriss-first-post/trackback/index.html
[238]: ../../../../2008/12/ew-whats-the-difference/trackback/index.html
[239]: ../../../../2008/12/eu-stacking-cannonballs/trackback/index.html
[240]: ../../../../2008/12/et-your-holiday-shopping-guide/trackback/index.html
[241]: ../../../../2008/11/es-the-ishango-bone/trackback/index.html
[242]: ../../../../2008/11/follow-up-the-mersenne-primes/trackback/index.html
[243]: ../../../../2008/11/er-the-great-internet-mersenne-prime-search/trackback/index.html
[244]: ../../../../2008/10/eq-ed-pegg-returns/trackback/index.html
[245]: ../../../../2008/10/ep-hipe/trackback/index.html
[246]: ../../../../2008/10/follow-up-loops-and-the-harmonic-series/trackback/index.html
[247]: ../../../../2008/10/paperdolls/trackback/index.html
[248]: ../../../../2008/10/eo-spaghetti-loops/trackback/index.html
[249]: ../../../../2008/09/en-plinko/trackback/index.html
[250]: ../../../../2008/09/em-awash-in-billiard-balls/trackback/index.html
[251]: ../../../../2008/09/el-math-dance-with-dr-schaffer-and-mr-stern/trackback/index.html
[252]: ../../../../2008/09/ek-the-law-of-small-numbers/trackback/index.html
[253]: ../../../../2008/09/ej-math-factor-at-the-farmers-market/trackback/index.html
[254]: ../../../../2008/08/ei-how-to-pass-a-cube-through-itself/trackback/index.html
[255]: ../../../../2008/08/follow-up-the-harmonic-series/trackback/index.html
[256]: ../../../../2008/08/eh-the-worm-makes-it/trackback/index.html
[257]: ../../../../2008/08/eg-the-colossal-book-of-short-puzzles-and-problems/trackback/index.html
[258]: ../../../../2008/07/ef-visions-of-symmetry/trackback/index.html
[259]: ../../../../2008/07/ee-tossem-beaver/trackback/index.html
[260]: ../../../../2008/07/ed-mathemagican-art-benjamin/trackback/index.html
[261]: ../../../../2008/07/follow-up-the-busy-beaver-function/trackback/index.html
[262]: ../../../../2008/07/ec-skyrocketing-functions/trackback/index.html
[263]: ../../../../2008/06/eb-busy-beavers-and-dumb-robots/trackback/index.html
[264]: ../../../../2008/06/ea-the-limits-of-computation/trackback/index.html
[265]: ../../../../2008/05/dz-mind-control-across-time-and-space/trackback/index.html
[266]: ../../../../2008/05/dy-the-symmetries-of-things/trackback/index.html
[267]: ../../../../2008/05/dx-dumb-robots/trackback/index.html
[268]: ../../../../2008/05/dw-the-online-encyclopedia-of-integer-sequences/trackback/index.html
[269]: ../../../../2008/05/dw-dealing-with-chaos/trackback/index.html
[270]: ../../../../2008/04/du-chaos-at-the-card-table/trackback/index.html
[271]: ../../../../2008/04/follow-up-smullyans-paradoxes/trackback/index.html
[272]: ../../../../2008/04/dt-speaking-of-self-reference/trackback/index.html
[273]: ../../../../2008/04/ds-math-chat-with-frank-morgan/trackback/index.html
[274]: ../../../../2008/04/dr-double-bubble/trackback/index.html
[275]: ../../../../2008/03/dq-we-are-not-liars/trackback/index.html
[276]: ../../../../2008/03/dp-would-chuck-wood/trackback/index.html
[277]: ../../../../2008/03/do-proofs-puzzles-and-conundra/trackback/index.html
[278]: ../../../../2008/03/dn-ed-burgers-trouser-puzzle/trackback/index.html
[279]: ../../../../2008/02/dm-on-codes-primes-and-kings/trackback/index.html
[280]: ../../../../2008/02/dl-the-wicked-king-problem/trackback/index.html
[281]: ../../../../2008/02/02/greetings-from-the-math-factor/index.html
[282]: ../../../../2008/01/dk-flipping-the-mattress/trackback/index.html
[283]: ../../../../2008/01/dj-pegg-on-numb3rs/trackback/index.html
[284]: ../../../../2008/01/09/follow-up-prime-dice/index.html
[285]: ../../../../2008/01/di-dice-games/trackback/index.html
[286]: ../../../../2008/01/dh-ice-cream-cake/trackback/index.html
[287]: ../../../../2008/01/dealornodeal/trackback/index.html
[288]: ../../../12/q-a-a-little-puzzle/trackback/index.html
[289]: ../../../12/dg-ants-on-a-rod/trackback/index.html
[290]: ../../../12/df-the-best-full-house/trackback/index.html
[291]: ../../../12/de-the-apples-in-stereo/trackback/index.html
[292]: ../../../12/q-and-a-deal-or-no-deal/trackback/index.html
[293]: ../../../12/dd-should-we-teach-college-algebra/trackback/index.html
[294]: ../../../11/dc-psychology-matters/trackback/index.html
[295]: ../../../11/db-envelope-mystery/trackback/index.html
[296]: ../../da-a-cake-conundrum/trackback/index.html
[297]: ../../cz-a-parlour-trick/trackback/index.html
[298]: ../../../09/cw-the-surreal-numbers/trackback/index.html
[299]: ../../../09/cv-dividing-the-loot/trackback/index.html
[300]: ../../../08/cu-eminently-logical-pirates/trackback/index.html
[301]: ../../../08/ct-odd-people/trackback/index.html
[302]: ../../../08/follow-up-weird-sums/trackback/index.html
[303]: ../../../08/cs-perfect-sums/trackback/index.html
[304]: ../../../07/cr-clock-confusion/trackback/index.html
[305]: ../../../06/cq-dollar-auction/trackback/index.html
[306]: ../../../06/cp-the-prisoners-dilemma/trackback/index.html
[307]: ../../../06/follow-up-mismatched-pennies/trackback/index.html
[308]: ../../../06/qa-numerous-numbers/trackback/index.html
[309]: ../../../06/co-mismatched-pennies/trackback/index.html
[310]: ../../../05/cn-name-that-date/trackback/index.html
[311]: ../../../05/cm-crossing-the-bridge/trackback/index.html
[312]: ../../../05/cl-some-number-of-numbers-sum/trackback/index.html
[313]: ../../../05/ck-the-third-tree/trackback/index.html
[314]: ../../../05/follow-up-the-stork-and-the-frog/trackback/index.html
[315]: ../../../04/cj-the-stork-and-the-frog/trackback/index.html
[316]: ../../../04/ci-the-royal-order-of-the-garter/trackback/index.html
[317]: ../../../04/15/ch-rayos-number/index.html
[318]: ../../../04/follow-up-grahams-number/trackback/index.html
[319]: ../../../04/09/cg-grahams-number/index.html
[320]: ../../../04/the-race/trackback/index.html
[321]: ../../../04/cf-mind-boggling/trackback/index.html
[322]: ../../../03/ce-big-numbers/trackback/index.html
[323]: ../../../03/qa-why-is-0-1/index.html
[324]: ../../../03/cd-alas-up-to-a-million-dollars-might-have-been-given-away/trackback/index.html
[325]: ../../../03/cc-fair-division/trackback/index.html
[326]: ../../../03/cb-pi-day/trackback/index.html
[327]: ../../../02/ca-cut-the-cake/trackback/index.html
[328]: ../../../02/bz-two-teams/trackback/index.html
[329]: ../../../02/by-guests-at-a-party/trackback/index.html
[330]: ../../../02/bw-the-math-factor-million-dollar-give-away/trackback/index.html
[331]: ../../../02/9s-strike-again/trackback/index.html
[332]: ../../../01/the-online-mind-reader/trackback/index.html
[333]: ../../../01/a-runcinated-dodecaplex/trackback/index.html
[334]: ../../../01/aha-escape/trackback/index.html
[335]: ../../../01/we-dont-know-the-way-out/trackback/index.html
[336]: ../../../../2006/12/the-smuggler-is-paid/trackback/index.html
[337]: ../../../../2006/12/the-smugglers-fee/trackback/index.html
[338]: ../../../../2006/11/when-did-you-say/trackback/index.html
[339]: ../../../../2006/11/puzzling-panelists/trackback/index.html
[340]: ../../../../2006/11/an-astronomical-cost/trackback/index.html
[341]: ../../../../2006/10/eternally-diminishing-returns/trackback/index.html
[342]: ../../../../2006/10/bananas-and-rockets/trackback/index.html
[343]: ../../../../2006/10/the-most-powerful-force/trackback/index.html
[344]: ../../../../2006/10/the-shape-of-the-universe/trackback/index.html
[345]: ../../../../2006/09/the-poincare-conjecture/trackback/index.html
[346]: ../../../../2006/09/bamboopalooza/trackback/index.html
[347]: ../../../../2006/09/catching-errors/trackback/index.html
[348]: ../../../../2006/09/trap-door-encryption/trackback/index.html
[349]: ../../../../2006/08/magic-numbers/trackback/index.html
[350]: ../../../../2006/08/casting-out-nines/trackback/index.html
[351]: ../../../../2006/08/the-ring-is-exchanged/trackback/index.html
[352]: ../../../../2006/08/another-puzzle-from-peter-winkler/trackback/index.html
[353]: ../../../../2006/07/dollar-cost-averaging/trackback/index.html
[354]: ../../../../2006/07/averages-are-not-what-they-seem/trackback/index.html
[355]: ../../../../2006/07/will-we-run-out-of-social-security-numbers/trackback/index.html
[356]: ../../../../2006/07/dennis-shasha-answers/trackback/index.html
[357]: ../../../../2006/07/dennis-shasha-asks-about-polish-multiplication/trackback/index.html
[358]: ../../../../2006/05/peter-winkler-answers/trackback/index.html
[359]: ../../../../2006/05/a-puzzle-from-peter-winkler/trackback/index.html
[360]: ../../../../2006/05/a-quick-game/trackback/index.html
[361]: ../../../../2006/04/the-principle-of-indifference-redux/trackback/index.html
[362]: ../../../../2006/04/choosing-balls-from-a-bag/trackback/index.html
[363]: ../../../../2006/04/more-sucker-bets/trackback/index.html
[364]: ../../../../2006/04/arrows-theorem/trackback/index.html
[365]: ../../../../2006/03/rumors-and-suckers/trackback/index.html
[366]: ../../../../2006/03/paradoxes-and-liars/trackback/index.html
[367]: ../../../../2006/03/the-pop-quiz/trackback/index.html
[368]: ../../../../2006/03/census-takers-puzzle/trackback/index.html
[369]: ../../../../2006/01/qed/trackback/index.html
[370]: ../../../../2005/12/17/the-eagle/index.html
[371]: ../../../../2005/12/counting-all/trackback/index.html
[372]: ../../../../2005/11/the-jalopy/trackback/index.html
[373]: ../../../../2005/11/bigger-and-smaller-infinities/trackback/index.html
[374]: ../../../../2005/11/no-vacancy/trackback/index.html
[375]: ../../../../2005/10/the-rational-ruler/trackback/index.html
[376]: ../../../../2005/10/the-way-out-of-the-forest/trackback/index.html
[377]: http://mathfactor.uark.edu/wp-login.php
[378]: http://mathfactor.uark.edu/feed/
[379]: http://mathfactor.uark.edu/comments/feed/
[380]: http://wordpress.org
[381]: http://weblogs.us
[382]: http://www.kuaf.org
[383]: http://math.uark.edu
[384]: http://uark.edu
[385]: http://validator.w3.org/check/referer
[386]: http://jigsaw.w3.org/css-validator/check/referer
[387]: http://wordpress.org/extend/plugins/podpress/
