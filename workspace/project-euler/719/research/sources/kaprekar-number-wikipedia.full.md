<!-- source: https://en.wikipedia.org/wiki/Kaprekar_number | converted from HTML -->

Kaprekar number - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Base-dependent property of integers

Not to be confused with [Kaprekar's constant][1].

In [mathematics][2], a [natural number][3] in a given [number base][4] is a p {\displaystyle p}[image: {\displaystyle p}] -**Kaprekar number**if the representation of its square in that base can be split into two partitions with the 2nd partition being p {\displaystyle p}[image: {\displaystyle p}] digits in length, that add up to the original number. For example, in [base 10][5], 45 is a 2-Kaprekar number, because 45 2 = 2025, and 20 + 25 = 45. The numbers are named after [D. R. Kaprekar][6].

## Definition and properties

[[edit][7]]

Let n {\displaystyle n}[image: {\displaystyle n}] be a natural number. Then the **Kaprekar function**for base 1"}}'> 1}"> b > 1 {\displaystyle b>1} 1}"/> and power 0"}}'> 0}"> p > 0 {\displaystyle p>0} 0}"/> F p, b: N → N {\displaystyle F_{p,b}:\mathbb {N} \rightarrow \mathbb {N} }[image: {\displaystyle F_{p,b}:\mathbb {N} \rightarrow \mathbb {N} }] is defined to be the following:

F p, b ( n) = α + β {\displaystyle F_{p,b}(n)=\alpha +\beta }[image: {\displaystyle F_{p,b}(n)=\alpha +\beta }],

where β = n 2 mod b p {\displaystyle \beta =n^{2}{\bmod {b}}^{p}}[image: {\displaystyle \beta =n^{2}{\bmod {b}}^{p}}] and

α = n 2 − β b p {\displaystyle \alpha ={\frac {n^{2}-\beta }{b^{p}}}}[image: {\displaystyle \alpha ={\frac {n^{2}-\beta }{b^{p}}}}]

It can also be expressed as:

F p, b ( n) = ⌊ n 2 b p ⌋ ( 1 − b p) + n 2 {\displaystyle F_{p,b}(n)=\left\lfloor {\frac {n^{2}}{b^{p}}}\right\rfloor (1-b^{p})+n^{2}}[image: {\displaystyle F_{p,b}(n)=\left\lfloor {\frac {n^{2}}{b^{p}}}\right\rfloor (1-b^{p})+n^{2}}]

A natural number n {\displaystyle n}[image: {\displaystyle n}] is a p {\displaystyle p}[image: {\displaystyle p}] -**Kaprekar number**if it is a [fixed point][8] for F p, b {\displaystyle F_{p,b}}[image: {\displaystyle F_{p,b}}], which occurs if F p, b ( n) = n {\displaystyle F_{p,b}(n)=n}[image: {\displaystyle F_{p,b}(n)=n}]. 0 {\displaystyle 0}[image: {\displaystyle 0}] and 1 {\displaystyle 1}[image: {\displaystyle 1}] are **trivial Kaprekar numbers**for all b {\displaystyle b}[image: {\displaystyle b}] and p {\displaystyle p}[image: {\displaystyle p}], all other Kaprekar numbers are **nontrivial Kaprekar numbers**.

The earlier example of 45 satisfies this definition with b = 10 {\displaystyle b=10}[image: {\displaystyle b=10}] and p = 2 {\displaystyle p=2}[image: {\displaystyle p=2}], because

β = n 2 mod b p = 45 2 mod 1 0 2 = 25 {\displaystyle \beta =n^{2}{\bmod {b}}^{p}=45^{2}{\bmod {1}}0^{2}=25}[image: {\displaystyle \beta =n^{2}{\bmod {b}}^{p}=45^{2}{\bmod {1}}0^{2}=25}] α = n 2 − β b p = 45 2 − 25 10 2 = 20 {\displaystyle \alpha ={\frac {n^{2}-\beta }{b^{p}}}={\frac {45^{2}-25}{10^{2}}}=20}[image: {\displaystyle \alpha ={\frac {n^{2}-\beta }{b^{p}}}={\frac {45^{2}-25}{10^{2}}}=20}] F 2, 10 ( 45) = α + β = 20 + 25 = 45 {\displaystyle F_{2,10}(45)=\alpha +\beta =20+25=45}[image: {\displaystyle F_{2,10}(45)=\alpha +\beta =20+25=45}]

A natural number n {\displaystyle n}[image: {\displaystyle n}] is a **sociable Kaprekar number**if it is a [periodic point][9] for F p, b {\displaystyle F_{p,b}}[image: {\displaystyle F_{p,b}}], where F p, b k ( n) = n {\displaystyle F_{p,b}^{k}(n)=n}[image: {\displaystyle F_{p,b}^{k}(n)=n}] for a positive [integer][10] k {\displaystyle k}[image: {\displaystyle k}] (where F p, b k {\displaystyle F_{p,b}^{k}}[image: {\displaystyle F_{p,b}^{k}}] is the k {\displaystyle k}[image: {\displaystyle k}] th [iterate][11] of F p, b {\displaystyle F_{p,b}}[image: {\displaystyle F_{p,b}}]), and forms a [cycle][12] of period k {\displaystyle k}[image: {\displaystyle k}]. A Kaprekar number is a sociable Kaprekar number with k = 1 {\displaystyle k=1}[image: {\displaystyle k=1}], and a **amicable Kaprekar number**is a sociable Kaprekar number with k = 2 {\displaystyle k=2}[image: {\displaystyle k=2}].

The number of iterations i {\displaystyle i}[image: {\displaystyle i}] needed for F p, b i ( n) {\displaystyle F_{p,b}^{i}(n)}[image: {\displaystyle F_{p,b}^{i}(n)}] to reach a fixed point is the Kaprekar function's [persistence][13] of n {\displaystyle n}[image: {\displaystyle n}], and undefined if it never reaches a fixed point.

There are only a finite number of p {\displaystyle p}[image: {\displaystyle p}] -Kaprekar numbers and cycles for a given base b {\displaystyle b}[image: {\displaystyle b}], because if n = b p + m {\displaystyle n=b^{p}+m}[image: {\displaystyle n=b^{p}+m}], where 0"}}'> 0}"> m > 0 {\displaystyle m>0} 0}"/> then

n 2 = ( b p + m) 2 = b 2 p + 2 m b p + m 2 = ( b p + 2 m) b p + m 2 {\displaystyle {\begin{aligned}n^{2}&=(b^{p}+m)^{2}\\&=b^{2p}+2mb^{p}+m^{2}\\&=(b^{p}+2m)b^{p}+m^{2}\\\end{aligned}}}[image: {\displaystyle {\begin{aligned}n^{2}&=(b^{p}+m)^{2}\\&=b^{2p}+2mb^{p}+m^{2}\\&=(b^{p}+2m)b^{p}+m^{2}\\\end{aligned}}}]

and β = m 2 {\displaystyle \beta =m^{2}}[image: {\displaystyle \beta =m^{2}}], α = b p + 2 m {\displaystyle \alpha =b^{p}+2m}[image: {\displaystyle \alpha =b^{p}+2m}], and n"}}'> n}"> F p, b ( n) = b p + 2 m + m 2 = n + ( m 2 + m) > n {\displaystyle F_{p,b}(n)=b^{p}+2m+m^{2}=n+(m^{2}+m)>n} n}"/>. Only when n ≤ b p {\displaystyle n\leq b^{p}}[image: {\displaystyle n\leq b^{p}}] do Kaprekar numbers and cycles exist.

If d {\displaystyle d}[image: {\displaystyle d}] is any divisor of p {\displaystyle p}[image: {\displaystyle p}], then n {\displaystyle n}[image: {\displaystyle n}] is also a p {\displaystyle p}[image: {\displaystyle p}] -Kaprekar number for base b p {\displaystyle b^{p}}[image: {\displaystyle b^{p}}].

In base b = 2 {\displaystyle b=2}[image: {\displaystyle b=2}], all even [perfect numbers][14] are Kaprekar numbers. More generally, any numbers of the form 2 n ( 2 n + 1 − 1) {\displaystyle 2^{n}(2^{n+1}-1)}[image: {\displaystyle 2^{n}(2^{n+1}-1)}] or 2 n ( 2 n + 1 + 1) {\displaystyle 2^{n}(2^{n+1}+1)}[image: {\displaystyle 2^{n}(2^{n+1}+1)}] for natural number n {\displaystyle n}[image: {\displaystyle n}] are Kaprekar numbers in [base 2][15].

### Set-theoretic definition and unitary divisors

[[edit][16]]

The set K ( N) {\displaystyle K(N)}[image: {\displaystyle K(N)}] for a given integer N {\displaystyle N}[image: {\displaystyle N}] can be defined as the set of integers X {\displaystyle X}[image: {\displaystyle X}] for which there exist natural numbers A {\displaystyle A}[image: {\displaystyle A}] and B {\displaystyle B}[image: {\displaystyle B}] satisfying the [Diophantine equation][17] [1]

X 2 = A N + B {\displaystyle X^{2}=AN+B}[image: {\displaystyle X^{2}=AN+B}], where 0 ≤ B < N {\displaystyle 0\leq B<N}[image: {\displaystyle 0\leq B<N}] X = A + B {\displaystyle X=A+B}[image: {\displaystyle X=A+B}]

An n {\displaystyle n}[image: {\displaystyle n}] -Kaprekar number for base b {\displaystyle b}[image: {\displaystyle b}] is then one which lies in the set K ( b n) {\displaystyle K(b^{n})}[image: {\displaystyle K(b^{n})}].

