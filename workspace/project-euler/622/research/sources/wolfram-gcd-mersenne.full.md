<!-- source: https://functions.wolfram.com/IntegerFunctions/GCD/03/01/0007/ | converted from HTML -->

Greatest common divisor: Specific values (formula 04.08.03.0007) n*1,*n*2,...,*n**m*], Specific values, Specialized values" />

 |

[image: Wolfram Research] [1][image: functions.wolfram.com] [2][image: Other Wolfram Sites] [3] |

 |  |

 |  |

 |

[image: Function Categories] [4][image: Graphics Gallery] [5][image: Notations] [6][image: General Identities] [7][image: About This Site] [8] |  | [image: Email Comments] [9] |

 |  |  |

 |

[image: Elementary Functions] [10] |

[image: Constants] [11] |

[image: Bessel-Type
Functions] [12] |

[image: Integer Functions] [13] |

[image: Polynomials] [14] |

[image: Gamma, Beta, Erf] [15] |

[image: Hypergeometric Functions] [16] |

[image: Elliptic Integrals] [17] |

[image: Elliptic Functions] [18] |

[image: Zeta Functions and Polylogarithms] [19] |

[image: Mathieu and Spheroidal Functions] [20] |

[image: Complex Components] [21] |

[image: Number Theory Functions] [22] |

[image: Generalized Functions] [23] |

 |
 |

 |  |  |

 |  |  |

 |  |  |

 | [image: Alphabetical Index] [24] |  |

 |  |  |

 |  |  |

 |  |  |

 |

 |

[image: Overview] [8] |

[image: Mathematica & This Site] [25] |

[image: The Developers] [26] |

[image: Our Vision] [27] |

[image: How to Cite This Site] [28] |

[image: FAQs] [29] |

 |
 |

 |  |  |

 |

 |

 |  |  |  |  |

 |  |

 |

 |

 |  |  |

 |  |  |  |  |

 |

 |  | [image: View Related Information In]
[image: The Documentation Center] [30]
[image: MathWorld] [31]

[image: Download All Formulas For This Function]
[image: Mathematica Notebook] [32]
[image: PDF File] [33]

[image: Download All Introductions For This Function]
[image: Mathematica Notebook] [34]
[image: PDF File] [35]

 |  |  |

 |

 |  |  |  |  |

 |

 |  |

[image: Developed with Mathematica -- Download a Free Trial Version] [36] |

 |

 |  |

 |

 |
 |
 |

 |

 |

 |
 |

 |
 |
 |

 |

GCD

 |

 |
 |

 |
 |
 |

 |

[image: Mathematica Notation] [37] [30]

[image: Traditional Notation] |

 |
 |

 |
 |
 |

 |

 |
 |
 |

 |

[Integer Functions][13][image: >]********[GCD[n 1, n 2,..., n m]][38][image: >] [Specific values][39][image: >] [Specialized values][40] |

 |
 |

 |
 |
 |

 |

**http://functions.wolfram.com/04.08.03.0007.01** |

 |
 |

 |
 |
 |

 |

 |
 |
 |

 |

 |

 |
 |

 |
 |
 |

 |

 |

 |
 |
 |

 |

Input Form |

 |
 |

 |
 |
 |

 |

GCD[2^m - 1, 2^n - 1] == 2^GCD[m, n] - 1 /; Element[m, Integers] && m > 0 && Element[n, Integers] && n > 0

 |

 |
 |

 |
 |
 |

 |

 |
 |
 |

 |

Standard Form |

 |
 |

 |
 |
 |

 |

Cell[BoxData[RowBox[List[RowBox[List[RowBox[List["GCD", "[", RowBox[List[RowBox[List[SuperscriptBox["2", "m"], "-", "1"]], ",", RowBox[List[SuperscriptBox["2", "n"], "-", "1"]]]], "]"]], "\[Equal]", RowBox[List[SuperscriptBox["2", RowBox[List["GCD", "[", RowBox[List["m", ",", "n"]], "]"]]], "-", "1"]]]], "/;", RowBox[List[RowBox[List["m", "\[Element]", "Integers"]], "\[And]", RowBox[List["m", ">", "0"]], "\[And]", RowBox[List["n", "\[Element]", "Integers"]], "\[And]", RowBox[List["n", ">", "0"]]]]]]]]

 |

 |
 |

 |
 |
 |

 |

 |
 |
 |

 |

MathML Form |

 |
 |

 |
 |
 |

 |

[41] |

 |
 |

 |

