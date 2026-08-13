<!-- source: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fractions/egyptian.html | converted from HTML -->

Egyptian Fractions

## Egyptian Fractions

The ancient Egyptians only used fractions of the form 1 / n so any other fraction had to be represented as a *sum of such unit fractions*and, furthermore, all the unit fractions were different!
Why? Is this a better system than our present day one? In fact, it *is*for some tasks.

This page explores some of the history and methods with puzzles and and gives you a summary of computer searches for such representations. There's lots of investigations to do in this area of maths suitable for 8-10 year olds as well as older students and it is also designed as a resource for teachers and educators. The Calculators embedded in the page provide helpful resources for your number searches.

This page has an auto-generated Content section which may take a second or two to appear.
This section will then disappear but you need to have JavaScript enabled in your browser.

The calculators on this page also require JavaScript but you appear to have switched JavaScript off (it is disabled). Please go to the Preferences for this browser and enable it if you want to use the calculators, then Reload this page.

Contents of this page

The [image: You do the Maths...] icon indicates a You do the Maths... section of questions to start your own investigations. The [image: calculator] calculator icon indicates that there is a live interactive calculator in that section.

- An Introduction to Egyptian Mathematics

- Henry Rhind and his Papyrus scroll

- Egyptian Fractions

- Why use Egyptian fractions today?
- A practical use of Egyptian Fractions[image: You do the Maths...]
- Comparing Egyptian fractions [image: You do the Maths...]
- A Calculator to convert a Fraction to an Egyptian Fraction[image: Calculator]

- Different representations for the same fraction

- Each fraction has an infinite number of Egyptian fraction forms

- Every ordinary fraction has an Egyptian Fraction form

- Fibonacci's Method a.k.a. the Greedy Algorithm[image: You do the Maths...]
- A Proof optional

- Shortest Egyptian Fractions

- The *greedy method*and the *shortest*Egyptian fraction
- A Calculator for Shortest Egyptian Fractions[image: Calculator]
- The number of Shortest Length Egyptian Fractions

  - Shortest Egyptian Fractions lengths for fraction T/B
  - Are there fractions whose shortest EF length is 3 (4, 5, ..) ?

- Finding patterns for shortest Egyptian Fractions
- How many Egyptian Fractions of shortest length are there for T/B?

- Fixed Length Egyptian Fractions[image: Calculator][image: You do the Maths...]

- Egyptian fractions for 4/n and the Erd&ouml;s-Straus Conjecture[image: You do the Maths...]
- 5/n = 1/x + 1/y + 1/z? [image: You do the Maths...]

- Smallest Denominators
- The 2/n Table of the Rhind Papyrus[image: You do the Maths...]
- Links and References

-->

## An Introduction to Egyptian Mathematics