It was shown in 2000 [1] that there is a [bijection][18] between the [unitary divisors][19] of N − 1 {\displaystyle N-1}[image: {\displaystyle N-1}] and the set K ( N) {\displaystyle K(N)}[image: {\displaystyle K(N)}] defined above. Let Inv ⁡ ( a, c) {\displaystyle \operatorname {Inv} (a,c)}[image: {\displaystyle \operatorname {Inv} (a,c)}] denote the [multiplicative inverse][20] of a {\displaystyle a}[image: {\displaystyle a}] modulo c {\displaystyle c}[image: {\displaystyle c}], namely the least positive integer m {\displaystyle m}[image: {\displaystyle m}] such that a m = 1 mod c {\displaystyle am=1{\bmod {c}}}[image: {\displaystyle am=1{\bmod {c}}}], and for each unitary divisor d {\displaystyle d}[image: {\displaystyle d}] of N − 1 {\displaystyle N-1}[image: {\displaystyle N-1}] let e = N − 1 d {\displaystyle e={\frac {N-1}{d}}}[image: {\displaystyle e={\frac {N-1}{d}}}] and ζ ( d) = d Inv ( d, e) {\displaystyle \zeta (d)=d\ {\text{Inv}}(d,e)}[image: {\displaystyle \zeta (d)=d\ {\text{Inv}}(d,e)}]. Then the function ζ {\displaystyle \zeta }[image: {\displaystyle \zeta }] is a bijection from the set of unitary divisors of N − 1 {\displaystyle N-1}[image: {\displaystyle N-1}] onto the set K ( N) {\displaystyle K(N)}[image: {\displaystyle K(N)}]. In particular, a number X {\displaystyle X}[image: {\displaystyle X}] is in the set K ( N) {\displaystyle K(N)}[image: {\displaystyle K(N)}] if and only if X = d Inv ( d, e) {\displaystyle X=d\ {\text{Inv}}(d,e)}[image: {\displaystyle X=d\ {\text{Inv}}(d,e)}] for some unitary divisor d {\displaystyle d}[image: {\displaystyle d}] of N − 1 {\displaystyle N-1}[image: {\displaystyle N-1}].

The numbers in K ( N) {\displaystyle K(N)}[image: {\displaystyle K(N)}] occur in complementary pairs, X {\displaystyle X}[image: {\displaystyle X}] and N − X {\displaystyle N-X}[image: {\displaystyle N-X}]. If d {\displaystyle d}[image: {\displaystyle d}] is a unitary divisor of N − 1 {\displaystyle N-1}[image: {\displaystyle N-1}] then so is e = N − 1 d {\displaystyle e={\frac {N-1}{d}}}[image: {\displaystyle e={\frac {N-1}{d}}}], and if X = d Inv ⁡ ( d, e) {\displaystyle X=d\operatorname {Inv} (d,e)}[image: {\displaystyle X=d\operatorname {Inv} (d,e)}] then N − X = e Inv ⁡ ( e, d) {\displaystyle N-X=e\operatorname {Inv} (e,d)}[image: {\displaystyle N-X=e\operatorname {Inv} (e,d)}].

## Kaprekar numbers for F p, b {\displaystyle F_{p,b}}[image: {\displaystyle F_{p,b}}]

[[edit][21]]

### *b*= 4*k*+ 3 and *p*= 2*n*+ 1

[[edit][22]]

Let k {\displaystyle k}[image: {\displaystyle k}] and n {\displaystyle n}[image: {\displaystyle n}] be natural numbers, the number base b = 4 k + 3 = 2 ( 2 k + 1) + 1 {\displaystyle b=4k+3=2(2k+1)+1}[image: {\displaystyle b=4k+3=2(2k+1)+1}], and p = 2 n + 1 {\displaystyle p=2n+1}[image: {\displaystyle p=2n+1}]. Then:

- X 1 = b p − 1 2 = ( 2 k + 1) ∑ i = 0 p − 1 b i {\displaystyle X_{1}={\frac {b^{p}-1}{2}}=(2k+1)\sum _{i=0}^{p-1}b^{i}}[image: {\displaystyle X_{1}={\frac {b^{p}-1}{2}}=(2k+1)\sum _{i=0}^{p-1}b^{i}}] is a Kaprekar number.

\n\\begin{align}\nX_1 & = \\frac{b^p - 1}{2} \\\\\n& = \\frac{b - 1}{2} \\sum_{i = 0}^{p - 1} b^i \\\\\n& = \\frac{4k + 3 - 1}{2} \\sum_{i = 0}^{2n + 1 - 1} b^i \\\\\n& = (2k + 1) \\sum_{i = 0}^{2n} b^i\n\\end{align}\n</math>\n\nThen,\n\n<math>\n\\begin{align}\nX_1^2 & = \\left(\\frac{b^p - 1}{2}\\right)^2 \\\\\n& = \\frac{b^{2p} - 2b^p + 1}{4} \\\\\n& = \\frac{b^p(b^p - 2) + 1}{4} \\\\\n& = \\frac{(4k + 3)^{2n + 1}(b^p - 2) + 1}{4} \\\\\n& = \\frac{(4k + 3)^{2n}(b^p - 2)(4k + 4) - (4k + 3)^{2n}(b^p - 2) + 1}{4} \\\\\n& = \\frac{-(4k + 3)^{2n}(b^p - 2) + 1}{4} + (k + 1)(4k + 3)^{2n}(b^p - 2) \\\\\n& = \\frac{-(4k + 3)^{2n - 1}(b^p - 2)(4k + 4) + (4k + 3)^{2n - 1}(b^p - 2) + 1}{4} + (k + 1)b^{2n}(b^{2n + 1} - 2) \\\\\n& = \\frac{(4k + 3)^{2n - 1}(b^p - 2) + 1}{4} + (k + 1)b^{2n}(b^p - 2) - (k + 1)b^{2n - 1}(b^{2n + 1} - 2) \\\\\n& = \\frac{(4k + 3)^{p - 2}(b^p - 2) + 1}{4} + \\sum_{i = p - 2}^{p - 1} (-1)^i(k + 1)b^i(b^p - 2) \\\\\n& = \\frac{(4k + 3)^{p - 2}(b^p - 2) + 1}{4} + (b^p - 2)(k + 1)\\sum_{i = p - 2}^{p - 1} (-1)^i b^i \\\\\n& = \\frac{(4k + 3)^{1}(b^p - 2) + 1}{4} + (b^p - 2)(k + 1)\\sum_{i = 1}^{p - 1} (-1)^i b^i \\\\\n& = \\frac{-(b^p - 2) + 1}{4} + (b^p - 2)(k + 1)\\sum_{i = 0}^{p - 1} (-1)^i b^i \\\\\n& = (b^p - 2)(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) + \\frac{-b^{2n + 1} + 3}{4} \\\\\n& = (b^p - 2)(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) + \\frac{-4b^{2n + 1} + 3b^{2n + 1} + 3}{4} \\\\\n& = (b^p - 2)(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) - b^p + \\frac{3b^{2n + 1} + 3}{4} \\\\\n& = (b^p - 2)(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) - b^p + \\frac{3(4k + 3)^{p - 2} + 3}{4} + 3(k + 1) \\sum_{i = p - 2}^{p - 1} (-1)^i b^i \\\\\n& = (b^p - 2)(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) - b^p + \\frac{3(4k + 3)^{1} + 3}{4} + 3(k + 1) \\sum_{i = 1}^{p - 1} (-1)^i b^i \\\\\n& = (b^p - 2)(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) - b^p + \\frac{-3 + 3}{4} + 3(k + 1) \\sum_{i = 0}^{p - 1} (-1)^i b^i \\\\\n& = (b^p - 2)(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) + 3(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) - b^p \\\\\n& = (b^p - 2 + 3)(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) - b^p \\\\\n& = (b^p + 1)(k + 1)\\left(\\sum_{i = 0}^{2n} (-1)^i b^i\\right) - b^p \\\\\n& = (b^p + 1)\\left(-1 + (k + 1)\\sum_{i = 0}^{2n} (-1)^i b^i\\right) + 1 \\\\\n& = (b^p + 1)\\left(k + (k + 1)\\sum_{i = 1}^{2n} (-1)^i b^i\\right) + 1 \\\\\n& = (b^p + 1)\\left(k + (k + 1)\\sum_{i = 1}^{n} b^{2i} - b^{2i - 1}\\right) + 1 \\\\\n& = (b^p + 1)\\left(k + (k + 1)\\sum_{i = 1}^{n} (b - 1)b^{2i - 1}\\right) + 1 \\\\\n& = (b^p + 1)\\left(k + \\sum_{i = 1}^{n} ((k + 1)b - k - 1)b^{2i - 1}\\right) + 1 \\\\\n& = (b^p + 1)\\left(k + \\sum_{i = 1}^{n} (kb + (4k + 3) - k - 1)b^{2i - 1}\\right) + 1 \\\\\n& = (b^p + 1)\\left(k + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right) + 1 \\\\\n& = b^p \\left(k + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right) + \\left(k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right)\n\\end{align}\n</math>\n\n\nThe two numbers <math>\\alpha</math> and <math>\\beta</math> are\n: <math>\\beta = X_1^2 \\bmod b^p = k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}</math>\n: <math>\\alpha = \\frac{X_1^2 - \\beta}{b^p} = k + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}</math>\nand their sum is\n\n<math>\n\\begin{align}\n\\alpha + \\beta & = \\left(k + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right) + \\left(k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right) \\\\\n& = 2k + 1 + \\sum_{i = 1}^{n} ((2k)b + 2(3k + 2))b^{2i - 1} \\\\\n& = 2k + 1 + \\sum_{i = 1}^{n} ((2k)b + (6k + 4))b^{2i - 1} \\\\\n& = 2k + 1 + \\sum_{i = 1}^{n} ((2k)b + (4k + 3))b^{2i - 1} + (2k + 1)b^{2i - 1} \\\\\n& = 2k + 1 + \\sum_{i = 1}^{n} ((2k + 1)b)b^{2i - 1} + (2k + 1)b^{2i - 1} \\\\\n& = 2k + 1 + \\sum_{i = 1}^{n} (2k + 1)b^{2i} + (2k + 1)b^{2i - 1} \\\\\n& = 2k + 1 + \\sum_{i = 1}^{2n} (2k + 1)b^{i} \\\\\n& = \\sum_{i = 0}^{2n} (2k + 1)b^{i} \\\\\n& = (2k + 1) \\sum_{i = 0}^{2n} b^i\n& = X_1 \\\\\n\\end{align}\n</math>\n\nThus, <math>X_1</math> is a Kaprekar number."}},"i":0}}]}'>

**Proof**

Let

X 1 = b p − 1 2 = b − 1 2 ∑ i = 0 p − 1 b i = 4 k + 3 − 1 2 ∑ i = 0 2 n + 1 − 1 b i = ( 2 k + 1) ∑ i = 0 2 n b i {\displaystyle {\begin{aligned}X_{1}&={\frac {b^{p}-1}{2}}\\&={\frac {b-1}{2}}\sum _{i=0}^{p-1}b^{i}\\&={\frac {4k+3-1}{2}}\sum _{i=0}^{2n+1-1}b^{i}\\&=(2k+1)\sum _{i=0}^{2n}b^{i}\end{aligned}}}[image: {\displaystyle {\begin{aligned}X_{1}&={\frac {b^{p}-1}{2}}\\&={\frac {b-1}{2}}\sum _{i=0}^{p-1}b^{i}\\&={\frac {4k+3-1}{2}}\sum _{i=0}^{2n+1-1}b^{i}\\&=(2k+1)\sum _{i=0}^{2n}b^{i}\end{aligned}}}]