<math xmlns='http://www.w3.org/1998/Math/MathML' mathematica:form='TraditionalForm' xmlns:mathematica='http://www.wolfram.com/XML/'> <semantics> <mrow> <mrow> <mrow> <mi> gcd </mi> <mo> &#8289; </mo> <mo> ( </mo> <mrow> <mrow> <msup> <mn> 2 </mn> <mi> m </mi> </msup> <mo> - </mo> <mn> 1 </mn> </mrow> <mo> , </mo> <mrow> <msup> <mn> 2 </mn> <mi> n </mi> </msup> <mo> - </mo> <mn> 1 </mn> </mrow> </mrow> <mo> ) </mo> </mrow> <mo> &#10869; </mo> <mrow> <msup> <mn> 2 </mn> <mrow> <mi> gcd </mi> <mo> &#8289; </mo> <mo> ( </mo> <mrow> <mi> m </mi> <mo> , </mo> <mi> n </mi> </mrow> <mo> ) </mo> </mrow> </msup> <mo> - </mo> <mn> 1 </mn> </mrow> </mrow> <mo> /; </mo> <mrow> <mrow> <mi> m </mi> <mo> &#8712; </mo> <msup> <semantics> <mi> &#8469; </mi> <annotation encoding='Mathematica'> TagBox[&quot;\[DoubleStruckCapitalN]&quot;, Function[Integers]] </annotation> </semantics> <mo> + </mo> </msup> </mrow> <mo> &#8743; </mo> <mrow> <mi> n </mi> <mo> &#8712; </mo> <msup> <semantics> <mi> &#8469; </mi> <annotation encoding='Mathematica'> TagBox[&quot;\[DoubleStruckCapitalN]&quot;, Function[Integers]] </annotation> </semantics> <mo> + </mo> </msup> </mrow> </mrow> </mrow> <annotation-xml encoding='MathML-Content'> <apply> <ci> Condition </ci> <apply> <eq /> <apply> <gcd /> <apply> <plus /> <apply> <power /> <cn type='integer'> 2 </cn> <ci> m </ci> </apply> <cn type='integer'> -1 </cn> </apply> <apply> <plus /> <apply> <power /> <cn type='integer'> 2 </cn> <ci> n </ci> </apply> <cn type='integer'> -1 </cn> </apply> </apply> <apply> <plus /> <apply> <power /> <cn type='integer'> 2 </cn> <apply> <gcd /> <ci> m </ci> <ci> n </ci> </apply> </apply> <cn type='integer'> -1 </cn> </apply> </apply> <apply> <and /> <apply> <in /> <ci> m </ci> <apply> <ci> SuperPlus </ci> <integers /> </apply> </apply> <apply> <in /> <ci> n </ci> <apply> <ci> SuperPlus </ci> <integers /> </apply> </apply> </apply> </apply> </annotation-xml> </semantics> </math>

 |

 |
 |

 |
 |
 |

 |

 |
 |
 |

 |

Rule Form |

 |
 |

 |
 |
 |

 |

Cell[BoxData[RowBox[List[RowBox[List["HoldPattern", "[", RowBox[List["GCD", "[", RowBox[List[RowBox[List[SuperscriptBox["2", "m_"], "-", "1"]], ",", RowBox[List[SuperscriptBox["2", "n_"], "-", "1"]]]], "]"]], "]"]], "\[RuleDelayed]", RowBox[List[RowBox[List[SuperscriptBox["2", RowBox[List["GCD", "[", RowBox[List["m", ",", "n"]], "]"]]], "-", "1"]], "/;", RowBox[List[RowBox[List["m", "\[Element]", "Integers"]], "&&", RowBox[List["m", ">", "0"]], "&&", RowBox[List["n", "\[Element]", "Integers"]], "&&", RowBox[List["n", ">", "0"]]]]]]]]]]

 |

 |
 |

 |
 |
 |

 |

 |
 |
 |

 |

Date Added to functions.wolfram.com (modification date) |

 |
 |

 |
 |
 |

 |

2001-10-29

 |

 |
 |

 |
 |
 |

 |  |

 |

 |


## Links

[1]: http://www.wolfram.com/
[2]: /
[3]: http://www.wolfram.com/resources/
[4]: /functions.html
[5]: /visualizations.html
[6]: /Notations/
[7]: /GeneralIdentities/
[8]: /About/
[9]: mailto:comments@functions.wolfram.com
[10]: /ElementaryFunctions/
[11]: /Constants/
[12]: /Bessel-TypeFunctions/
[13]: /IntegerFunctions/
[14]: /Polynomials/
[15]: /GammaBetaErf/
[16]: /HypergeometricFunctions/
[17]: /EllipticIntegrals/
[18]: /EllipticFunctions/
[19]: /ZetaFunctionsandPolylogarithms/
[20]: /MathieuandSpheroidalFunctions/
[21]: /ComplexComponents/
[22]: /NumberTheoryFunctions/
[23]: /GeneralizedFunctions/
[24]: /alphabeticalIndex.html
[25]: /About/mathematica.html
[26]: /About/developers.html
[27]: /About/ourvision.html
[28]: /About/citation.html
[29]: /About/faq.html
[30]: http://reference.wolfram.com/mathematica/ref/GCD.html
[31]: http://mathworld.wolfram.com/GreatestCommonDivisor.html
[32]: /NB/GCD.nb
[33]: /PDF/GCD.pdf
[34]: /introductions/NB/GCD.nb
[35]: /introductions/PDF/GCD.pdf
[36]: http://www.wolfram.com/products/mathematica/trial.cgi
[37]: http://www.wolfram.com
[38]: /IntegerFunctions/GCD
[39]: /IntegerFunctions/GCD/03
[40]: /IntegerFunctions/GCD/03/01
[41]: http://www.mathmlcentral.com/Tools/FromMathMLURL.jsp?url=http://functions.wolfram.com/IntegerFunctions/GCD/03/01/0007/mathml.txt&format=GIF
