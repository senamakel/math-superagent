<!-- source: https://ar5iv.labs.arxiv.org/html/0806.3585 | converted from HTML -->

[0806.3585] Improved Bounds on the Sizes of S ⋅ P Numbers

# Improved Bounds on the Sizes of S ⋅ \cdot P Numbers Thanks: The second author gratefully acknowledges the support of a Harvard Mathematics Department Highbridge Fellowship.

Paul Myer Kominers and Scott Duke Kominers Address:
Student, Department of Mathematics, Massachusetts Institute of Technology Email address: [pkoms@mit.edu][1] Address:
Student, Department of Mathematics, Harvard University
c/o 8520 Burning Tree Road
Bethesda, MD 20817 Email address: [kominers@fas.harvard.edu][2]

## 1. Introduction

A number which is *S ⋅ \cdot P in base r r*is a positive integer which is equal to the sum of its base- r r digits multiplied by the product of its base- r r digits. That is, a n ​ r n + ⋯ + a 1 ​ r + a 0 a_{n}r^{n}+\cdots+a_{1}r+a_{0} (here and hereafter, 0 ≤ a i < r 0\leq a_{i}<r for all 0 ≤ i ≤ n 0\leq i\leq n) is S ⋅ \cdot P if and only if

 | a n r n + ⋯ + a 1 r + a 0 = a 0 ⋯ a n ( a 0 + ⋯ + a n). a_{n}r^{n}+\cdots+a_{1}r+a_{0}=a_{0}\cdots a_{n}(a_{0}+\cdots+a_{n}). |  |

For example, 144 = 1 ⋅ 4 ⋅ 4 ⋅ ( 1 + 4 + 4) 144=1\cdot 4\cdot 4\cdot(1+4+4) is S ⋅ \cdot P in base 10 10 and 6 = 1 ⋅ 2 ⋅ ( 1 + 2) 6=1\cdot 2\cdot(1+2) is S ⋅ \cdot P in base 4 4.

Parameśwaran [5] conjectured that the number of base- 10 10 S ⋅ \cdot P numbers is finite. Several authors subsequently gave proofs of Parameśwaran’s conjecture and generalizations to other bases (see [1]), as well as enumerations of S ⋅ \cdot P numbers (see [4, 2]). Recently, Shah Ali [6] gave a new argument proving that the number of base- r r S ⋅ \cdot P numbers is finite for any r > 1 r>1. In his proof, Shah Ali [6] obtained the first effective bound on the sizes of S ⋅ \cdot P numbers:

###### Proposition 1.

( [6]) A number which is S ⋅ \cdot P in base r > 1 r>1 has at most 2 ​ r ​ ( r − 1) 2 2r(r-1)^{2} digits.

However, a quick check in the case r = 2 r=2 shows that this bound is far from sharp. While Proposition 1 shows that a base- 2 2 S ⋅ \cdot P number can have at most 4 4 digits, quick analysis shows that there is a unique base- 2 2 S ⋅ \cdot P number, 1 1. Indeed, if a n ​ 2 n + ⋯ + a 1 ​ 2 + a 0 a_{n}2^{n}+\cdots+a_{1}2+a_{0} is S ⋅ \cdot P in base 2 2 then a i = 1 a_{i}=1 for 0 ≤ i ≤ n 0\leq i\leq n. However, we then must have

 | 2 n + 1 − 1 = 2 n + ⋯ + 2 0 = a n ​ 2 n + ⋯ + a 0 = a n + ⋯ + a 0 = 1 + ⋯ + 1 = n + 1; 2^{n+1}-1=2^{n}+\cdots+2^{0}=a_{n}2^{n}+\cdots+a_{0}=a_{n}+\cdots+a_{0}=1+\cdots+1=n+1; |  |

it follows easily that n = 0 n=0.

## 2. A Sharp Bound

Modifying Shah Ali’s [6] method, we obtain an improved bound on the number of digits in a base- r r S ⋅ \cdot P number. As we will discuss in Section 3, our bound is sharp in the case r = 2 r=2.

