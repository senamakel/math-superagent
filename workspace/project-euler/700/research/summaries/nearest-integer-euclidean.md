<!-- source: http://www.numbertheory.org/php/neuclid.html | full text at research/sources/nearest-integer-euclidean.full.md -->

A nearest integer Euclidean algorithm

### Nearest integer Euclidean algorithm

If r is a real number, by [r] we mean the *nearest integer to r*. Thus |r - [r]| ≤ 1/2 and if r = t + 1/2, where t is an integer, then [r] = t + 1.
Alternatively, [r] = [image: lfloor] r + 1/2 [image: rfloor], the integer part of r + 1/2,
Hence [r] = r + &theta;, where -1/2 < &theta; &le 1/2.

Then if m and n are integers, n > 0 and q = [m/n], we have m/n = q + &theta;, where -1/2 < &theta; ≤ 1/2.
Hence m = nq + n&theta;, where -n/2 < n&theta; ≤ n/2.
Hence m = nq + es, where -n/2 < es ≤ n/2 and s is an integer, 0 ≤ s ≤ n/2 and e = 1 if &theta; ≥ 0, while e = -1 if &theta; < 0.
We write e = e(m,n).

Then with r 0 = m and r 1 = n > 0, we define r k recursively for 2 ≤ k ≤ l+1, r k > 0 and e k+1 = e(r k-1,r k), where q k = [r k-1 / r k] for 1 ≤ k ≤ l:

r 0 | = | r 1 q 1 + e 2 r 2 | (-r 1 / 2 < e 2 r 2 ≤ r 1 / 2) |

r 1 | = | r 2 q 2 + e 3 r 3 | (-r 2 / 2 < e 3 r 3 ≤ r 2 /2) |

 | &middot;&middot;&middot; |  |  |

r k-1 | = | r k q k + e k+1 r k+1 | (-r k / 2 < e k+1 r k+1 ≤ r k / 2) |

 | &middot;&middot;&middot; |  |  |

r l-1 | = | r l q l |  |

Then r l = gcd(m,n).

The s k and t k are also printed in tabular form, where it is convenient to define e 0 = 1 = e 1 and where

s 0 = 1, | s 1 = 0, | e k s k = s k-2 – q k-1 s k-1, |  |

t 0 = 0, | t 1 = 1, | e k t k = t k-2 – q k-1 t k-1, | k = 2,..., l+1. |

Then r k = s k m + t k n for 0 ≤ k ≤ l+1, where r l+1 = 0. The number of steps is no greater than the number in Euclid's algorithm.

(Based on Exercise 5, page 67, *Elementary Number theory and its applications*, by Ken Rosen.
Also see Chapter 39 (Kettenbr&uuml;che nach n&auml;chsten Ganzen), page 168, *Kettenbr&uuml;che*, by Oscar Perron, Chelsea 1950.
We print the nearest integer continued fraction expansion m/n = q 1 +e 2 /q 2 + ⋯ +e l /q l.

x 0 = m/n, x n = a n - 1/x n+1, where a n = [x n], n ≥ 0.
This gives a continued fraction m/n = a 0 - 1/a 1 - &middot;&middot;&middot; - 1/a l, where |a i | ≥ 2 for all i ≥ 1.
The notation m/n = (a 0,a 1,...,a l) goes back to A. Hurwitz, Werke, Seite 85.-->

*Last modified 26th January 2009*
[Return to main page][1]


## Links

[1]: ./cfrac.html