Then,

X 1 2 = ( b p − 1 2) 2 = b 2 p − 2 b p + 1 4 = b p ( b p − 2) + 1 4 = ( 4 k + 3) 2 n + 1 ( b p − 2) + 1 4 = ( 4 k + 3) 2 n ( b p − 2) ( 4 k + 4) − ( 4 k + 3) 2 n ( b p − 2) + 1 4 = − ( 4 k + 3) 2 n ( b p − 2) + 1 4 + ( k + 1) ( 4 k + 3) 2 n ( b p − 2) = − ( 4 k + 3) 2 n − 1 ( b p − 2) ( 4 k + 4) + ( 4 k + 3) 2 n − 1 ( b p − 2) + 1 4 + ( k + 1) b 2 n ( b 2 n + 1 − 2) = ( 4 k + 3) 2 n − 1 ( b p − 2) + 1 4 + ( k + 1) b 2 n ( b p − 2) − ( k + 1) b 2 n − 1 ( b 2 n + 1 − 2) = ( 4 k + 3) p − 2 ( b p − 2) + 1 4 + ∑ i = p − 2 p − 1 ( − 1) i ( k + 1) b i ( b p − 2) = ( 4 k + 3) p − 2 ( b p − 2) + 1 4 + ( b p − 2) ( k + 1) ∑ i = p − 2 p − 1 ( − 1) i b i = ( 4 k + 3) 1 ( b p − 2) + 1 4 + ( b p − 2) ( k + 1) ∑ i = 1 p − 1 ( − 1) i b i = − ( b p − 2) + 1 4 + ( b p − 2) ( k + 1) ∑ i = 0 p − 1 ( − 1) i b i = ( b p − 2) ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) + − b 2 n + 1 + 3 4 = ( b p − 2) ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) + − 4 b 2 n + 1 + 3 b 2 n + 1 + 3 4 = ( b p − 2) ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) − b p + 3 b 2 n + 1 + 3 4 = ( b p − 2) ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) − b p + 3 ( 4 k + 3) p − 2 + 3 4 + 3 ( k + 1) ∑ i = p − 2 p − 1 ( − 1) i b i = ( b p − 2) ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) − b p + 3 ( 4 k + 3) 1 + 3 4 + 3 ( k + 1) ∑ i = 1 p − 1 ( − 1) i b i = ( b p − 2) ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) − b p + − 3 + 3 4 + 3 ( k + 1) ∑ i = 0 p − 1 ( − 1) i b i = ( b p − 2) ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) + 3 ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) − b p = ( b p − 2 + 3) ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) − b p = ( b p + 1) ( k + 1) ( ∑ i = 0 2 n ( − 1) i b i) − b p = ( b p + 1) ( − 1 + ( k + 1) ∑ i = 0 2 n ( − 1) i b i) + 1 = ( b p + 1) ( k + ( k + 1) ∑ i = 1 2 n ( − 1) i b i) + 1 = ( b p + 1) ( k + ( k + 1) ∑ i = 1 n b 2 i − b 2 i − 1) + 1 = ( b p + 1) ( k + ( k + 1) ∑ i = 1 n ( b − 1) b 2 i − 1) + 1 = ( b p + 1) ( k + ∑ i = 1 n ( ( k + 1) b − k − 1) b 2 i − 1) + 1 = ( b p + 1) ( k + ∑ i = 1 n ( k b + ( 4 k + 3) − k − 1) b 2 i − 1) + 1 = ( b p + 1) ( k + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) + 1 = b p ( k + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) + ( k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) {\displaystyle {\begin{aligned}X_{1}^{2}&=\left({\frac {b^{p}-1}{2}}\right)^{2}\\&={\frac {b^{2p}-2b^{p}+1}{4}}\\&={\frac {b^{p}(b^{p}-2)+1}{4}}\\&={\frac {(4k+3)^{2n+1}(b^{p}-2)+1}{4}}\\&={\frac {(4k+3)^{2n}(b^{p}-2)(4k+4)-(4k+3)^{2n}(b^{p}-2)+1}{4}}\\&={\frac {-(4k+3)^{2n}(b^{p}-2)+1}{4}}+(k+1)(4k+3)^{2n}(b^{p}-2)\\&={\frac {-(4k+3)^{2n-1}(b^{p}-2)(4k+4)+(4k+3)^{2n-1}(b^{p}-2)+1}{4}}+(k+1)b^{2n}(b^{2n+1}-2)\\&={\frac {(4k+3)^{2n-1}(b^{p}-2)+1}{4}}+(k+1)b^{2n}(b^{p}-2)-(k+1)b^{2n-1}(b^{2n+1}-2)\\&={\frac {(4k+3)^{p-2}(b^{p}-2)+1}{4}}+\sum _{i=p-2}^{p-1}(-1)^{i}(k+1)b^{i}(b^{p}-2)\\&={\frac {(4k+3)^{p-2}(b^{p}-2)+1}{4}}+(b^{p}-2)(k+1)\sum _{i=p-2}^{p-1}(-1)^{i}b^{i}\\&={\frac {(4k+3)^{1}(b^{p}-2)+1}{4}}+(b^{p}-2)(k+1)\sum _{i=1}^{p-1}(-1)^{i}b^{i}\\&={\frac {-(b^{p}-2)+1}{4}}+(b^{p}-2)(k+1)\sum _{i=0}^{p-1}(-1)^{i}b^{i}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)+{\frac {-b^{2n+1}+3}{4}}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)+{\frac {-4b^{2n+1}+3b^{2n+1}+3}{4}}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}+{\frac {3b^{2n+1}+3}{4}}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}+{\frac {3(4k+3)^{p-2}+3}{4}}+3(k+1)\sum _{i=p-2}^{p-1}(-1)^{i}b^{i}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}+{\frac {3(4k+3)^{1}+3}{4}}+3(k+1)\sum _{i=1}^{p-1}(-1)^{i}b^{i}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}+{\frac {-3+3}{4}}+3(k+1)\sum _{i=0}^{p-1}(-1)^{i}b^{i}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)+3(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}\\&=(b^{p}-2+3)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}\\&=(b^{p}+1)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}\\&=(b^{p}+1)\left(-1+(k+1)\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)+1\\&=(b^{p}+1)\left(k+(k+1)\sum _{i=1}^{2n}(-1)^{i}b^{i}\right)+1\\&=(b^{p}+1)\left(k+(k+1)\sum _{i=1}^{n}b^{2i}-b^{2i-1}\right)+1\\&=(b^{p}+1)\left(k+(k+1)\sum _{i=1}^{n}(b-1)b^{2i-1}\right)+1\\&=(b^{p}+1)\left(k+\sum _{i=1}^{n}((k+1)b-k-1)b^{2i-1}\right)+1\\&=(b^{p}+1)\left(k+\sum _{i=1}^{n}(kb+(4k+3)-k-1)b^{2i-1}\right)+1\\&=(b^{p}+1)\left(k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+1\\&=b^{p}\left(k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)\end{aligned}}}[image: {\displaystyle {\begin{aligned}X_{1}^{2}&=\left({\frac {b^{p}-1}{2}}\right)^{2}\\&={\frac {b^{2p}-2b^{p}+1}{4}}\\&={\frac {b^{p}(b^{p}-2)+1}{4}}\\&={\frac {(4k+3)^{2n+1}(b^{p}-2)+1}{4}}\\&={\frac {(4k+3)^{2n}(b^{p}-2)(4k+4)-(4k+3)^{2n}(b^{p}-2)+1}{4}}\\&={\frac {-(4k+3)^{2n}(b^{p}-2)+1}{4}}+(k+1)(4k+3)^{2n}(b^{p}-2)\\&={\frac {-(4k+3)^{2n-1}(b^{p}-2)(4k+4)+(4k+3)^{2n-1}(b^{p}-2)+1}{4}}+(k+1)b^{2n}(b^{2n+1}-2)\\&={\frac {(4k+3)^{2n-1}(b^{p}-2)+1}{4}}+(k+1)b^{2n}(b^{p}-2)-(k+1)b^{2n-1}(b^{2n+1}-2)\\&={\frac {(4k+3)^{p-2}(b^{p}-2)+1}{4}}+\sum _{i=p-2}^{p-1}(-1)^{i}(k+1)b^{i}(b^{p}-2)\\&={\frac {(4k+3)^{p-2}(b^{p}-2)+1}{4}}+(b^{p}-2)(k+1)\sum _{i=p-2}^{p-1}(-1)^{i}b^{i}\\&={\frac {(4k+3)^{1}(b^{p}-2)+1}{4}}+(b^{p}-2)(k+1)\sum _{i=1}^{p-1}(-1)^{i}b^{i}\\&={\frac {-(b^{p}-2)+1}{4}}+(b^{p}-2)(k+1)\sum _{i=0}^{p-1}(-1)^{i}b^{i}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)+{\frac {-b^{2n+1}+3}{4}}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)+{\frac {-4b^{2n+1}+3b^{2n+1}+3}{4}}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}+{\frac {3b^{2n+1}+3}{4}}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}+{\frac {3(4k+3)^{p-2}+3}{4}}+3(k+1)\sum _{i=p-2}^{p-1}(-1)^{i}b^{i}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}+{\frac {3(4k+3)^{1}+3}{4}}+3(k+1)\sum _{i=1}^{p-1}(-1)^{i}b^{i}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}+{\frac {-3+3}{4}}+3(k+1)\sum _{i=0}^{p-1}(-1)^{i}b^{i}\\&=(b^{p}-2)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)+3(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}\\&=(b^{p}-2+3)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}\\&=(b^{p}+1)(k+1)\left(\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)-b^{p}\\&=(b^{p}+1)\left(-1+(k+1)\sum _{i=0}^{2n}(-1)^{i}b^{i}\right)+1\\&=(b^{p}+1)\left(k+(k+1)\sum _{i=1}^{2n}(-1)^{i}b^{i}\right)+1\\&=(b^{p}+1)\left(k+(k+1)\sum _{i=1}^{n}b^{2i}-b^{2i-1}\right)+1\\&=(b^{p}+1)\left(k+(k+1)\sum _{i=1}^{n}(b-1)b^{2i-1}\right)+1\\&=(b^{p}+1)\left(k+\sum _{i=1}^{n}((k+1)b-k-1)b^{2i-1}\right)+1\\&=(b^{p}+1)\left(k+\sum _{i=1}^{n}(kb+(4k+3)-k-1)b^{2i-1}\right)+1\\&=(b^{p}+1)\left(k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+1\\&=b^{p}\left(k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)\end{aligned}}}]

