<!-- source: https://t5k.org/glossary/page.php?sort=GilbreathsConjecture | converted from HTML -->

The Prime Glossary: Gilbreath's conjecture

# Gilbreath's conjecture

In 1958, Norman O. Gilbreath was doodling on a napkin. He started by writing down the first few [primes][1]:

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...

Under these he put their differences:

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...
1, 2, 2, 4, 2, 4, 2, 4, 6, 2, ...

Under these he put the unsigned difference of the differences. And he continued this process of finding iterated differences:

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ...
1, 2, 2, 4, 2, 4, 2, 4, 6, 2, ...
1, 0, 2, 2, 2, 2, 2, 2, 4, ...
1, 2, 0, 0, 0, 0, 0, 2, ...
1, 2, 0, 0, 0, 0, 2, ...
1, 2, 0, 0, 0, 2, ...
1, 2, 0, 0, 2, ...
1, 2, 0, 2, ...
1, 2, 2, ...
1, 0, ...
1, ...

**Gilbreath's [Conjecture][2]**is that the numbers in the first column are all one (after the initial two). Two of Gilbreath's students verified this conjecture for the first 64,419 rows. Since then it has been checked to higher and higher limits, and continues to hold. For example, by 1993 Andrew Odlyzko had checked this conjecture using the primes up to 10,000,000,000,000 (that is 346,065,536,839 rows)!

As if often the case, Gilbreath was not the first to look at the conjecture that bears his name. Proth claimed to have proven this result in 1878, but his proof turned out to be faulty.

How do we check this conjecture? Certainly Odlyzko did not check all iterated differences for all of the primes up to 10 13 (this would require the computation of about 5 22 numbers)! To understand what he did do, first notice that the first number in each row of differences must be odd (because 2 is the only even prime). Also, if the row starts with a 1 and then *n*entries which are either 0 or 2, then the next *n*rows must start with a one. So Odlyzko looked for a row that began with a 1 and enough 0's or 2's to complete his work. For this he only needed to complete the first 635 rows. (Check his article for other ways to speed this process up.)

Smallest *k*for which the first pi(*x*) (the number of primes less than or equal to *x*) entries in the *k*th row are 0, 1 or 2

*x* | pi(*x*) | *k* |  | *x* | pi(*x*) | *k* |

10 2 | 25 | 5 |  | 10 3 | 168 | 15 |

10 4 | 1,229 | 35 |  | 10 5 | 9,592 | 65 |

10 6 | 78,498 | 95 |  | 10 7 | 664,579 | 135 |

10 8 | 5,761,455 | 175 |  | 10 9 | 50,847,534 | 248 |

10 10 | 455,052,511 | 329 |  | 10 11 | 4,118,054,813 | 417 |

10 12 | 37,607,912,018 | 481 |  | 10 13 | 346,065,536,839 | 635 |

Richard Guy suggests that there is nothing special about the [sequence][3] of primes, that it is just the fact the the primes grow slowly and are reasonably distributed. Perhaps if we knew enough about the maximal [gaps between primes][4], or about the distribution of these [gaps][4], then we could complete the proof.

**Related pages**(outside of this work)

- [The gaps between primes][5]

**References:**

Guy94**R. K. Guy**, *Unsolved problems in number theory*, Springer-Verlag, 1994. New York, NY, ISBN 0-387-94289-0. **[MR 96e:11002][6]**[An excellent resource! Guy briefly describes many open questions, then provides numerous references. See his newer editions of this text.] Odlyzko93**A. M. Odlyzko**, "Iterated absolute values of differences of consecutive primes," *Math. Comp.*, **61**(1993) 373-380. **[MR 93k:11119][7]**( [Abstract available][8]) Proth1878**F. Proth**, "Th&eacute;or&egrave;mes sur les nombres premiers," *C. R. Acad. Sci. Paris*, **85**(1877) 329-331.

Printed from the PrimePages <t5k.org> &copy; Reginald McLean.


## Links

[1]: /glossary/xpage/Prime.html
[2]: /glossary/xpage/Conjecture.html
[3]: /glossary/xpage/Sequence.html
[4]: /glossary/xpage/PrimeGaps.html
[5]: /notes/gaps.html
[6]: http://www.ams.org/mathscinet-getitem?mr=96e:11002
[7]: http://www.ams.org/mathscinet-getitem?mr=93k:11119
[8]: /references/refs.cgi?long=Odlyzko93