###### Proposition 2.

A number which is S ⋅ \cdot P in base r > 1 r>1 has at most 2 ​ ( r − 1) 3 − 2 ​ ( r − 1) + 1 = 2 ​ ( r − 1) ​ ( r 2 − 2 ​ r) + 1 2(r-1)^{3}-2(r-1)+1=2(r-1)(r^{2}-2r)+1 digits.

###### Proof.

Let a n ​ r n + ⋯ + a 1 ​ r + a 0 a_{n}r^{n}+\cdots+a_{1}r+a_{0} be S ⋅ \cdot P in base r r with n ≥ 0 n\geq 0, so that

 | a n r n + ⋯ + a 1 r + a 0 = a 0 ⋯ a n ( a 0 + ⋯ + a n). a_{n}r^{n}+\cdots+a_{1}r+a_{0}=a_{0}\cdots a_{n}(a_{0}+\cdots+a_{n}). |  |

Then, 0 < a i < r 0<a_{i}<r for all 0 ≤ i ≤ n 0\leq i\leq n, so that we have

(1) |  | ( min 0 ≤ i ≤ n { a i }) ⋅ ( r n + 1 − 1 r − 1) ≤ a 0 ⋯ a n ( a 0 + ⋯ + a n). \left(\min_{0\leq i\leq n}\{a_{i}\}\right)\cdot\left(\frac{r^{n+1}-1}{r-1}\right)\leq a_{0}\cdots a_{n}(a_{0}+\cdots+a_{n}). |  |

Then, since min 0 ≤ i ≤ n ⁡ { a i } > 0 \min_{0\leq i\leq n}\{a_{i}\}>0, we may divide both sides of ( 1) by min 0 ≤ i ≤ n ⁡ { a i } \min_{0\leq i\leq n}\{a_{i}\} and obtain

(2) |  | r n + 1 − 1 r − 1 ≤ a 0 ⋯ a n min 0 ≤ i ≤ n ⁡ { a i } ​ ( a 0 + ⋯ + a n) ≤ ( r − 1) n ​ ( n + 1) ​ ( r − 1), \displaystyle\frac{r^{n+1}-1}{r-1}\leq\frac{a_{0}\cdots a_{n}}{\min_{0\leq i\leq n}\{a_{i}\}}(a_{0}+\cdots+a_{n})\leq(r-1)^{n}(n+1)(r-1), |  |

as max 0 ≤ i ≤ n ⁡ { a i } < r \max_{0\leq i\leq n}\{a_{i}\}<r. Rearranging ( 2) gives

(3) |  | ( 1 + 1 r − 1) n + 1 = ( r r − 1) n + 1 ≤ ( n + 1) ​ ( r − 1) + 1 ( r − 1) n + 1. \left(1+\frac{1}{r-1}\right)^{n+1}=\left(\frac{r}{r-1}\right)^{n+1}\leq(n+1)(r-1)+\frac{1}{(r-1)^{n+1}}. |  |

By the Binomial Theorem, the left side of ( 3) is equal to

 | 1 + n + 1 r − 1 + ( n + 1) ​ n 2 ​ ( r − 1) 2 + ⋯, 1+\frac{n+1}{r-1}+\frac{(n+1)n}{2(r-1)^{2}}+\cdots, |  |

hence we obtain

(4) |  | 1 + n + 1 r − 1 + ( n + 1) ​ n 2 ​ ( r − 1) 2 ≤ ( n + 1) ​ ( r − 1) + 1 ( r − 1) n + 1. 1+\frac{n+1}{r-1}+\frac{(n+1)n}{2(r-1)^{2}}\leq(n+1)(r-1)+\frac{1}{(r-1)^{n+1}}. |  |

Simplifying ( 4), we find