The two numbers α {\displaystyle \alpha }[image: {\displaystyle \alpha }] and β {\displaystyle \beta }[image: {\displaystyle \beta }] are

β = X 1 2 mod b p = k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1 {\displaystyle \beta =X_{1}^{2}{\bmod {b}}^{p}=k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}}[image: {\displaystyle \beta =X_{1}^{2}{\bmod {b}}^{p}=k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}}] α = X 1 2 − β b p = k + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1 {\displaystyle \alpha ={\frac {X_{1}^{2}-\beta }{b^{p}}}=k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}}[image: {\displaystyle \alpha ={\frac {X_{1}^{2}-\beta }{b^{p}}}=k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}}]

and their sum is

α + β = ( k + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) + ( k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) = 2 k + 1 + ∑ i = 1 n ( ( 2 k) b + 2 ( 3 k + 2)) b 2 i − 1 = 2 k + 1 + ∑ i = 1 n ( ( 2 k) b + ( 6 k + 4)) b 2 i − 1 = 2 k + 1 + ∑ i = 1 n ( ( 2 k) b + ( 4 k + 3)) b 2 i − 1 + ( 2 k + 1) b 2 i − 1 = 2 k + 1 + ∑ i = 1 n ( ( 2 k + 1) b) b 2 i − 1 + ( 2 k + 1) b 2 i − 1 = 2 k + 1 + ∑ i = 1 n ( 2 k + 1) b 2 i + ( 2 k + 1) b 2 i − 1 = 2 k + 1 + ∑ i = 1 2 n ( 2 k + 1) b i = ∑ i = 0 2 n ( 2 k + 1) b i = ( 2 k + 1) ∑ i = 0 2 n b i = X 1 {\displaystyle {\begin{aligned}\alpha +\beta &=\left(k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)\\&=2k+1+\sum _{i=1}^{n}((2k)b+2(3k+2))b^{2i-1}\\&=2k+1+\sum _{i=1}^{n}((2k)b+(6k+4))b^{2i-1}\\&=2k+1+\sum _{i=1}^{n}((2k)b+(4k+3))b^{2i-1}+(2k+1)b^{2i-1}\\&=2k+1+\sum _{i=1}^{n}((2k+1)b)b^{2i-1}+(2k+1)b^{2i-1}\\&=2k+1+\sum _{i=1}^{n}(2k+1)b^{2i}+(2k+1)b^{2i-1}\\&=2k+1+\sum _{i=1}^{2n}(2k+1)b^{i}\\&=\sum _{i=0}^{2n}(2k+1)b^{i}\\&=(2k+1)\sum _{i=0}^{2n}b^{i}&=X_{1}\\\end{aligned}}}[image: {\displaystyle {\begin{aligned}\alpha +\beta &=\left(k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)\\&=2k+1+\sum _{i=1}^{n}((2k)b+2(3k+2))b^{2i-1}\\&=2k+1+\sum _{i=1}^{n}((2k)b+(6k+4))b^{2i-1}\\&=2k+1+\sum _{i=1}^{n}((2k)b+(4k+3))b^{2i-1}+(2k+1)b^{2i-1}\\&=2k+1+\sum _{i=1}^{n}((2k+1)b)b^{2i-1}+(2k+1)b^{2i-1}\\&=2k+1+\sum _{i=1}^{n}(2k+1)b^{2i}+(2k+1)b^{2i-1}\\&=2k+1+\sum _{i=1}^{2n}(2k+1)b^{i}\\&=\sum _{i=0}^{2n}(2k+1)b^{i}\\&=(2k+1)\sum _{i=0}^{2n}b^{i}&=X_{1}\\\end{aligned}}}]

Thus, X 1 {\displaystyle X_{1}}[image: {\displaystyle X_{1}}] is a Kaprekar number.

- X 2 = b p + 1 2 = X 1 + 1 {\displaystyle X_{2}={\frac {b^{p}+1}{2}}=X_{1}+1}[image: {\displaystyle X_{2}={\frac {b^{p}+1}{2}}=X_{1}+1}] is a Kaprekar number for all natural numbers n {\displaystyle n}[image: {\displaystyle n}].

\n\\begin{align}\nX_2 & = \\frac{b^{2n + 1} + 1}{2} \\\\\n& = \\frac{b^{2n + 1} - 1}{2} + 1 \\\\\n& = X_1 + 1\n\\end{align}\n</math>\n\nThen,\n\n<math>\n\\begin{align}\nX_2^2 & = (X_1 + 1)^2 \\\\\n& = X_1^2 + 2 X_1 + 1 \\\\\n& = X_1^2 + 2 X_1 + 1 \\\\\n& = b^p \\left(k + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right) + \\left(k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right) + b^p - 1 + 1 \\\\\n& = b^p \\left(k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right) + \\left(k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right)\n\\end{align}\n</math>\n\nThe two numbers <math>\\alpha</math> and <math>\\beta</math> are\n: <math>\\beta = X_2^2 \\bmod b^p = k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}</math>\n: <math>\\alpha = \\frac{X_2^2 - \\beta}{b^p} = k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}</math>\nand their sum is\n\n<math>\n\\begin{align}\n\\alpha + \\beta & = \\left(k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right) + \\left(k + 1 + \\sum_{i = 1}^{n} (kb + (3k + 2))b^{2i - 1}\\right) \\\\\n& = 2k + 2 + \\sum_{i = 1}^{n} ((2k)b + 2(3k + 2))b^{2i - 1} \\\\\n& = 2k + 2 + \\sum_{i = 1}^{n} ((2k)b + (6k + 4))b^{2i - 1} \\\\\n& = 2k + 2 + \\sum_{i = 1}^{n} ((2k)b + (4k + 3))b^{2i - 1} + (2k + 1)b^{2i - 1} \\\\\n& = 2k + 2 + \\sum_{i = 1}^{n} ((2k + 1)b)b^{2i - 1} + (2k + 1)b^{2i - 1} \\\\\n& = 2k + 2 + \\sum_{i = 1}^{n} (2k + 1)b^{2i} + (2k + 1)b^{2i - 1} \\\\\n& = 2k + 2 + \\sum_{i = 1}^{2n} (2k + 1)b^{i} \\\\\n& = 1 + \\sum_{i = 0}^{2n} (2k + 1)b^{i} \\\\\n& = 1 + (2k + 1) \\sum_{i = 0}^{2n} b^{i} \\\\\n& = 1 + X_1 \\\\\n& = X_2\n\\end{align}\n</math>\n\nThus, <math>X_2</math> is a Kaprekar number."}},"i":0}}]}'>

**Proof**

Let

X 2 = b 2 n + 1 + 1 2 = b 2 n + 1 − 1 2 + 1 = X 1 + 1 {\displaystyle {\begin{aligned}X_{2}&={\frac {b^{2n+1}+1}{2}}\\&={\frac {b^{2n+1}-1}{2}}+1\\&=X_{1}+1\end{aligned}}}[image: {\displaystyle {\begin{aligned}X_{2}&={\frac {b^{2n+1}+1}{2}}\\&={\frac {b^{2n+1}-1}{2}}+1\\&=X_{1}+1\end{aligned}}}]

Then,

X 2 2 = ( X 1 + 1) 2 = X 1 2 + 2 X 1 + 1 = X 1 2 + 2 X 1 + 1 = b p ( k + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) + ( k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) + b p − 1 + 1 = b p ( k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) + ( k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) {\displaystyle {\begin{aligned}X_{2}^{2}&=(X_{1}+1)^{2}\\&=X_{1}^{2}+2X_{1}+1\\&=X_{1}^{2}+2X_{1}+1\\&=b^{p}\left(k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+b^{p}-1+1\\&=b^{p}\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)\end{aligned}}}[image: {\displaystyle {\begin{aligned}X_{2}^{2}&=(X_{1}+1)^{2}\\&=X_{1}^{2}+2X_{1}+1\\&=X_{1}^{2}+2X_{1}+1\\&=b^{p}\left(k+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+b^{p}-1+1\\&=b^{p}\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)\end{aligned}}}]

The two numbers α {\displaystyle \alpha }[image: {\displaystyle \alpha }] and β {\displaystyle \beta }[image: {\displaystyle \beta }] are

β = X 2 2 mod b p = k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1 {\displaystyle \beta =X_{2}^{2}{\bmod {b}}^{p}=k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}}[image: {\displaystyle \beta =X_{2}^{2}{\bmod {b}}^{p}=k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}}] α = X 2 2 − β b p = k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1 {\displaystyle \alpha ={\frac {X_{2}^{2}-\beta }{b^{p}}}=k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}}[image: {\displaystyle \alpha ={\frac {X_{2}^{2}-\beta }{b^{p}}}=k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}}]

and their sum is

