<!-- source: https://dms.umontreal.ca/~andrew/Binomial/elementary.html | converted from HTML -->

Elementary Number Theory.

# Elementary Number Theory.

For a given integer *n*we define to be the product of those integers that are not divisible by *p*.

Wilson's Theorem, which states that , may be generalized to prime powers as follows:

---

**Lemma 1***For any given prime power we have

where is **-1**, unless in which case is *1*.*

---

This was originally [proved][1] by Gauss in *Disquisitiones Arithmeticae*, the main idea being to multiply each number with its inverse modulo *p*.

We may [deduce][2] from Lemma 1, the following:

---

**Corollary 1***For any given prime power , let be the least non-negative residue of . Then

where is as in Lemma 1.*

---

In 1808 Legendre showed that the exact power of *p*dividing is

**(17)**

Writing *n*in base *p*as above, we define the *sum of digits function*. Then (17) equals

**(18)**

These can be [proved][3] from a suitable induction hypothesis.

Given integers *n*and *m*, we take *r=n-m*. Define if there is a `carry' in the *j*th digit when we add *m*and *r*in base *p*; otherwise let (including ). We now use (18) to deduce

---

**Kummer's Theorem***The power to which prime *p*divides the binomial coefficient is given by the number of `carries' when we add *m*and *n-m*in base *p*.*

---

**Proof:**One should check that, for each integer ,

Now, by (18), we know that the power of *p*dividing is

By definition, this equals

the total number of `carries'.

---

By a similar [argument][4] we also have that, for each ,
**(19)**
The improvement, (2), of Lucas' Theorem is easily deduced from the equation

which was discovered by Anton, Stickelberger and then Hensel. For an arbitrary prime power , we may [generalize this result][5] by using the results that we have collected above.

---


## Links

[1]: pflemma1.html
[2]: pflemma1.html#pfcor1
[3]: pfeq1718.html
[4]: pfeq19.html
[5]: genlucas.html