(5) |  | n ≤ 2 ​ ( r − 1) 3 − 2 ​ ( r − 1) + 2 n + 1 ​ ( 1 ( r − 1) n − 1 − ( r − 1) 2). n\leq 2(r-1)^{3}-2(r-1)+\frac{2}{n+1}\left(\frac{1}{(r-1)^{n-1}}-(r-1)^{2}\right). |  |

Now, since r > 1 r>1 and n ≥ 0 n\geq 0, we have that ( r − 1) 1 − n − ( r − 1) 2 ≤ 0 (r-1)^{1-n}-(r-1)^{2}\leq 0. It then follows from ( 5) that n ≤ 2 ​ ( r − 1) 3 − 2 ​ ( r − 1) n\leq 2(r-1)^{3}-2(r-1). ∎

## 3. Remarks

Use of a computer algebra system suggests that [1] implies the effective bound

(6) |  | n + 1 ≤ W − 1 ​ ( log ⁡ ( r − 1) − log ⁡ ( r) r) log ⁡ ( r − 1) − log ⁡ ( r) n+1\leq\frac{W_{-1}\left(\frac{\log(r-1)-\log(r)}{r}\right)}{\log(r-1)-\log(r)} |  |

on the number ( n + 1) (n+1) of digits of a base- r r S ⋅ \cdot P number. Here, W − 1 ​ ( ⋅) W_{-1}(\cdot) is the ( − 1) st (-1)^{\text{st}} analytic branch of the *Lambert W W -Function*, the multivalued inverse of the function f ⁡ ( W) = W ​ e W f(W)=We^{W}. (Weisstein [7] summarizes the fundamental properties of the W W -function. Corless et al. [3] survey several relevant applications and present an efficient method of evaluating the W W -function to arbitrary precision.) Although we have been unable to prove the bound ( 6), we have verified it for 1 < r ≤ 999 1<r\leq 999.

The bound given in Proposition 2 is sharp for the case r = 2 r=2; this is a 75% improvement on the bound of Shah Ali’s [6] Proposition 1. Furthermore, although ( 6) is generally far smaller than the cubic bound of Proposition 2, ( 6) gives at best that an S ⋅ \cdot P number in base 2 2 has no more than two digits. Thus, our Proposition 2 is the first sharp bound found for the case r = 2 r=2.

For the case r = 10 r=10, Proposition 2 gives a bound of 1441 1441 digits, an 11% improvement upon Proposition 1. However, this bound is far weaker than the bounds given in [1], which show that a base- 10 10 S ⋅ \cdot P number can have at most 60 60 digits.

## Acknowledgements

The authors greatly appreciate the referee’s helpful comments and suggestions on an earlier draft of the work.

## References

- [1] Paul Belcher, H. J. Godwin, Andrew Lobb, Nick Lord, K. Robin McLean and Phillip Williams, On S ⋅ \cdot P numbers, Math. Gaz. 82 (March 1998) pp. 72–75.
- [2] Ezra Bussmann, S ⋅ \cdot P numbers in bases other than 10, Math. Gaz. 85 (July 2001) pp. 245–248.
- [3] R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, and D. E. Knuth, On the Lambert W W function, Adv. Comp. Math. 5 (December 1996) pp. 329-359.
- [4] K. Robin McLean, There are only three S ⋅ \cdot P numbers, Math. Gaz. 83 (March 1999) pp. 32–39.
- [5] S. Parameśwaran, Numbers and their digits – a structural pattern, Math. Gaz. 81 (July 1997) p. 263.
- [6] H. A. Shah Ali, The number of S ⋅ \cdot P numbers is finite, Math. Gaz. 92 (March 2008) pp. 64–65.
- [7] Eric W. Weisstein, Lambert’s W W -function, CRC Concise Encyclopedia of Mathematics, CRC Press (2003) pp. 1684–1685.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:pkoms@mit.edu
[2]: mailto:kominers@fas.harvard.edu
[3]: /html/0806.3584
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/0806.3585
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0806.3585
[9]: https://arxiv.org/pdf/0806.3585
[10]: /html/0806.3587
