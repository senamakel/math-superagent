<!-- source: https://arxiv.org/html/2301.09664v1 | converted from HTML -->

A Useful Inequality for theBinary Entropy Function

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2301.09664v1 [math.CO] 23 Jan 2023

# A Useful Inequality for the
Binary Entropy Function

Ravi B. Boppana Thanks: Department of Mathematics, Massachusetts Institute of Technology, Cambridge, Massachusetts, USA. Email address: rboppana@mit.edu.

January 23, 2023

###### Abstract

We provide a simple proof of a curious inequality for the binary entropy function, an inequality that has been used in two different contexts. In the 1980’s, Boppana used this entropy inequality to prove lower bounds on Boolean formulas. More recently, the inequality was used to achieve major progress on Frankl’s union-closed sets conjecture. Our proof of the entropy inequality uses basic differential calculus.

## 1 Introduction

In this note, we provide a simple proof of a curious inequality for the binary entropy function, an inequality that has been used in two different contexts.

Let h h be the binary entropy function, defined on the interval [0, 1] [0,1] as follows:

 | h ⁡ ( x) = { − x ​ log ⁡ x − ( 1 − x) ​ log ⁡ ( 1 − x) if 0 < x < 1; 0 if x = 0 or x = 1. h(x)=\begin{cases}-x\log x-(1-x)\log(1-x)&\text{if $0<x<1$;}\\ 0&\text{if $x=0$ or $x=1$.}\end{cases} |  |

Here log \log means natural logarithm (base e e).

The following lemma is the inequality that we will prove.

###### Lemma.

If 0 ≤ x ≤ 1 0\leq x\leq 1, then

 | h ⁡ ( x 2) ≥ ϕ ​ x ​ h ​ ( x), h(x^{2})\geq\phi xh(x), |  |

where ϕ \phi is the golden ratio, 5 + 1 2 \frac{\sqrt{5}+1}{2}.

The history of this entropy inequality is interesting. Boppana [2, 3] first used this inequality to prove lower bounds on Boolean formulas. More precisely, he proved a two-variable inequality on the binary entropy function, which as a special case yields the one-variable inequality above. His proof of the two-variable inequality was computer assisted. In unpublished work [4], he gave a simple proof of the one-variable inequality. This simple proof is the one we will record in this note.

More than 30 years later, the same inequality was used to make major progress on Frankl’s union-closed sets conjecture. Gilmer [8] used the information-theoretic concept of entropy to achieve a breakthrough on the union-closed conjecture. Immediately after, the entropy inequality above was used to improve Gilmer’s bound by Alweiss, Huang, and Sellke [1], Chase and Lovett [6], Pebody [9], and Sawin [10]. Regarding the entropy inequality itself, Alweiss, Huang, and Sellke [1] gave a proof using computer assistance. Chase and Lovett [6] cited the proof of [1]. Pebody [9] wrote “to be proven”. Sawin [10] gave a symbolic proof, noting that it is “somewhat complicated, though it would not be surprising if a simple symbolic proof exists”. Our proof confirms that a simple symbolic proof exists.

Further progress on the union-closed conjecture was given by Cambie [5], Ellis [7], and Yu [11].

## 2 Proof of the entropy inequality

In this section, we provide a proof of the entropy inequality using basic differential calculus.

###### Lemma.

If 0 ≤ x ≤ 1 0\leq x\leq 1, then

 | h ⁡ ( x 2) ≥ ϕ ​ x ​ h ​ ( x), h(x^{2})\geq\phi xh(x), |  |

where ϕ \phi is the golden ratio, 5 + 1 2 \frac{\sqrt{5}+1}{2}.

###### Proof.

Let ℝ \mathbb{R} be the set of real numbers. It will be convenient to extend h h to all of ℝ \mathbb{R} as follows:

 | h ⁡ ( x) = { − x ​ log ⁡ | x | − ( 1 − x) ​ log ⁡ | 1 − x | if x ≠ 0 and x ≠ 1; 0 if x = 0 or x = 1. h(x)=\begin{cases}-x\log\lvert x\rvert-(1-x)\log\lvert 1-x\rvert&\text{if $x\neq 0$ and $x\neq 1$;}\\ 0&\text{if $x=0$ or $x=1$.}\end{cases} |  |

Let f f be the function on ℝ \mathbb{R} defined by

 | f ⁡ ( x) = h ⁡ ( x 2) − ϕ ​ x ​ h ​ ( x). f(x)=h(x^{2})-\phi xh(x). |  |

To prove the lemma, we will show that f f is nonnegative on [0, 1] [0,1].

The first derivative f ′ f^{\prime} is defined on ℝ ∖ { − 1, 1 } \mathbb{R}\smallsetminus\{-1,1\}, the second derivative f ′′ f^{\prime\prime} is defined on ℝ ∖ { − 1, 0, 1 } \mathbb{R}\smallsetminus\{-1,0,1\}, and the third derivative f ′′′ f^{\prime\prime\prime} is defined on ℝ ∖ { − 1, 0, 1 } \mathbb{R}\smallsetminus\{-1,0,1\}. Taking derivatives three times, we see that if x ∈ ℝ ∖ { − 1, 0, 1 } x\in\mathbb{R}\smallsetminus\{-1,0,1\}, then

 | f ′′′ ​ ( x) = p ⁡ ( x) x ​ ( 1 − x 2) 2, f^{\prime\prime\prime}(x)=\frac{p(x)}{x(1-x^{2})^{2}}\,, |  |

where p p is the cubic polynomial defined by

 | p ⁡ ( x) = − ϕ ​ x 3 − 4 ​ x 2 + 3 ​ ϕ ​ x + 2 ​ ϕ − 4. p(x)=-\phi x^{3}-4x^{2}+3\phi x+2\phi-4. |  |

Because the leading coefficient of p p is negative and p ⁡ ( 0) p(0) is negative, p p has at least one negative root. Thus p p has at most two nonnegative roots. Hence the third derivative f ′′′ f^{\prime\prime\prime} has at most two roots in ( 0, 1) (0,1).

By Rolle’s theorem, applied three times, it follows that f f itself has at most five roots in [0, 1] [0,1], counting multiplicity. The function f f has a double root at 0 0, a double root at ϕ − 1 \phi^{-1}, and a single root at 1 1. Thus we have found all five roots of f f in [0, 1] [0,1].

Because f f has a double root at ϕ − 1 \phi^{-1}, it is either all nonnegative or all nonpositive on [0, 1] [0,1]. For x x a tiny positive number, f ⁡ ( x) f(x) is positive. Hence f f is nonnegative on [0, 1] [0,1]. ∎

## References

- [1] Ryan Alweiss, Brice Huang, and Mark Sellke. Improved lower bound for Frankl’s union-closed sets conjecture. [arXiv:2211.11731][3], 2022.
- [2] Ravi B. Boppana. Amplification of probabilistic Boolean formulas. *26th Annual IEEE Symposium on Foundations of Computer Science*, pp. 20–29, 1985. Final version in [3].
- [3] Ravi B. Boppana. Amplification of probabilistic Boolean formulas. *Advances in Computing Research*, volume 5, JAI Press, pp. 27-45, 1989. Preliminary version in [2].
- [4] Ravi B. Boppana. Unpublished notes, 1989.
- [5] Stijn Cambie. Better bounds for the union-closed sets conjecture using the entropy approach. [arXiv:2212.12500][4], 2022.
- [6] Zachary Chase and Shachar Lovett. Approximate union closed conjecture. [arXiv:2211.11689][5], 2022.
- [7] David Ellis. Note: a counterexample to a conjecture of Gilmer which would imply the union-closed conjecture. [arXiv:2211.12401][6], 2022.
- [8] Justin Gilmer. A constant lower bound for the union-closed sets conjecture. [arXiv:2211.09055][7], 2022.
- [9] Luke Pebody. Extension of a method of Gilmer. [arXiv:2211.13139][8], 2022.
- [10] Will Sawin. An improved lower bound for the union-closed sets conjecture. [arXiv:2211.11504][9], 2022.
- [11] Lei Yu. Dimension-free bounds for the union-closed sets conjecture. [arXiv:2212.00658][10], 2022.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://arxiv.org/pdf/2211.11731
[4]: https://arxiv.org/pdf/2212.12500
[5]: https://arxiv.org/pdf/2211.11689
[6]: https://arxiv.org/pdf/2211.12401
[7]: https://arxiv.org/pdf/2211.09055
[8]: https://arxiv.org/pdf/2211.13139
[9]: https://arxiv.org/pdf/2211.11504
[10]: https://arxiv.org/pdf/2212.00658