α + β = ( k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) + ( k + 1 + ∑ i = 1 n ( k b + ( 3 k + 2)) b 2 i − 1) = 2 k + 2 + ∑ i = 1 n ( ( 2 k) b + 2 ( 3 k + 2)) b 2 i − 1 = 2 k + 2 + ∑ i = 1 n ( ( 2 k) b + ( 6 k + 4)) b 2 i − 1 = 2 k + 2 + ∑ i = 1 n ( ( 2 k) b + ( 4 k + 3)) b 2 i − 1 + ( 2 k + 1) b 2 i − 1 = 2 k + 2 + ∑ i = 1 n ( ( 2 k + 1) b) b 2 i − 1 + ( 2 k + 1) b 2 i − 1 = 2 k + 2 + ∑ i = 1 n ( 2 k + 1) b 2 i + ( 2 k + 1) b 2 i − 1 = 2 k + 2 + ∑ i = 1 2 n ( 2 k + 1) b i = 1 + ∑ i = 0 2 n ( 2 k + 1) b i = 1 + ( 2 k + 1) ∑ i = 0 2 n b i = 1 + X 1 = X 2 {\displaystyle {\begin{aligned}\alpha +\beta &=\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)\\&=2k+2+\sum _{i=1}^{n}((2k)b+2(3k+2))b^{2i-1}\\&=2k+2+\sum _{i=1}^{n}((2k)b+(6k+4))b^{2i-1}\\&=2k+2+\sum _{i=1}^{n}((2k)b+(4k+3))b^{2i-1}+(2k+1)b^{2i-1}\\&=2k+2+\sum _{i=1}^{n}((2k+1)b)b^{2i-1}+(2k+1)b^{2i-1}\\&=2k+2+\sum _{i=1}^{n}(2k+1)b^{2i}+(2k+1)b^{2i-1}\\&=2k+2+\sum _{i=1}^{2n}(2k+1)b^{i}\\&=1+\sum _{i=0}^{2n}(2k+1)b^{i}\\&=1+(2k+1)\sum _{i=0}^{2n}b^{i}\\&=1+X_{1}\\&=X_{2}\end{aligned}}}[image: {\displaystyle {\begin{aligned}\alpha +\beta &=\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)+\left(k+1+\sum _{i=1}^{n}(kb+(3k+2))b^{2i-1}\right)\\&=2k+2+\sum _{i=1}^{n}((2k)b+2(3k+2))b^{2i-1}\\&=2k+2+\sum _{i=1}^{n}((2k)b+(6k+4))b^{2i-1}\\&=2k+2+\sum _{i=1}^{n}((2k)b+(4k+3))b^{2i-1}+(2k+1)b^{2i-1}\\&=2k+2+\sum _{i=1}^{n}((2k+1)b)b^{2i-1}+(2k+1)b^{2i-1}\\&=2k+2+\sum _{i=1}^{n}(2k+1)b^{2i}+(2k+1)b^{2i-1}\\&=2k+2+\sum _{i=1}^{2n}(2k+1)b^{i}\\&=1+\sum _{i=0}^{2n}(2k+1)b^{i}\\&=1+(2k+1)\sum _{i=0}^{2n}b^{i}\\&=1+X_{1}\\&=X_{2}\end{aligned}}}]

Thus, X 2 {\displaystyle X_{2}}[image: {\displaystyle X_{2}}] is a Kaprekar number.

### *b*= *m*2*k*+ *m*+ 1 and *p*= *mn*+ 1

[[edit][23]]

Let m {\displaystyle m}[image: {\displaystyle m}], k {\displaystyle k}[image: {\displaystyle k}], and n {\displaystyle n}[image: {\displaystyle n}] be natural numbers, the number base b = m 2 k + m + 1 {\displaystyle b=m^{2}k+m+1}[image: {\displaystyle b=m^{2}k+m+1}], and the power p = m n + 1 {\displaystyle p=mn+1}[image: {\displaystyle p=mn+1}]. Then:

- X 1 = b p − 1 m = ( m k + 1) ∑ i = 0 p − 1 b i {\displaystyle X_{1}={\frac {b^{p}-1}{m}}=(mk+1)\sum _{i=0}^{p-1}b^{i}}[image: {\displaystyle X_{1}={\frac {b^{p}-1}{m}}=(mk+1)\sum _{i=0}^{p-1}b^{i}}] is a Kaprekar number.
- X 2 = b p + m − 1 m = X 1 + 1 {\displaystyle X_{2}={\frac {b^{p}+m-1}{m}}=X_{1}+1}[image: {\displaystyle X_{2}={\frac {b^{p}+m-1}{m}}=X_{1}+1}] is a Kaprekar number.

### *b*= *m*2*k*+ *m*+ 1 and *p*= *mn*+ *m*− 1

[[edit][24]]

Let m {\displaystyle m}[image: {\displaystyle m}], k {\displaystyle k}[image: {\displaystyle k}], and n {\displaystyle n}[image: {\displaystyle n}] be natural numbers, the number base b = m 2 k + m + 1 {\displaystyle b=m^{2}k+m+1}[image: {\displaystyle b=m^{2}k+m+1}], and the power p = m n + m − 1 {\displaystyle p=mn+m-1}[image: {\displaystyle p=mn+m-1}]. Then:

- X 1 = m ( b p − 1) 4 = ( m − 1) ( m k + 1) ∑ i = 0 p − 1 b i {\displaystyle X_{1}={\frac {m(b^{p}-1)}{4}}=(m-1)(mk+1)\sum _{i=0}^{p-1}b^{i}}[image: {\displaystyle X_{1}={\frac {m(b^{p}-1)}{4}}=(m-1)(mk+1)\sum _{i=0}^{p-1}b^{i}}] is a Kaprekar number.
- X 2 = m b p + 1 4 = X 3 + 1 {\displaystyle X_{2}={\frac {mb^{p}+1}{4}}=X_{3}+1}[image: {\displaystyle X_{2}={\frac {mb^{p}+1}{4}}=X_{3}+1}] is a Kaprekar number.

### *b*= *m*2*k*+ *m*2 − *m*+ 1 and *p*= *mn*+ 1

[[edit][25]]

Let m {\displaystyle m}[image: {\displaystyle m}], k {\displaystyle k}[image: {\displaystyle k}], and n {\displaystyle n}[image: {\displaystyle n}] be natural numbers, the number base b = m 2 k + m 2 − m + 1 {\displaystyle b=m^{2}k+m^{2}-m+1}[image: {\displaystyle b=m^{2}k+m^{2}-m+1}], and the power p = m n + m − 1 {\displaystyle p=mn+m-1}[image: {\displaystyle p=mn+m-1}]. Then:

- X 1 = ( m − 1) ( b p − 1) m = ( m − 1) ( m k + 1) ∑ i = 0 p − 1 b i {\displaystyle X_{1}={\frac {(m-1)(b^{p}-1)}{m}}=(m-1)(mk+1)\sum _{i=0}^{p-1}b^{i}}[image: {\displaystyle X_{1}={\frac {(m-1)(b^{p}-1)}{m}}=(m-1)(mk+1)\sum _{i=0}^{p-1}b^{i}}] is a Kaprekar number.
- X 2 = ( m − 1) b p + 1 m = X 1 + 1 {\displaystyle X_{2}={\frac {(m-1)b^{p}+1}{m}}=X_{1}+1}[image: {\displaystyle X_{2}={\frac {(m-1)b^{p}+1}{m}}=X_{1}+1}] is a Kaprekar number.

### *b*= *m*2*k*+ *m*2 − *m*+ 1 and *p*= *mn*+ *m*− 1

[[edit][26]]

Let m {\displaystyle m}[image: {\displaystyle m}], k {\displaystyle k}[image: {\displaystyle k}], and n {\displaystyle n}[image: {\displaystyle n}] be natural numbers, the number base b = m 2 k + m 2 − m + 1 {\displaystyle b=m^{2}k+m^{2}-m+1}[image: {\displaystyle b=m^{2}k+m^{2}-m+1}], and the power p = m n + m − 1 {\displaystyle p=mn+m-1}[image: {\displaystyle p=mn+m-1}]. Then:

- X 1 = b p − 1 m = ( m k + 1) ∑ i = 0 p − 1 b i {\displaystyle X_{1}={\frac {b^{p}-1}{m}}=(mk+1)\sum _{i=0}^{p-1}b^{i}}[image: {\displaystyle X_{1}={\frac {b^{p}-1}{m}}=(mk+1)\sum _{i=0}^{p-1}b^{i}}] is a Kaprekar number.
- X 2 = b p + m − 1 m = X 3 + 1 {\displaystyle X_{2}={\frac {b^{p}+m-1}{m}}=X_{3}+1}[image: {\displaystyle X_{2}={\frac {b^{p}+m-1}{m}}=X_{3}+1}] is a Kaprekar number.

## Kaprekar numbers and cycles of F p, b {\displaystyle F_{p,b}}[image: {\displaystyle F_{p,b}}] for specific p {\displaystyle p}[image: {\displaystyle p}], b {\displaystyle b}[image: {\displaystyle b}]

[[edit][27]]

All numbers are in base b {\displaystyle b}[image: {\displaystyle b}].

Base b {\displaystyle b}[image: {\displaystyle b}] | Power p {\displaystyle p}[image: {\displaystyle p}] | Nontrivial Kaprekar numbers n ≠ 0 {\displaystyle n\neq 0}[image: {\displaystyle n\neq 0}], n ≠ 1 {\displaystyle n\neq 1}[image: {\displaystyle n\neq 1}] | Cycles |

[2][28] | 1 | 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

[3][29] | 1 | 2, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

[4][30] | 1 | 3, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

[5][31] | 1 | 4, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

[6][32] | 1 | 5, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

7 | 1 | 3, 4, 6, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

[8][33] | 1 | 7, 10 | 2 → 4 → 2 |

[9][34] | 1 | 8, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

[10][35] | 1 | 9, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

11 | 1 | 5, 6, A, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

[12][36] | 1 | B, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

13 | 1 | 4, 9, C, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

14 | 1 | D, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

15 | 1 | 7, 8, E, 10 |

2 → 4 → 2

9 → B → 9

 |

[16][37] | 1 | 6, A, F, 10 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

2 | 2 | 11 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

3 | 2 | 22, 100 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

4 | 2 | 12, 22, 33, 100 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

5 | 2 | 14, 31, 44, 100 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

6 | 2 | 23, 33, 55, 100 |

15 → 24 → 15

41 → 50 → 41

 |

7 | 2 | 22, 45, 66, 100 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

8 | 2 | 34, 44, 77, 100 |

4 → 20 → 4

11 → 22 → 11

45 → 56 → 45

 |

2 | 3 | 111, 1000 | 10 → 100 → 10 |

3 | 3 | 111, 112, 222, 1000 | 10 → 100 → 10 |

2 | 4 | 110, 1010, 1111, 10000 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

3 | 4 | 121, 2102, 2222, 10000 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

2 | 5 | 11111, 100000 |

10 → 100 → 10000 → 1000 → 10

111 → 10010 → 1110 → 1010 → 111

 |

3 | 5 | 11111, 22222, 100000 | 10 → 100 → 10000 → 1000 → 10 |

2 | 6 | 11100, 100100, 111111, 1000000 |

100 → 10000 → 100

1001 → 10010 → 1001

100101 → 101110 → 100101

 |

3 | 6 | 10220, 20021, 101010, 121220, 202202, 212010, 222222, 1000000 |

100 → 10000 → 100

122012 → 201212 → 122012

 |

2 | 7 | 1111111, 10000000 |

10 → 100 → 10000 → 10

1000 → 1000000 → 100000 → 1000

100110 → 101111 → 110010 → 1010111 → 1001100 → 111101 → 100110

 |