Some of the oldest writing in the world is on a form of paper made from papyrus reeds that grew all along the Nile river in Egypt. [image: map of upper Nile] [1] [The image is a link to [David Joyce's site][2] on the History of Maths at Clarke University.] The reeds were squashed and pressed into long sheets like a roll of wall-paper and left to dry in the sun. When dry, these scrolls could be rolled up and easily carried or stored.

Some of the papyrus scrolls date back to about 2000 BC, around the time of the construction of the larger Egyptian pyramids. Because there are deserts on either side of the Nile, papyrus scrolls have been well preserved in the dry conditions.

So what was on them do you think? How to preserve a body as a mummy? Maybe it was how to construct the extensive system of canals used for irrigation across Egypt or on storage of grain in their great storage granaries? Perhaps they tell how to build boats out of papyrus reeds which float very well because pictures of these boats have been found in many Egyptian tombs?
The surprising answer is that the oldest ones are about *mathematics!*

### Henry Rhind and his Papyrus scroll

One of the papyrus scrolls, discovered in a tomb in Thebes, was bought by a 25 year old Scotsman, Henry Rhind at a market in Luxor, Egypt, in 1858. After his death at the age of 30, the scroll found its way to the British Museum in London in 1864 and remained there ever since, being referred to as the **Rhind Mathematical Papyrus**(or RMP for short).

[image: Rhind papyrus] [3] So what did it say?

The hieroglyphs (picture-writing) on the papyrus were only deciphered in 1842 (and the Babylonian clay-tablet cuneiform writing was deciphered later that century).

It starts off by saying that the scribe "Ahmes" is writing it about 1600 BC but that he had copied it from "ancient writings" which, from his description of the Pharoah of that time dates it to 2000 BC or earlier. The picture is also a link so click on it to go to the St Andrews MacTutor biography of Ahmes.

Since early civilisations would need to predict the start of spring accurately in order to sow seeds, then a large part of such mathematical writing has applications in astronomy. Also, calculations were needed for surveying (geometry) and for building and for accounting and for sharing bread and beer (given as wages) amongst several workers.

On this page we will look at how the Egyptians of 4000 years ago worked with fractions.

## Egyptian Fractions

The Egyptians of 3000 BC had an interesting way to represent fractions.
Although they had a notation for 1 / 2 and 1 / 3 and 1 / 4 and so on (these are called **reciprocals**or **unit fractions**since they are 1 / n for some number n), their notation did not allow them to write 2 / 5 or 3 / 4 or 4 / 7 as we would today.

Instead, they were able to write *any*fraction as ***a sum of unit fractions***where **all the unit fractions were different**.

For example,

3 / 4 = 1 / 2 + 1 / 4

6 / 7 = 1 / 2 + 1 / 3 + 1 / 42

*A fraction written as a sum of distinct unit fractions*is called an ***Egyptian Fraction***.

### Why use Egyptian fractions today?

Suppose you and 7 other friends go for a pizza. You all like the same kind but you don't want a whole one each. The 8 of you decide to buy 5 identical pizzas. How do you divide them up between you? Decimals don't help and that you each get 5/8 only tells you what the problem is (split 5 things into 8 parts) not the solution! It is easier with beer or sacks of grain. This was an everyday problem in ancient Egypt when barley loaves may have to be divided amongst workers.

### A practical use of Egyptian Fractions

So suppose Fatima has 5 loaves of bread to share among the 8 workers who have helped dig her fields today and clear the irrigation channels. They all need 5/8 of a loaf each. *Pause for a minute and decide how YOU would solve this problem before reading on.....*

HINT: What if there were only 4 loaves not 5 to be split amongst 8 people?

- First Fatima sees that they all get at least half a loaf,
so she uses 4 of the loaves to give all 8 of them half a loaf each.
She has one whole loaf left.
- Now it is easy to divide one loaf into 8, so they get an extra eighth of a loaf each

All the loaves are used and divided equally between the 8 workers. On the picture here they each receive one red part ( 1 / 2 a loaf) and one green part ( 1 / 8 of a loaf): [image: 4 loaves split into halves and 1 split into eighths]

and 5 / 8 = 1 / 2 + 1 / 8

The Egyptian solution has the added benefits of

- fewer crumbs/slices than dividing each loaf into 8 and giving 5 slices to each person.
- it is easy to see everyone has an identical number of pieces of the same sizes.
- each portion received is a fraction 1/n of a loaf. All the fractions are different and unit fractions

Try the following using the Egyptian style of thinking:

#### You do the Maths...

1. Suppose Fatima had 3 loaves to share between 4 people. How would she do it?

3/4 = 1/2 + 1/4

2. ...and what if it was 2 loaves amongst 5 people?

2/5 = 1/3 + 1/15 is the simplest solution

3. ...or 4 loaves between 5 people?

4/5 = 1/2 + 1/4 + 1/20 or
4/5 = 1/2 + 1/5 + 1/10

4. What about 13 loaves to share among 12 people? We could give them one loaf each and divide the 13 th into 12 parts for the final portion to give to everyone.
Try representing 13 / 12 as 1 / 2 + 1 / 3 + 1 / *. What does this mean - that is, how would you divide the loaves using this representation?
Was this easier?

12/13 = 1/2 + 1/3 + 1/12 + 1/156 12/13 = 1/2 + 1/3 + 1/13 + 1/78 12/13 = 1/2 + 1/4 + 1/6 + 1/156

It turns out that Egyptian fractions are not only a very pratical solution to *some*everyday problems today but are interesting in their own right. They had practical uses in the ancient Egyptian method of multiplying and dividing, and every fraction t / b can always be written as an Egyptian fraction, which we will show further down on this page. There are also many unsolved problems concerning them, which are still a puzzle to mathematicians today.

### A Calculator to convert a Fraction to and from an Egyptian Fraction

An Egyptian Fraction for t / b is a sum of unit fractions, *all different*.

- Enter your fraction in the boxes below and then click on the **Convert to an Egyptian fraction**button EF"> and the denominators of an equivalent Egyptian fraction will be put Denominators box and displayed in the RESULTS window.
- Alternatively, type in a list of the unit fraction's denominators (they need not all be different but they should all be bigger than 1) and then press the Fraction"> button to fill in the fraction boxes with its sum.

Use the Shortest Unit Fraction Sum Calculator or the Fixed Length Egyptian Fractions Calculator to find **all**the Egyptian Fractions but this calculator is quicker if you just want one.
**The method used in this calculator is the Greedy Algorithm**which we will examine in more detail below. The disadvantage of the "greedy" method is that sometimes it will fail to fully convert a fraction if a denominator gets too large for the Calculator.

Fraction &harr; Unit Fractions Sum C A L C U L A T O R

Fraction |  | Denominators |

 | Convert the Fraction to an list of denominators"> EF">
Fraction">
 |  |

[image: --] |

R E S U L T S

[image: calculator]: | Fraction &harr; EF | Shortest EF | Fixed Length EFs | EFs for 1 | --> productive EFs | Harmonic Numbers |

## Different representations for the same fraction

We have already seen that 3 / 4 = 1 / 2 + 1 / 4
Can you write 3 / 4 as 1 / 2 + 1 / 5 + 1 / *?
What about 3 / 4 as 1 / 2 + 1 / 6 + 1 / *?
How many more can you find?

Here are some results that mathematicians have proved:

- Every fraction t / b can be written as a sum of unit fractions...
- .. and each can be written in an infinite number of such ways!

Now let's examine each of these in turn and I'll try to convince you that each is true for all fractions t / b less than one (so that T, the number on top, is smaller than B, the bottom number).

You can skip over these two sub-sections if you like.

### Each fraction has an infinite number of Egyptian fraction forms

To see why the second fact is true, consider this:

1 = 1 / 2 + 1 / 3 + 1 / 6 (*)

So if
3 / 4 = 1 / 2 + 1 / 4
Let's use (*) to *expand*the final fraction 1 / 4:
So let's divide equation (*) by 4:

1 / 4 = 1 / 8 + 1 / 12 + 1 / 24

which we can then feed back into our Egyptian fraction for 3 / 4:
3 / 4 = 1 / 2 + 1 / 4
3 / 4 = 1 / 2 + 1 / 8 + 1 / 12 + 1 / 24
But now we can do the same thing for the final fraction here, dividing equation (*) by 24 this time. Since we are choosing the largest denominator to expand, it will be replaced by even larger ones so we won't repeat any denominators that we have used already:

1 / 24 = 1 / 48 + 1 / 72 + 1 / 144

and so
3 / 4 = 1 / 2 + 1 / 8 + 1 / 12 + 1 / 48 + 1 / 72 + 1 / 144
Now we can repeat the process by again expanding the last term: 1 / 144 and so on for ever!
Each time we get a different set of unit fractions which add to 3 / 4!
This shows conclusively once we have found one way of writing t / b as a sum of unit fractions, then we can derive as many other representations as we wish! If T=1 already (so we have 1 / B) then using (*) we can always start off the process by dividing (*) by B to get an initial 3 unit fractions that sum to 1 / B.

### Every ordinary fraction has an Egyptian Fraction form

We now show there is *always*at least one set of distinct unit fractions which sum to any given fraction t / b ≤1 by actually showing how to find such a sum.

## Fibonacci's Greedy Algorithm for finding Egyptian Fractions

This method and a proof are given by Fibonacci in his book *Liber Abaci*produced in 1202, the book in which he mentions the rabbit problem involving the [Fibonacci Numbers][4]. **It is the method used in the Fraction &harr; EF CALCULATOR above**.

Remember that

- **t / b and
- if t=1 the problem is solved since t / b is already a unit fraction, so
- we are interested in those fractions where **t>1**.

The method is to find the **biggest unit fraction we can and take it from t / b**and hence its other name - the **greedy algorithm**.
With what is left, we repeat the process. We will show that this series of unit fractions always decreases, never repeats a fraction and eventually will stop. Such processes are now called *algorithms*and this is an example of a *greedy algorithm*since we (greedily) take the largest unit fraction we can and then repeat on the remainder.

Let's look at an example before we present the proof: 521 / 1050.
521 / 1050 is less than one-half (since 521 is less than a half of 1050) but it is bigger than one-third. So the largest unit fraction we can take away from 521 / 1050 is 1 / 3:

521 / 1050 = 1 / 3 + R

What is the remainder?

521 / 1050 - 1 / 3 = 171 / 1050 = 57 / 350

So we repeat the process on 57 / 350:
This time the largest unit fraction less than 57 / 350 is 1 / 7 and the remainder is 1 / 50.

How do we know it is 7? Divide the bottom (larger) number, 350, by the top one, 57, and we get 6.14... . So we need a number larger than 6 (since we have 6 + 0.14) and the next one above 6 is 7.)

So

521 / 1050 = 1 / 3 + 57 / 350
= 1 / 3 + 1 / 7 + 7 / 350
= 1 / 3 + 1 / 7 + 1 / 50

The sequence of remainders is important in the proof that we do not have to keep on doing this for ever for some fractions t / b:

521 / 1050, 171 / 1050, 7 / 1050

*The numerator of the remainder is getting smaller each time*. If it keeps decreasing then it must eventually reach 1 and the process stops. In this example, we find the numerator becomes a factor of the denominator and so the final remainder is a unit fraction and we can stop.

Practice with these examples and then we'll have a look at finding *short*Egyptian fractions.

### You do the Maths...

The Greedy method is used in the Fraction &harr; EF CALCULATOR above

1. What does the greedy method give for 5 / 21?
What if you started with 1 / 6 (what is the remainder)?

5/12 = 1/5 + 1/27 + 1/945 by the Greedy method but
5/21 = 1/6 + 1/14

2. Can you improve on the greedy method's solution for 9 / 20 (that is, use fewer unit fractions)? [Hint: Express 9 as a sum of two numbers which are factors of 20.]

9/20 = 1/3 + 1/9 + 1/180
9/20 = 1/4 + 1/5

3. The numbers in the denominators can get quite large using the greedy method: What does the greedy method give for 5 / 91?
Can you find a *two term Egyptian fraction*for 5 / 91?
[Hint: Since 91 = 7x13, try unit fractions which are multiples of 7.]

5/91 = 1/19 + 1/433 + 1/249553 + 1/93414800161 + 1/too large
5/91 = 1/28 + 1/52

### A Proof

This section is optional: click on the button see the proof.

Now let's see how we can show this is true for all fractions t / b. We want

t / b = 1 / u 1 + 1 / u 2 + ... + 1 / u n
where u 1 2 n

Also, we are choosing the largest u 1 at each stage, hence the name of "the greedy algorithm".
What does this mean?
It means that

1 / u 1 t / b

but that 1 / u 1 is the *largest*such fraction. For instance, we found that 1 / 3 was the largest unit fraction less than 521 / 1050. This means that 1 / 2 would be *bigger*than 521 / 1050.
In general, if 1 / u 1 is the largest unit fraction less than t / b then

1 / u 1 -1 > t / b

To find the largest denominator, evaluate b / t and use that value if it is an integer, or else round it up if not.

Since t>1, neither 1 / u 1 nor 1 / u 1 -1 equal t / b.

**What is the remainder?**

It is

t / b – 1 / u 1 = (t*u 1 – b) / (b*u 1)

Also, since

1 / (u 1 -1) > t / b

then multiplying both sides by b we have

b/ (u 1 -1) > t

or, multiplying both sides by (u 1 -1) and expanding the brackets, then adding t and subtracting b from both sides we have:

b > t (u 1 - 1)
b > t u 1 - t
t > t u 1 - b

Now t*u 1 – b was the *numerator of the remainder*and we have just shown that *it is smaller than the original numerator*t. If the remainder, in its lowest terms, has a 1 on the top, we are finished. Otherwise, we can *repeat the process*on the remainder, which has a smaller denominator and so the remainder when we take off its largest unit fraction gets smaller still. Since t is a whole (positive) number, this process *must*inevitably terminate with a numerator of 1 at some stage.

That completes the proof that

- There is always a *finite*list of unit fractions whose sum is any given fraction t / b
- We can find such a sum by taking the largest unit fraction at each stage and repeating on the remainder (the *greedy algorithm*)
- The unit fractions so chosen get smaller and smaller (and so all are unique)

The next section explores the ***shortest**Egyptian fractions *for any given fraction.

## Shortest Egyptian Fractions

### The *greedy method*and the *shortest*Egyptian fraction

However, the Egyptian fraction produced by the greedy method may not be the shortest such fraction. Here is an example:
by the greedy method, 4 / 17 reduces to

4 / 17 = 1 / 5 + 1 / 29 + 1 / 1233 + 1 / 3039345

whereas we can also check that

4 / 17 = 1 / 5 + 1 / 30 + 1 / 510

Here is the complete list of all the *shortest*representations of t / b for b up to 11. We use a *list notation*here to make the unit fractions more readable. For instance, above we saw that:

4 / 5 = 1 / 2 + 1 / 4 + 1 / 20

which we will write as:

4 / 5 = [2, 4, 20]

2 / 3 | = [2, 6] |

2 / 5 | = [3, 15] |

2 / 7 | = [4, 28] |

2 / 9 | = [5, 45] = [6, 18] |

2 / 11 | = [6, 66] |

 |

3 / 4 | = [2, 4] |

3 / 5 | = [2, 10] |

3 / 7 | = [3, 11, 231] = [3, 12, 84] = [3, 14, 42] = [3, 15, 35] = [4, 6, 84] = [4, 7, 28] |

3 / 8 | = [3, 24] = [4, 8] |

3 / 10 | = [4, 20] = [5, 10] |

3 / 11 | = [4, 44] |

 |

4 / 5 | = [2, 4, 20] = [2, 5, 10] |

4 / 7 | = [2, 14] |

4 / 9 | = [3, 9] |

4 / 11 | = [3, 33] |

 |

5 / 6 | = [2, 3] |

5 / 7 | = [2, 5, 70] = [2, 6, 21] = [2, 7, 14] |

5 / 8 | = [2, 8] |

5 / 9 | = [2, 18] |

5 / 11 | = [3, 9, 99] = [3, 11, 33] = [4, 5, 220] |

 |

6 / 7 | = [2, 3, 42] |

6 / 11 | = [2, 22] |

 |

7 / 8 | = [2, 3, 24] = [2, 4, 8] |

7 / 9 | = [2, 4, 36] = [2, 6, 9] |

7 / 10 | = [2, 5] |

7 / 11 | = [2, 8, 88] = [2, 11, 22] |

 |

8 / 9 | = [2, 3, 18] |

8 / 11 | = [2, 5, 37, 4070] = [2, 5, 38, 1045] = [2, 5, 40, 440] = [2, 5, 44, 220] = [2, 5, 45, 198] = [2, 5, 55, 110] = [2, 5, 70, 77] = [2, 6, 17, 561] = [2, 6, 18, 198] = [2, 6, 21, 77] = [2, 6, 22, 66] = [2, 7, 12, 924] = [2, 7, 14, 77] = [2, 8, 10, 440] = [2, 8, 11, 88] = [3, 4, 7, 924] |

 |

9 / 10 | = [2, 3, 15] |

9 / 11 | = [2, 4, 15, 660] = [2, 4, 16, 176] = [2, 4, 20, 55] = [2, 4, 22, 44] = [2, 5, 10, 55] |

 |

10 / 11 | = [2, 3, 14, 231] = [2, 3, 15, 110] = [2, 3, 22, 33] |

8 / 11 has an unusually large number of different (shortest) representations!

#### A Calculator for Shortest Egyptian Fractions

The calculator below will find all the Egyptian fractions of shortest length for an ordinary fraction.

Shortest Egyptian Fractions C A L C U L A T O R

[image: calculator]: | Fraction &harr; EF | Shortest EF | Fixed Length EFs | EFs for 1 | --> productive EFs | Harmonic Numbers |

### The number of Shortest Length Egyptian Fractions

Here is a table of the ***lengths***of the *shortest*Egyptian Fractions for all fractions t / b (Top over Bottom) where the denominator B takes all values up to 30:

### Shortest Egyptian Fractions lengths

KEY:

–  | means the fraction t / b is not in its lowest form  |

.  | means the fraction t / b is bigger than 1 |

The *minimum*number of unit fractions that are needed for t / b

\B: 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 T\ 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 2| 2 - 2 - 2 - 2 - 2 - 2 - 2 - 2 - 2 - 2 - 2 - 2 - 2 - 2 - 3| . 2 2 - 3 2 - 2 2 - 3 2 - 2 2 - 3 2 - 2 2 - 2 2 - 2 2 - 4| . . 3 - 2 - 2 - 2 - 3 - 2 - 3 - 2 - 2 - 2 - 3 - 2 - 3 - 5| . . . 2 3 2 2 - 3 2 3 2 - 2 3 2 2 - 2 3 3 2 - 2 2 2 2 - 6| . . . . 3 - - - 2 - 3 - - - 2 - 3 - - - 2 - 2 - - - 2 - 7| . . . . . 3 3 2 3 2 2 - 3 3 3 2 3 2 - 3 3 2 3 2 2 - 3 2 8| . . . . . . 3 - 4 - 3 - 2 - 4 - 3 - 2 - 2 - 3 - 3 - 3 - 9| . . . . . . . 3 4 - 3 2 - 2 2 - 4 2 - 3 3 - 3 2 - 2 3 - 10| . . . . . . . . 4 - 3 - - - 3 - 2 - 2 - 3 - - - 2 - 2 - 11| . . . . . . . . . 3 3 3 3 3 3 2 3 2 2 - 3 2 3 3 3 2 3 2 12| . . . . . . . . . . 4 - - - 3 - 3 - - - 2 - 4 - - - 4 - 13| . . . . . . . . . . . 4 3 3 3 3 3 3 3 2 3 2 2 - 3 3 3 2 14| . . . . . . . . . . . . 3 - 4 - 4 - - - 3 - 3 - 2 - 4 - 15| . . . . . . . . . . . . . 4 4 - 4 - - 3 4 - - 2 - 2 2 - 16| . . . . . . . . . . . . . . 5 - 3 - 3 - 4 - 3 - 3 - 3 - 17| . . . . . . . . . . . . . . . 3 4 3 3 3 4 3 3 3 3 3 3 2 18| . . . . . . . . . . . . . . . . 4 - - - 4 - 3 - - - 4 - 19| . . . . . . . . . . . . . . . . . 3 3 3 4 3 3 4 3 3 4 3 20| . . . . . . . . . . . . . . . . . . 4 - 4 - - - 4 - 4 - 21| . . . . . . . . . . . . . . . . . . . 4 5 - 3 4 - - 4 - 22| . . . . . . . . . . . . . . . . . . . . 5 - 4 - 4 - 3 - 23| . . . . . . . . . . . . . . . . . . . . . 3 4 4 3 3 4 3 24| . . . . . . . . . . . . . . . . . . . . . . 4 - - - 4 - 25| . . . . . . . . . . . . . . . . . . . . . . . 4 4 3 4 - 26| . . . . . . . . . . . . . . . . . . . . . . . . 4 - 4 - 27| . . . . . . . . . . . . . . . . . . . . . . . . . 4 5 - 28| . . . . . . . . . . . . . . . . . . . . . . . . . . 5 - 29| . . . . . . . . . . . . . . . . . . . . . . . . . . . 4  |

### Are there fractions whose shortest Egyptian Fraction length is 3 (or 4 or 5, ..) ?

From the table above, we see the "smallest" fraction that needs *three*terms is T=4 B=5 i.e. 4 / 5
In fact there are *two*ways to write 4 / 5 as a sum of *three*unit fractions:

4 / 5 = 1 / 2 + 1 / 4 + 1 / 20 and 4 / 5 = 1 / 2 + 1 / 5 + 1 / 10

There are many other fractions whose shortest Egyptian fraction has 3 unit fractions. Those with a denominator 10 or less are:

4 / 5 3 / 7 5 / 7 6 / 7 7 / 8 7 / 9 8 / 9 9 / 10

**Is there a fraction that needs 4 unit fractions?**
Yes! 8 / 11 cannot be written as a sum of less than 4 unit fractions, for instance

8 / 11 = 1 / 2 + 1 / 6 + 1 / 22 + 1 / 66

and there are 15 other Egyptian fractions of length 4 for this fraction.
Other fractions with a denominator 20 or less that need at least 4 unit fractions are:

8 / 11 9 / 11 10 / 11 12 / 13 13 / 14 15 / 16 8 / 17 14 / 17 15 / 17 9 / 19 14 / 19 15 / 19 17 / 19 18 / 19

This leads us naturally to ask:
**Is there a fraction that needs 5 unit fractions?**
Yes! The smallest numerator and denominator are for the fraction 16 / 17

16 / 17 = 1 / 2 + 1 / 3 + 1 / 17 + 1 / 34 + 1 / 51

and there are 38 other Egyptian fractions of length 5 for this fraction.
Other fractions with a denominator 40 or less that need 5 unit fractions are:

16 / 17 21 / 23 22 / 23 27 / 29 28 / 29 30 / 31 32 / 34 33 / 34 36 / 37 37 / 38 38 / 39

Continuing:
**The smallest fraction needing 6 unit fractions is 77 / 79**

77 / 79 = 1 / 2 + 1 / 3 + 1 / 8 + 1 / 79 + 1 / 474 + 1 / 632

and there are 159 other Egyptian fractions of length 6 for this fraction.
Other fractions with a denominator up to 130 that need 6 unit fractions are:

77 / 79 101 / 107 102 / 103 104 / 107 106 / 107 108 / 109 112 / 113 115 / 118 117 / 118 119 / 127 123 / 127

**The smallest fraction needing 7 unit fractions is 732 / 733**

732 / 733 = 1 / 2 + 1 / 3 + 1 / 7 + 1 / 45 + 1 / 7330 + 1 / 20524 + 1 / 26388

seems to be the one with the smallest numbers (the maximum denominator is the least among all the solutions) according to David Epstein in [this MathForum post][5] of March 2000.
He also states that he found 2771 separate 7-term Egyptian fractions for this fraction.

**The smallest fraction needing 8 unit fractions is 27538 / 27539**.
Mr. Huang Zhibin () of China in April 2014 has verified that this fraction needs 8 unit fractions and gives this example:

27538 / 27539 = 1 / 2 + 1 / 3 + 1 / 7 + 1 / 43 + 1 / 1933 + 1 / 14893663 + 1 / 1927145066572824 + 1 / 212829231672162931784

Beyond 8 unit fractions is unknown territory!

- [A097049][6] has the numerators and [A097048][7] the denominators of these "smallest" fractions which need at least 2,3,4,5,... terms in any Egyptian Fraction.

### Finding patterns for shortest Egyptian Fractions

There seem to be lots of patterns to spot in the table above.
The top row, for instance, seems to have the pattern that 2 / B can be written as a sum of just 2 unit fractions (providing that B is odd since otherwise, 2 / B would not be in its "lowest form"). The odd numbers are those of the form 2i+1 as i goes from 1 upwards. Let's list some of these in full:

i | 2 / (2i+1) |

1  | 2 / 3 = 1 / 2 + 1 / 6 |

2  | 2 / 5 = 1 / 3 + 1 / 15 |

3  | 2 / 7 = 1 / 4 + 1 / 28 |

4  | 2 / 9 = 1 / 5 + 1 / 45
2 / 9 = 1 / 6 + 1 / 18 |

5  | 2 / 11 = 1 / 6 + 1 / 66 |

6  | 2 / 13 = 1 / 7 + 1 / 91 |

7  | 2 / 15 = 1 / 8 + 1 / 120
2 / 15 = 1 / 9 + 1 / 45
2 / 15 = 1 / 10 + 1 / 30
2 / 15 = 1 / 12 + 1 / 20 |

Let's concentrate on the first sum on each line since some of the fractions above have more than one form as a sum of two unit fractions.

It looks as if

2 / 2i+1 = 1 / i+1 + 1 /?

Can you spot how we can use (2i+1) and i to find the missing number?
Here is the table again with the (2i+1) and i+1 parts in red and the **?**number is in green:

i | 2 / 2i+1 | = 1 / i+1 + 1 /? |

1 | 2 / 3 | = 1 / 2 + 1 / 6 |

2 | 2 / 5 | = 1 / 3 + 1 / 15 |

3 | 2 / 7 | = 1 / 4 + 1 / 28 |

4 | 2 / 9 | = 1 / 5 + 1 / 45 | = 1 / 6 + 1 / 18 |

5 | 2 / 11 | = 1 / 6 + 1 / 66 |

6 | 2 / 13 | = 1 / 7 + 1 / 91 |

7 | 2 / 15 | = 1 / 8 + 1 / 120 | = 1 / 9 + 1 / 45 | = 1 / 10 + 1 / 30 | = 1 / 12 + 1 / 20 |

8 | 2 / 17 | = 1 / 9 + 1 / 153 |

9 | 2 / 19 | = 1 / 10 + 1 / 190 |

Yes! Just multiply the red numbers i+1 and 2i+1 to get the green ones!

So it looks like we may have the pattern:

2 | =  | 1 | +  | 1 |

2i + 1 | i + 1 | (i + 1)(2i + 1) |

We can check it by simplifying the fraction on the right and the algebra will show us that the formula is *always true*.

Ben Thurston (May 2017) emailed me two other simple formulae:

1 | =  | 1 | +  | 1 |

a b | a (a + b) | b (a + b) |

1 | =  | 1 | +  | 1 | +  | 1 |

a b c | a (ab + bc + ca) | b (ab + bc + ca) | c (ab + bc + ca) |

For example, the first formula applies to 1 / 15 = 1 / 3×5 = 1 / 3×8 + 1 / 5×8 = 1 / 24 + 1 / 40

### How many Egyptian Fractions of shortest length are there for T/B?

Here is a table like the one above, but this time each entry is a **count**of all the ways we can write t / b as a sum of the **minimum**number of unit fractions:
For instance, we have seen that 4 / 5 can be written with a minimum of 2 unit fractions, so **2**appears in the first table under t / b = 4 / 5.
But we saw that 4 / 5 has *two ways*in which it can be so written, so in the following table we have entry 2 under t / b = 4 / 5.
2 / 15 needs at least 2 unit fractions in its Egyptian form: here are all the variations:

2 / 15 | = 1 / 8 + 1 / 120 |

 | = 1 / 9 + 1 / 45 |

 | = 1 / 10 + 1 / 30 |

 | = 1 / 12 + 1 / 20 |

so it has *four*representations. In the table below, under t / b = 2 / 15 we have the entry *4*:

```
NUMBER of Shortest Egyptian Fractions:\B  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30T\                                                                                        2  .  1  -  1  -  1  -  2  -  1  -  1  -  4  -  1  -  1  -  4  -  1  -  2  -  3  -  1  - 3  .  .  1  1  -  6  2  -  2  1  -  8  3  -  2  1  -  8  4  -  2  1  -  1  3  -  3  1  - 4  .  .  .  2  -  1  -  1  -  1  -  4  -  3  -  4  -  1  -  2  -  1  - 10  -  2  -  7  - 5  .  .  .  .  1  3  1  1  -  3  2  5  1  -  1  5  2  1  -  1 15  8  3  -  1  1  2  1  - 6  .  .  .  .  .  1  -  -  -  1  -  1  -  -  -  1  -  2  -  -  -  1  -  1  -  -  -  1  - 7  .  .  .  .  .  .  2  2  1  2  2  1  -  7  5  3  1  5  2  -  5  3  2 10  1  1  -  2  2 8  .  .  .  .  .  .  .  1  - 16  -  3  -  2  - 23  -  2  -  1  -  1  -  3  -  6  -  4  - 9  .  .  .  .  .  .  .  .  1  5  -  1  1  -  1  1  - 14  1  -  3  2  -  8  1  -  1  1  -10  .  .  .  .  .  .  .  .  .  3  -  1  -  -  -  3  -  1  -  1  -  1  -  -  -  1  -  1  -11  .  .  .  .  .  .  .  .  .  .  2  1  1  2  2  1  1  3  1  1  -  1  1  2  3  3  1  4  212  .  .  .  .  .  .  .  .  .  .  .  3  -  -  -  1  -  1  -  -  -  1  - 47  -  -  - 29  -13  .  .  .  .  .  .  .  .  .  .  .  .  6  2  1  1  2  1  5  4  1  2  1  1  -  2  5  1  114  .  .  .  .  .  .  .  .  .  .  .  .  .  1  -  2  -  5  -  -  -  1  -  4  -  1  - 10  -15  .  .  .  .  .  .  .  .  .  .  .  .  .  .  5  4  -  3  -  -  1 13  -  -  1  -  1  1  -16  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 39  -  1  -  1  -  7  -  1  -  4  -  2  -17  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  3  2  1  1  2  4  1  1  2  4  2  118  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  -  -  -  5  -  1  -  -  - 14  -19  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  1  1  1  2  1  8  2  2  6  620  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  5  -  4  -  -  -  8  -  5  -21  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  3 37  -  1  4  -  -  4  -22  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 23  -  6  -  6  -  1  -23  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  3  5  1  1  3  324  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  2  -  -  -  1  -25  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  1  4  1  5  -26  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  2  -  1  -27  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  5 20  -28  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 16  -29  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  7
```

 |

## Fixed Length Egyptian Fractions

The shortest Egyptian fractions do not always give the smallest numbers.
For example, the smallest number of unit fractions for 8 / 11 is 4; there are 16 of them and the one with the smallest numbers (i.e. the one whose largest denominator is the smallest) is 8/11 = 1/2 + 1/6 + 1/22 + 1/66
However, if we look for a larger collection, of 5 unit fractions, we find smaller numbers still:
8/11 = 1/2 + 1/11 + 1/12 + 1/33 + 1/44 and
8/11 = 1/3 + 1/4 + 1/11 + 1/33 + 1/44

Here we investigate Egyptian Fractions with more than the smallest number of reciprocals.
We have already seen that every fraction t / b has an Egyptian Fraction and, what is more, an infinite number of longer and longer Egyptian fraction forms.
So let's see what we can find about the number of Egyptian fractions for t / b of a given length L.

### A Fixed Length Egyptian Fraction Calculator

Fixed Length Egyptian fraction C A L C U L A T O R

[image: calculator]: | Fraction &harr; EF | Shortest EF | Fixed Length EFs | EFs for 1 | --> productive EFs | Harmonic Numbers |

### You Do the Maths...

1.

  1. Find the formula for the n-th sum in this series:

1 | +  | 1 | =  | 2 |

2 | 6 | 3 |

1 | +  | 1 | +  | 1 | =  | 3 |

2 | 6 | 12 | 4 |

1 | +  | 1 | +  | 1 | +  | 1 | =  | 4 |

2 | 6 | 12 | 20 | 5 |

... | =  | n |

n + 1 |

The unit fraction denominators on the left-hand-sides: 2, 6, 12, 20, ... are the [Oblong Numbers][8] k(k+1).
  2. Prove that your formula works.

## Odd denominators

In 1954 Breusch proved that every fraction with an odd denominator has an Egyptian fraction consisting of only odd denominators.
Here is a table of one example for each fraction less than 1 with an odd denominator up to 11, giving the Egyptian fraction as a list of the denominators. All these have the smallest maximum Egyptian fraction denominator:

1/3 &rarr; {5, 9, 45} |  | 1/5 &rarr; {9, 15, 45} |  | 1/7 &rarr; {15, 21, 35} |  | 1/9 &rarr; {15, 35, 63} |  | 1/11 &rarr; {21, 33, 77} |

2/3 &rarr; {3,5,9,45} |  | 2/5 &rarr; {3,15} |  | 2/7 &rarr; {7,15,21,35} |  | 2/9 &rarr; {5, 45} |  | 2/11 &rarr; {9, 33, 45, 55} |

 |  | 3/5 &rarr; {3,5,15} |  | 3/7 &rarr; {3,15,35} |  | 1/3 |  | 3/11 &rarr; {5, 15, 165} |

 |  | 4/5 &rarr; {3,5,7,15,21,105} |  | 4/7 &rarr; {3,7,15,35} |  | 4/9 &rarr; {3, 9} |  | 4/11 &rarr; {3, 33} |

 |  |  |  | 5/7 &rarr; {3,5,9,21,45} |  | 5/9 &rarr; {3, 5, 45} |  | 5/11 &rarr; {3, 11, 33} |

 |  |  |  | 6/7 &rarr; {3,5,7,9,21,45} |  | 2/3 |  | 6/11 &rarr; {3, 9, 11, 99} |

 |  |  |  |  |  | 7/9 &rarr; {3, 5, 9, 15, 35, 45, 63} |  | 7/11 &rarr; {3, 5, 15, 33, 165} |

 |  |  |  |  |  | 8/9 &rarr; {3, 5, 7, 9, 21, 35, 63, 105} |  | 8/11 &rarr; {3, 5, 9, 21, 45, 77} |

 |  |  |  |  |  |  |  | 9/11 &rarr; {3, 5, 9, 11, 21, 45, 77} |

 |  |  |  |  |  |  |  | 10/11 &rarr; {3, 5, 7, 11, 15, 21, 55, 105} |

- **4512 Solution:A Special Case of Egyptian Fractions**R Breusch *Amer Math Monthly*(March 1954) pages 200-201

The exercises below introduce a powerful and simple proof technique which uses just the even-ness and odd-ness of numbers, called their *parity*to prove some observations about the list above.
We return to this kind of reasoning when we consider **Egyptian fractions for 1 with odd denominator**later on this page.

### You do the Maths...

1. Looking at the list above, the lengths of the Egyptian fractions vary. However, a pattern emerges when we look at whether a list is of even or odd length.
Where do the even-length Egyptian fractions occur?
Can you make a conjecture?

If the numerator is even, the length of the Egyptian fraction is even.
If the numerator is odd, the length of the Egyptian fraction is odd.
**The parity of the numerator in a fraction with an odd denominator is the same as the parity of the length of an Egyptian fraction with only odd denominator unit fractions**

2. Consider an Egyptian fraction of just 2 odd denominators. Let's say 1/(2n+1) + 1/(2m+1). What can you say about the sum in terms of oddness and evenness (this is called *parity*)?

1/(2n+1) + 1/(2m+1) = (2n +2m + 2)/(2mn+2m+2n+1) = even/odd

3. Suppose we have 3 odd denominators in an Egyptian fraction. What about the parity of the sum of them?

1/(2n+1) + 1/(2m+1) = (2n +2m + 2)/(2mn+2m+2n+1) = even/odd
For three terms we have the above for two plus 1/odd:
even/odd 1 + 1/odd 2 = (even×odd 2 + odd 1)/(odd 1 ×odd 2) = odd/odd

4. Generalise the above for an all-odd-denominator Egyptian fraction for p/q if q is odd.

The total of any number of odd denominator unit fractions must have an odd denominator.
A total of even/odd can have only even length Egyptian fractions if all the denominators are odd
A total of odd/odd can have only odd length Egyptian fractions if all the denominators are odd.

## Egyptian Fractions for 1

Earlier we used an Egyptian Fraction for 1 in a proof that every Egyptian fraction can be expanded into an infinite number of alternative sums for the same fraction. We used:

1 = 1 / 2 + 1 / 3 + 1 / 6

This is both the the shortest way (3 fractions) and the one with the smallest maximum denominator (6). Before you read on, you might like to try and find 4 different unit fractions that sum to 1.

Hint:
6 = 3 + 2 + 1 and since it is a sum of different divisors of 6, we can divide by 6 to find our 3-term Egyptian fraction for 1 shown above.
Can you find another number which is also a sum of some of its divisors?
What about 12 = 6 + 4 + 2?
Dividing by 12 gives us 1 = 1 / 2 + 1 / 3 + 1 / 6 which we already know.

### Egyptian fractions for 1 by Length

Here is a fixed length Egyptian fraction for 1 that uses 4 unit fractions:

12 = 6 + 3 + 2 + 1 Dividing by 12 gives 1 = 1 / 2 + 1 / 4 + 1 / 6 + 1 / 12

Other solutions are found from

18 = 9 + 6 + 2 + 1> &hArr; 1 = 1 / 2 + 1 / 3 + 1 / 9 + 1 / 18
20 = 10 + 5 + 4 + 1 &hArr; 1 = 1 / 2 + 1 / 4 + 1 / 5 + 1 / 20
24 = 12 + 8 + 3 + 1 &hArr; 1 = 1 / 2 + 1 / 3 + 1 / 8 + 1 / 24
30 = 15 + 10 + 3 + 2 &hArr; 1 = 1 / 2 + 1 / 3 + 1 / 10 + 1 / 15
42 = 24 + 14 + 6 + 1 &hArr; 1 = 1 / 2 + 1 / 3 + 1 / 7 + 1 / 42

so there are 6 Egyptian fractions for 1 of length 4.

How about 5 different unit fractions that sum to 1?
There are more than 10 but less than 100.

Use the Calculator above to see all 72 solutions
The one with smallest denominators is 1 = 1/2 + 1/4 + 1/10 + 1/12 + 1/15

We found:

- 1 way to write 1 as a sum of 3 different unit fractions
- 6 ways to write it as a sum of 4 different unit fractions
- 72 ways to write it as a sum of 5

The number of ways to write 1 as a sum of 3, 4, 5, 6, 7 and 8 different unit fractions is

1, 6, 72, 2320, 245765, 151182379 which is [A006585][9]

We do not know any more terms in this series as the only approach so far has been to perform a computer search and the number of solutions is getting very large very quickly!
A table of the solutions for smaller lengths is given in [A073546][10] but the Calculator above will find these for you.

### Egyptian fractions for 1 by denominator sum

One was to get both short Egyptian fractions first as well as having smaller denominators is to organize any list of Egyptian fractions by the sum of the denominators in each Egyptian fraction.
Here is a list of Egyptian fractions for 1 arranged in order of denominator sum up to 50:

Denoms of
EF for 1 | Denom
sum |

1 | 1 |

2, 3, 6  | 11  |

2, 4, 6, 12  | 24  |

2, 3, 10, 15  | 30  |

2, 4, 5, 20  | 31  |

2, 3, 9, 18  | 32  |

2, 3, 8, 24  | 37  |

3, 4, 5, 6, 20  | 38  |

2, 4, 10, 12, 15  | 43  |

2, 4, 9, 12, 18
2, 5, 6, 12, 20  | 45  |

2, 4, 8, 12, 24
3, 4, 6, 10, 12, 15  | 50  |

### Egyptian fractions for 1 that begin 1/n

It seems there is always an Egyptian fraction for 1 which begins with 1/n for any n we like!
One such expression for 1 as a sum of distinct unit fractions of which the largest is 1/n is always guaranteed to exist for any and every n>1 as was shown by Botts in 1967:

- **A Chain Reaction Process in Number Theory**, Truman Botts, *Mathematics Magazine*, Vol. 40, No. 2 (1967), pages 55-65

Starting from 1 = 1/2 + 1/3 + 1/6, he uses the Splitting Equation:

1 | = | 1 | + | 1 |

n | n + 1 | n ( n + 1) |

to replace the smallest 1/n by the right-hand side of this equation. If any duplicates arise, he uses it again on one of the duplicates.
He proves that by repeating this process we can eventually remove all duplicates with any value 1/n as the largest unit fraction.
However the resulting lists of Egyptian fractions become quite long quite quickly:

Denominators | Length |

2, 3, 6 | 3 |

3, 4, 6, 7, 12, 42 | 6 |

4, 5, 6, 7, 12, 13, 20, 42, 156 | 9 |

5, 6, 7, 8, 12, 13, 20, 21, 30, 42, 43, 56, 156, 420, 1806 | 15 |

6, 7, 8, 9, 12, 13, 20, 21, 30, 31, 42, 43, 44, 56, 57, 72, 156, 420, 930, 1806, 1807, 1892, 3192, 3263442 | 24 |

7, 8, 9, 10, 12, 13, 20, 21, 30, 31, 42, 43, 44, 45, 56, 57, 58, 72, 73, 90, 156, 420, 930, 1806, 1807, 1808, 1892, 1893, 1980, 3192, 3193, 3306, 5256, 3263442, 3263443, 3267056, 3581556, 10192056, 10650056950806 | 39 |

Two questions now arise

Is there a method that produces shorter Egyptian fractions for 1 beginning with a given 1/n?
Is there a method that produces smaller denominators than the above, that is, the maximum denominator is "small"?

Here is a table of some of the shorter Egyptian fractions for 1 beginning with 1/n:

n | Denominators  |

2 | 2, 3, 6 |

3 | 3, 4, 6, 10, 12, 15 |

4 | 4, 5, 6, 9, 10, 15, 18, 20 |

5 | 5, 6, 8, 9, 10, 12, 15, 18, 20, 24 |

6 | 6, 7, 8, 9, 10, 12, 14, 15, 18, 24, 28 |

7 | 7, 8, 9, 10, 11, 12, 14, 15, 18, 22, 24, 28, 33 |

8 | 8, 9, 10, 11, 12, 14, 15, 18, 20, 21, 22, 28, 30, 33, 35, 40 |

These are not the shortest: 3, 4, 5, 6, 20 is shorter starting with 3 but maybe they have the smallest (maximum) denominators?
**Can you find any shorter or with smaller numbers?**

Prof Greg Martin of the University of British Columbia has found a remarkable Egyptian fraction for 1 with 454 denominators all less than 1000:

97, 103, 109, 113, 127, 131, 137, 190, 192, 194, 195, 196, 198, 200,
203, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217,
218, 219, 220, 221, 225, 228, 230, 231, 234, 235, 238, 240, 244, 245,
248, 252, 253, 254, 255, 256, 259, 264, 265, 266, 267, 268, 272, 273,
274, 275, 279, 280, 282, 284, 285, 286, 287, 290, 291, 294, 295, 296,
299, 300, 301, 303, 304, 306, 308, 309, 312, 315, 319, 320, 321, 322,
323, 327, 328, 329, 330, 332, 333, 335, 338, 339, 341, 342, 344, 345,
348, 351, 352, 354, 357, 360, 363, 364, 365, 366, 369, 370, 371, 372,
374, 376, 377, 378, 380, 385, 387, 390, 391, 392, 395, 396, 399, 402,
403, 404, 405, 406, 408, 410, 411, 412, 414, 415, 416, 418, 420, 423,
424, 425, 426, 427, 428, 429, 430, 432, 434, 435, 437, 438, 440, 442,
445, 448, 450, 451, 452, 455, 456, 459, 460, 462, 464, 465, 468, 469,
470, 472, 473, 474, 475, 476, 477, 480, 481, 483, 484, 485, 486, 488,
490, 492, 493, 494, 495, 496, 497, 498, 504, 505, 506, 507, 508, 510,
511, 513, 515, 516, 517, 520, 522, 524, 525, 527, 528, 530, 531, 532,
533, 536, 539, 540, 546, 548, 549, 550, 551, 552, 553, 555, 558, 559,
560, 561, 564, 567, 568, 570, 572, 574, 575, 576, 580, 581, 582, 583,
584, 585, 588, 589, 590, 594, 595, 598, 603, 605, 608, 609, 610, 611,
612, 616, 618, 620, 621, 623, 624, 627, 630, 635, 636, 637, 638, 640,
642, 644, 645, 646, 648, 649, 650, 651, 654, 657, 658, 660, 663, 664,
665, 666, 667, 670, 671, 672, 675, 676, 678, 679, 680, 682, 684, 685,
688, 689, 690, 693, 696, 700, 702, 703, 704, 705, 707, 708, 710, 711,
712, 713, 714, 715, 720, 725, 726, 728, 730, 731, 735, 736, 740, 741,
742, 744, 748, 752, 754, 756, 759, 760, 762, 763, 765, 767, 768, 770,
774, 775, 776, 777, 780, 781, 782, 783, 784, 786, 790, 791, 792, 793,
798, 799, 800, 804, 805, 806, 808, 810, 812, 814, 816, 817, 819, 824,
825, 826, 828, 830, 832, 833, 836, 837, 840, 847, 848, 850, 851, 852,
854, 855, 856, 858, 860, 864, 868, 869, 870, 871, 872, 873, 874, 876,
880, 882, 884, 888, 890, 891, 893, 896, 897, 899, 900, 901, 903, 904,
909, 910, 912, 913, 915, 917, 918, 920, 923, 924, 925, 928, 930, 931,
935, 936, 938, 940, 944, 945, 946, 948, 949, 950, 952, 954, 957, 960,
962, 963, 966, 968, 969, 972, 975, 976, 979, 980, 981, 986, 987, 988,
989, 990, 992, 994, 996, 999

- [Slides][11] of a seminar by Greg Martin on Dense Egyptian Fractions presented in March 2009 containing this Egyptian fraction on pages 10 and 11.

### Egyptian fractions for 1 with even denominators

Look at the following table of denominators of Egyptian fractions for 1 which are all even, each having one more unit fraction than the previous one:

2, 4, 6, 12
2, 4, 6, 14, 84
2, 4, 6, 14, 86, 3612
2, 4, 6, 14, 86, 3614, 6526884
2, 4, 6, 14, 86, 3614, 6526886, 21300113901612
2, 4, 6, 14, 86, 3614, 6526886, 21300113901614, 226847426110843688722000884

There seems to be a pattern here:
The last denominator 1/(2D) can be replaced by two new ones, the smallest of which is 1/(2D+2) and both the old and the two new denominators are even.
A little algebra shows why:

1 | =  | 1 | +  | 1 | ..... Let's call this the Expand Even Rule |

2D | 2D + 2 | 2D(D + 1) |

The expansion preserves the evenness of the denominators.
We can continue this expansion and so show that

There is always an expansion of 1 as an Egyptian fraction with distinct even denominators of any length greater than 3.

#### You do the Maths...

Above we expanded the final even denominator. This section helps you to explote what happens if we expanded the others using the Expand Even Rule?

1. If we start from 2,2 as the denominators of our initial Egyptian fraction for 1, what does the Rule give if we expand one of the 2's?

2, 4, 4

2. What about expanding 4?

6,12

If we start with the Egyptian fraction denominators 2, 4, 4 and expanded the final 4, which Egyptian fraction for 1 do we get?

2, 4, 6, 12

3. Starting from 2, 4, 6, 12 expand the 6 to get a new Egyptian fraction for 1.

2, 4, 8, 12, 24

4. In your previous answer, expand the 8 or one of the others. Which Egyptian fractions do you get?

**2**, 4, 8, 12, 24 -> **4, 4**, 4, 8, 12, 24
2, **4**, 8, 12, 24 -> 2, **6, 12**, 12, 24
2, 4, **8**, 12, 24 -> 2, 4, **10, 40**, 12, 24
2, 4, 8, **12**, 24 -> 2, 4, 8, **14, 84**, 24
2, 4, 8, 12, **24**-> 2, 4, 8, 12, **26, 312**

### Egyptian fractions for 1 with odd denominators

When it comes to all denominators being odd, the problem is quite different! There are none of lengths 2, 3, 4, 5, 6, 7 or 8!
The first has 9 unit fractions and there are 5 of them with denominators as follows:

3, 5, 7, 9, 11, 15, 35, 45, 231
3, 5, 7, 9, 11, 15, 21, 231, 315
3, 5, 7, 9, 11, 15, 33, 45, 385
3, 5, 7, 9, 11, 15, 21, 165, 693
3, 5, 7, 9, 11, 15, 21, 135, 10395

A computer search reveals that there are none of length 10.
There do not seem to be any Egyptian fractions for 1 with an even number of odd denominators.
Earlier we encountered such a pattern when considering an Egyptian fraction fraction with solely odd denominators.
Some thought about evenness and oddness (*parity*) reveals why there never will be: Can you find a reason why the length must be odd?

The proof uses a *parity argument*that is, it uses just the oddness and evenness of numbers.
Any odd number can be written as 2n + 1 and every even number is of the form 2n
a SUM of two odd numbers is even: 2n + 1 + 2m + 1 = 2n + 2m + 2 = 2(n + m + 1)
a sum of an even number of odds is always even a PRODUCT of two odd numbers is odd: (2n + 1)(2m + 1) = 4nm + 2n + 2m + 1 = 2(2nm + n + m) + 1
a product of any number of odd numbers is always odd. Therefore an odd number can never have an even factor. Only even numbers have even factors. Consider just two unit fractions with odd denominator that sum to 1 and add them to get a single fraction as follows

1 =  | 1 | +  | 1 | =  | odd1 + odd2 |

odd1 | odd2 | odd1×odd2 |

The numerator is a sum of two odds and so is even.
The denominator is a product of 2 odds and so is odd.
So the numerator and denominator cannot be identical and the fraction cannot be 1.

The same thing happens if we have a sum of 4 unit fractions with odd denominators:
The numerator is a sum of an even number of odds and so must be even
the collected denominator is a product of odd numbers and is therefore odd.
So the fraction can never be reduced to 1 when there are an even number of unit fractions summing to 1.

**Thus an Egyptian fraction for 1 which has only odd denominators can never be of even length.**

There are Egyptian fractions for 1 with odd denominators and of odd length from 11 as shown here: length 11 3, 5, 7, 9, 15, 21, 27, 35, 63, 105, 135 length 13 3, 5, 7, 9, 15, 21, 35, 45, 63, 99, 105, 143, 195 length 15 3, 5, 7, 9, 15, 21, 35, 45, 63, 105, 135, 189, 255, 323, 399 length 17 3, 5, 7, 9, 15, 21, 35, 45, 63, 105, 135, 255, 323, 399, 483, 575, 675 length 19 3, 5, 7, 11, 15, 21, 35, 45, 63, 77, 91, 143, 209, 273, 285, 315, 399, 441, 931 length 21 3, 5, 7, 11, 15, 21, 33, 35, 55, 77, 165, 231, 255, 323, 399, 483, 575, 675, 783, 899, 1023 length 23 3, 5, 7, 11, 15, 21, 35, 45, 63, 77, 105, 165, 231, 255, 323, 399, 483, 575, 675, 783, 899, 1023, 1155 ... so it seems likely these exist for every odd length from 9 upwards.... ...and we can prove this if, as with proving that there are an infinite number of Egyptian fractions derivable from any Egyptian fraction in the section above, we can find an expansion formula for 1/odd that uses 3 odd denominators.
Try to find one yourself or else

For instance a bit of algebraic manipulation will show that:

1 | =  | 1 | +  | 1 | +  | 1 |

2n + 1 | 2n + 3 | (n + 1) (2 n + 3) – 1 | (n + 2) (2n + 1) (2 n + 3) |

If n itself is odd and only then will each of the 3 denominators on the right be odd too.

So now we know:

There will always be odd length Egyptian fraction for 1 consisting of only odd denominators for *all odd lengths from 9 onwards*.

What we still don't know is how many there are of odd length n for n from 11 onwards.
Nor indeed do we know the ones with the smallest numbers, that is, the largest denominator in the Egyptian fractions for 1 of a given (odd) length which is the smallest possible.

- **93.20 Egyptian Fraction Representations of 1 with Odd Denominators**, Peter Shiu, *The Mathematical Gazette*Vol. 93, No. 527 (2009), pages 271-276

### Egyptian fractions for 1 in various arrangements

Here is a list of the Egyptian fractions for 1 that have the smallest denominators for a given length. We allow any number as denominator but still maintain the Egyptian fraction condition that all the denominators are different:

Egyptian fractions for 1 (scroll up and down)

Length | EF Denominators |

3 | 2 3 6 |

4 | 2 4 6 12 |

5 | 2 4 10 12 15 |

6 | 3 4 6 10 12 15 |

7 | 3 4 9 10 12 15 18 |

8 | 3 5 9 10 12 15 18 20
4 5 6 9 10 15 18 20 |

9 | 4 5 8 9 10 15 18 20 24
4 6 8 9 10 12 15 18 24 |

10 | 5 6 8 9 10 12 15 18 20 24 |

11 | 5 6 8 9 10 15 18 20 21 24 28
5 7 8 9 10 14 15 18 20 24 28
6 7 8 9 10 12 14 15 18 24 28 |

12 | 4 8 9 10 12 15 18 20 21 24 28 30
6 7 8 9 10 14 15 18 20 24 28 30 |

13 | 4 8 9 11 12 18 20 21 22 24 28 30 33
4 8 10 11 12 15 20 21 22 24 28 30 33
4 9 10 11 12 15 18 20 21 22 28 30 33
5 8 9 10 11 12 18 21 22 24 28 30 33
5 8 9 10 11 15 18 20 21 22 24 28 33
6 7 8 9 11 14 18 20 22 24 28 30 33
6 7 8 10 11 14 15 20 22 24 28 30 33
6 7 9 10 11 14 15 18 20 22 28 30 33
6 8 9 10 11 12 15 18 20 22 24 30 33
6 8 9 10 11 12 15 18 21 22 24 28 33
7 8 9 10 11 12 14 15 18 22 24 28 33  |

14 | 6 8 9 10 11 15 18 20 21 22 24 28 30 33
7 8 9 10 11 14 15 18 20 22 24 28 30 33 |

15 | 6 8 9 11 14 15 18 20 21 22 24 28 30 33 35 |

16 | 6 8 11 12 14 15 18 20 21 22 24 28 30 33 35 36 |

17 | 6 10 11 12 14 15 18 20 21 22 24 28 30 33 35 36 40 |

18 | 7 10 11 12 14 15 18 20 21 22 24 28 30 33 35 36 40 42 |

So of all the Egyptian fractions for 1 with 3 fractions, the smallest has all denominators no bigger than 6.
Of those Egyptian fractions for 1 with 4 fractions, the smallest has no denominator bigger than 12. and for 5 fractions, the smallest has no denominator bigger than 15.
The series of these **smallest maximum denominators**(the **minimax**solution) in the Egyptian fractions for 1 of various lengths is given by:
6, 12, 15, 15, 18, 20, 24, 24, 28, 30, 33, 33, 35, 36, 40, 42, ... [A030659][12].

Here we list Egyptian fractions of 1 arranged by maximum denominator irrespective of length and **ordered by the sum of the denominators**:

Denominators | Max
Den |

1 | 1 |

2, 3, 6 | 6 |

2, 4, 6, 12 | 12 |

2, 3, 10, 15
2, 4, 10, 12, 15 | 15 |

2, 3, 9, 18
2, 4, 9, 12, 18 | 18 |

2, 4, 5, 20
2, 5, 6, 12, 20
3, 4, 5, 6, 20 | 20 |

2, 3, 8, 24
2, 4, 8, 12, 24 | 24 |

2, 3, 12, 21, 28
2, 4, 6, 21, 28
2, 4, 7, 14, 28 | 28 |

 |  |

Den
Sum | Denominators |

1  | 1  |

11  | 2, 3, 6 |

24  | 2, 4, 6, 12 |

30  | 2, 3, 10, 15 |

31  | 2, 4, 5, 20 |

32  | 2, 3, 9, 18 |

37  | 2, 3, 8, 24 |

38  | 3, 4, 5, 6, 20 |

43  | 2, 4, 10, 12, 15 |

45  | 2, 4, 9, 12, 18
2, 5, 6, 12, 20,  |

50  | 2, 4, 8, 12, 24
3, 4, 6, 10, 12, 15,  |

52  | 3, 4, 6, 9, 12, 18 |

 |

The series ordered by maximum denominator is
1, 6, 12, 15, 18, 20, 24, 28, 30, 33, 35, 36, 40, 42, 45, 48, ... [A092671][13]
The series of sums is 1, 11, 24, 30, 31, 32, 37, 38, 43, 45, 50, 52, 53, 54, 55, 57, 59, 60, 61, 62, 64, 65, 66, 67, 69, 71, 73, 74, 75, 76, 78, ... [A052428][14], the **strict Egyptian numbers**.
Graham showed that every integer from 78 onwards is in the list! The missing numbers up to 77 are 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 33, 34, 35, 36, 39, 40, 41, 42, 44, 46, 47, 48, 49, 51, 56, 58, 63, 68, 70, 72, 77 [A051882][15]. He uses two more "splitting" expansions one of which is :

1 =  | 1 | + ... + | 1 | =  | 1 | +  | 1 | + ... +  | 1 |

d 1 | d k | 2 | 2 d 1 | 2 d k |

and the second is the same but replacing the 1/2 by

1  | =  | 1 | +  | 1 | +  | 1 | +  | 1 |

2 | 3 | 7 | 78 | 91 |

The first splitting formula shows that there are Egyptian fractions for 1 consisting of only even denominators and how to derive one from any Egyptian fraction for 1.
The counts of the number of Egyptian fractions for 1 with sum 1,2,3,... gives the series 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, ... [A051907][16] but all values after the 77th are non-zero.
The number of solutions is small for sums up to 100 but the larger counts in that range are
6 solutions with a sum of 71,
11 solutions for sums 95 and 99 but
12 solutions for sum 92.
You can verify these counts and see the Egyptian fractions using the Calculator in the next section.

- **A theorem on partitions**R. L. Graham in *Journal of the Australian Mathematical Society*Vol 3 (1963), pages 435-441 [image: pdf link] [17]

If we want those sums that have just 1 Egyptian fraction for 1 we get the list 1, 11, 24, 30, 31, 32, 37, 38, 43, 52, 53, 54, 55, 59, 60, 61, 65, 73, 75, 80, 91 [A051909][18] but after this point there may be no more, all the other sums having at least 2 Egyptian fractions for 1 with that sum.

### Egyptian fractions for other integers and the Splitting Algorithm

There are Egyptian fractions for 2 and for 3:

Denominators of an Egyptian fraction for 2: 2, 3, 4, 5, 6, 8, 9, 10, 15, 18, 20, 24
Denominators of an Egyptian fraction for 3: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 34, 100, 11934, 14536368

Can you find an Egyptian fraction for 4? for 5?
We know this is possible because earlier in this section we saw we can find a list of unique unit fractions for 1 starting from a smallest denominator of n for any (positive) n we like.
So starting from 4=1+1+1+1, we expand the second 1 as 1/2+1/3+1/6.
4 = 1 + 1/2+1/3+1/6 +1+1
Now expand the next 1 using *a minimum denominator of 7*: for instance with denominators 7, 8, 9, 10, 12, 13, 20, 21, 30, 31, 42, 43, 44, 45, 56, 57, 58, 72, 73, 90, 156, 420, 930, 1806, 1807, 1808, 1892, 1893, 1980, 3192, 3193, 3306, 5256, 3263442, 3263443, 3267056, 3581556, 10192056 and 10650056950806.
Expand the final duplicated 1 but now with a minumum denominator of 1 more than the largest one just found (10650056950806), guaranteeing uniqueness of denominators in our expansion for 4.
This proves existence of a sum of unit fractions for any (positive) integer N but they involve huge denominators and there are much shorter expansions too.

This leads us to a new algortihm for finding Egyptian fractions for m/n, called **the Splitting Algorithm**.
It works by finding a representation of m as an Egyptian fraction that we now know always exists.
Then we multiply each denominator by n so get a sum of distinct unit fractions whose sum is m/n.

### A Calculator for finding Egyptian fractions of 1

This Calculator will count the Egyptian fractions for 1 for a given denominator sum.
"Find" will also show the Egyptian fractions.
You can limit the search by giving an 'up to' number of solutions to be found.
Generally a single solution can be found up to a sum of 1000 within a minute or so, depending on the speed of your computer. There is always at least one solution for any sum bigger than 77.

Egyptian fractions for 1 C A L C U L A T O R

 | EFs for using any even odd denominators and with sum up to  |

 | find up to solutions for each sum |

R E S U L T S

[image: less space]
[image: more space] |

 |

[image: calculator]: | Fraction &harr; Egyptian fraction | Shortest EF | Fixed Length EFs | EFs for 1 | --> productive EFs | Harmonic Numbers |

-->

#### You do the Maths...

1. Suppose we now allowed unit fractions which sum to 1 to have **repeated**unit fractions e.g.

1 = 1 / 2 + 1 / 4 + 1 / 4 = 1 / 3 + 1 / 3 + 1 / 3

There is now a total of 14 ways to write 1 as a sum of 4 unit fractions including those solutions we found above. What are they?
Check your answers with [A002966][19]
2. Fibonacci's Greedy algorithm to find Egyptian fractions with a sum of 1 is as follows:

Choose the largest unit fraction we can, write it down and subtract it
Repeat this on the remainder until we find the remainder is itself a unit fraction not equal to one already written down.
At this point we could stop or else continue splitting the unit fraction into smaller fractions.

To use this method to find a set of unit fractions that sum to 1:
So we would start with 1 / 2 as the largest unit fraction less than 1:

1 = 1 / 2 + ( 1 / 2 remaining)

so we repeat the process on the remainder: the largest fraction less than 1 / 2 is 1 / 3:

1 = 1 / 2 + 1 / 3 + ( 1 / 6 remaining).

We could stop now or else continue with 1 / 7 as the largest unit fraction less than 1 / 6...

1 = 1 / 2 + 1 / 3 + 1 / 7 + ...

Find a few more terms, choosing the largest unit fraction at each point rather than stopping.
The infinite sequence of denominators is called **Sylvester's Sequence**.
*Check your answers at [A000058][20] in Sloane's [Online Encyclopedia of Integer Sequences][21].*
3. Investigate shortest Egyptian fractions for 3 / n:

  1. Find a fraction of the form 3 / n that is not a sum of two unit fractions.
  2. Is it always possible to write 3 / n as a sum of *three*unit fractions ?
Give a formula for the different cases to verify your answer.

4. Find a value for n where 4 / n cannot be expressed as a sum of *two*unit fractions.

### The Inheritance Puzzle

This is an old puzzle mentioned in many puzzle books in various guises:

A man who had 12 horses and 3 children wrote his will to leave 1/2 of his horses to Pat, 1/3 to Chris and 1/12 to Sam.
However, just after he died one of his horses died too.
How were the children to divide the 11 remaining horses so as to fulfil the terms of the will?

The answer is that a friend calls by and offers to add his own horse to the 11 others.
Now they can split the horses with

- 1/2 = 6 horses going to Pat
- 1/3 = 4 horses going to Chris
- 1/12 = 1 horse going to Sam

a total of 11 horses exactly as specified in the will but leaving one horse over - the horse the friend brought. The friend could leave taking his horse with him and the children too go home happy.
***What happened here? ***
The answer lies in the peculiar conditions of the will since 1/2 + 1/3 + 1/12 = 11/12 and not 12/12!
It works because the denominators 2, 3 and 12 are all factors of 12.

Here is another variation on the same inheritance puzzle:

A cactus collector had 11 rare cactii and in her will she left 1/2 of the collection to one other collector, 1/4 to another collector and 1/6 to a third. When she died how could the plants be divided as specified without splitting any?

The same solution applies, with the loan of one extra plant which is then returned on successful division of the 12 and the collectors receive 12/2 = 6, 12/4 = 3 and 12/6 = 2 and of course 6 + 3 + 2 = 11.

This kind of problem is designed from solutions to Egyptian fractions for 1 where the denominators are all factors of their sum plus 1.
For instance in the cactii puzzle 11 = 6 + 3 + 2 and 6, 3, 2 are all factors of 11 + 1 = 12.
If we can divide these factors into 12 and also include 1/12 then we have an Egyptian fraction for 1 as follows:
1 = 12/12 = 12/6 + 12/3 + 12/2 + 1/12 = 1/2 + 1/4 + 1/6 + 1/12 but note that not all Egyptian fractions for 1 have this form:
24, 8, 3, 2 are all divisors of 24 and dividing each into 24 gives 1/24 + 1/8 + 1/3 + 1/2 = 1 but 8 + 3 + 2 is only 13.

***Numbers that are the sum of a subset of their divisors***are called **pseudo perfect numbers**, named by Sierpinski in 1965.
For example, the smaller ones are:

n | Divisors
with sum n | Divisors/n |

6 | 1, 2, 3 | 1/6 + 2/6 + 3/6 = 1 |

12 | 2, 4, 6 | 2/12 + 4/12 + 6/12 = 1 |

12 | 1, 2, 3, 6 | 1/12 + 2/12 + 3/12 + 6/12 = 1 |

18 | 3, 6, 9 | 3/12 + 6/18 + 9/18 = 1 |

18 | 1, 2, 6, 9 | 1/18 + 2/18 + 6/18 + 9/18 = 1 |

20 | 1, 4, 5, 10 | 1/20 + 4/20 + 5/20 + 10/20 = 1 |

The list of pseudo perfect (or semiperfect) numbers starts:
6, 12, 18, 20, 24, 28, 30, 36, 40, 42, 48, 54, 56, 60, 66,... [A005835][22]
If n = a + b + ... + c is in the list where the right hand side consists only of divisors of n then 2n = 2a + 2b + ... + 2c and 3n = 3a + 3b + ... + 3c and so on must also be in the list.
The pseudo perfect numbers that are not a multiple of another pseudo perfect number are called **primitive pseudo perfect numbers**:
6, 20, 28, 88, 104, 272, 304, 350, 368, 464, 490, 496, ... [A006036][23]

#### You do the Maths...

1. There are a total of 7 possible puzzles like the horses and the cactus collection above if there are 3 inheritors.
What are they?

number
to share | Proportions | Shares with
1 loaned |

7 | 1/2, 1/4, 1/8 | 4, 2, 1 |

11 | 1/2, 1/3, 1/12 | 6, 4, 1 |

11 | 1/2, 1/4, 1/6 | 6, 3, 2 |

17 | 1/2, 1/3, 1/9 | 9, 6, 2 |

19 | 1/2, 1/4, 1/5 | 10, 5, 4 |

23 | 1/2, 1/3, 1/8 | 12 ,8, 3 |

41 | 1/2, 1/3, 1/7 | 21, 14, 6 |

2. Suppose there are 23 horses and any number of inheritors. What combination of fractions gives a similar puzzle now?

3 kids 1/8, 1/3, 1/2
4 kids 1/24, 1/12, 1/3, 1/2 or
4 kids 1/24, 1/6, 1/4, 1/2 or
4 kids 1/12, 1/8, 1/4, 1/2
5 kids 1/12, 1/8, 1/6, 1/4, 1/3

3. One collector of rare pottery had 8 people to share the collection between. But one pot got broken.
What size of collection and what proportions give a similar puzzle?

60 pots, one broken, divided in proportions 1/60, 1/30, 1/20, 1/12, 1/10, 1/6, 1/5 and 1/3.

4. 60 has 34 subsets of its divisors that sum to 60. It is pseudoperfect in 34 different ways.

  1. What are the divisors of 60? 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60
  2. Which subsets of divisors sum to 60? For example, the smallest subset is {10,20,30}.

Length 3: 10, 20, 30 Length 4: 3, 12, 15, 30
4, 6, 20, 30
5, 10, 15, 30
1, 2, 12, 15, 30
1, 3, 6, 20, 30
1, 4, 5, 20, 30 Length 5: 1, 4, 10, 15, 30
2, 3, 5, 20, 30
2, 3, 10, 15, 30
2, 6, 10, 12, 30
3, 5, 10, 12, 30
3, 10, 12, 15, 20
4, 5, 6, 15, 30 Length 6: 1, 2, 3, 4, 20, 30
1, 2, 5, 10, 12, 30
1, 2, 10, 12, 15, 20
1, 3, 4, 10, 12, 30
1, 3, 5, 6, 15, 30
2, 3, 4, 6, 15, 30
2, 5, 6, 12, 15, 20
3, 4, 5, 6, 12, 30
3, 4, 6, 12, 15, 20
4, 5, 6, 10, 15, 20 Length 7: 1, 2, 3, 4, 5, 15, 30
1, 2, 4, 5, 6, 12, 30
1, 2, 4, 6, 12, 15, 20
1, 3, 4, 5, 12, 15, 20
1, 3, 5, 6, 10, 15, 20
2, 3, 4, 5, 6, 10, 30
2, 3, 4, 6, 10, 15, 20
3, 4, 5, 6, 10, 12, 20 Length 8: 1, 2, 3, 4, 5, 10, 15, 20
1, 2, 4, 5, 6, 10, 12, 20

  3. In how many ways is 120 pseudoperfect? 278 subsets of its divisors sum to 120.

5. By contrast, 20 and 28 are pseudoperfect in only one way. What are those subsets?

The divisors of 20 are 1, 2, 4, 5, 10, 20
Its unique subset totalling 20 is 1, 4, 5, 10
The divisors of 28 are 1, 2, 4, 7, 14, 28

6. What is special about the pseudoperfect numbers 6 and 28?

Both are pseudoperfect in only one way but for both these numbers the subset of divisors includes every divisor except the number itself.
Such numbers are called **Perfect numbers**. The list of these is sparse and grows rapidly. It begins:
6, 28, 496, 8128, 33550336, ... [A000396][24]
All in this list are even and no one knows if there is an *odd*perfect number.

- [536 Puzzles and Curious Problems][25] H E Dudeney (1970 paperback edition of the original of 1967)
Puzzle 172 deals with the first Inheritor problem in this section and expands on it. The puzzles in this book are quite unique, amusing and very comprehensive. A large proportion of the book is given over to solutions and the maths behind them. A real treasure.

## Two more unsolved problems

Here are two problems about numbers which can be written using just 3 different unit fractions.

### Egyptian fractions for 4/n and the Erd&ouml;s-Straus Conjecture

Every fraction of the form 3/n where n is not a multiple of 3 *and odd*can be written as 1/a + 1/b + 1/c for distinct *odd*a, b and c. For a proof see

- **A Proof of a Conjecture on Egyptian Fractions**T. R. Hagedorn *The American Mathematical Monthly*, Vol. 107, (2000), pages 62-63

What about 3/n when n is even?
Can 4/n and 5/n be written as as a sum of just three unit fractions also?

Although many fractions of the form 4/n can be written as a sum of just two unit fractions, others, such as 4/5 and 4/13 need three or more.

In 1948, the famous mathematician [Paul Erd&ouml;s][26] (1913-1996) together with [E. G. Straus][27] suggested the following:

The [Erd&ouml;s-Straus Conjecture][28]:
*Every*fraction 4 / n can be written as a sum of three unit fractions.

They have no restriction on the three unit fractions being unique, so for this problem, repetitions of unit fractions are allowed. It has been verified that 3 unit fractions **can**found for all values of n up to 51,000,000-th prime 1003162753 but as yet no one has *proved*it true *for all values of n*nor has anyone found a number n for which it is *not*true. And what if we insisted that the three fractions be distinct?
The Calculator above shows that for any given n there are many ways to choose the whole numbers, x, y and z for the three unit fraction denominators.
Using the calculator above, can you **find patterns for some values of n, x, y and z**?

For instance: among all the result of three fractions summing to 4 / n when n is *even*, we have:  |

n | x | y | z |

6 | 3 | 4 | 12 |

8 | 4 | 5 | 20 |

10 | 5 | 6 | 30 |

12 | 6 | 7 | 42 |

... |

 |

How would you write this pattern mathematically?

4 | = | 2 | = | 1 | + | 1 | + | 1 |

2n | n | n | n + 1 | n(n + 1) |

Here is a list of all the 3-term Egyptian fractions for 4 / n for n from 5 to 15.

4/5= | 1/2 + 1/4 + 1/20
1/2 + 1/5 + 1/10
 |

4/6=
2/3 | 1/2 + 1/7 + 1/42
1/2 + 1/8 + 1/24
1/2 + 1/9 + 1/18
1/2 + 1/10 + 1/15
1/3 + 1/4 + 1/12
 |

4/7= | 1/2 + 1/15 + 1/210
1/2 + 1/16 + 1/112
1/2 + 1/18 + 1/63
1/2 + 1/21 + 1/42
1/3 + 1/6 + 1/14
 |

4/8=
1/2 | 1/3 + 1/7 + 1/42
1/3 + 1/8 + 1/24
1/3 + 1/9 + 1/18
1/3 + 1/10 + 1/15
1/4 + 1/5 + 1/20
1/4 + 1/6 + 1/12
 |

4/9= | 1/3 + 1/10 + 1/90
1/3 + 1/12 + 1/36
1/4 + 1/6 + 1/36
1/4 + 1/9 + 1/12
 |

 |

4/10=
2/5 | 1/3 + 1/16 + 1/240
1/3 + 1/18 + 1/90
1/3 + 1/20 + 1/60
1/3 + 1/24 + 1/40
1/4 + 1/7 + 1/140
1/4 + 1/8 + 1/40
1/4 + 1/10 + 1/20
1/4 + 1/12 + 1/15
1/5 + 1/6 + 1/30
 |

4/11= | 1/3 + 1/34 + 1/1122
1/3 + 1/36 + 1/396
1/3 + 1/42 + 1/154
1/3 + 1/44 + 1/132
1/4 + 1/9 + 1/396
1/4 + 1/11 + 1/44
1/4 + 1/12 + 1/33
 |

4/12=
1/3 | 1/4 + 1/13 + 1/156
1/4 + 1/14 + 1/84
1/4 + 1/15 + 1/60
1/4 + 1/16 + 1/48
1/4 + 1/18 + 1/36
1/4 + 1/20 + 1/30
1/4 + 1/21 + 1/28
1/5 + 1/8 + 1/120
1/5 + 1/9 + 1/45
1/5 + 1/10 + 1/30
1/5 + 1/12 + 1/20
1/6 + 1/7 + 1/42
1/6 + 1/8 + 1/24
1/6 + 1/9 + 1/18
1/6 + 1/10 + 1/15
 |

 |

4/13= | 1/4 + 1/18 + 1/468
1/4 + 1/20 + 1/130
1/4 + 1/26 + 1/52
1/5 + 1/10 + 1/130
 |

4/14=
2/7 | 1/4 + 1/29 + 1/812
1/4 + 1/30 + 1/420
1/4 + 1/32 + 1/224
1/4 + 1/35 + 1/140
1/4 + 1/36 + 1/126
1/4 + 1/42 + 1/84
1/4 + 1/44 + 1/77
1/5 + 1/12 + 1/420
1/5 + 1/14 + 1/70
1/5 + 1/20 + 1/28
1/6 + 1/9 + 1/126
1/6 + 1/12 + 1/28
1/6 + 1/14 + 1/21
1/7 + 1/8 + 1/56
 |

 |

4/15= | 1/4 + 1/61 + 1/3660
1/4 + 1/62 + 1/1860
1/4 + 1/63 + 1/1260
1/4 + 1/64 + 1/960
1/4 + 1/65 + 1/780
1/4 + 1/66 + 1/660
1/4 + 1/68 + 1/510
1/4 + 1/69 + 1/460
1/4 + 1/70 + 1/420
1/4 + 1/72 + 1/360
1/4 + 1/75 + 1/300
1/4 + 1/76 + 1/285
1/4 + 1/78 + 1/260
1/4 + 1/80 + 1/240
1/4 + 1/84 + 1/210
1/4 + 1/85 + 1/204
1/4 + 1/90 + 1/180
1/4 + 1/96 + 1/160
1/4 + 1/100 + 1/150
1/4 + 1/105 + 1/140
1/4 + 1/108 + 1/135
1/4 + 1/110 + 1/132
1/5 + 1/16 + 1/240
1/5 + 1/18 + 1/90
1/5 + 1/20 + 1/60
1/5 + 1/24 + 1/40
1/6 + 1/11 + 1/110
1/6 + 1/12 + 1/60
1/6 + 1/14 + 1/35
1/6 + 1/15 + 1/30
1/7 + 1/10 + 1/42
1/8 + 1/10 + 1/24
1/9 + 1/10 + 1/18  |

 |

Can you spot any further patterns here?
Use the Calculator above to help with your investigations.

If you do find any more, let me know (see contact details at the foot of this page) and I will put your results here.
If we can find a set of cases that cover *all values of n*, then we have a proof of the **Erd&ouml;s-Straus conjecture**.

Here are some simple cases for 4/n that we can easily see have 3 unit fractions since the 3 fractions need not have different denominators:

- Here is a simple formula for *even denominators*because:

4 | =  | 2 | =  | 1 | +  | 1 | +  | 1 |

2n | n | n | 2n | 2n |

This formula duplicates a fraction. Gary Detlef's version has the advantage that all the fractions are different:

4 | =  | 2 | =  | 1 | +  | 1 | +  | 1 |

2n | n | n | n + 1 | n( n + 1) |

- Here are some of Mordell's cases that take care of many values of n:

4 | =  | 1 | +  | 1 | +  | 1 |

3n | 3n | 2n | 2n |

4 | =  | 1 | +  | 1 | +  | 1 |

4n−1 | 2n | 2n | n(4n−1) |

4 | =  | 1 | +  | 1 | +  | 1 |

4n−2 | n | n(4n−2) | n(4n−2) |

4 | =  | 1 | +  | 1 | +  | 1 |

8n−3 | 2n | n(2n−3) | n(2n−3) |

- What about multiples of 3?

  -

4 | =  | 1 | +  | 1 | +  | 1 |

3n−1 | n | 3n−1 | n(3n−1) |

  -

4 | =  | 1 | +  | 1 | +  | 1 | =  | 1 | +  | 1 | +  | 1 |

3n | 2n | 2n | 3n | n | 4n | 12n |

So we only need investigate fractions of the form 4 / 3n+1
- Furthermore, if we have a solution for 4 / n then we automatically have solutions for 4 / n k for all k by multiplying each of the original denominators by k. For example:

4 | =  | 1 | +  | 1 | +  | 1 |

5 | 2 | 4 | 20 |

If we divide both sides by n and we have a simple formula for three unit fractions for 4/(5n):

4 | =  | 1 | +  | 1 | +  | 1 |

5n | 2n | 4n | 20n |

This means that we need only examine *prime*denominators.

Continuing in this way, we can eliminate many forms of denominator from the list of those needing verification - but no one has managed to find a proof for all n yet!

In Mordell's **Diophantine Equations**published by Academic Press in 1969, he showed that we can reduce the unknown (unproven) cases to just those *prime*denominators n which have a remainder of 1, 11 2, 13 2, 17 2, 19 2 or 23 2 when divided by 840 (see [A139665][29]).
If you want to check the cases Mordell says are solved, these two equations from Ben Thurston (October 2016) will help fill in some of the more awkward cases:

4 | =  | 1 | +  | 1 | +  | 1 |

12n + 7 | 3(n + 1) | 3(n + 1)(3n + 2) | (12n + 7)(3n + 2) |

4 | =  | 1 | +  | 1 | +  | 1 |

24n + 13 | 2(3n + 2) | 2(n + 1)(24n + 13) | 2(n + 1)(24n + 13)(3n + 2) |

- **Diophantine Equations**Louis J Mordell, Academic Press (1967), pp. 287-290.

#### You do the Maths...

1. The number of solutions to 4 / n as a sum of 3 unit fractions is:

The first value is 4 / 3:
1 solution for 4 / 3 = 1 / 1 + 1 / 4 + 1 / 12
1 solution for 4 / 4 = 1 / 2 + 1 / 3 + 1 / 6
2 ways for 4 / 5
5 ways for 4 / 6 = 2 / 3
...

The series of counts is (0,0), 1, 1, 2, 5, ...
How does it continue?
*Check your answers with [A073101][30] in Neil Sloane's [Online Encyclopedia of Integer Sequences][31]. *
**If**the Erd&ouml;s-Straus Conjecture is true then the only zeroes in the whole infinite series are for n=1 and 2.

With thanks to Robert David Acker, Jr. for suggesting this topic.

### 5/n = 1/x + 1/y + 1/z?

Another famous mathematician, [Sierpinski][32] suggested in 1956 that the same applied to all fractions of the form 5 / n, that is that each of these also can be expressed as a sum of 3 unit fractions.

Let's check some smaller values of n: there are:
0 solutions for 5 / 2
1 solution for 5 / 3: 5 / 3 = 1 / 1 + 1 / 2 + 1 / 6
2 for 5 / 4: 5 / 4 = 1 / 1 + 1 / 5 + 1 / 20 and 1 / 1 + 1 / 6 + 1 / 12;
1 for 5 / 5; what is it?
The number of solutions this time is the series 0,1,2,1,1,3,5,9,6,3,12,... which is [A075248][33] in Neil Sloane's [Online Encyclopedia of Integer Sequences][31]. If the conjecture is true, then there are no zeroes in this series apart from the starting value for n=2. It has been verified for all n up to 922321,

- **Sur les d&eacute;compositiones de nombres rationelles en fractions primaries**W Sierpinski, *Mathesis*65 (1956), pages 16-32

#### You do the Maths...

1.

  1. Find the single set of 3 unit fractions with a sum of 5 / 6.
  2. Find the three sets of 3 for 5 / 7.
  3. What formulae can you find for special cases of 5 / n as a sum of 3 unit fractions?

2. From the table of lengths of the shortest Egyptian fractions above, find a fraction that needs 5 unit fractions for its Egyptian fraction.
3. Can you find a fraction that cannot be written using less than 6 unit fractions for its Egyptian fraction?
4. Investigate Egyptian fractions which have only *odd*denominators.
Is it possible to find a sum of odd Egyptian fractions for *every*fraction a / b?

The above will give you some ideas for your own experiments and the References below point to more information and ideas.
Happy calculating!

## Smallest Denominators

Apart from the shortest Egyptian fractions (those with the fewest unit fractions), we can also look for the *smallest*numbers in the denominators.
As we saw at the start of the **Fixed Length Egyptian Fractions**section above, the smallest denominators do not always appear in the *shortest*Egyptian fractions.

- The *shortest*for 8/11 is
8/11 = 1/2 + 1/6 + 1/22 + 1/66
and 15 others, but this one has the fewest numbers with just 4 unit fractions but it includes a denominator of 66;
- The Egyptian fraction for 8/11 with *smallest numbers*has no denominator larger than 44 and there are two such Egyptian fractions both containing 5 unit fractions (out of the 667 of length 5):
8/11 = 1/2 + 1/11 + 1/12 + 1/33 + 1/44 and
8/11 = 1/3 + 1/4 + 1/11 + 1/33 + 1/44

## The 2/n table of the Rhind Papyrus

Here is the Table at the start of the Rhind mathematical papyrus. It is a table of unit fractions for 2 / n for the odd values of n from 3 to 101.
Sometimes the shortest Egyptian fraction is ignored in the table in favour of a longer decomposition. Only one sum of unit fractions is given when several are possible. The scribe tends to favour unit fractions with even denominators, since this makes their use in multiplication and division easier. The Egyptian multiplication method was based on doubling and adding, in exactly the same way that a binary computer uses today, so it is easy to double when the unit fractions are even.
Also, he prefers to use smaller numbers. Their method of writing numerals was decimal more like the Roman numerals than our decimal place system though. He seems to reject any form that would need a numeral bigger than 999. All the shortest forms and alternative shortest forms are given here in an extra column.

2 | =  | 1 | +  | 1 | +  | 1 | +  | 1 |

 |  |  |  |  |

n | a | b | c | d |

n | a | b | c | d | shortest? |

5 | 3 | 15 |  |  | &radic; |  |

7 | 4 | 28 |  |  | &radic; |  |

9 | 6 | 18 |  |  | &radic; | 5 45 |

11 | 6 | 66 |  |  | &radic; |  |

13 | 8 | 52 | 104 |  | × | 7 91 |

15 | 10 | 30 |  |  | &radic; | 8 120
9 45
12 20 |

17 | 12 | 51 | 68 |  | × | 9 153 |

19 | 12 | 76 | 114 |  | × | 10 190 |

21 | 14 | 42 |  |  | &radic; | 11 231
12 84
15 35 |

23 | 12 | 276 |  |  | &radic; |  |

25 | 15 | 75 |  |  | &radic; | 13 325 |

27 | 18 | 54 |  |  | &radic; | 15 135
24 378 |

29 | 24 | 58 | 174 | 232 | × | 15 435 |

31 | 20 | 124 | 155 |  | × | 16 496 |

33 | 22 | 66 |  |  | &radic; | 21 77
18 198
17 561 |

35 | 30 | 42 |  |  | &radic; | 21 105
20 140
18 630 |

37 | 24 | 111 | 296 |  | × | 19 703 |

39 | 26 | 78 |  |  | &radic; | 24 104
21 273
20 780 |

41 | 24 | 246 | 328 |  | × | 21 861 |

43 | 42 | 86 | 129 | 301 | × | 22 946 |

45 | 30 | 90 |  |  | &radic; | 36 60
35 63
27 135
25 225
24 360
23 1035 |

 |

n | a | b | c | d | shortest? |

47 | 30 | 141 | 470 |  | &radic; | 24 1128 |

49 | 28 | 196 |  |  | &radic; | 25 1225 |

51 | 34 | 102 |  |  | &radic; | 30 170
27 459
26 1326 |

53 | 30 | 318 | 795 |  | × | 27 1431 |

55 | 30 | 330 |  |  | &radic; | 40 88
33 165
28 1540 |

57 | 38 | 114 |  |  | &radic; | 33 209
30 570
29 1653 |

59 | 36 | 236 | 531 |  | × | 30 1770 |

61 | 40 | 244 | 488 | 610 | × | 31 1891 |

63 | 42 | 126 |  |  | &radic; | 56 72
45 105
36 252
35 315
33 693
32 2016 |

65 | 39 | 195 |  |  | &radic; | 45 117
35 455
33 2145 |

67 | 40 | 335 | 536 |  | × | 34 2278 |

69 | 46 | 138 |  |  | &radic; | 39 299
36 828
35 2415 |

71 | 40 | 568 | 710 |  | × | 36 2556 |

73 | 60 | 219 | 292 | 365 | × | 37 2701 |

75 | 50 | 150 |  |  | &radic; | 60 100
45 225
42 350
40 600
39 975
38 2850 |

 |

n | a | b | c | d | shortest? |

77 | 44 | 308 |  |  | &radic; | 63 99
42 462
39 3003 |

79 | 60 | 237 | 316 | 790 | × | 40 3160 |

81 | 54 | 162 |  |  | &radic; | 45 405
42 1134
41 3321 |

83 | 60 | 332 | 415 | 498 | × | 42 3486
also
166 249 498 |

85 | 51 | 255 |  |  | &radic; | 55 187
45 765
43 3655 |

87 | 58 | 174 |  |  | &radic; | 48 464
45 1305
44 3828 |

89 | 60 | 356 | 534 | 890 | × | 45 4005
184 of length 3 |

91 | 70 | 130 |  |  | &radic; | 52 364
49 637
46 4186 |

93 | 62 | 186 |  |  | &radic; | 51 527
48 1488
47 4371 |

95 | 60 | 380 | 570 |  | × | 60 228&nbsp
57 285
50 950
48 4560 |

97 | 56 | 679 | 776 |  | × | 49 4753 |

99 | 66 | 198 |  |  | &radic; | 90 110
63 231
55 495
54 594
51 1683
50 4950 |

101 | 101 | 202 | 303 | 606 | × | 51 5151 |

 |

All those with n a multiple of 3 follow the same pattern:

2 / 3n = 1 / 2n + 1 / 6n

But there are still some mysteries here.
For instance why choose

2 / 95 = 1 / 60 + 1 / 380 + 1 / 570

instead of the much simpler

2 / 95 = 1 / 60 + 1 / 228?

Why stop at 103? There is a sum for 2 / 103 with two unit fractions but it contains a four digit number:

2 / 103 = 1 / 52 + 1 / 5356

and all of the other 65 of length 3 contain a denominator of at most 1236.
The one with this least maximum denominator is: 2 / 103 = 1 / 60 + 1 / 515 + 1 / 1236
There are only two of length 4 that don't use four digit numbers:

2 / 103 = 1 / 103 + 1 / 206 + 1 / 309 + 1 / 618
2 / 103 = 1 / 72 + 1 / 309 + 1 / 824 + 1 / 927.

The Calculator above may help with your investigations.

### You do the Maths...

1. Is there a pattern common to all the 2 / 5n forms in the papyrus table?
2. Is there a pattern common to all the 2 / 7n forms in the papyrus table?
3. Which fractions in the table could be found by the Fibonacci method?

## Productive Egyptian Fractions

Some fractions have a special form of Egyptian fraction where each denominator is a factor of the next. For example:

4 | =  | 1 | +  | 1 | +  | 1 |

5 | 2 | 2×2 | 2×2×5 |

In fact, such representations are useful for a system of measurements such as the pounds-shillings-pence (&pound; s d) monetary system or the stones-pounds-ounces system of weights.
There were 12 pence (denoted d) in every shilling (s), 20 shillings in every pound (&pound;) so &pound;2 3s 11d could be represented as &pound; 2 + 3/20 + 11/(20×12).
Similarly there are 16 ounces in 1 pound weight and 14 pounds in one stone. 2 stone 9 pounds and 3 ounces is therefore 2 + 9/14 + 3/(14×16) ounces.

In the Rhind Table above 26 of the 49 Egyptian fractions have this format for 2/n, that is all but two of those with two unit fractions. The two exceptions are

2 / 35 = 1 / 30 + 1 / 42
2 / 91 = 1 / 70 + 1 / 130

These are covered by the equation

2 | =  | 1 | +  | 1 | where v =  | a+b | and a+b is even |

a b | a v | b v | 2 |

which applies to a total of 8 two-unit fractions in the Rhind table. [34]

### Every fraction has a Egyptian fraction as accumulated Products

Cohen only focuses on a "greedy" method of generating them and restricts his attention to those where *each new factor is never smaller than the one before it*when we order the denominators in increasing size. With this restriction, he proves a productive Egyptian fraction always exists and that it is unique.

3 | =  | 1 | +  | 1 | =  | 1 | +  | 1 |

8 | 3 | 3×8 | 4 | 4×2 |

 | factors 3,8
increasing |  | factors 4,2
decreasing |

Cohen called these *Egyptian fraction expansions*but earlier (1923) Gibbs had called them *Productive Fractions*. We will call them **ordered productive Egyptian fractions**if the each new factor is no smaller than the previous one (as in Cohen's paper) and and **productive Egyptian fractions**if there is no restriction on the size of the next new factor.

A good shorthand is to **list the new factors**of a productive Egyptian fraction, for example

13/20 = 1/2 + 1/8 + 1/40 = 1/**2**+ 1/(2×**4**) + 1/(2×4×**5**) has the successive factors **2, 4, 5**
7/8 = 1/2 + 1/4 + 1/8 = 1/**2**+ 1/(2×**2**) + 1/(2×2×**2**) has the successive factors **2, 2, 2**
= 1/2 + 1/4 + 1/12 + 1/24 = 1/**2**+ 1/(2×**2**) + 1/(2×2×**3**) + 1/(2×2×3×**2**) with successive factors: **2, 2, 3, 2**

### A Productive Egyptian Fraction Calculator

If the numbers get too large, the rest of the unit fractions' denominators are indicated by "...".

Productive EF C A L C U L A T O R

 | for |
 |

 | all productive Egyptian fractions of length  |

with successive factors =1)"> |

R E S U L T S

[image: less space]
[image: more space] |

 |

[image: calculator]: | Fraction &harr; EF | Shortest EF | Fixed Length EFs | EFs for 1 | --> Productive EFs | Harmonic Numbers |

### You Do The Maths...

1. Which fractions have *successive prime*factors starting from 2?

  1. 2,3;
  2. 2,3,5;
  3. 2,3,5,7;
  4. ...

The product of the first n prime numbers is the n-th *primorial number*: 2, 2×3=6, 2×3×5=30, ... [A002110][35].
Check your answers with [A064646][36] and [A064647][37]
2.

  1. Which productive fractions have only 2s as their products? for example:
7/8 is 1/2 + 1/(2×2) + 1/(2×2×2)
  2. Find a formula for the numerators and for the denominators of these fractions

3. Repeat the previous question for productive fractions whose factor is 3 each time.
4. Find the fractions whose successive factors are

  1. 2, 3
  2. 2, 3, 4
  3. 2, 3, 4, 5
  4. 2, 3, 4, 5, 6
  5. 2, 3, ..., n

How are these fractions related to the *factorial numbers*n! = 1×2×3×...×n? [A000142][38]
5. Find the fractions with these successive factors:

  1. 3, 2
  2. 4, 3, 2
  3. 5, 4, 3, 2

6. What happens to the unit fractions if the productive fraction has 1 as a successive factor?

- **Egyptian Fraction Expansions**, Robert Cohen *Mathematics Magazine*Vol. 46, No. 2 (Mar., 1973), pages 76-80
- **649. Productive Fractions**R W M Gibbs, *Math. Gaz.*(1923) pages 233-234
He also deals with recurring sets of new factors and subtracting unit fractions as well as adding them

### Lengths of shortest Productive Egyptian fractions

Every unit fraction has a productive Egyptian Fraction :

1 / 2 | = 1 / 3 | + 1 / 6 |

1 / 3 | = 1 / 4 | + 1 / 12 |

1 / 4 | = 1 / 5 | + 1 / 20 |

1 / 5 | = 1 / 6 | + 1 / 30 |

1 / 6 | = 1 / 7 | + 1 / 42 |

1 / 7 | = 1 / 8 | + 1 / 56 |

which is summarised by the algebraic identity

1 | = | 1 | + | 1 | **Productive expansion equation**

n | n + 1 | n ( n + 1) |

A similar identity holds for all fractions 2/odd:

2 | = | 1 | + | 1 |

2n + 1 | n + 1 | (n + 1) ( 2n + 1) |

Here is a table of the lengths of the shortest productive Egyptian fractions for fractions less and one and with a denominator up to 30, similar to the one above for all Egyptian fractions. This table includes all fractions whether in their lowest form or not:

**Length of the Shortest Productive Egyptian fraction for Fraction T / B**

KEY: | .  | means the fraction t / b is not less than 1.  |

12 | is the *minimum*number of unit fractions that are needed to sum to t / b. |

Find T (top or numerator) down the side and B (bottom or denominator) across the top.

```
\B:                 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3T\  2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1| 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2| . 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3| . . 2 2 2 3 2 2 2 2 2 3 2 2 2 2 2 3 2 2 2 2 2 2 2 2 2 2 2 4| . . . 3 2 2 2 2 2 2 2 3 2 2 2 3 2 2 2 2 2 2 2 3 2 2 2 3 2 5| . . . . 3 4 2 2 2 3 2 3 2 2 2 3 2 2 2 3 3 3 2 2 3 2 2 2 2 6| . . . . . 5 2 2 2 2 2 4 3 2 2 2 2 3 2 2 2 2 2 2 3 2 2 2 2 7| . . . . . . 3 3 3 3 2 2 2 3 3 4 2 3 2 2 3 3 2 3 2 2 2 3 2 8| . . . . . . . 4 3 4 2 4 2 2 2 5 2 3 2 2 2 2 2 3 3 3 2 3 2 9| . . . . . . . . 4 4 2 4 3 2 2 2 2 4 3 3 4 3 2 3 2 2 3 4 210| . . . . . . . . . 5 3 3 4 2 2 3 2 2 2 4 3 4 2 2 3 2 2 2 211| . . . . . . . . . . 4 5 3 4 3 4 3 4 2 2 2 5 3 4 3 3 3 3 212| . . . . . . . . . . . 6 5 3 2 5 2 3 2 2 2 2 2 5 4 2 3 4 213| . . . . . . . . . . . . 6 5 3 3 3 4 3 4 3 3 2 2 2 3 4 3 314| . . . . . . . . . . . . . 6 3 5 3 5 3 2 3 4 2 3 2 2 2 4 315| . . . . . . . . . . . . . . 4 4 3 5 2 4 3 4 2 2 3 2 2 2 216| . . . . . . . . . . . . . . . 5 4 5 3 3 4 4 2 4 4 3 2 3 217| . . . . . . . . . . . . . . . . 5 6 4 5 3 6 3 4 4 3 3 3 318| . . . . . . . . . . . . . . . . . 7 4 5 4 4 2 5 4 2 3 4 219| . . . . . . . . . . . . . . . . . . 5 6 5 5 3 3 5 4 3 5 320| . . . . . . . . . . . . . . . . . . . 7 5 7 3 3 3 4 4 4 221| . . . . . . . . . . . . . . . . . . . . 6 6 3 5 5 3 2 4 322| . . . . . . . . . . . . . . . . . . . . . 7 4 4 5 4 3 3 423| . . . . . . . . . . . . . . . . . . . . . . 5 6 4 5 4 4 324| . . . . . . . . . . . . . . . . . . . . . . . 7 6 4 5 6 325| . . . . . . . . . . . . . . . . . . . . . . . . 7 6 4 5 326| . . . . . . . . . . . . . . . . . . . . . . . . . 7 6 5 527| . . . . . . . . . . . . . . . . . . . . . . . . . . 7 6 428| . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 629| . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
```

 |

Here is the table of the same fractions but this time counting the number of productive Egyptian fractions there are of the shortest length:

Number of Shortest Productive Egyptian fractions for Fraction T / B

```
\B:                  1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3T\   2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 | 1 1 2 1 3 1 3 2 3 1 5 1 3 3 4 1 5 1 5 3 3 1 7 2 3 3 5 1 7 2 | . 1 1 1 1 1 2 2 1 1 3 1 1 3 3 1 2 1 3 3 1 1 5 2 1 3 3 1 3 3 | . . 1 1 1 1 2 1 2 1 2 1 2 1 2 1 3 2 3 1 2 1 3 1 2 2 2 1 3 4 | . . . 1 1 1 1 1 1 1 1 1 1 2 2 1 2 1 1 2 1 1 3 2 1 2 1 2 3 5 | . . . . 1 1 1 1 1 1 1 2 1 1 1 1 1 1 2 3 3 2 2 1 3 1 2 1 3 6 | . . . . . 1 1 1 1 1 1 2 1 1 2 1 1 1 2 1 1 1 2 1 1 2 2 1 1 7 | . . . . . . 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 2 1 1 2 1 1 8 | . . . . . . . 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 2 9 | . . . . . . . . 1 1 1 2 1 1 1 1 1 1 1 1 4 1 2 2 1 1 1 2 210 | . . . . . . . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 111 | . . . . . . . . . . 1 2 1 1 2 1 2 2 1 1 1 1 2 2 1 2 3 1 112 | . . . . . . . . . . . 2 1 1 1 1 1 1 1 1 1 1 1 2 2 1 1 1 113 | . . . . . . . . . . . . 1 1 1 1 1 1 2 3 1 1 1 1 1 1 3 1 214 | . . . . . . . . . . . . . 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 115 | . . . . . . . . . . . . . . 1 1 1 2 1 1 1 1 1 1 1 1 1 1 116 | . . . . . . . . . . . . . . . 1 1 1 1 1 1 1 1 2 1 1 1 1 117 | . . . . . . . . . . . . . . . . 1 2 1 3 1 1 1 2 1 1 2 1 318 | . . . . . . . . . . . . . . . . . 2 1 1 1 1 1 2 2 1 1 1 119 | . . . . . . . . . . . . . . . . . . 1 3 1 1 1 1 2 2 1 2 220 | . . . . . . . . . . . . . . . . . . . 3 1 1 1 1 1 1 1 1 121 | . . . . . . . . . . . . . . . . . . . . 1 1 1 2 1 1 1 1 122 | . . . . . . . . . . . . . . . . . . . . . 1 1 1 2 1 1 1 123 | . . . . . . . . . . . . . . . . . . . . . . 1 2 1 2 1 1 124 | . . . . . . . . . . . . . . . . . . . . . . . 2 2 1 1 2 125 | . . . . . . . . . . . . . . . . . . . . . . . . 2 2 1 1 126 | . . . . . . . . . . . . . . . . . . . . . . . . . 2 1 1 127 | . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1 128 | . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 129 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
```

 |

### Are there an infinite number of productive Egyptian fractions for every fraction?

Since every Egyptian fraction has a productive Egyptian fraction, we can try the method we used above to show that every productive Egyptian fraction can be expanded.
If the final *factor*was n (the ratio between the final two unit fractions in a productive Egyptian fraction), then we can replace it using the Expansion Equation that we used earlier, as follows:

t | = ...  | 1 | + | 1 | = ... | 1 | + | 1 | +  | 1 |

b | a | n a | a | (n+1) a | n (n + 1) a |

This is easier when we look at the **list of successive factors**so that, for example

13/20 = 1/2 + 1/8 + 1/40 = 1/**2**(1 + 1/**4**(1 + 1/**5**)) = 1/**2**+ 1/(2×**4**) + 1/(2×4×**5**) has the successive factors **2, 4, 5**.

The final factor n of any productive Egyptian fraction can be replaced by the two factors n + 1, n:

t/b | productive EF | successive
factors | expanded
factors | expanded
productive EF |

13/20 | 1/2 + 1/8 + 1/40  | 2, 4, 5 | 2, 4, 6, 5 | 1/2 + 1/8 + 1/48 + 1/240 |

1/2 + 1/8 + 1/48 + 1/240 | 2, 4, 6, 5 | 2, 4, 6, 6, 5 | 1/2 + 1/8 + 1/48 + 1/288 + 1/1440 |

So every fraction has a productive Egyptian fraction and we have just shown that we can extend each one by one more factored term as often as we like.

## The Harmonic Numbers

Summing the reciprocals from 1 up to n and the series of such sums have long intrigued mathematicians. The sums of the reciprocals of 1 up to n are called **the Harmonic Numbers**H(n) and the series H(1), H(2), H(3), ... is called **the Harmonic Series**:

H(n) =  | 1 | +  | 1 | +  | 1 | +  | 1 | + ... +  | 1 |

1 | 2 | 3 | 4 | n |

The series is called Harmonic because if we stretch a string tightly and twang it, we hear a certain note. Stopping the string at the half way point makes a sound an octave above the first note. If instead we take just one third of the length we get another note that seems harmonious to the ear in relation to the whole string. We also get harmonious sounds if we take one quarter and one fifth and so on for some time.
Pythagoras first noted this connection with harmonious sound and the lengths of plucked strings.
When a string is plucked as on a violin for instance, there is not only the "pure" note but also other quieter notes produced by these "harmonic" notes called overtones.

The first few values of H(n) are:

n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ... |  |

H(n) | 1
1 | 3
2 | 11
6 | 25
12 | 137
60 | 49
20 | 363
140 | ... | [A001008][39] the Wolstenholme numbers

---

[A002805][40] |

1 | 2 | 6 | 12 | 60 | 20 | 140 | [A002805][40] |

n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ... |

H(n) | 1
1 | 3
2 | 11
2×3 | 50
2×3×4 | 274
2×3×4×5 | 1764
2×3×4×5×6 | 13068
2×3×4×5×6×7 | ... | [A000254][41] the Stirling numbers of the first kind

---

[A000142][38] the Factorial numbers |

The second table is the same fractions for H(n) but without simplifying the sums.
The numerators give the total number of cycles in all permutations of length n+1 and the fractions give the ratio (probability) of a random permutation on n+1 letters having exactly two cycles!
What can we say about H(n)? Is any Harmonic number ever exactly an integer for instance?
Subtracting one Harmonic number from another larger one H(n) – H(k) gives us the sum of a consecutive set of the unit fractions 1/(k+1) + ... + 1/n. Are any of these ever integers?
Unfortunately, the answers are no; no finite sum of the series of unit fraction starting at 1 or at another unit fraction will ever sum to a whole number.

### The sum of all unit fractions

The series of reciprocals of *all*the natural numbers from 2 onwards is called **the Harmonic Series**and the question of whether or not its sum has a finite value or not is now a classic maths problem. There is a very easy proof to show that the harmonic series series "diverges", that is, summed for ever, it gets infinitely large.
In case you want to think about it yourself, the answer is revealed in an optional section:

Let's look at the first term: 1/2,
The next **2**terms: 1/3 + 1/4 but 1/3 > 1/4 so

1 | + | 1 | >  | 1 | + | 1 | = | 1 |

3 | 4 | 4 | 4 | 2 |

Now look at
the next **4**terms:

1 | + | 1 | + | 1 | + | 1 | >  | 1 | + | 1 | + | 1 | + | 1 | = | 1 |

5 | 6 | 7 | 8 | 8 | 8 | 8 | 8 | 2 |

similarly the sum of
the next **8**terms will exceed 1/2.
Since the Harmonic series sum goes on for ever, then we can always find another batch of 2 n terms whose sum adds more than 1/2 to the total,
so the total is always larger than any given number, it never settles down to a fixed value, it grows for ever or "diverges".
This result has been known since at least 1650 (Pietro Mengoli).

- **75.11 The Noninteger Property of Sums of Reciprocals of Successive Integers**Duane W. Detemple *The Mathematical Gazette*, Vol. 75, No. 472 (Jun., 1991), pages 193-194
Here is a proof that no consectuive reciprocals sum to an integer, simpler than that of the original of G.Poly&agrave; and G.Szeg&ouml; of 1976.

### The Overhanging books puzzle

[image: bookstack] There is a surprising application of the divergence of the Harmonic Series that makes a good Science Fair demonstration.
Suppose we have a shelf of identical books (or bricks or dominoes etc).

If we lay them down one on top of another what is the maximum overhang we can achieve?
Can the top book ever completely overhang the bottom book?

[image: bookstack] For **two**books we can get an overhang of 1/2 a book length;
The two books now have a centre of gravity in the centre of their overlap, so the bottom one can overhang and extra 1/4 of a book length.
The centre of gravity of the **three**books means they can have an overhang of 1/6, and so on for more books.
The extra overhang for **four**and more books is 1/8, 1/10, 1/12, ... .
The total overhang for **n**books is therefore H(n-1)/2.

How many books will it take before the overhang exceeds the length of one book?
Answer: H(4)/2 = 25/24 which is bigger than 1 so:

5 stacked books are sufficient for the top one to totally overhang the bottom one!

Can we get a bigger overhang? Yes! Since the Harmonic series diverges, we can get an overhang as large as we like, but it may take a large number of books and *very*delicate balancing! Since it is very difficult to find lots of identically sized books, try playing cards.
Theoretically for an overhang of 2 book lengths, we need to find the value of n for which H(n) > 4

H(30) = 3.99498713092
H(31) = 4.02724519544

so we need 32 books to get an overhang of 2 complete books!
For 3 book lengths, the first n with H(n) > 6 is n = 227 so that stack would be 228 books tall and n = 1674 before H(n) exceeds 8.

### A Harmonic Number Calculator

The values of the Harmonic function in this calculator are computed approximately but the digits shown are accurate.
All digits shown are correct and are within the accuracy of the approximation.

Harmonic Number C A L C U L A T O R

H( )  |

 | [image: less space]
[image: more space] |

 |

[image: calculator]: | Fraction &harr; EF | Shortest EF | Fixed Length EFs | EFs for 1 | --> productive EFs | Harmonic Numbers |

If we had 1,000,000 playing cards perfectly arranged to give the maximum overhang of the top card, how many card lengths would it overhang?

H(1 000 000) = 14.392726722865724 so the top card would overhang by more than 7 card lengths.

#### References

- [Concrete Mathematics][42] (2nd edition, 1994) by Graham, Knuth and Patashnik, Addison-Wesley page 278 expression (6.66):

H(n) &asymp; ln(n) + &gamma; +  | 1 | – | 1 | with error< | 1 |

2n | 12 n 2 | 120 n 4 |

where &gamma; is *Euler's constant*&gamma; = 0.5772156649015328606....
- **Problem 52: Overhanging dominoes**R T Sharp, Pi Mu Epsilon Journal (1954) 1 (10): 411-412 [image: pdf link] [43]
This seems to be the first appearance of the book stacking problem and its solution.
- **The Harmonic Series Diverges Again and Again**, [image: pdf link] [44] S J Kifowit, T A Stamps Twenty proofs, all elementary, of the divergence of the harmonic series.
- **More Proofs of Divergence of the Harmonic Series**S J Kifowit (unpublished) [image: pdf link] [45] Proofs 21 to 45 at the level of first year university Calculus.
- See also [S J Kifowit publications][46] where there are links to his other excellent presentations and handouts on the Harmonic series.

## Egyptian fraction Links and References

- [David Eppstein][47] of University of California, Irvine has a host of links on all sorts of information on Egyptian Fractions and a comprehensive guide to the different algorithms that can be used to write your own Egyptian Fraction computer programs, although his are described using many different techniques available in the Mathematica package and there are references to C and C++ sources too.
- Dr Scott William's page on [The Rhind 2/n Table][48] has a list of the fractions 2 / n written as Egyptian fractions in the Rhind papyrus that we mentioned at the start of this page and that is given in full earlier on this page. He also includes a discussion and analysis of the fractions chosen and suggestions of the methods the Egyptians might have used. He has some interesting pages on African mathematics and mathematicians from ancient times to today.
- [Eric Weisstein's Mathworld article on Egyptian Fractions][49] has many references too.
- **Fibonacci on Egyptian Fractions**M. Dunton and R. E. Grimm, *Fibonacci Quarterly*vol 4 (1966), pages 339-353. Here Grimm and Dunton give an English translation and explanation using modern notation of the section in chapter 7 of Fibonacci's *Liber Abaci*which gives methods of expressing a fraction as a sum of unit fractions. Fibonacci deals with several special cases called *distinctions*before giving the "greedy" algorithm above as the seventh and general method. [image: pdf link][image: in new window] [50]
- [The Rhind Mathematical Papyrus][51] G Robins, C Shute, British Museum Press, 1987, (88 pages, paperback) is highly recommended for its explanations of the arithmetic methods that may have been used in the 2/n table and the other tables and problems in the papyrus. It has excellent colour photographs of the papyrus and many illustrations. Buy it from the Amazon.co.uk site [use the link above] as it is *much*cheaper than the Amazon.com site!
- [Unsolved Problems in Number Theory][52] (3rd edition 2004) by R Guy, Springer
Section D11 (pages 252-262) is all about unsolved problems in Egyptian Fractions and there is also has an extensive bibliography on the subject. This is essential reading for the serious researcher!
Problem D11 is about Egyptian Fractions and contains many references and interesting results.
- [Count Like an Egyptian: A Hands-on Introduction to Ancient Mathematics][53] David Reimer, Princeton Press (2014)
is a new and detailed book explaining much more about the Rhind papyrus, its methods, the background and history, with a host of detail and worked examples. An excellent manual for those who want to delve more deeply into the mathematical methods of the ancient Egyptians. Uses no advanced maths beyond secondary school level. Recommended!

The following two books are recommended if you want to read more about the extraordinary Hungarian mathematician Paul Erd&ouml;s

- [The Man Who Loved Only Numbers: The Story of Paul Erdos and the Search for Mathematical Truth][54] by P Hoffmann, Fourth Estate (1999) paperback
- [My Brain Is Open: The Mathematical Journeys of Paul Erdos][55] B Schechter, Simon & Schuster (2000) paperback
- or try this highly acclaimed DVD:
[N is a Number: A Portrait of Paul Erd&ouml;s][56] (2007) Region 1, USA and Canada only, for NSTC (non-EU) TVs.

On the History of Egyptian mathematics, I recommend:

- [Mathematics in the Time of the Pharaohs][57] by Richard J Gillings, Dover, 1972 is an inexpensive and readable account of the mathematics in the Rhind Papyrus, it contents and methods. Recommended!
- [The Exact Sciences in Antiquity][58] by Otto Neugebauer, Dover, second edition 1969, is another great book covering not only Egyptian arithmetic but also the Babylonian, Sumerian and Greek contributions to both number notation and arithmetic as well as astronomy. It is about the history of the mathematics more than the maths itself and is now, rightly, a classic on this subject.

---

[image: Valid HTML 4.01!] [59] &copy; 2004-2017 [Dr Ron Knott][60]
Created:2004,

****[Back to Dr Knott's Fibonacci Home page][61]


## Links

[1]: http://aleph0.clarku.edu/~djoyce/mathhist/egypt.html
[2]: http://aleph0.clarku.edu/~djoyce/mathhist/mathhist.html
[3]: http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Ahmes.html
[4]: http://../Fibonacci/
[5]: http://mathforum.org/kb/message.jspa?messageID=232194
[6]: http://oeis.org/A097049
[7]: http://oeis.org/A097048
[8]: ../Figurate/figurate.html#oblong
[9]: http://oeis.org/A006585
[10]: http://oeis.org/A073546
[11]: http://www.math.ubc.ca/~gerg/index.shtml?abstract=DEF
[12]: http://oeis.org/A030659
[13]: http://oeis.org/A092671
[14]: http://oeis.org/A052428
[15]: http://oeis.org/A051882
[16]: http://oeis.org/A051907
[17]: http://www.math.ucsd.edu/~ronspubs/63_02_partitions.pdf
[18]: http://oeis.org/A051909
[19]: http://oeis.org/A002966
[20]: http://oeis.org/A000058
[21]: http://www.research.att.com/~njas/sequences/Seis.html
[22]: http://oeis.org/A005835
[23]: http://oeis.org/A006036
[24]: http://oeis.org/A000396
[25]: http://www.amazon.com/exec/obidos/ASIN/0684717557/fibonacnumbersan
[26]: http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Erdos.html
[27]: http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Straus.html
[28]: http://mathworld.wolfram.com/Erdos-StrausConjecture.html
[29]: http://oeis.org/A139665
[30]: http://oeis.org/A073101
[31]: http://oeis.org
[32]: http://www-groups.dcs.st-and.ac.uk/~history/Mathematicians/Sierpinski.html
[33]: http://oeis.org/A075248
[34]: allhaveFef
[35]: http://oeis.org/A002110
[36]: http://oeis.org/A064646
[37]: http://oeis.org/A064647
[38]: http://oeis.org/A000142
[39]: http://oeis.org/A001008
[40]: http://oeis.org/A002805
[41]: http://oeis.org/A000254
[42]: http://www.amazon.com/exec/obidos/ASIN/0201558025/fibonacnumbersan
[43]: http://www.maa.org/sites/default/files/Hudleson-MMz-201007804.pdf
[44]: http://stevekifowit.com/pubs/sum2.pdf
[45]: http://stevekifowit.com/pubs/harm2.pdf
[46]: http://stevekifowit.com/pubs/
[47]: http://www.ics.uci.edu/~eppstein/numth/egypt/
[48]: http://www.math.buffalo.edu/mad/Ancient-Africa/mad_ancient_egyptroll2-n.html
[49]: http://mathworld.wolfram.com/EgyptianFraction.html
[50]: http://www.fq.math.ca/Scanned/4-4/dunton.pdf
[51]: http://www.amazon.co.uk/exec/obidos/ASIN/0714109444/fibonacnumbers04
[52]: http://www.amazon.co.uk/exec/obidos/ASIN/0387208607/fibonacnumbers04
[53]: http://www.amazon.co.uk/exec/obidos/ASIN/0691160120/fibonacnumbers04
[54]: http://www.amazon.com/exec/obidos/ASIN/1857028295/fibonacnumbersan
[55]: http://www.amazon.com/exec/obidos/ASIN/0684859807/fibonacnumbersan
[56]: http://www.amazon.com/exec/obidos/ASIN/B0002MQFI2/fibonacnumbersan
[57]: http://www.amazon.com/exec/obidos/ASIN/048624315X/fibonacnumbersan
[58]: http://www.amazon.com/exec/obidos/ASIN/0486223329/fibonacnumbersan
[59]: http://validator.w3.org/
[60]: ../contactron.html
[61]: ../Fibonacci/fib.html