3 | 7 | 1111111, 1111112, 2222222, 10000000 |

10 → 100 → 10000 → 10

1000 → 1000000 → 100000 → 1000

1111121 → 1111211 → 1121111 → 1111121

 |

2 | 8 | 1010101, 1111000, 10001000, 10101011, 11001101, 11111111, 100000000 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

3 | 8 | 2012021, 10121020, 12101210, 21121001, 20210202, 22222222, 100000000 | ∅ {\displaystyle \varnothing }[image: {\displaystyle \varnothing }] |

2 | 9 | 10010011, 101101101, 111111111, 1000000000 |

10 → 100 → 10000 → 100000000 → 10000000 → 100000 → 10

1000 → 1000000 → 1000

10011010 → 11010010 → 10011010

 |

## Extension to negative integers

[[edit][38]]

Kaprekar numbers can be extended to the negative integers by use of a [signed-digit representation][39] to represent each integer.

## See also

[[edit][40]]

- [Arithmetic dynamics][41]
- [Automorphic number][42]
- [Dudeney number][43]
- [Factorion][44]
- [Happy number][45]
- [Kaprekar's constant][46]
- [Meertens number][47]
- [Narcissistic number][48]
- [Perfect digit-to-digit invariant][49]
- [Perfect digital invariant][50]
- [Sum-product number][51]

## Notes

[[edit][52]]

1. 1 2 Iannucci ( 2000)

## References

[[edit][53]]

- D. R. Kaprekar (1980–1981). "On Kaprekar numbers". *[Journal of Recreational Mathematics][54]*. **13**: 81– 82.
- M. Charosh (1981–1982). "Some Applications of Casting Out 999...'s". *[Journal of Recreational Mathematics][54]*. **14**: 111– 118.
- Iannucci, Douglas E. (2000). ["The Kaprekar Numbers"][55]. *[Journal of Integer Sequences][56]*. **3**: 00.1.2. [Bibcode][57]: [2000JIntS...3...12I][58].

- [v][59]
- [t][60]
- [e][61]

Classes of [natural numbers][3]

 |

[Powers][62] and related numbers

 |

- [Achilles][63]
- [Power of 2][64]
- [Power of 3][65]
- [Power of 10][66]
- [Square][67]
- [Cube][68]
- [Fourth power][69]
- [Fifth power][70]
- [Sixth power][71]
- [Seventh power][72]
- [Eighth power][73]
- [Perfect power][74]
- [Powerful][75]
- [Prime power][76]

 |

 |

Of the form *a*× 2*b*± 1

 |

- [Cullen][77]
- [Double Mersenne][78]
- [Fermat][79]
- [Mersenne][80]
- [Proth][81]
- [Thabit][82]
- [Woodall][83]

 |

 |

Other polynomial numbers

 |

- [Hilbert][84]
- [Idoneal][85]
- [Leyland][86]
- [Loeschian][87]
- [Lucky numbers of Euler][88]

 |

 |

[Recursively][89] defined numbers

 |

- [Fibonacci][90]
- [Jacobsthal][91]
- [Leonardo][92]
- [Lucas][93]
- [Narayana][94]
- [Padovan][95]
- [Pell][96]
- [Perrin][97]
- [Graham][98]

 |

 |

Possessing a specific set of other numbers

 |

- [Amenable][99]
- [Congruent][100]
- [Knödel][101]
- [Riesel][102]
- [Sierpiński][103]

 |

 |

Expressible via specific sums

 |

- [Nonhypotenuse][104]
- [Polite][105]
- [Practical][106]
- [Primary pseudoperfect][107]
- [Ulam][108]
- [Wolstenholme][109]

 |

 |

[Figurate numbers][110]

 |

[2-dimensional][111] |

[centered][112] |

- [Centered triangular][113]
- [Centered square][114]
- [Centered pentagonal][115]
- [Centered hexagonal][116]
- [Centered heptagonal][117]
- [Centered octagonal][118]
- [Centered nonagonal][119]
- [Centered decagonal][120]
- [Star][121]

 |

[non-centered][122] |

- [Triangular][123]
- [Square][67]
- [Square triangular][124]
- [Pentagonal][125]
- [Hexagonal][126]
- [Heptagonal][127]
- [Octagonal][128]
- [Nonagonal][129]
- [Decagonal][130]
- [Dodecagonal][131]

 |

 |

[3-dimensional][132] |

[centered][133] |

- [Centered tetrahedral][134]
- [Centered cube][135]
- [Centered octahedral][136]
- [Centered dodecahedral][137]
- [Centered icosahedral][138]

 |

[non-centered][139] |

- [Tetrahedral][140]
- [Cubic][68]
- [Octahedral][141]
- [Dodecahedral][142]
- [Icosahedral][143]
- [Stella octangula][144]

 |

[pyramidal][145] |

- [Square pyramidal][146]

 |

 |

[4-dimensional][147] |

non-centered |

- [Pentatope][148]
- [Squared triangular][149]
- [Tesseractic][69]

 |

 |

 |

 |

Combinatorial numbers

 |

- [Bell][150]
- [Cake][151]
- [Catalan][152]
- [Dedekind][153]
- [Delannoy][154]
- [Euler][155]
- [Eulerian][156]
- [Fuss–Catalan][157]
- [Lah][158]
- [Lazy caterer's sequence][159]
- [Lobb][160]
- [Motzkin][161]
- [Narayana][162]
- [Ordered Bell][163]
- [Schröder][164]
- [Schröder–Hipparchus][165]
- [Stirling first][166]
- [Stirling second][167]
- [Telephone number][168]
- [Wedderburn–Etherington][169]

 |

 |

[Primes][170]

 |

- [Wieferich][171]
- [Wall–Sun–Sun][172]
- [Wolstenholme prime][173]
- [Wilson][174]

 |

 |

[Pseudoprimes][175]

 |

- [Carmichael number][176]
- [Catalan pseudoprime][177]
- [Elliptic pseudoprime][178]
- [Euler pseudoprime][179]
- [Euler–Jacobi pseudoprime][180]
- [Fermat pseudoprime][181]
- [Frobenius pseudoprime][182]
- [Lucas pseudoprime][183]
- [Lucas–Carmichael number][184]
- [Perrin pseudoprime][185]
- [Somer–Lucas pseudoprime][186]
- [Strong pseudoprime][187]

 |

 |

[Arithmetic functions][188] and [dynamics][189]

 |

[Divisor functions][190] |

- [Abundant][191]
- [Almost perfect][192]
- [Arithmetic][193]
- [Betrothed][194]
- [Colossally abundant][195]
- [Deficient][196]
- [Descartes][197]
- [Hemiperfect][198]
- [Highly abundant][199]
- [Highly composite][200]
- [Hyperperfect][201]
- [Multiply perfect][202]
- [Perfect][14]
- [Practical][106]
- [Primitive abundant][203]
- [Quasiperfect][204]
- [Refactorable][205]
- [Semiperfect][206]
- [Sublime][207]
- [Superabundant][208]
- [Superior highly composite][209]
- [Superperfect][210]

 |

[Prime omega functions][211] |

- [Almost prime][212]
- [Semiprime][213]

 |

[Euler's totient function][214] |

- [Highly cototient][215]
- [Highly totient][216]
- [Noncototient][217]
- [Nontotient][218]
- [Perfect totient][219]
- [Sparsely totient][220]

 |

[Aliquot sequences][221] |

- [Amicable][222]
- [Perfect][14]
- [Sociable][223]
- [Untouchable][224]

 |

[Primorial][225] |

- [Euclid][226]
- [Fortunate][227]

 |

 |

 |

Other [prime factor][228] or [divisor][229] related numbers

 |

- [Blum][230]
- [Cyclic][231]
- [Erdős–Nicolas][232]
- [Erdős–Woods][233]
- [Friendly][234]
- [Giuga][235]
- [Harmonic divisor][236]
- [Jordan–Pólya][237]
- [Lucas–Carmichael][184]
- [Pronic][238]
- [Regular][239]
- [Rough][240]
- [Smooth][241]
- [Sphenic][242]
- [Størmer][243]
- [Super-Poulet][244]

 |

 |

[Numeral system][245] -dependent numbers

 |

[Arithmetic functions][188]
and [dynamics][189] |

- [Persistence][13]

  - [Additive][246]
  - [Multiplicative][247]

[Digit sum][248] |

- [Digit sum][248]
- [Digital root][249]
- [Self][250]
- [Sum-product][51]

 |

Digit product |

- [Multiplicative digital root][251]
- [Sum-product][51]

 |

Coding-related |

- [Meertens][47]

 |

Other |

- [Dudeney][43]
- [Factorion][44]
- [Kaprekar][252]
- [Kaprekar's constant][46]
- [Keith][253]
- [Lychrel][254]
- [Narcissistic][48]
- [Perfect digit-to-digit invariant][49]
- [Perfect digital invariant][50]

  - [Happy][45]

 |

 |

[P-adic numbers][255] -related |

- [Automorphic][42]

  - [Trimorphic][256]

 |

[Digit][257] -composition related |

- [Palindromic][258]
- [Pandigital][259]
- [Repdigit][260]
- [Repunit][261]
- [Self-descriptive][262]
- [Smarandache–Wellin][263]
- [Undulating][264]

 |

Digit- [permutation][265] related |

- [Cyclic][266]
- [Digit-reassembly][267]
- [Parasitic][268]
- [Primeval][269]
- [Transposable][270]

 |

Divisor-related |

- [Equidigital][271]
- [Extravagant][272]
- [Frugal][273]
- [Harshad][274]
- [Polydivisible][275]
- [Smith][276]
- [Vampire][277]

 |

Other |

- [Friedman][278]

 |

 |

 |

[Binary numbers][279]

 |

- [Evil][280]
- [Odious][281]
- [Pernicious][282]

 |

 |

Generated via a [sieve][283]

 |

- [Lucky][284]
- [Prime][285]

 |

 |

[Sorting][286] related

 |

- [Pancake number][287]
- [Sorting number][288]

 |

 |

[Natural language][289] related

 |

- [Aronson's sequence][290]
- [Ban][291]

 |

 |

[Graphemics][292] related

 |

- [Strobogrammatic][293]

 |

 |

- [294] [Mathematics portal][295]

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Kaprekar_number&oldid=1368200114][296] "

[Categories][297]:

- [Arithmetic dynamics][298]
- [Base-dependent integer sequences][299]
- [Diophantine equations][300]
- [Number theory][301]
- [Indian inventions][302]

Hidden categories:

- [Articles with short description][303]
- [Short description is different from Wikidata][304]

Search

Kaprekar number

24 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Kaprekar's_constant
[2]: https://en.wikipedia.org/wiki/Mathematics
[3]: https://en.wikipedia.org/wiki/Natural_number
[4]: https://en.wikipedia.org/wiki/Number_base
[5]: https://en.wikipedia.org/wiki/Base_10
[6]: https://en.wikipedia.org/wiki/D._R._Kaprekar
[7]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=1
[8]: https://en.wikipedia.org/wiki/Fixed_point_(mathematics)
[9]: https://en.wikipedia.org/wiki/Periodic_point
[10]: https://en.wikipedia.org/wiki/Integer
[11]: https://en.wikipedia.org/wiki/Iterated_function
[12]: https://en.wikipedia.org/wiki/Periodic_sequence
[13]: https://en.wikipedia.org/wiki/Persistence_of_a_number
[14]: https://en.wikipedia.org/wiki/Perfect_number
[15]: https://en.wikipedia.org/wiki/Base_2
[16]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=2
[17]: https://en.wikipedia.org/wiki/Diophantine_equation
[18]: https://en.wikipedia.org/wiki/Bijection
[19]: https://en.wikipedia.org/wiki/Unitary_divisor
[20]: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
[21]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=3
[22]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=4
[23]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=5
[24]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=6
[25]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=7
[26]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=8
[27]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=9
[28]: https://en.wikipedia.org/wiki/Base-2
[29]: https://en.wikipedia.org/wiki/Base-3
[30]: https://en.wikipedia.org/wiki/Base-4
[31]: https://en.wikipedia.org/wiki/Base-5
[32]: https://en.wikipedia.org/wiki/Base-6
[33]: https://en.wikipedia.org/wiki/Base-8
[34]: https://en.wikipedia.org/wiki/Base-9
[35]: https://en.wikipedia.org/wiki/Base-10
[36]: https://en.wikipedia.org/wiki/Base-12
[37]: https://en.wikipedia.org/wiki/Base-16
[38]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=10
[39]: https://en.wikipedia.org/wiki/Signed-digit_representation
[40]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=11
[41]: https://en.wikipedia.org/wiki/Arithmetic_dynamics#Other_areas_in_which_number_theory_and_dynamics_interact
[42]: https://en.wikipedia.org/wiki/Automorphic_number
[43]: https://en.wikipedia.org/wiki/Dudeney_number
[44]: https://en.wikipedia.org/wiki/Factorion
[45]: https://en.wikipedia.org/wiki/Happy_number
[46]: https://en.wikipedia.org/wiki/Kaprekar's_routine
[47]: https://en.wikipedia.org/wiki/Meertens_number
[48]: https://en.wikipedia.org/wiki/Narcissistic_number
[49]: https://en.wikipedia.org/wiki/Perfect_digit-to-digit_invariant
[50]: https://en.wikipedia.org/wiki/Perfect_digital_invariant
[51]: https://en.wikipedia.org/wiki/Sum-product_number
[52]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=12
[53]: /w/index.php?title=Kaprekar_number&amp;action=edit&amp;section=13
[54]: https://en.wikipedia.org/wiki/Journal_of_Recreational_Mathematics
[55]: https://cs.uwaterloo.ca/journals/JIS/VOL3/iann2a.html
[56]: https://en.wikipedia.org/wiki/Journal_of_Integer_Sequences
[57]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[58]: https://ui.adsabs.harvard.edu/abs/2000JIntS...3...12I
[59]: https://en.wikipedia.org/wiki/Template:Classes_of_natural_numbers
[60]: https://en.wikipedia.org/wiki/Template_talk:Classes_of_natural_numbers
[61]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Classes_of_natural_numbers
[62]: https://en.wikipedia.org/wiki/Exponentiation
[63]: https://en.wikipedia.org/wiki/Achilles_number
[64]: https://en.wikipedia.org/wiki/Power_of_two
[65]: https://en.wikipedia.org/wiki/Power_of_three
[66]: https://en.wikipedia.org/wiki/Power_of_10
[67]: https://en.wikipedia.org/wiki/Square_number
[68]: https://en.wikipedia.org/wiki/Cube_(algebra)
[69]: https://en.wikipedia.org/wiki/Fourth_power
[70]: https://en.wikipedia.org/wiki/Fifth_power_(algebra)
[71]: https://en.wikipedia.org/wiki/Sixth_power
[72]: https://en.wikipedia.org/wiki/Seventh_power
[73]: https://en.wikipedia.org/wiki/Eighth_power
[74]: https://en.wikipedia.org/wiki/Perfect_power
[75]: https://en.wikipedia.org/wiki/Powerful_number
[76]: https://en.wikipedia.org/wiki/Prime_power
[77]: https://en.wikipedia.org/wiki/Cullen_number
[78]: https://en.wikipedia.org/wiki/Double_Mersenne_number
[79]: https://en.wikipedia.org/wiki/Fermat_number
[80]: https://en.wikipedia.org/wiki/Mersenne_prime
[81]: https://en.wikipedia.org/wiki/Proth_number
[82]: https://en.wikipedia.org/wiki/Thabit_number
[83]: https://en.wikipedia.org/wiki/Woodall_number
[84]: https://en.wikipedia.org/wiki/Hilbert_number
[85]: https://en.wikipedia.org/wiki/Idoneal_number
[86]: https://en.wikipedia.org/wiki/Leyland_number
[87]: https://en.wikipedia.org/wiki/Loeschian_number
[88]: https://en.wikipedia.org/wiki/Lucky_numbers_of_Euler
[89]: https://en.wikipedia.org/wiki/Recursion
[90]: https://en.wikipedia.org/wiki/Fibonacci_sequence
[91]: https://en.wikipedia.org/wiki/Jacobsthal_number
[92]: https://en.wikipedia.org/wiki/Leonardo_number
[93]: https://en.wikipedia.org/wiki/Lucas_number
[94]: https://en.wikipedia.org/wiki/Supergolden_ratio#Narayana_sequence
[95]: https://en.wikipedia.org/wiki/Padovan_sequence
[96]: https://en.wikipedia.org/wiki/Pell_number
[97]: https://en.wikipedia.org/wiki/Perrin_number
[98]: https://en.wikipedia.org/wiki/Graham's_number
[99]: https://en.wikipedia.org/wiki/Amenable_number
[100]: https://en.wikipedia.org/wiki/Congruent_number
[101]: https://en.wikipedia.org/wiki/Knödel_number
[102]: https://en.wikipedia.org/wiki/Riesel_number
[103]: https://en.wikipedia.org/wiki/Sierpiński_number
[104]: https://en.wikipedia.org/wiki/Nonhypotenuse_number
[105]: https://en.wikipedia.org/wiki/Polite_number
[106]: https://en.wikipedia.org/wiki/Practical_number
[107]: https://en.wikipedia.org/wiki/Primary_pseudoperfect_number
[108]: https://en.wikipedia.org/wiki/Ulam_number
[109]: https://en.wikipedia.org/wiki/Wolstenholme_number
[110]: https://en.wikipedia.org/wiki/Figurate_number
[111]: https://en.wikipedia.org/wiki/Plane_(mathematics)
[112]: https://en.wikipedia.org/wiki/Centered_polygonal_number
[113]: https://en.wikipedia.org/wiki/Centered_triangular_number
[114]: https://en.wikipedia.org/wiki/Centered_square_number
[115]: https://en.wikipedia.org/wiki/Centered_pentagonal_number
[116]: https://en.wikipedia.org/wiki/Centered_hexagonal_number
[117]: https://en.wikipedia.org/wiki/Centered_heptagonal_number
[118]: https://en.wikipedia.org/wiki/Centered_octagonal_number
[119]: https://en.wikipedia.org/wiki/Centered_nonagonal_number
[120]: https://en.wikipedia.org/wiki/Centered_decagonal_number
[121]: https://en.wikipedia.org/wiki/Star_number
[122]: https://en.wikipedia.org/wiki/Polygonal_number
[123]: https://en.wikipedia.org/wiki/Triangular_number
[124]: https://en.wikipedia.org/wiki/Square_triangular_number
[125]: https://en.wikipedia.org/wiki/Pentagonal_number
[126]: https://en.wikipedia.org/wiki/Hexagonal_number
[127]: https://en.wikipedia.org/wiki/Heptagonal_number
[128]: https://en.wikipedia.org/wiki/Octagonal_number
[129]: https://en.wikipedia.org/wiki/Nonagonal_number
[130]: https://en.wikipedia.org/wiki/Decagonal_number
[131]: https://en.wikipedia.org/wiki/Dodecagonal_number
[132]: https://en.wikipedia.org/wiki/Three-dimensional_space
[133]: https://en.wikipedia.org/wiki/Centered_polyhedral_number
[134]: https://en.wikipedia.org/wiki/Centered_tetrahedral_number
[135]: https://en.wikipedia.org/wiki/Centered_cube_number
[136]: https://en.wikipedia.org/wiki/Centered_octahedral_number
[137]: https://en.wikipedia.org/wiki/Centered_dodecahedral_number
[138]: https://en.wikipedia.org/wiki/Centered_icosahedral_number
[139]: https://en.wikipedia.org/wiki/Polyhedral_number
[140]: https://en.wikipedia.org/wiki/Tetrahedral_number
[141]: https://en.wikipedia.org/wiki/Octahedral_number
[142]: https://en.wikipedia.org/wiki/Dodecahedral_number
[143]: https://en.wikipedia.org/wiki/Icosahedral_number
[144]: https://en.wikipedia.org/wiki/Stella_octangula_number
[145]: https://en.wikipedia.org/wiki/Pyramidal_number
[146]: https://en.wikipedia.org/wiki/Square_pyramidal_number
[147]: https://en.wikipedia.org/wiki/Four-dimensional_space
[148]: https://en.wikipedia.org/wiki/Pentatope_number
[149]: https://en.wikipedia.org/wiki/Squared_triangular_number
[150]: https://en.wikipedia.org/wiki/Bell_number
[151]: https://en.wikipedia.org/wiki/Cake_number
[152]: https://en.wikipedia.org/wiki/Catalan_number
[153]: https://en.wikipedia.org/wiki/Dedekind_number
[154]: https://en.wikipedia.org/wiki/Delannoy_number
[155]: https://en.wikipedia.org/wiki/Euler_number
[156]: https://en.wikipedia.org/wiki/Eulerian_number
[157]: https://en.wikipedia.org/wiki/Fuss–Catalan_number
[158]: https://en.wikipedia.org/wiki/Lah_number
[159]: https://en.wikipedia.org/wiki/Lazy_caterer's_sequence
[160]: https://en.wikipedia.org/wiki/Lobb_number
[161]: https://en.wikipedia.org/wiki/Motzkin_number
[162]: https://en.wikipedia.org/wiki/Narayana_number
[163]: https://en.wikipedia.org/wiki/Ordered_Bell_number
[164]: https://en.wikipedia.org/wiki/Schröder_number
[165]: https://en.wikipedia.org/wiki/Schröder–Hipparchus_number
[166]: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind
[167]: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
[168]: https://en.wikipedia.org/wiki/Telephone_number_(mathematics)
[169]: https://en.wikipedia.org/wiki/Wedderburn–Etherington_number
[170]: https://en.wikipedia.org/wiki/Prime_number
[171]: https://en.wikipedia.org/wiki/Wieferich_prime#Wieferich_numbers
[172]: https://en.wikipedia.org/wiki/Wall–Sun–Sun_prime
[173]: https://en.wikipedia.org/wiki/Wolstenholme_prime
[174]: https://en.wikipedia.org/wiki/Wilson_prime#Wilson_numbers
[175]: https://en.wikipedia.org/wiki/Pseudoprime
[176]: https://en.wikipedia.org/wiki/Carmichael_number
[177]: https://en.wikipedia.org/wiki/Catalan_pseudoprime
[178]: https://en.wikipedia.org/wiki/Elliptic_pseudoprime
[179]: https://en.wikipedia.org/wiki/Euler_pseudoprime
[180]: https://en.wikipedia.org/wiki/Euler–Jacobi_pseudoprime
[181]: https://en.wikipedia.org/wiki/Fermat_pseudoprime
[182]: https://en.wikipedia.org/wiki/Frobenius_pseudoprime
[183]: https://en.wikipedia.org/wiki/Lucas_pseudoprime
[184]: https://en.wikipedia.org/wiki/Lucas–Carmichael_number
[185]: https://en.wikipedia.org/wiki/Perrin_number#Perrin_primality_test
[186]: https://en.wikipedia.org/wiki/Somer–Lucas_pseudoprime
[187]: https://en.wikipedia.org/wiki/Strong_pseudoprime
[188]: https://en.wikipedia.org/wiki/Arithmetic_function
[189]: https://en.wikipedia.org/wiki/Arithmetic_dynamics
[190]: https://en.wikipedia.org/wiki/Divisor_function
[191]: https://en.wikipedia.org/wiki/Abundant_number
[192]: https://en.wikipedia.org/wiki/Almost_perfect_number
[193]: https://en.wikipedia.org/wiki/Arithmetic_number
[194]: https://en.wikipedia.org/wiki/Betrothed_numbers
[195]: https://en.wikipedia.org/wiki/Colossally_abundant_number
[196]: https://en.wikipedia.org/wiki/Deficient_number
[197]: https://en.wikipedia.org/wiki/Descartes_number
[198]: https://en.wikipedia.org/wiki/Hemiperfect_number
[199]: https://en.wikipedia.org/wiki/Highly_abundant_number
[200]: https://en.wikipedia.org/wiki/Highly_composite_number
[201]: https://en.wikipedia.org/wiki/Hyperperfect_number
[202]: https://en.wikipedia.org/wiki/Multiply_perfect_number
[203]: https://en.wikipedia.org/wiki/Primitive_abundant_number
[204]: https://en.wikipedia.org/wiki/Quasiperfect_number
[205]: https://en.wikipedia.org/wiki/Refactorable_number
[206]: https://en.wikipedia.org/wiki/Semiperfect_number
[207]: https://en.wikipedia.org/wiki/Sublime_number
[208]: https://en.wikipedia.org/wiki/Superabundant_number
[209]: https://en.wikipedia.org/wiki/Superior_highly_composite_number
[210]: https://en.wikipedia.org/wiki/Superperfect_number
[211]: https://en.wikipedia.org/wiki/Prime_omega_function
[212]: https://en.wikipedia.org/wiki/Almost_prime
[213]: https://en.wikipedia.org/wiki/Semiprime
[214]: https://en.wikipedia.org/wiki/Euler's_totient_function
[215]: https://en.wikipedia.org/wiki/Highly_cototient_number
[216]: https://en.wikipedia.org/wiki/Highly_totient_number
[217]: https://en.wikipedia.org/wiki/Noncototient
[218]: https://en.wikipedia.org/wiki/Nontotient
[219]: https://en.wikipedia.org/wiki/Perfect_totient_number
[220]: https://en.wikipedia.org/wiki/Sparsely_totient_number
[221]: https://en.wikipedia.org/wiki/Aliquot_sequence
[222]: https://en.wikipedia.org/wiki/Amicable_numbers
[223]: https://en.wikipedia.org/wiki/Sociable_numbers
[224]: https://en.wikipedia.org/wiki/Untouchable_number
[225]: https://en.wikipedia.org/wiki/Primorial
[226]: https://en.wikipedia.org/wiki/Euclid_number
[227]: https://en.wikipedia.org/wiki/Fortunate_number
[228]: https://en.wikipedia.org/wiki/Prime_factor
[229]: https://en.wikipedia.org/wiki/Divisor
[230]: https://en.wikipedia.org/wiki/Blum_integer
[231]: https://en.wikipedia.org/wiki/Cyclic_number_(group_theory)
[232]: https://en.wikipedia.org/wiki/Erdős–Nicolas_number
[233]: https://en.wikipedia.org/wiki/Erdős–Woods_number
[234]: https://en.wikipedia.org/wiki/Friendly_number
[235]: https://en.wikipedia.org/wiki/Giuga_number
[236]: https://en.wikipedia.org/wiki/Harmonic_divisor_number
[237]: https://en.wikipedia.org/wiki/Jordan–Pólya_number
[238]: https://en.wikipedia.org/wiki/Pronic_number
[239]: https://en.wikipedia.org/wiki/Regular_number
[240]: https://en.wikipedia.org/wiki/Rough_number
[241]: https://en.wikipedia.org/wiki/Smooth_number
[242]: https://en.wikipedia.org/wiki/Sphenic_number
[243]: https://en.wikipedia.org/wiki/Størmer_number
[244]: https://en.wikipedia.org/wiki/Super-Poulet_number
[245]: https://en.wikipedia.org/wiki/Numeral_system
[246]: https://en.wikipedia.org/wiki/Additive_persistence
[247]: https://en.wikipedia.org/wiki/Multiplicative_persistence
[248]: https://en.wikipedia.org/wiki/Digit_sum
[249]: https://en.wikipedia.org/wiki/Digital_root
[250]: https://en.wikipedia.org/wiki/Self_number
[251]: https://en.wikipedia.org/wiki/Multiplicative_digital_root
[252]: https://en.wikipedia.org/wiki/Kaprekar_number
[253]: https://en.wikipedia.org/wiki/Keith_number
[254]: https://en.wikipedia.org/wiki/Lychrel_number
[255]: https://en.wikipedia.org/wiki/P-adic_numbers
[256]: https://en.wikipedia.org/wiki/Trimorphic_number
[257]: https://en.wikipedia.org/wiki/Numerical_digit
[258]: https://en.wikipedia.org/wiki/Palindromic_number
[259]: https://en.wikipedia.org/wiki/Pandigital_number
[260]: https://en.wikipedia.org/wiki/Repdigit
[261]: https://en.wikipedia.org/wiki/Repunit
[262]: https://en.wikipedia.org/wiki/Self-descriptive_number
[263]: https://en.wikipedia.org/wiki/Smarandache–Wellin_number
[264]: https://en.wikipedia.org/wiki/Undulating_number
[265]: https://en.wikipedia.org/wiki/Permutation
[266]: https://en.wikipedia.org/wiki/Cyclic_number
[267]: https://en.wikipedia.org/wiki/Digit-reassembly_number
[268]: https://en.wikipedia.org/wiki/Parasitic_number
[269]: https://en.wikipedia.org/wiki/Primeval_number
[270]: https://en.wikipedia.org/wiki/Transposable_integer
[271]: https://en.wikipedia.org/wiki/Equidigital_number
[272]: https://en.wikipedia.org/wiki/Extravagant_number
[273]: https://en.wikipedia.org/wiki/Frugal_number
[274]: https://en.wikipedia.org/wiki/Harshad_number
[275]: https://en.wikipedia.org/wiki/Polydivisible_number
[276]: https://en.wikipedia.org/wiki/Smith_number
[277]: https://en.wikipedia.org/wiki/Vampire_number
[278]: https://en.wikipedia.org/wiki/Friedman_number
[279]: https://en.wikipedia.org/wiki/Binary_number
[280]: https://en.wikipedia.org/wiki/Evil_number
[281]: https://en.wikipedia.org/wiki/Odious_number
[282]: https://en.wikipedia.org/wiki/Pernicious_number
[283]: https://en.wikipedia.org/wiki/Sieve_theory
[284]: https://en.wikipedia.org/wiki/Lucky_number
[285]: https://en.wikipedia.org/wiki/Generation_of_primes
[286]: https://en.wikipedia.org/wiki/Sorting_algorithm
[287]: https://en.wikipedia.org/wiki/Pancake_sorting
[288]: https://en.wikipedia.org/wiki/Sorting_number
[289]: https://en.wikipedia.org/wiki/Natural_language
[290]: https://en.wikipedia.org/wiki/Aronson's_sequence
[291]: https://en.wikipedia.org/wiki/Ban_number
[292]: https://en.wikipedia.org/wiki/Graphemics
[293]: https://en.wikipedia.org/wiki/Strobogrammatic_number
[294]: https://en.wikipedia.org/wiki/File:Symbol_portal_class.svg
[295]: https://en.wikipedia.org/wiki/Portal:Mathematics
[296]: https://en.wikipedia.org/w/index.php?title=Kaprekar_number&amp;oldid=1368200114
[297]: /wiki/Help:Category
[298]: /wiki/Category:Arithmetic_dynamics
[299]: /wiki/Category:Base-dependent_integer_sequences
[300]: /wiki/Category:Diophantine_equations
[301]: /wiki/Category:Number_theory
[302]: /wiki/Category:Indian_inventions
[303]: /wiki/Category:Articles_with_short_description
[304]: /wiki/Category:Short_description_is_different_from_Wikidata
