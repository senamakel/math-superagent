<!-- source: https://ar5iv.labs.arxiv.org/html/1904.01874 | converted from HTML -->

[1904.01874] Contents

A variant of Ostrowski numeration

Emmanuel Cabanillas

ABSTRACT :

In this article, we propose a variant of the usual Ostrowski α \alpha -numeration ( where α \alpha is a real in [0, 1 [[0,1[) that codes integers ( positive as well as negative) and reals of [0, 1 [[0,1[( instead of [− α, 1 − α [[-\alpha,1-\alpha[), so that for every integer n n, n n and { n ​ α } \{n\alpha\} have the same coding sequence. These coding sequences respect natural lexicographic orders and will be used to prove well known results on order properties of Kronecker sequences ( { n ​ α − β }) n (\{n\alpha-\beta\})_{n}.

## 1 Introduction

### 1.1 overview

Ostrowski’s numeration system is based on convergents ( q n) n ∈ ℕ (q_{n})_{n\in\mathbb{N}} of a real α ∈ [0, 1 [\alpha\in[0,1[and code, with a sequence of digits non negative integers as well as reals in [− α, 1 − α [[-\alpha,1-\alpha[( see [6] for the original article and [1] for a survey). Definitions are mentioned in 2.1
In 2.2 and 2.3, we propose a variant of this system : it is still based on ( q n) n (q_{n})_{n}, but the ” markovian condition” is changed and we will be able to code any integer n n and any real { n ​ α } \{n\alpha\} with the same finite sequence ( { x } \{x\} denotes the fractional part of a real x x). We study separately the cases α \alpha irrational and α \alpha rational. This last case could appear uninteresting, but it is useful for applications to numerical semigroups for example ( see [3]).
In 3, we give some dynamical aspects of this α \alpha -numeration.
In 4, we use it to explore some order properties of Kronecker sequences ( { n ​ α + β }) n (\{n\alpha+\beta\})_{n}, as the famous ” three distance theorem”. These sequences have been widely studied with various points of view and we refer to [1] for an exhaustive bibliography.

### 1.2 notations

All along this paper, we will denote : ℤ \mathbb{Z} the set of integers, ℕ ∗ \mathbb{N}^{*} the set of positive integers and ℕ \mathbb{N} the set of non negative integers.
For all reals x x, ⌊ x ⌋ \lfloor x\rfloor denotes its floor , ⌈ x ⌉ \lceil x\rceil its ceiling and { x } \{x\} its fractional part.
For a sequence d = ( d k) k ∈ ℕ ∗ d=(d_{k})_{k\in\mathbb{N}^{*}}, we use the following notations for slices of d d: for all integers r, s r,s such that 0 < r ⩽ s 0<r\leqslant s:

 | d [r, s] = ( d r, d r + 1, ⋯, d s); d [r, ∞] = ( d r, d r + 1, ⋯) d_{[r,s]}=(d_{r},d_{r+1},\cdots,d_{s})\hskip 8.5359pt;\hskip 8.5359ptd_{[r,\infty]}=(d_{r},d_{r+1},\cdots) |  |

We will also use concatenation of sequences and intuitive notations as ( 3, 5, 0 4, 1, 6, 0 ∞) (3,5,0^{4},1,6,0^{\infty}) to denote ( 3, 5, 0, 0, 0, 0, 1, 6, 0, 0, 0, ⋯) (3,5,0,0,0,0,1,6,0,0,0,\cdots). Moreover, if ( a k) k ∈ ℕ ∗ (a_{k})_{k\in\mathbb{N}^{*}} is a sequence of positive integers and if we restrict ourself to sequences in ∏ k { 0 ⋯ a k } \prod_{k}\{0\cdots a_{k}\}, then max \max at the index k k will denote a k a_{k}: for example, ( max, 1, 0, max, 3, ⋯,) (\max,1,0,\max,3,\cdots,) means ( a 1, 1, 0, a 4, 3, …) (a_{1},1,0,a_{4},3,...). So, the notation max r \max^{r} or ( max, 0) r (\max,0)^{r}, where r ∈ ℕ ∪ { ∞ } r\in\mathbb{N}\cup\{\infty\} will often be used. For example : ( 0 2, max 3, 0 4, ( max, 0) ∞) (0^{2},\max^{3},0^{4},(\max,0)^{\infty}) denotes the sequence ( 0, 0, a 3, a 4, a 5, 0, 0, 0, 0, a 10, 0, a 12, 0, a 14, 0, ⋯) (0,0,a_{3},a_{4},a_{5},0,0,0,0,a_{10},0,a_{12},0,a_{14},0,\cdots).

For α \alpha -numeration, we will often use two lexicographic orders on sequences of ℝ ℕ ∗ \mathbb{R}^{\mathbb{N}^{*}}:
▶ \blacktriangleright the reversed lexicographic order ( RLO) denoted ⩽ 𝑅 \underset{R}{\leqslant}:

 | d ​ ⩽ 𝑅 ​ d ′ ⇔ d = d ′ ​ or ​ ∃ j ∈ ℕ ∗, { d j < d j ′ ∀ i > j, d i = d i ′ d\underset{R}{\leqslant}d^{\prime}\Leftrightarrow d=d^{\prime}\text{ or }\exists j\in\mathbb{N}^{*},\begin{cases}d_{j}<d^{\prime}_{j}\\ \forall i>j,d_{i}=d^{\prime}_{i}\end{cases} |  |

▶ \blacktriangleright the alternate lexicographic order ( ALO) denoted ⩽ 𝐴 \underset{A}{\leqslant}:

 | d ​ ⩽ 𝐴 ​ d ′ ⇔ d = d ′ ​ or ​ ∃ j ∈ ℕ ∗, { ( − 1) j − 1 ​ d j < ( − 1) j − 1 ​ d j ′ ∀ i ∈ { 1 ⋯ j − 1 }, d i = d ′ i d\underset{A}{\leqslant}d^{\prime}\Leftrightarrow d=d^{\prime}\text{ or }\exists j\in\mathbb{N}^{*},\begin{cases}(-1)^{j-1}d_{j}<(-1)^{j-1}d^{\prime}_{j}\\ \forall i\in\{1\cdots j-1\},d_{i}=d^{\prime}_{i}\end{cases} |  |

ALO is a total order on ℝ ℕ ∗ \mathbb{R}^{\mathbb{N}^{*}}, but RLO is only a partial order on ℝ ℕ ∗ \mathbb{R}^{\mathbb{N}^{*}}. Now, RLO is a total order on on ℝ ( ℕ ∗) \mathbb{R}^{(\mathbb{N}^{*})}, the set of real sequences that ends with 0 ∞ 0^{\infty}.
We will also use ALO with a shift on indices for continued fraction expansions in 1.3 ( named CFE in this paper).

### 1.3 continued fraction expansions

All results given in this subsection are well known and we just want to underline some notations and simple facts.

∙ \bullet Every irrational θ \theta can be uniquely represented by its continued fraction expansion ( CFE) and we will write θ = [t 0, t 1, ⋯] = [t k] k ∈ ℕ \theta=[t_{0},t_{1},\cdots]=[t_{k}]_{k\in\mathbb{N}}, such that t k ∈ ℕ ∗ t_{k}\in\mathbb{N}^{*} for all k ∈ ℕ ∗ k\in\mathbb{N}^{*} and t 0 ∈ ℤ t_{0}\in\mathbb{Z}. θ \theta is the limit of the ” convergents” ( [t 0, t 1, ⋯, t n]) n ([t_{0},t_{1},\cdots,t_{n}])_{n}, a sequence of rationals defined inductively by :

 | ∀ x ∈ ℝ, ∀ x 1, ⋯, x n ∈ ℝ + ∗, [x] = x; [x, x 1, ⋯, x n] = x + 1 [x 1, ⋯, x n] ​ ( 1) \forall x\in\mathbb{R},\forall x_{1},\cdots,x_{n}\in\mathbb{R}_{+}^{*},[x]=x\hskip 8.5359pt;\hskip 8.5359pt[x,x_{1},\cdots,x_{n}]=x+\frac{1}{[x_{1},\cdots,x_{n}]}\hskip 8.5359pt(1) |  |

We will denote, for all integer n n, p n q n \frac{p_{n}}{q_{n}} ( or p n ​ ( θ) q n ​ ( θ) \frac{p_{n}(\theta)}{q_{n}(\theta)} if necessary) the reduced fraction that represents [t 0, t 1, ⋯, t n] [t_{0},t_{1},\cdots,t_{n}].
In addition, if we define φ \varphi:

 | φ: { ℤ × ( ℕ ∗) ℕ ∗ → ℝ \ ℚ ( t k) k ∈ ℕ → [t k] k ∈ ℕ \varphi:\begin{cases}\mathbb{Z}\times(\mathbb{N}^{*})^{\mathbb{N}^{*}}\to\mathbb{R}\backslash\mathbb{Q}\\ (t_{k})_{k\in\mathbb{N}}\to[t_{k}]_{k\in\mathbb{N}}\end{cases} |  |

this map is bijective and increasing, with the Alternate Lexicographic Order ( ALO) on ℤ × ( ℕ ∗) ℕ \mathbb{Z}\times(\mathbb{N}^{*})^{\mathbb{N}} defined by :

 | ( t k) k ∈ ℕ ⩽ A ( t k ′) k ∈ ℕ ⇔ ( ∀ k ∈ ℕ, t k = t k ′) or ∃ j ∈ ℕ, { ∀ k ∈ { 0 ⋯ j − 1 }, t k = t ′ k ( − 1) j ​ t j < ( − 1) j ​ t j ′ (t_{k})_{k\in\mathbb{N}}\leqslant_{A}(t^{\prime}_{k})_{k\in\mathbb{N}}\Leftrightarrow(\forall k\in\mathbb{N},t_{k}=t^{\prime}_{k})\text{ or }\exists j\in\mathbb{N},\begin{cases}\forall k\in\{0\cdots j-1\},t_{k}=t^{\prime}_{k}\\ (-1)^{j}t_{j}<(-1)^{j}t^{\prime}_{j}\end{cases} |  |

We also have an expression for the inverse function of φ \varphi:

 | φ − 1: { ℝ \ ℚ → ℤ × ( ℕ ∗) ℕ ∗ θ → ( t k) k ∈ ℕ, with ​ t 0 = ⌊ θ ⌋; ∀ k ∈ ℕ ∗, t k = A ​ T k − 1 ​ ( { θ }) \varphi^{-1}:\begin{cases}\mathbb{R}\backslash\mathbb{Q}\to\mathbb{Z}\times(\mathbb{N}^{*})^{\mathbb{N}^{*}}\\ \theta\to(t_{k})_{k\in\mathbb{N}},\text{ with }t_{0}=\lfloor\theta\rfloor;\forall k\in\mathbb{N}^{*},t_{k}=AT^{k-1}(\{\theta\})\end{cases} |  |

where T T is the Gauss map : ] 0, 1 [→ [0, 1 [, x → { 1 / x }]0,1[\to[0,1[,x\to\{1/x\} and A: x → ⌊ 1 / x ⌋ A:x\to\lfloor 1/x\rfloor. We know that T k ​ ( α) ≠ 0 T^{k}(\alpha)\not=0 for all k ∈ ℕ k\in\mathbb{N} if and only if α \alpha is irrational in ] 0, 1 []0,1[.

∙ \bullet The case of rationals seems easier, since these one are represented by finite CFE, namely the convergents of irrationals. But, we would like to associate to them infinite CFE, in order to extend φ \varphi to an increasing map with ALO.
We introduce an ∞ \infty number : ℕ ∗ ¯ \overline{\mathbb{N}^{*}} will denote ℕ ∗ ∪ { ∞ } \mathbb{N}^{*}\cup\{\infty\}, with the usual extension of the order ( ∀ n ∈ ℕ ∗, n < ∞ \forall n\in\mathbb{N}^{*},n<\infty) and of the operations ( ∀ n ∈ ℕ ¯, n + ∞ = ∞ \forall n\in\overline{\mathbb{N}},n+\infty=\infty and 1 / ∞ = 0 1/\infty=0). Then, we can end CFE of rationals with an infinite sequence of ∞ \infty. With those conventions, the former map φ \varphi extends to an increasing and bijective map φ ~ \tilde{\varphi} from a subset E E of ℤ × ( ℕ ∗ ¯) ℕ ∗ \mathbb{Z}\times(\overline{\mathbb{N}^{*}})^{\mathbb{N}^{*}} to ℝ \mathbb{R}. Then, φ ~ − 1 \tilde{\varphi}^{-1} is given by the same expressions, if we extend T T and A A to [0, 1 [[0,1[, with T ⁡ ( 0) = 0 T(0)=0 and A ⁡ ( 0) = ∞ A(0)=\infty.
We can precise E E: it is the set of sequences ( t k) k (t_{k})_{k} such that t 0 ∈ ℤ t_{0}\in\mathbb{Z} and t k ∈ ℕ ∗ ¯ t_{k}\in\overline{\mathbb{N}^{*}} for k ∈ ℕ ∗ k\in\mathbb{N}^{*}, such that t k = ∞ ⇒ ( t k + 1 = ∞ CLOSE t_{k}=\infty\Rightarrow(t_{k+1}=\infty and ( t k − 1 ≠ 1 t_{k-1}\not=1 or k = 1 k=1)). So to say : if the sequence contains ∞ \infty, the last ” finite digit” in the CFE is greater or equal to 2 2. We will prefer an alternative way : we will end CFE of rationals with [1, ∞ ∞] [1,\infty^{\infty}], where ∞ ∞ \infty^{\infty} denotes an infinite sequence of ∞ \infty. Then, we extend naturally the ALO to sequences of CFE, described by :

 | 𝒞 = { ( t k) ∈ ℤ × ℕ ∗ × ( ℕ ∗ ¯) ℕ, ∀ k ⩾ 2, ( t k = ∞ ⇒ ( t k + 1 = ∞ and t k − 1 ∈ { ∞, 1 }) } \mathcal{C}=\{(t_{k})\in\mathbb{Z}\times\mathbb{N}^{*}\times(\overline{\mathbb{N}^{*}})^{\mathbb{N}},\forall k\geqslant 2,(t_{k}=\infty\Rightarrow(t_{k+1}=\infty\text{ and }t_{k-1}\in\{\infty,1\})\} |  |

The extension of φ \varphi to an increasing and bijective map φ 1 \varphi_{1} from 𝒞 \mathcal{C} to ℝ \mathbb{R} is quite natural, but its inverse function will use more complicated maps T 1 T_{1} and A 1 A_{1}:

We consider the map I: u → ⌈ u ⌉ − 1 I:u\to\lceil u\rceil-1 and A 1, T 1 A_{1},T_{1} both defined on [0, 1] [0,1] by :

 | A 1: { 0 → ∞ 1 → 1 x → I ⁡ ( 1 / x) ​ if ​ x ≠ 0, 1; T 1: { 0 → 0 1 → 0 x → 1 ​ if ​ 1 / x ∈ ℕ \ { 0, 1 } x → { 1 / x } ​ else A_{1}:\begin{cases}0\to\infty\\ 1\to 1\\ x\to I(1/x)\text{ if }x\not=0,1\end{cases}\hskip 8.5359pt;\hskip 8.5359ptT_{1}:\begin{cases}0\to 0\\ 1\to 0\\ x\to 1\text{ if }1/x\in\mathbb{N}\backslash\{0,1\}\\ x\to\{1/x\}\text{ else}\end{cases} |  |

We can now express the inverse function of φ 1 \varphi_{1}:

 | φ 1 − 1: { ℝ → 𝒞 θ → ( t k) k ∈ ℕ, with ​ t 0 = I ⁡ ( θ); ∀ k ∈ ℕ ∗, t k = A 1 ​ T 1 k − 1 ​ ( θ − I ⁡ ( θ)) \varphi_{1}^{-1}:\begin{cases}\mathbb{R}\to\mathcal{C}\\ \theta\to(t_{k})_{k\in\mathbb{N}},\text{ with }t_{0}=I(\theta);\forall k\in\mathbb{N}^{*},t_{k}=A_{1}T_{1}^{k-1}(\theta-I(\theta))\end{cases} |  |

For convenience, we abreviate CFE of rationals and omit ∞ ∞ \infty^{\infty}, the infinite ” ∞ \infty ” ending sequence. So, 9 / 4 = [2, 3, 1] 9/4=[2,3,1] and ∀ n ∈ ℤ, n = [n − 1, 1] \forall n\in\mathbb{Z},n=[n-1,1].

N.B : all along this paper, CFE of a real ( so for any rational) α \alpha will denote φ 1 − 1 ​ ( α) \varphi_{1}^{-1}(\alpha), but the notation [t 0, t 1, ⋯, t k] [t_{0},t_{1},\cdots,t_{k}] will be more general ( see (1)).

### 1.4 semi-convergents and best rationals

∙ \bullet Let α \alpha be a real with CFE [a k] k ∈ ℕ [a_{k}]_{k\in\mathbb{N}} and ( p k / q k) k (p_{k}/q_{k})_{k} its convergents sequence, such that p k / q k = [a 0, ⋯, a k] p_{k}/q_{k}=[a_{0},\cdots,a_{k}], for all k k such that a k < ∞ a_{k}<\infty ( see beginning of this section).
A *semi-convergent*of α \alpha is any rational of the form m ​ p k + p k − 1 m ​ q k + q k − 1 \frac{mp_{k}+p_{k-1}}{mq_{k}+q_{k-1}}, with m ∈ { 0 ⋯ a k } m\in\{0\cdots a_{k}\} and k ∈ ℕ k\in\mathbb{N} such that a k < ∞ a_{k}<\infty ( we take m > 0 m>0 if k = 0 k=0 to avoid 1 / 0 1/0!). So, convergents are particular semi-convergents.

###### Lemma 1

Let α \alpha be a real with CFE [a k] k ∈ ℕ [a_{k}]_{k\in\mathbb{N}}. Semi-convergents of α \alpha are exactly the rationals with CFE [a 0, ⋯, a s − 1, b s, 1] [a_{0},\cdots,a_{s-1},b_{s},1], such that s ∈ ℕ, b s ∈ { 1 ⋯ a s } s\in\mathbb{N},b_{s}\in\{1\cdots a_{s}\} and a s + 1 < ∞ a_{s+1}<\infty.

Proof :
Consequence of the definition and the well known fact : ∀ m ∈ ℕ, [a 0, ⋯, a s − 1, m] = m ​ p s − 1 + p s − 2 m ​ q s − 1 + q s − 2 \forall m\in\mathbb{N},[a_{0},\cdots,a_{s-1},m]=\frac{mp_{s-1}+p_{s-2}}{mq_{s-1}+q_{s-2}}. ■ \blacksquare

∙ \bullet Let α \alpha be a rational and [a 0, a 1, a 2, ⋯, a r, 1] [a_{0},a_{1},a_{2},\cdots,a_{r},1] its CFE. ( we denote a r + 1 = 1 a_{r+1}=1)
We have the following induction formula :

 | p − 2 = 0; p − 1 = 1; ∀ n ∈ { 0 ⋯ r + 1 }, p n = a n p n − 1 + p n − 2 p_{-2}=0\hskip 8.5359pt;\hskip 8.5359ptp_{-1}=1\hskip 8.5359pt;\hskip 8.5359pt\forall n\in\{0\cdots r+1\}\hskip 8.5359pt,\hskip 8.5359ptp_{n}=a_{n}p_{n-1}+p_{n-2} |  |

 | q − 2 = 1; q − 1 = 0; ∀ n ∈ { 0 ⋯ r + 1 }, q n = a n q n − 1 + q n − 2 q_{-2}=1\hskip 8.5359pt;\hskip 8.5359ptq_{-1}=0\hskip 8.5359pt;\hskip 8.5359pt\forall n\in\{0\cdots r+1\}\hskip 8.5359pt,\hskip 8.5359ptq_{n}=a_{n}q_{n-1}+q_{n-2} |  |

We have α = p r + p r − 1 q r + q r − 1 = p r + 1 q r + 1 \alpha=\frac{p_{r}+p_{r-1}}{q_{r}+q_{r-1}}=\frac{p_{r+1}}{q_{r+1}}.

Let α ′ = [a 0 ′, a 1 ′, ⋯, a r ′ ′, 1] \alpha^{\prime}=[a^{\prime}_{0},a^{\prime}_{1},\cdots,a^{\prime}_{r^{\prime}},1] be an other rational with r ′ ⩾ r r^{\prime}\geqslant r. With obvious notations, we see that , for n ∈ { 0 ⋯ r } n\in\{0\cdots r\}:

 | ( ∀ k ∈ { 0 ⋯ n }, a k ⩽ a k ′) ⇒ ( ∀ k ∈ { 0 ⋯ n }, p k ⩽ p k ′ and q k ⩽ q k ′) (\forall k\in\{0\cdots n\},a_{k}\leqslant a^{\prime}_{k})\Rightarrow\left(\forall k\in\{0\cdots n\},p_{k}\leqslant p^{\prime}_{k}\text{ and }q_{k}\leqslant q^{\prime}_{k}\right) |  |

In addition, for j, n j,n integers such that 1 ⩽ j ⩽ n ⩽ r 1\leqslant j\leqslant n\leqslant r:

 | ( a j < a j ′ and ∀ k ∈ { 1 ⋯ j − 1 }, a k ⩽ a k ′) ⇒ q j < q j ′ (a_{j}<a^{\prime}_{j}\text{ and }\forall k\in\{1\cdots j-1\},a_{k}\leqslant a^{\prime}_{k})\Rightarrow q_{j}<q^{\prime}_{j} |  |

∙ \bullet Now, we would like to precise the CFE of reals in [θ, θ ′] ⟷ \overset{\longleftrightarrow}{[\theta,\theta^{\prime}]} ( denotes the set of reals that are between θ \theta and θ ′ \theta^{\prime}, even if θ > θ ′ \theta>\theta^{\prime}), where θ \theta and θ ′ \theta^{\prime} are two different reals and find the rationals in this interval with the lowest reduced denominator.

First, we introduce a simple and natural notion :

###### Definition 1 ( CFE-depth of a real)

.
let x x be a real. We name *CFE-depth*of x x the non negative integer, denoted μ ⁡ ( x) \mu(x) and defined by : μ ⁡ ( x) = + ∞ \mu(x)=+\infty if x x is irrational and μ ⁡ ( x) = s \mu(x)=s, if x = [a 0, a 1, ⋯, a s, 1] x=[a_{0},a_{1},\cdots,a_{s},1] is the CFE of x x.

We remark that :

 | μ ⁡ ( x) = 0 ⇔ x ∈ ℤ; ∀ n ∈ ℤ, μ ⁡ ( x + n) = μ ⁡ ( x); ∀ x ∉ ℤ, μ ⁡ ( T ⁡ ( x)) = μ ⁡ ( x) − 1 \mu(x)=0\Leftrightarrow x\in\mathbb{Z}\hskip 8.5359pt;\hskip 8.5359pt\forall n\in\mathbb{Z},\mu(x+n)=\mu(x)\hskip 8.5359pt;\hskip 8.5359pt\forall x\not\in\mathbb{Z},\mu(T(x))=\mu(x)-1 |  |

We denote θ = [t k] k ∈ ℕ \theta=[t_{k}]_{k\in\mathbb{N}} and θ ′ = [t k ′] k ∈ ℕ \theta^{\prime}=[t^{\prime}_{k}]_{k\in\mathbb{N}}, according to our φ 1 \varphi_{1} -representation. We will abreviate t t and t ′ t^{\prime} these CFE-sequences. We denote r r the smallest integer k k such that t k ≠ t k ′ t_{k}\not=t^{\prime}_{k}. Then we have r ⩽ min ⁡ ( μ ⁡ ( θ), μ ⁡ ( θ ′)) + 2 r\leqslant\min(\mu(\theta),\mu(\theta^{\prime}))+2, when θ \theta or θ ′ \theta^{\prime} is rational ( if they are both irrationals, r r is finite ! ). Indeed, the extremal case when r = μ ⁡ ( θ) + 2 r=\mu(\theta)+2 for example corresponds to θ = [t 0, ⋯, t r − 2, 1] \theta=[t_{0},\cdots,t_{r-2},1] and θ ′ = [t 0, ⋯, t r − 2, 1, t r ′, …] \theta^{\prime}=[t_{0},\cdots,t_{r-2},1,t^{\prime}_{r},...], with t r ′ < ∞ t^{\prime}_{r}<\infty.

We remark that, all integers in [θ, θ ′] ⟷ \overset{\longleftrightarrow}{[\theta,\theta^{\prime}]} minimize the denominator of their reduced fraction : it is 1 1!! So, we can suppose that ⌊ θ ⌋ = ⌊ θ ′ ⌋ \lfloor\theta\rfloor=\lfloor\theta^{\prime}\rfloor and even that θ, θ ′ ∈ [0, 1 [\theta,\theta^{\prime}\in[0,1[.
The following Lemma proves that, in that case, there is only one rational in [θ, θ ′] ⟷ \overset{\longleftrightarrow}{[\theta,\theta^{\prime}]}, that minimizes the value of its denominator : it is usually named the ” best rational” in [θ, θ ′] ⟷ \overset{\longleftrightarrow}{[\theta,\theta^{\prime}]}

###### Proposition 1

let θ \theta and θ ′ \theta^{\prime} be two different reals in [0, 1 [[0,1[and θ = [t k] k ∈ ℕ, θ ′ = [t k ′] k ∈ ℕ \theta=[t_{k}]_{k\in\mathbb{N}},\theta^{\prime}=[t^{\prime}_{k}]_{k\in\mathbb{N}} their respective CFE. We denote r r the lowest integer k k such that t k ≠ t k ′ t_{k}\not=t^{\prime}_{k}.
(i) there is a unique rational in [θ, θ ′] ⟷ \overset{\longleftrightarrow}{[\theta,\theta^{\prime}]} that minimizes the denominator. We denote it γ \gamma.
- if r ⩽ min ⁡ ( μ ⁡ ( θ), μ ⁡ ( θ ′)) r\leqslant\min(\mu(\theta),\mu(\theta^{\prime})), then γ = [t 0, ⋯, t r − 1, min ⁡ ( t r, t r ′), 1] \gamma=[t_{0},\cdots,t_{r-1},\min(t_{r},t^{\prime}_{r}),1].
- else, μ ⁡ ( θ) < μ ⁡ ( θ ′) \mu(\theta)<\mu(\theta^{\prime}) ( up to swap) and γ = θ \gamma=\theta.
(ii) in both cases, μ ⁡ ( γ) ⩽ min ⁡ ( μ ⁡ ( θ), μ ⁡ ( θ ′)) \mu(\gamma)\leqslant\min(\mu(\theta),\mu(\theta^{\prime})) and γ = [t 0, ⋯, t s − 1, min ⁡ ( t s, t s ′), 1] \gamma=[t_{0},\cdots,t_{s-1},\min(t_{s},t^{\prime}_{s}),1], where s = μ ⁡ ( γ) ⩽ r s=\mu(\gamma)\leqslant r and ∀ k ∈ { 0 ⋯ s − 1 }, t k = t k ′ \forall k\in\{0\cdots s-1\},t_{k}=t^{\prime}_{k}.
(iii) the best rational in [θ, θ ′] ⟷ \overset{\longleftrightarrow}{[\theta,\theta^{\prime}]} is the common semi-convergent of θ \theta and θ ′ \theta^{\prime} with the greatest denominator.

Proof :
(i) if r ⩽ min ⁡ ( μ ⁡ ( θ), μ ⁡ ( θ ′)) r\leqslant\min(\mu(\theta),\mu(\theta^{\prime})). Suppose that t r < t r ′ t_{r}<t^{\prime}_{r}. We have for ( d k) k ∈ ℕ ∈ 𝒞 (d_{k})_{k\in\mathbb{N}}\in\mathcal{C}:

 | [d k] k ∈ ℕ ∈ [θ, θ ′] ⟷ ⇔ { ∀ k < j, d k = t k = t k ′ σ r ( t) ⩽ A σ r ( d) ⩽ A σ r ( t ′) ( ∗) [d_{k}]_{k\in\mathbb{N}}\in\overset{\longleftrightarrow}{[\theta,\theta^{\prime}]}\Leftrightarrow\begin{cases}\forall k<j,d_{k}=t_{k}=t^{\prime}_{k}\\ \sigma^{r}(t)\leqslant_{A}\sigma^{r}(d)\leqslant_{A}\sigma^{r}(t^{\prime})\hskip 8.5359pt(*)\end{cases} |  |

where σ \sigma is the usual shift : for any sequence u u, ∀ k ∈ ℕ, σ ​ ( u) k = u k + 1 \forall k\in\mathbb{N},\sigma(u)_{k}=u_{k+1}.
But, if we want the lowest denominator for the rational [d k] k ∈ ℕ [d_{k}]_{k\in\mathbb{N}}, we have to choose the lowest d k d_{k} or the ∞ \infty value ( if possible), for all k k. So we have to choose first d r = t r d_{r}=t_{r} and then, the condition (*) becomes : σ r + 1 ( d) ⩽ A σ r + 1 ( t) \sigma^{r+1}(d)\leqslant_{A}\sigma^{r+1}(t). So, we choose d r + 1 = 1 d_{r+1}=1 and ∀ k > r + 1, d k = ∞ \forall k>r+1,d_{k}=\infty.
- else, one at least of μ ⁡ ( θ) \mu(\theta) and μ ⁡ ( θ ′) \mu(\theta^{\prime}) is finite and they can not be equal, since r r can not be greater than both of them. Suppose μ ⁡ ( θ) < μ ⁡ ( θ ′) \mu(\theta)<\mu(\theta^{\prime}), then we have μ ⁡ ( θ) < r \mu(\theta)<r and ∀ k ∈ { 0 ⋯ μ ( θ) }, t k = t k ′ \forall k\in\{0\cdots\mu(\theta)\},t_{k}=t^{\prime}_{k}. So, the same arguments as in the previous case prove that θ \theta is the best rational in [θ, θ ′] ⟷ \overset{\longleftrightarrow}{[\theta,\theta^{\prime}]}.

(ii) it is plain in the first case, since μ ⁡ ( γ) = r \mu(\gamma)=r. If μ ⁡ ( θ) < r \mu(\theta)<r and μ ⁡ ( θ) < μ ⁡ ( θ ′) \mu(\theta)<\mu(\theta^{\prime}), then γ = θ \gamma=\theta and t s = t s ′ t_{s}=t^{\prime}_{s}.

(iii) is a consequence of (ii), Lemma 1 and the remark following it. ■ \blacksquare

Remark : as a direct consequence of (iii) : θ \theta is the best rational in [θ, θ ′] ⟷ \overset{\longleftrightarrow}{[\theta,\theta^{\prime}]} if and only if θ \theta is a semi-convergent of θ ′ \theta^{\prime}.

∙ \bullet Let α \alpha be a real, [a k] k ∈ ℕ ∗ [a_{k}]_{k\in\mathbb{N}^{*}} its CFE and r = μ ⁡ ( α) r=\mu(\alpha), the CFE-depth of α \alpha. So, we denote [a 0, a 1, ⋯, a r, 1] [a_{0},a_{1},\cdots,a_{r},1] the CFE of α \alpha if α \alpha is rational. We also denote ( p n / q n) n (p_{n}/q_{n})_{n} the usual sequence of convergents of α \alpha.
We consider the usual notion of best rational approximation of a real α \alpha: for p, q p,q two integers, p / q p/q is said a *best rational approximation*of α \alpha if and only if :

 | ∀ q ′ ∈ { 1 ⋯ q − 1 }, ∀ p ′ ∈ ℤ, | p ′ q ′ − α | > | p q − α | \forall q^{\prime}\in\{1\cdots q-1\}\hskip 8.5359pt,\hskip 8.5359pt\forall p^{\prime}\in\mathbb{Z}\hskip 8.5359pt,\hskip 8.5359pt\left|\dfrac{p^{\prime}}{q^{\prime}}-\alpha\right|>\left|\dfrac{p}{q}-\alpha\right| |  |

It is well known that best rational approximation of a real are exactly its reduced convergents.
Now, we can consider two sided similar definitions :

###### Definition 2 ( best sided rational approximation)

.
for p, q p,q two integers, p / q p/q is said a *best left rational approximation*of α \alpha if and only if :

 | ∀ q ′ ∈ { 1 ⋯ q − 1 }, ∀ p ′ ∈ ℤ, p ′ q ′ < p q ⩽ α or p ′ q ′ > α \forall q^{\prime}\in\{1\cdots q-1\}\hskip 8.5359pt,\hskip 8.5359pt\forall p^{\prime}\in\mathbb{Z}\hskip 8.5359pt,\hskip 8.5359pt\dfrac{p^{\prime}}{q^{\prime}}<\dfrac{p}{q}\leqslant\alpha\hskip 8.5359pt\text{ or }\hskip 8.5359pt\dfrac{p^{\prime}}{q^{\prime}}>\alpha |  |

p / q p/q is said a *best right rational approximation*of α \alpha if and only if :

 | ∀ q ′ ∈ { 1 ⋯ q − 1 }, ∀ p ′ ∈ ℤ, p ′ q ′ > p q ⩾ α or p ′ q ′ < α \forall q^{\prime}\in\{1\cdots q-1\}\hskip 8.5359pt,\hskip 8.5359pt\forall p^{\prime}\in\mathbb{Z}\hskip 8.5359pt,\hskip 8.5359pt\dfrac{p^{\prime}}{q^{\prime}}>\dfrac{p}{q}\geqslant\alpha\hskip 8.5359pt\text{ or }\hskip 8.5359pt\dfrac{p^{\prime}}{q^{\prime}}<\alpha |  |

Here is a corollary of Proposition 1 :

###### Corollary 1

.
(i) best left rational approximations of α \alpha are the semi-convergents of α \alpha, that are lower than α \alpha.
(ii) best right rational approximations of α \alpha are the semi-convergents of α \alpha, that are greater than α \alpha.

Proof :
(i) we remark that p / q p/q is a best left rational approximation of α \alpha if and only if p / q p/q is the best rational in [p / q, α] [p/q,\alpha] and use the remark below Proposition 1. Same arguments for (ii). ■ \blacksquare

If we denote ( p k / q k) k (p_{k}/q_{k})_{k} the reduced convergents of α \alpha, then :
- its best left rational approximations are :

 | p 2 ​ i + m ​ p 2 ​ i + 1 q 2 ​ i + m ​ q 2 ​ i + 1; i ∈ { 0 ⋯ ( μ ( α) − 1) / 2 }; m ∈ { 0 ⋯ a 2 ​ i + 2 } \frac{p_{2i}+mp_{2i+1}}{q_{2i}+mq_{2i+1}}\hskip 8.5359pt;\hskip 8.5359pti\in\{0\cdots(\mu(\alpha)-1)/2\}\hskip 8.5359pt;\hskip 8.5359ptm\in\{0\cdots a_{2i+2}\} |  |

- its best right rational approximations are :

 | p 2 ​ i − 1 + m ​ p 2 ​ i q 2 ​ i − 1 + m ​ q 2 ​ i; i ∈ { 1 ⋯ μ ( α) / 2 }; m ∈ { 0 ⋯ a 2 ​ i + 1 } \frac{p_{2i-1}+mp_{2i}}{q_{2i-1}+mq_{2i}}\hskip 8.5359pt;\hskip 8.5359pti\in\{1\cdots\mu(\alpha)/2\}\hskip 8.5359pt;\hskip 8.5359ptm\in\{0\cdots a_{2i+1}\} |  |

## 2 A numeration system

### 2.1 Ostrowski’s numeration

We will only deal here with the case α \alpha irrational, even if the rational case is interesting ( see next section). We denote Ω α \Omega_{\alpha} the set of sequences of integers defined as follows ( we denote [a k] k ∈ ℕ [a_{k}]_{k\in\mathbb{N}} the continued fraction expansion of α \alpha) :

 | Ω α = { ( d n) n ∈ ℕ ∗, d 1 ∈ { 0 ⋯ a 1 − 1 }, ∀ k ∈ ℕ ∗ \ { 1 }, d k ∈ { 0 ⋯ a k } and ( d k = a k ⇒ d k − 1 = 0) } \Omega_{\alpha}=\{(d_{n})_{n\in\mathbb{N}^{*}},d_{1}\in\{0\cdots a_{1}-1\},\forall k\in\mathbb{N}^{*}\backslash\{1\},d_{k}\in\{0\cdots a_{k}\}\text{ and }(d_{k}=a_{k}\Rightarrow d_{k-1}=0)\} |  |

What we call ” markovian condition” is the last implication : d k = a k ⇒ d k − 1 = 0 d_{k}=a_{k}\Rightarrow d_{k-1}=0.
From this set of infinite sequences, we extract two subsets, that will be our numeration sets for reals and integers respectively : O α O_{\alpha} is the set of sequences d d of Ω α \Omega_{\alpha} such that d d does not ” end with” ( max, 0) ∞ (\max,0)^{\infty}, an infinite sequence a k 0 a k + 2 0 ⋯ a_{k}0a_{k+2}0\cdots. So to say, there is an infinite number of even and an infinite number of odd values of k k such that d k < a k d_{k}<a_{k}. Now, O ( α) O_{(\alpha)} is the set of sequences d d of Ω α \Omega_{\alpha} ( or O α O_{\alpha}) that ends with an infinite sequence of 0 0: so to say d k = 0 d_{k}=0 for any sufficiently large k k.

We define then two maps :

 | f α: { O ( α) → ℕ d → ∑ k = 1 ∞ d k ​ q k − 1; g α: { O α → [− α, 1 − α [d → ∑ k = 1 ∞ d k ​ ( α ​ q k − 1 − p k − 1) f_{\alpha}:\begin{cases}O_{(\alpha)}\to\mathbb{N}\\ d\to\sum\limits_{k=1}^{\infty}d_{k}q_{k-1}\end{cases}\hskip 8.5359pt;\hskip 8.5359ptg_{\alpha}:\begin{cases}O_{\alpha}\to[-\alpha,1-\alpha[\\ d\to\sum\limits_{k=1}^{\infty}d_{k}(\alpha q_{k-1}-p_{k-1})\end{cases} |  |

It is well known that f α f_{\alpha} and g α g_{\alpha} are well defined and are bijective. Moreover :

 | ∀ d ∈ O ( α), { f α ​ ( d) ​ α } = { g α ​ ( d) } \forall d\in O_{(\alpha)},\hskip 8.5359pt\{f_{\alpha}(d)\alpha\}=\{g_{\alpha}(d)\} |  |

But, we will emphasize an other aspect : the maps above are increasing for the usual order on ℕ \mathbb{N} and ℝ \mathbb{R} respectively and following orders on O ( α) O_{(\alpha)} and O α O_{\alpha}.

- the reversed lexicographic order ( RLO) on O ( α) O_{(\alpha)}:

 | d ​ ⩽ 𝑅 ​ d ′ ⇔ d = d ′ ​ or ​ ∃ j ∈ ℕ ∗, { d j < d j ′ ∀ i > j, d i = d i ′ d\underset{R}{\leqslant}d^{\prime}\Leftrightarrow d=d^{\prime}\text{ or }\exists j\in\mathbb{N}^{*},\begin{cases}d_{j}<d^{\prime}_{j}\\ \forall i>j,d_{i}=d^{\prime}_{i}\end{cases} |  |

- the alternate lexicographic order ( ALO) on O α O_{\alpha}:

 | d ​ ⩽ 𝐴 ​ d ′ ⇔ d = d ′ ​ or ​ ∃ j ∈ ℕ ∗, { ( − 1) j − 1 ​ d j < ( − 1 j − 1 ​ d j ′ CLOSE ∀ i ∈ { 1 ⋯ j − 1 }, d i = d ′ i d\underset{A}{\leqslant}d^{\prime}\Leftrightarrow d=d^{\prime}\text{ or }\exists j\in\mathbb{N}^{*},\begin{cases}(-1)^{j-1}d_{j}<(-1^{j-1}d^{\prime}_{j}\\ \forall i\in\{1\cdots j-1\},d_{i}=d^{\prime}_{i}\end{cases} |  |

These are total orders on these sets respectively.

Our aim is to find a variant of Ostrowski numeration that has same properties, but that code reals of [0, 1 [[0,1[instead of [− α, 1 − α [[-\alpha,1-\alpha[and also all integers, positive as well as negative ones.
We will see that it suffices to change the markovian condition : instead of d k = a k ⇒ d k − 1 = 0 d_{k}=a_{k}\Rightarrow d_{k-1}=0, we take d k = 0 ⇒ ( d k − 1 = a k − 1 CLOSE d_{k}=0\Rightarrow(d_{k-1}=a_{k-1} or d i = 0 d_{i}=0 for all i ⩾ k i\geqslant k).

### 2.2 α \alpha -numeration for a rational α \alpha

Why do we consider this case α \alpha rational ? Indeed, the set { { n ​ α }, n ∈ ℕ } \{\{n\alpha\},n\in\mathbb{N}\} is finite and trivial. It can not define a base of numeration for [0, 1 [[0,1[. But the order properties of the sequence ( { n ​ α }) n ∈ ℕ (\{n\alpha\})_{n\in\mathbb{N}} are not obvious and our Ostrowski-like numeration will help.

∙ \bullet Let α \alpha be a rational in [0, 1 [[0,1[and α = [0, a 1, ⋯, a r, 1] \alpha=[0,a_{1},\cdots,a_{r},1] its CFE. We will denote ( p k / q k) 0 ⩽ k ⩽ r + 1 (p_{k}/q_{k})_{0\leqslant k\leqslant r+1} its convergents, so that α = p r + 1 q r + 1 \alpha=\frac{p_{r+1}}{q_{r+1}}.

###### Definition 3 ( α \alpha -admissible sequences)

.
a sequence d d in ℕ r \mathbb{N}^{r} is said *α \alpha -admissible*if and only if :

 | ∀ j ∈ { 1 ⋯ r }, { d j ∈ { 0 ⋯ a j } d j = 0 ⇒ ( ∀ i ⩾ j, d i = 0) or d j − 1 = a j − 1 \forall j\in\{1\cdots r\},\begin{cases}d_{j}\in\{0\cdots a_{j}\}\\ d_{j}=0\Rightarrow(\forall i\geqslant j,d_{i}=0)\text{ or }d_{j-1}=a_{j-1}\end{cases} |  |

We will denote E α E_{\alpha} the set of α \alpha -admissible sequences.

Remark : for j = 1 j=1, the second condition reduces to d 1 = 0 ⇒ ∀ i ⩾ 1, d i = 0 d_{1}=0\Rightarrow\forall i\geqslant 1,d_{i}=0. So to say, d = ( 0, ⋯, 0) d=(0,\cdots,0) is the only element of E α E_{\alpha}, whose first coordinate is 0 0.

###### Lemma 2

.
(i)

 | ∀ d ∈ E α, ∀ k ∈ { 1 ⋯ r }, ∑ i = 1 k d i q i − 1 < q k + q k − 1 \forall d\in E_{\alpha},\forall k\in\{1\cdots r\},\hskip 8.5359pt\sum_{i=1}^{k}d_{i}q_{i-1}<q_{k}+q_{k-1} |  |

(ii) let d, d ′ ∈ E α d,d^{\prime}\in E_{\alpha} and n ∈ { 1 ⋯ r } n\in\{1\cdots r\} such that d n ′ > 0 d^{\prime}_{n}>0.

 | ∀ k ∈ { 1 ⋯ n }, ∑ i = 1 k ( d i − d i ′) q i − 1 < q k \forall k\in\{1\cdots n\},\hskip 8.5359pt\sum_{i=1}^{k}(d_{i}-d^{\prime}_{i})q_{i-1}<q_{k} |  |

Proof :
(i) by plain induction on k k.
(ii) by induction ( on 2 ranks) on k k:
- it is true for k = 0 k=0 ( obvious) and for k = 1 k=1: indeed d 1 ′ > 0 d^{\prime}_{1}>0 ( else, we would have d ′ = 0 d^{\prime}=0 and d n ′ = 0 d^{\prime}_{n}=0) : then ( d 1 − d 1 ′) ​ q 0 ⩽ ( a 1 − 1) ​ q 0 = q 1 − 1 (d_{1}-d^{\prime}_{1})q_{0}\leqslant(a_{1}-1)q_{0}=q_{1}-1.
- we suppose that it is true for the ranks k − 2 k-2 and k − 1 k-1, where k k is an integer in { 2 ⋯ n } \{2\cdots n\}. Then, we have two cases for the rank k k:
▶ \blacktriangleright Case 1 : d k − d k ′ ⩽ a k − 1 d_{k}-d^{\prime}_{k}\leqslant a_{k}-1, then, with the induction hypothesis on rank k − 1 k-1:

 | ∑ i = 1 k ( d i − d i ′) ​ q i − 1 < q k − 1 + ( a k − 1) ​ q k − 1 = a k ​ q k − 1 = q k − q k − 2 < q k \sum_{i=1}^{k}(d_{i}-d^{\prime}_{i})q_{i-1}<q_{k-1}+(a_{k}-1)q_{k-1}=a_{k}q_{k-1}=q_{k}-q_{k-2}<q_{k} |  |

the last inequality is true, for k ⩾ 2 k\geqslant 2.
▶ \blacktriangleright Case 2 : d k = a k, d k ′ = 0 d_{k}=a_{k},d^{\prime}_{k}=0, then d k − 1 ′ = a k − 1 d^{\prime}_{k-1}=a_{k-1} ( else, we would have d j ′ = 0 d^{\prime}_{j}=0 for all j ⩾ k j\geqslant k, but d n ′ ≠ 0 d^{\prime}_{n}\not=0) and d k − 1 − d k − 1 ′ ⩽ 0 d_{k-1}-d^{\prime}_{k-1}\leqslant 0. So with the induction hypothesis on rank k − 2 k-2:

 | ∑ i = 1 k ( d i − d i ′) ​ q i − 1 < q k − 2 + a k ​ q k − 1 = q k \sum_{i=1}^{k}(d_{i}-d^{\prime}_{i})q_{i-1}<q_{k-2}+a_{k}q_{k-1}=q_{k} |  |

■ \blacksquare

We consider the reversed lexicographic order ( RLO) denoted ⩽ 𝑅 \underset{R}{\leqslant} on ℕ r \mathbb{N}^{r}:

 | d ⩽ 𝑅 d ′ ⇔ d = d ′ or ∃ j ∈ { 1 ⋯ r }, { d j < d j ′ ∀ i ∈ { j + 1 ⋯ r }, d i = d ′ i d\underset{R}{\leqslant}d^{\prime}\Leftrightarrow d=d^{\prime}\text{ or }\exists j\in\{1\cdots r\},\begin{cases}d_{j}<d^{\prime}_{j}\\ \forall i\in\{j+1\cdots r\},d_{i}=d^{\prime}_{i}\end{cases} |  |

It is a total order on E α E_{\alpha}.

###### Lemma 3

the map Ψ α \Psi_{\alpha} below is increasing from ( E α, ⩽ R) (E_{\alpha},\leqslant_{R}) to ( { 0 ⋯ q r + 1 − 1 }, ⩽) (\{0\cdots q_{r+1}-1\},\leqslant).

 | Ψ α: { E α → { 0 ⋯ q r + 1 − 1 } d → ∑ j = 1 r d j ​ q j − 1 \Psi_{\alpha}:\begin{cases}E_{\alpha}\to\{0\cdots q_{r+1}-1\}\\ d\to\sum\limits_{j=1}^{r}d_{j}q_{j-1}\end{cases} |  |

Proof :
First, for all d ∈ E α, Ψ α ( d) ∈ { 0 ⋯ q r + 1 − 1 } d\in E_{\alpha},\Psi_{\alpha}(d)\in\{0\cdots q_{r+1}-1\}, with Lemma 2 (i).
Now, let prove that Ψ α \Psi_{\alpha} is increasing. Let d, d ′ ∈ E α d,d^{\prime}\in E_{\alpha}, such that d < R d ′ d<_{R}d^{\prime}. We have j ∈ { 1 ⋯ r } j\in\{1\cdots r\}, such that :

 | d j < d j ′ and ∀ i ∈ { j + 1 ⋯ r }, d i = d i ′ d_{j}<d^{\prime}_{j}\hskip 8.5359pt\text{ and }\hskip 8.5359pt\forall i\in\{j+1\cdots r\},d_{i}=d^{\prime}_{i} |  |

So :

 | Ψ α ​ ( d ′) − Ψ α ​ ( d) = ∑ i = 1 j − 1 ( d i ′ − d i) ​ q i − 1 + ( d j ′ − d j) ​ q j − 1 \Psi_{\alpha}(d^{\prime})-\Psi_{\alpha}(d)=\sum_{i=1}^{j-1}(d^{\prime}_{i}-d_{i})q_{i-1}+(d^{\prime}_{j}-d_{j})q_{j-1} |  |

We just have to prove that : ∑ i = 1 j − 1 ( d i − d i ′) ​ q i − 1 < q j − 1 \sum\limits_{i=1}^{j-1}(d_{i}-d^{\prime}_{i})q_{i-1}<q_{j-1}, since d j ′ − d j ⩾ 1 d^{\prime}_{j}-d_{j}\geqslant 1. This is shown by Lemma 2 (ii), for d j ′ > 0 d^{\prime}_{j}>0. ■ \blacksquare

Now, we prove that Ψ α \Psi_{\alpha} is surjective : the following algorithm explains the inverse function of Ψ α \Psi_{\alpha}. We will denote m k = q k + q k − 1 m_{k}=q_{k}+q_{k-1} for any k ∈ { 0 ⋯ r } k\in\{0\cdots r\}. So m r = q r + 1 m_{r}=q_{r+1}.

###### Algorithm 1

let n ∈ { 0 ⋯ m r − 1 } n\in\{0\cdots m_{r}-1\}.
With the following algorithm, we have d ∈ E α d\in E_{\alpha} and Ψ α ​ ( d) = n \Psi_{\alpha}(d)=n.

Input: n n

Output: ( d i) i ∈ { 1 ⋯ r } (d_{i})_{i\in\{1\cdots r\}}

for*k ← r k\leftarrow r to 1 1 step − 1 -1*do

d k ← max ⁡ ( 0, ⌊ n − q k − 2 q k − 1 ⌋) d_{k}\leftarrow\max\left(0,\left\lfloor\frac{n-q_{k-2}}{q_{k-1}}\right\rfloor\right);

n ← n − d k ​ q k − 1 n\leftarrow n-d_{k}q_{k-1} end for

Proof :
We begin with a remark : if n < m s n<m_{s} for an integer s ∈ { 1 ⋯ r } s\in\{1\cdots r\}, then : d k = 0 d_{k}=0 for k ∈ { s + 1 ⋯ r } k\in\{s+1\cdots r\}. Indeed, we will have n < m k n<m_{k} for all k ∈ { s ⋯ r } k\in\{s\cdots r\} so n − q k − 2 < q k − 1 n-q_{k-2}<q_{k-1} for all k ∈ { s + 1 ⋯ r } k\in\{s+1\cdots r\}.
Let us prove the result by induction on s s, where s s in an integer such that n ∈ { 0 ⋯ m s − 1 } n\in\{0\cdots m_{s}-1\}:
- for s = 1 s=1, m 1 = a 1 + 1 m_{1}=a_{1}+1. Let n ∈ { 0 ⋯ a 1 } n\in\{0\cdots a_{1}\}. Then d 1 = n d_{1}=n and d = ( d 1) ∈ E α, Ψ α ​ ( d) = d 1 = n d=(d_{1})\in E_{\alpha},\Psi_{\alpha}(d)=d_{1}=n.
- we suppose that the algorithm is available for all n ∈ { 0 ⋯ m s − 1 − 1 } n\in\{0\cdots m_{s-1}-1\}, with s ⩾ 2 s\geqslant 2.
Let n ∈ { m s − 1 ⋯ m s − 1 } n\in\{m_{s-1}\cdots m_{s}-1\}. Then q s − 1 ⩽ n − q s − 2 < ( a s + 1) ​ q s − 1 q_{s-1}\leqslant n-q_{s-2}<(a_{s}+1)q_{s-1}, so d s ∈ { 1 ⋯ a s } d_{s}\in\{1\cdots a_{s}\}. We denote n 1 = n − d s ​ q s − 1 n_{1}=n-d_{s}q_{s-1}, the value of n n after the loop for k = s k=s. We have : q s − 2 ⩽ n 1 < q s − 1 + q s − 2 = m s − 1 q_{s-2}\leqslant n_{1}<q_{s-1}+q_{s-2}=m_{s-1}. By induction hypothesis, d ′ = ( d 1, ⋯, d s − 1) ∈ E α d^{\prime}=(d_{1},\cdots,d_{s-1})\in E_{\alpha} and n 1 = Ψ α ​ ( d ′) = ∑ i = 1 s − 1 d i ​ q i − 1 n_{1}=\Psi_{\alpha}(d^{\prime})=\sum\limits_{i=1}^{s-1}d_{i}q_{i-1}. But, n = n 1 + d s ​ q s − 1 n=n_{1}+d_{s}q_{s-1} and so Ψ α ​ ( d) = n \Psi_{\alpha}(d)=n, because we have d ∈ E α d\in E_{\alpha}: indeed, we have 2 subcases :
▶ \blacktriangleright Case 1 : if n 1 ⩾ m s − 2 n_{1}\geqslant m_{s-2}, then d s − 1 > 0 d_{s-1}>0 and, since ( d 1, ⋯, d s − 1) ∈ E α (d_{1},\cdots,d_{s-1})\in E_{\alpha}, then d ∈ E α d\in E_{\alpha}.
▶ \blacktriangleright Case 2 : if n 1 < m s − 2 n_{1}<m_{s-2} ( which leads to s ⩾ 3 s\geqslant 3, for m 0 = q 0 m_{0}=q_{0}), then d s − 1 = 0 d_{s-1}=0 and n 2 = n 1 n_{2}=n_{1} ( n 2 n_{2}: the value of n n after the loop for k = s − 1 k=s-1). But, since n 1 ⩾ q s − 2 n_{1}\geqslant q_{s-2}, then n 2 − q s − 4 ⩾ a s − 2 ​ q s − 3 n_{2}-q_{s-4}\geqslant a_{s-2}q_{s-3} and finally d s − 2 = a s − 2 d_{s-2}=a_{s-2}. By induction hypothesis, d ′ = ( d 1, ⋯, d s − 3, a s − 2, 0) d^{\prime}=(d_{1},\cdots,d_{s-3},a_{s-2},0) is α \alpha -admissible, so d ∈ E α d\in E_{\alpha}. ■ \blacksquare

###### Proposition 2

Ψ α \Psi_{\alpha} is an order isomorphism between ( E α, ⩽ R) (E_{\alpha},\leqslant_{R}) and ( { 0 ⋯ q r + 1 − 1 }, ⩽) (\{0\cdots q_{r+1}-1\},\leqslant).

Remark : as a direct consequence : E α E_{\alpha} has q r + 1 q_{r+1} elements.

Proof :
a direct consequence of Lemma 3 and Algorithm 1 ■ \blacksquare

∙ \bullet Now, we will deal with α \alpha -numeration for elements of U α = { { k ​ α }, k ∈ ℕ } U_{\alpha}=\{\{k\alpha\},k\in\mathbb{N}\}. Since, α = p r + 1 q r + 1 \alpha=\frac{p_{r+1}}{q_{r+1}} and this fraction is reduced, we have U α = { n q r + 1, n ∈ { 0 ⋯ q r + 1 − 1 } } U_{\alpha}=\{\frac{n}{q_{r+1}},n\in\{0\cdots q_{r+1}-1\}\}. So, this set is very simple, but we will focus on the map k → { k ​ α } k\to\{k\alpha\}, with the order point of view :
We consider the alternate lexicographic order ( ALO) denoted ⩽ 𝐴 \underset{A}{\leqslant} on ℝ r \mathbb{R}^{r}:

 | d ⩽ 𝐴 d ′ ⇔ d = d ′ or ∃ j ∈ { 1 ⋯ r }, { ( − 1) j − 1 ​ d j < ( − 1) j − 1 ​ d j ′ ∀ i ∈ { 1 ⋯ j − 1 }, d i = d ′ i d\underset{A}{\leqslant}d^{\prime}\Leftrightarrow d=d^{\prime}\text{ or }\exists j\in\{1\cdots r\},\begin{cases}(-1)^{j-1}d_{j}<(-1)^{j-1}d^{\prime}_{j}\\ \forall i\in\{1\cdots j-1\},d_{i}=d^{\prime}_{i}\end{cases} |  |

It is another total order on E α E_{\alpha}. We define also :

 | ∀ i ∈ { − 2 ⋯ r }, δ i = ( − 1) i ( q i α − p i) \forall i\in\{-2\cdots r\},\hskip 8.5359pt\delta_{i}=(-1)^{i}(q_{i}\alpha-p_{i}) |  |

We have, with a 0 = 0 a_{0}=0 here :

 | δ − 2 = α; δ − 1 = 1; δ 0 = { α } = α; ∀ i ∈ { 0 ⋯ r }, δ i = − a i δ i − 1 + δ i − 2 \delta_{-2}=\alpha\hskip 8.5359pt;\hskip 8.5359pt\delta_{-1}=1\hskip 8.5359pt;\hskip 8.5359pt\delta_{0}=\{\alpha\}=\alpha\hskip 8.5359pt;\hskip 8.5359pt\forall i\in\{0\cdots r\},\hskip 8.5359pt\delta_{i}=-a_{i}\delta_{i-1}+\delta_{i-2} |  |

Let T T be the Gauss map : ] 0, 1 [→ [0, 1 [, x → { 1 / x }]0,1[\to[0,1[,x\to\{1/x\}.
By induction on i i, with the fact that : a i = ⌊ 1 T i − 1 ​ ( α) ⌋ a_{i}=\left\lfloor\frac{1}{T^{i-1}(\alpha)}\right\rfloor if i ⩽ r − 1 i\leqslant r-1, we obtain :

 | ∀ i ∈ { 0 ⋯ r − 1 }, δ i δ i − 1 = T i ( α) \forall i\in\{0\cdots r-1\},\frac{\delta_{i}}{\delta_{i-1}}=T^{i}(\alpha) |  |

Beware : for i = r i=r, T r − 1 ​ ( α) = [0, a r, 1] = 1 a r + 1 T^{r-1}(\alpha)=[0,a_{r},1]=\frac{1}{a_{r}+1}, so :

 | δ r δ r − 1 = δ r − 2 − a r ​ δ r − 1 δ r − 1 = 1 T r − 1 ​ ( α) − a r = 1 \frac{\delta_{r}}{\delta_{r-1}}=\frac{\delta_{r-2}-a_{r}\delta_{r-1}}{\delta_{r-1}}=\frac{1}{T^{r-1}(\alpha)}-a_{r}=1 |  |

So : δ r = δ r − 1 \delta_{r}=\delta_{r-1}. We will prove ( proof of Algorithm 2) that δ r = δ r − 1 = 1 q r + 1 \delta_{r}=\delta_{r-1}=\frac{1}{q_{r+1}}.
To summarize this :

 | ∀ i ∈ { 0 ⋯ r − 1 }, 0 < δ i < δ i − 1; δ r = δ r − 1 = 1 q r + 1 \forall i\in\{0\cdots r-1\},0<\delta_{i}<\delta_{i-1}\hskip 8.5359pt;\hskip 8.5359pt\delta_{r}=\delta_{r-1}=\frac{1}{q_{r+1}} |  |

###### Lemma 4

let d, d ′ ∈ E α d,d^{\prime}\in E_{\alpha} and j ∈ { 1 ⋯ r } j\in\{1\cdots r\}, , then :

 | ( − 1) j − 1 ​ ( d j ′ − d j) > 0 ⇒ ∑ i = j + 1 r ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 < δ j − 1 (-1)^{j-1}(d^{\prime}_{j}-d_{j})>0\Rightarrow\sum\limits_{i=j+1}^{r}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}<\delta_{j-1} |  |

Proof :
First, we remark that, for all i i, we have ( − 1) i ​ ( d i ′ − d i) ⩽ a i (-1)^{i}(d^{\prime}_{i}-d_{i})\leqslant a_{i}, so :

 | ∑ i = j + 1 r ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 ⩽ ∑ i = j + 1 r a i ​ δ i − 1 = ∑ i = j + 1 r ( δ i − 2 − δ i) = δ j − 1 + δ j − δ r − 1 − δ r \sum\limits_{i=j+1}^{r}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}\leqslant\sum\limits_{i=j+1}^{r}a_{i}\delta_{i-1}=\sum\limits_{i=j+1}^{r}(\delta_{i-2}-\delta_{i})=\delta_{j-1}+\delta_{j}-\delta_{r-1}-\delta_{r} |  |

▶ \blacktriangleright Case 1 : if ( − 1) j + 1 ​ ( d j + 1 ′ − d j + 1) ⩽ a j + 1 − 1 (-1)^{j+1}(d^{\prime}_{j+1}-d_{j+1})\leqslant a_{j+1}-1, then :

 | ∑ i = j + 1 r ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 ⩽ δ j − 1 − δ r − 1 − δ r < δ j − 1 \sum\limits_{i=j+1}^{r}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}\leqslant\delta_{j-1}-\delta_{r-1}-\delta_{r}<\delta_{j-1} |  |

▶ \blacktriangleright Case 2 : if ( − 1) j + 1 ​ ( d j + 1 ′ − d j + 1) = a j + 1 (-1)^{j+1}(d^{\prime}_{j+1}-d_{j+1})=a_{j+1}.
▶ ⁣ ▶ \blacktriangleright\blacktriangleright Subcase 1 : if j j is even, d j + 1 ′ = 0 d^{\prime}_{j+1}=0 and d j + 1 = a j + 1 d_{j+1}=a_{j+1}. We can not have d j ′ = a j d^{\prime}_{j}=a_{j}, for, with our hypothesis, d j > d j ′ d_{j}>d^{\prime}_{j}. So d i ′ = 0 d^{\prime}_{i}=0 for all i > j i>j and :

 | ∑ i = j + 1 r ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 = a j + 1 ​ δ j − ∑ i = j + 2 r ( − 1) i ​ d i ​ δ i − 1 ⩽ ∑ p = 0 ( r − j − 1) / 2 a j + 2 ​ p + 1 ​ δ j + 2 ​ p = \sum\limits_{i=j+1}^{r}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}=a_{j+1}\delta_{j}-\sum_{i=j+2}^{r}(-1)^{i}d_{i}\delta_{i-1}\leqslant\sum_{p=0}^{(r-j-1)/2}a_{j+2p+1}\delta_{j+2p}= |  |

 | = ∑ p = 0 ( r − j − 1) / 2 ( δ j + 2 ​ p − 1 − δ j + 2 ​ p + 1) = δ j − 1 − δ r ′ < δ j − 1 =\sum_{p=0}^{(r-j-1)/2}(\delta_{j+2p-1}-\delta_{j+2p+1})=\delta_{j-1}-\delta_{r^{\prime}}<\delta_{j-1} |  |

with r ′ = r r^{\prime}=r or r − 1 r-1.
▶ ⁣ ▶ \blacktriangleright\blacktriangleright Subcase 2 : if j j is odd, similar arguments lead to the same conclusion ( we swap d d and d ′ d^{\prime}). ■ \blacksquare

###### Proposition 3

.
(i) the map Λ α \Lambda_{\alpha} ( defined below) is an order isomorphism, with ALO on E α E_{\alpha}:

 | Λ α: { E α → { n q r + 1, n ∈ { 0 ⋯ q r + 1 − 1 } } d → ∑ j = 1 r d j ​ ( − 1) j − 1 ​ δ j − 1 \Lambda_{\alpha}:\begin{cases}E_{\alpha}\to\left\{\frac{n}{q_{r+1}},n\in\{0\cdots q_{r+1}-1\}\right\}\\ d\to\sum\limits_{j=1}^{r}d_{j}(-1)^{j-1}\delta_{j-1}\end{cases} |  |

(ii) we have :

 | ∀ n ∈ { 0 ⋯ q r + 1 − 1 }, { n α } = Λ α ( Ψ α − 1 ( n)) \forall n\in\{0\cdots q_{r+1}-1\},\{n\alpha\}=\Lambda_{\alpha}(\Psi_{\alpha}^{-1}(n)) |  |

Proof :
(i) First, we will show that Λ α \Lambda_{\alpha} is increasing : let d, d ′ ∈ E α d,d^{\prime}\in E_{\alpha} with d < A d ′ d<_{A}d^{\prime}. Then, we have j ∈ { 1 ⋯ r } j\in\{1\cdots r\} such that :

 | ( − 1) j − 1 ​ d j < ( − 1) j − 1 ​ d j ′ ​ and ​ ∀ i < j, d i = d i ′ (-1)^{j-1}d_{j}<(-1)^{j-1}d^{\prime}_{j}\hskip 8.5359pt\text{ and }\hskip 8.5359pt\forall i<j,d_{i}=d^{\prime}_{i} |  |

So :

 | Λ α ​ ( d ′) − Λ α ​ ( d) = ( − 1) j − 1 ​ ( d j ′ − d j) ​ δ j − 1 + ∑ i = j + 1 r ( − 1) i − 1 ​ ( d i ′ − d i) ​ δ i − 1 \Lambda_{\alpha}(d^{\prime})-\Lambda_{\alpha}(d)=(-1)^{j-1}(d^{\prime}_{j}-d_{j})\delta_{j-1}+\sum_{i=j+1}^{r}(-1)^{i-1}(d^{\prime}_{i}-d_{i})\delta_{i-1} |  |

Now :

 | ( − 1) j − 1 ​ ( d j ′ − d j) ​ δ j − 1 ⩾ δ j − 1 (-1)^{j-1}(d^{\prime}_{j}-d_{j})\delta_{j-1}\geqslant\delta_{j-1} |  |

so with Lemma 4, we obtain :

 | Λ α ​ ( d ′) − Λ α ​ ( d) > 0 \Lambda_{\alpha}(d^{\prime})-\Lambda_{\alpha}(d)>0 |  |

Now that we have proved that Λ α \Lambda_{\alpha} is increasing, we can easily deduce that Λ α ( E α) ⊂ [0, 1 [\Lambda_{\alpha}(E_{\alpha})\subset[0,1[: first, remark that ( 0, ⋯, 0) (0,\cdots,0) is the lowest element of E α E_{\alpha} ( with ALO), so Λ α ​ ( d) ⩾ 0 \Lambda_{\alpha}(d)\geqslant 0 for all d ∈ E α d\in E_{\alpha}. Now, ( a 1, 0, a 3, 0, ⋯) (a_{1},0,a_{3},0,\cdots) is the greatest element of E α E_{\alpha} for ALO, so :

 | ∀ d ∈ E α, Λ α ​ ( d) ⩽ ∑ p = 0 ( r − 1) / 2 a 2 ​ p + 1 ​ δ 2 ​ p = ∑ p = 0 ( r − 1) / 2 ( δ 2 ​ p − 1 − δ 2 ​ p + 1) = δ − 1 − δ r ′ < 1 \forall d\in E_{\alpha},\Lambda_{\alpha}(d)\leqslant\sum_{p=0}^{(r-1)/2}a_{2p+1}\delta_{2p}=\sum_{p=0}^{(r-1)/2}(\delta_{2p-1}-\delta_{2p+1})=\delta_{-1}-\delta_{r^{\prime}}<1 |  |

with r ′ = r r^{\prime}=r or r − 1 r-1.

(ii) we just have to show this equality to complete the proof : let d ∈ E α d\in E_{\alpha}. It is sufficient to prove that Λ α ​ ( d) = { Ψ α ​ ( d) ​ α } \Lambda_{\alpha}(d)=\{\Psi_{\alpha}(d)\alpha\}. Now :

 | Λ α ​ ( d) = ∑ j = 1 r d j ​ ( q j − 1 ​ α − p j − 1) = α ​ Ψ α ​ ( d) − k \Lambda_{\alpha}(d)=\sum\limits_{j=1}^{r}d_{j}(q_{j-1}\alpha-p_{j-1})=\alpha\Psi_{\alpha}(d)-k |  |

where k = ∑ j = 1 r d j ​ p j − 1 k=\sum\limits_{j=1}^{r}d_{j}p_{j-1} is an integer. So Λ α ​ ( d) = { Ψ α ​ ( d) ​ α } \Lambda_{\alpha}(d)=\{\Psi_{\alpha}(d)\alpha\} modulo 1. But, we have seen that both terms are in [0, 1 [[0,1[, q.e.d. ■ \blacksquare

Remarks : result (ii) means that the map n → { n ​ α } n\to\{n\alpha\} ( with 0 ⩽ n < q r + 1 0\leqslant n<q_{r+1}), is, from the order point of view, the ” same thing” as the identity ( E α, R ​ L ​ O) → ( E α, A ​ L ​ O) (E_{\alpha},RLO)\to(E_{\alpha},ALO).

We can sum up these formulae : ∀ n ∈ { 0 ⋯ q r + 1 − 1 } \forall n\in\{0\cdots q_{r+1}-1\}, with d = Ψ α − 1 ​ ( n) d=\Psi_{\alpha}^{-1}(n):

 | n = ∑ j = 1 r d j ​ q j − 1; ⌊ n ​ α ⌋ = ∑ j = 1 r d j ​ p j − 1; { n ​ α } = ∑ j = 1 r ( − 1) j − 1 ​ d j ​ δ j − 1 n=\sum_{j=1}^{r}d_{j}q_{j-1}\hskip 8.5359pt;\hskip 8.5359pt\lfloor n\alpha\rfloor=\sum_{j=1}^{r}d_{j}p_{j-1}\hskip 8.5359pt;\hskip 8.5359pt\{n\alpha\}=\sum_{j=1}^{r}(-1)^{j-1}d_{j}\delta_{j-1} |  |

The following algorithm expresses the inverse function of Λ α \Lambda_{\alpha}.

###### Algorithm 2

let β ∈ { n q r + 1, n ∈ ℕ } \beta\in\{\frac{n}{q_{r+1}},n\in\mathbb{N}\}. Applying the algorithm below, we have :
(i) b ∈ E α b\in E_{\alpha}.
(ii) β = Λ α ​ ( b) \beta=\Lambda_{\alpha}(b).

Input: β \beta

Output: ( b i) i ∈ { 1 ⋯ r } (b_{i})_{i\in\{1\cdots r\}}

for*k ← 1 k\leftarrow 1 to r r*do

b k ← min ⁡ ( a k, ⌈ β δ k − 1 ⌉) b_{k}\leftarrow\min\left(a_{k},\left\lceil\frac{\beta}{\delta_{k-1}}\right\rceil\right);

β ← b k ​ δ k − 1 − β \beta\leftarrow b_{k}\delta_{k-1}-\beta end for

Proof :
First, we denote ( β k) k ∈ { 0 ⋯ r } (\beta_{k})_{k\in\{0\cdots r\}} the finite sequence defined by :

 | β 0 = β; ∀ k ∈ { 1 ⋯ r }, β k = b k δ k − 1 − β k − 1 \beta_{0}=\beta\hskip 8.5359pt;\hskip 8.5359pt\forall k\in\{1\cdots r\}\hskip 8.5359pt,\hskip 8.5359pt\beta_{k}=b_{k}\delta_{k-1}-\beta_{k-1} |  |

Thus, β k \beta_{k} is the value of β \beta after k k loops in Algorithm 2. So, we have :

 | b k = min ⁡ ( a k, ⌈ β k − 1 / δ k − 1 ⌉) b_{k}=\min(a_{k},\lceil\beta_{k-1}/\delta_{k-1}\rceil) |  |

(i) let us verify that b ∈ E α b\in E_{\alpha}: by induction on k k, we will prove that ” ( b 1, ⋯, b k) (b_{1},\cdots,b_{k}) is α \alpha -admissible and that − δ k < β k < δ k − 1 -\delta_{k}<\beta_{k}<\delta_{k-1} for all k ∈ { 0 ⋯ r } k\in\{0\cdots r\} ”.
- it is true for k = 0 k=0, since δ 0 = α > 0 \delta_{0}=\alpha>0 and δ − 1 = 1 \delta_{-1}=1.
- we suppose that it is true for k − 1 k-1 with k ∈ { 1 ⋯ r } k\in\{1\cdots r\}. Then, β k − 1 δ k − 1 > − 1 \frac{\beta_{k-1}}{\delta_{k-1}}>-1, so ⌈ β k − 1 δ k − 1 ⌉ ⩾ 0 \left\lceil\frac{\beta_{k-1}}{\delta_{k-1}}\right\rceil\geqslant 0 and 0 ⩽ b k ⩽ a k 0\leqslant b_{k}\leqslant a_{k}. If b k − 1 > 0 b_{k-1}>0, then ( b 1, ⋯, b k) (b_{1},\cdots,b_{k}) is α \alpha -admissible, for ( b 1, ⋯, b k − 1) ∈ E α (b_{1},\cdots,b_{k-1})\in E_{\alpha}. If b k − 1 = 0 b_{k-1}=0, then β k − 2 ⩽ 0 \beta_{k-2}\leqslant 0 and we have 2 cases :
▶ \blacktriangleright Case 1 : if β k − 2 = 0 \beta_{k-2}=0, then by obvious induction, β i = 0 \beta_{i}=0 and b i = 0 b_{i}=0 for all i ⩾ k − 1 i\geqslant k-1.
▶ \blacktriangleright Case 2 : else, we have β k − 2 < 0 \beta_{k-2}<0, so k ⩾ 3 k\geqslant 3 and :

 | β k − 3 = b k − 2 ​ δ k − 3 − β k − 2 > b k − 2 ​ δ k − 3 \beta_{k-3}=b_{k-2}\delta_{k-3}-\beta_{k-2}>b_{k-2}\delta_{k-3} |  |

So β k − 3 δ k − 3 > b k − 2 \frac{\beta_{k-3}}{\delta_{k-3}}>b_{k-2}, which leads to b k − 2 = a k − 2 b_{k-2}=a_{k-2}.
In these both cases, we have : ( b 1, ⋯, b k) (b_{1},\cdots,b_{k}) satisfies the conditions of E α E_{\alpha}.
Now : by induction hypothesis, we have :

 | − δ k − 1 < β k − 1 < δ k − 2 -\delta_{k-1}<\beta_{k-1}<\delta_{k-2} |  |

▶ \blacktriangleright Case 1 : if β k − 1 δ k − 1 ⩽ a k \frac{\beta_{k-1}}{\delta_{k-1}}\leqslant a_{k}, then : b k = ⌈ β k − 1 δ k − 1 ⌉ b_{k}=\left\lceil\frac{\beta_{k-1}}{\delta_{k-1}}\right\rceil so β k − 1 ⩽ b k ​ δ k − 1 \beta_{k-1}\leqslant b_{k}\delta_{k-1}, so β k ⩾ 0 \beta_{k}\geqslant 0 and b k < β k − 1 δ k − 1 + 1 b_{k}<\frac{\beta_{k-1}}{\delta_{k-1}}+1, so β k < δ k − 1 \beta_{k}<\delta_{k-1}.
▶ \blacktriangleright Case 2 : if β k − 1 δ k − 1 > a k \frac{\beta_{k-1}}{\delta_{k-1}}>a_{k}, then b k = a k b_{k}=a_{k} and β k < 0 \beta_{k}<0. Moreover :

 | β k = a k ​ δ k − 1 − β k − 1 > a k ​ δ k − 1 − δ k − 2 = − δ k \beta_{k}=a_{k}\delta_{k-1}-\beta_{k-1}>a_{k}\delta_{k-1}-\delta_{k-2}=-\delta_{k} |  |

(ii)

 | Λ α ​ ( b) = ∑ k = 1 r ( − 1) k ​ b k ​ δ k − 1 = ∑ k = 1 r ( ( − 1) k ​ β k − ( − 1) k − 1 ​ β k − 1) = ( − 1) r ​ β r − β \Lambda_{\alpha}(b)=\sum_{k=1}^{r}(-1)^{k}b_{k}\delta_{k-1}=\sum_{k=1}^{r}((-1)^{k}\beta_{k}-(-1)^{k-1}\beta_{k-1})=(-1)^{r}\beta_{r}-\beta |  |

we also have β = Λ α ​ ( b) + ( − 1) r ​ β r \beta=\Lambda_{\alpha}(b)+(-1)^{r}\beta_{r}. Now, − δ r < β r < δ r − 1 -\delta_{r}<\beta_{r}<\delta_{r-1}.
Claim : ” for every k ∈ { − 1 ⋯ r − 1 }, q r + 1 δ k k\in\{-1\cdots r-1\},q_{r+1}\delta_{k} is the k t ​ h k^{th} remainder, denoted ρ k \rho_{k} in the euclidean algorithm between p r + 1 p_{r+1} and q r + 1 q_{r+1} and we have ρ r − 1 = 1 \rho_{r-1}=1.”
Indeed, by double induction on k k:
- it is true for k = − 1 k=-1 and k = 0 k=0, since q r + 1 ​ δ − 1 = q r + 1 = ρ − 1 q_{r+1}\delta_{-1}=q_{r+1}=\rho_{-1} and q r + 1 ​ δ 0 = p r + 1 = ρ 0 q_{r+1}\delta_{0}=p_{r+1}=\rho_{0}.
- then, both sequences satisfy the same double induction formula :

 | ∀ k ∈ { 1 ⋯ r − 1 }, q r + 1 δ k = q r + 1 δ k − 2 − a k q r + 1 δ k − 1; ρ k = ρ k − 2 − a k ρ k − 1 \forall k\in\{1\cdots r-1\},q_{r+1}\delta_{k}=q_{r+1}\delta_{k-2}-a_{k}q_{r+1}\delta_{k-1}\hskip 8.5359pt;\hskip 8.5359pt\rho_{k}=\rho_{k-2}-a_{k}\rho_{k-1} |  |

Now, euclidean algorithm stops when we obtain a rest equal to 0, and the former rest is the greatest common divisor of ρ − 1 \rho_{-1} and ρ 0 \rho_{0}, namely 1 1 here, since the convergent fractions are reduced. So, ρ r − 1 = 1 \rho_{r-1}=1. But, we have chosen the continued fraction expansion of α \alpha, that ends with 1 1, so ρ r − 2 = a r + 1 \rho_{r-2}=a_{r}+1, and q r + 1 ​ δ r = ρ r − 2 − a r ​ ρ r − 1 = 1 q_{r+1}\delta_{r}=\rho_{r-2}-a_{r}\rho_{r-1}=1.
We conclude : δ r = δ r − 1 = 1 q r + 1 \delta_{r}=\delta_{r-1}=\frac{1}{q_{r+1}} and | β r | ∈ [0, 1 / q r + 1 [|\beta_{r}|\in[0,1/q_{r+1}[.
Now, the former facts show that β k ​ q r + 1 ∈ ℤ \beta_{k}q_{r+1}\in\mathbb{Z} for all k k, so : β r = 0 \beta_{r}=0. ■ \blacksquare

∙ \bullet We can easily extend this numeration to [0, 1 [[0,1[, by adding a last ” digit” that can range in [0, 1 [[0,1[. First, we extend the ALO to E α × [0, 1 [E_{\alpha}\times[0,1[: ( d, ϵ) ⩽ A ( d ′, ϵ ′) (d,\epsilon)\leqslant_{A}(d^{\prime},\epsilon^{\prime}) if and only if ( d = d ′ d=d^{\prime} and ϵ ⩽ ϵ ′ \epsilon\leqslant\epsilon^{\prime}) or d < A d ′ d<_{A}d^{\prime}.

###### Corollary 2

the map Λ ~ α \tilde{\Lambda}_{\alpha} is an order isomorphism, with ALO on E α × [0, 1 [E_{\alpha}\times[0,1[:

 | Λ ~ α: { E α × [0, 1 [→ [0, 1 [( d, ϵ) → ∑ j = 1 r d j ​ ( − 1) j − 1 ​ δ j − 1 + ϵ ​ δ r \tilde{\Lambda}_{\alpha}:\begin{cases}E_{\alpha}\times[0,1[\to[0,1[\\ (d,\epsilon)\to\sum\limits_{j=1}^{r}d_{j}(-1)^{j-1}\delta_{j-1}+\epsilon\delta_{r}\end{cases} |  |

Proof :
a direct consequence of Proposition 3. ■ \blacksquare

Remark : if Λ ~ α ​ ( d, ϵ) = β \tilde{\Lambda}_{\alpha}(d,\epsilon)=\beta then ϵ = { q r + 1 ​ β } \epsilon=\{q_{r+1}\beta\}, with usual notations.

### 2.3 α \alpha -numeration for an irrational α \alpha

∙ \bullet Let α \alpha be an irrational and [a k] k ∈ ℕ [a_{k}]_{k\in\mathbb{N}} its CFE. We extend our notion of α \alpha -admissible sequence :

###### Definition 4 ( α \alpha -admissible sequences)

.
a sequence d d in ℕ ℕ ∗ \mathbb{N}^{\mathbb{N}^{*}} is said *α \alpha -admissible*if and only if d d does not end with ( max, 0) ∞ (\max,0)^{\infty}, an infinite sequence of a k, 0, a k + 2, 0, ⋯ a_{k},0,a_{k+2},0,\cdots ( so to say there are an infinite number of even and odd indices k k such that d k > 0 d_{k}>0 or d k + 1 < a k d_{k+1}<a_{k}) and :

 | ∀ j ∈ ℕ ∗, { d j ∈ { 0 ⋯ a j } d j = 0 ⇒ ( ∀ i ⩾ j, d i = 0) or d j − 1 = a j − 1 \forall j\in\mathbb{N}^{*},\begin{cases}d_{j}\in\{0\cdots a_{j}\}\\ d_{j}=0\Rightarrow(\forall i\geqslant j,d_{i}=0)\text{ or }d_{j-1}=a_{j-1}\end{cases} |  |

Thus, the null-sequence is the only α \alpha -admissible sequence that begins with 0 0. We denote E α E_{\alpha} the set of α \alpha -admissible sequences and E ( α) E_{(\alpha)} the subset of E α E_{\alpha} of sequences, that ends with 0 ∞ 0^{\infty}, an infinite sequence of 0 0.

∙ \bullet We consider two lexicographic total order, respectively on E α E_{\alpha} and E ( α) E_{(\alpha)}:
- the reversed lexicographic order ( RLO) on E ( α) E_{(\alpha)}:

 | d ​ ⩽ 𝑅 ​ d ′ ⇔ d = d ′ ​ or ​ ∃ j ∈ ℕ ∗, { d j < d j ′ ∀ i > j, d i = d i ′ d\underset{R}{\leqslant}d^{\prime}\Leftrightarrow d=d^{\prime}\text{ or }\exists j\in\mathbb{N}^{*},\begin{cases}d_{j}<d^{\prime}_{j}\\ \forall i>j,d_{i}=d^{\prime}_{i}\end{cases} |  |

- the alternate lexicographic order ( ALO) on E α E_{\alpha}:

 | d ​ ⩽ 𝐴 ​ d ′ ⇔ d = d ′ ​ or ​ ∃ j ∈ ℕ ∗, { ( − 1) j − 1 ​ d j < ( − 1 j − 1 ​ d j ′ CLOSE ∀ i ∈ { 1 ⋯ j − 1 }, d i = d ′ i d\underset{A}{\leqslant}d^{\prime}\Leftrightarrow d=d^{\prime}\text{ or }\exists j\in\mathbb{N}^{*},\begin{cases}(-1)^{j-1}d_{j}<(-1^{j-1}d^{\prime}_{j}\\ \forall i\in\{1\cdots j-1\},d_{i}=d^{\prime}_{i}\end{cases} |  |

∙ \bullet We define :

 | ∀ i ∈ ℕ ∪ { − 1 }, δ i = ( − 1) i ​ ( q i ​ α − p i) \forall i\in\mathbb{N}\cup\{-1\}\hskip 8.5359pt,\hskip 8.5359pt\delta_{i}=(-1)^{i}(q_{i}\alpha-p_{i}) |  |

with, as usual p i / q i p_{i}/q_{i} being the reduced fraction of the convergent [a 0, ⋯, a i] [a_{0},\cdots,a_{i}]. We have then :

 | δ − 1 = 1; δ 0 = α; ∀ i ∈ ℕ ∗, δ i = − a i ​ δ i − 1 + δ i − 2 \delta_{-1}=1\hskip 8.5359pt;\hskip 8.5359pt\delta_{0}=\alpha\hskip 8.5359pt;\hskip 8.5359pt\forall i\in\mathbb{N}^{*}\hskip 8.5359pt,\hskip 8.5359pt\delta_{i}=-a_{i}\delta_{i-1}+\delta_{i-2} |  |

Let T T be the Gauss map : ] 0, 1 [\ ℚ →] 0, 1 [\ ℚ, x → { 1 / x }]0,1[\backslash\mathbb{Q}\to]0,1[\backslash\mathbb{Q},x\to\{1/x\}.
By induction on i i, with the fact that : a i = ⌊ 1 T i − 1 ​ ( α) ⌋ a_{i}=\left\lfloor\frac{1}{T^{i-1}(\alpha)}\right\rfloor if i ∈ ℕ ∗ i\in\mathbb{N}^{*}, we obtain :

 | ∀ i ∈ ℕ, δ i δ i − 1 = T i ​ ( α) \forall i\in\mathbb{N}\hskip 8.5359pt,\hskip 8.5359pt\frac{\delta_{i}}{\delta_{i-1}}=T^{i}(\alpha) |  |

( δ i) i ∈ ℕ (\delta_{i})_{i\in\mathbb{N}} is a decreasing and positive sequence, that converges towards 0 0.

###### Lemma 5

let d, d ′ ∈ E α d,d^{\prime}\in E_{\alpha} and j ∈ { 1 ⋯ r } j\in\{1\cdots r\}, , then :

 | ( − 1) j − 1 ​ ( d j ′ − d j) > 0 ⇒ ∑ i = j + 1 ∞ ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 < δ j − 1 (-1)^{j-1}(d^{\prime}_{j}-d_{j})>0\Rightarrow\sum\limits_{i=j+1}^{\infty}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}<\delta_{j-1} |  |

Proof :
We have 2 cases :
▶ \blacktriangleright Case 1 : if ( − 1) j + 1 ​ ( d j + 1 ′ − d j + 1) ⩽ a j + 1 − 1 (-1)^{j+1}(d^{\prime}_{j+1}-d_{j+1})\leqslant a_{j+1}-1, then :

 | ∑ i = j + 1 ∞ ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 ⩽ ( a j + 1 − 1) ​ δ j + ∑ i = j + 2 ∞ ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 \sum\limits_{i=j+1}^{\infty}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}\leqslant(a_{j+1}-1)\delta_{j}+\sum\limits_{i=j+2}^{\infty}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1} |  |

But, nor d d nor d ′ d^{\prime} ends with ( max, 0) ∞ (\max,0)^{\infty}, an infinite sequence of ” ( a k, 0) (a_{k},0) ”, so :

 | ∃ k > j + 1, ( − 1) k ​ ( d k ′ − d k) ​ < a k; ∀ i > ​ j, ( − 1) i ​ ( d i ′ − d i) ⩽ a i \exists k>j+1,(-1)^{k}(d^{\prime}_{k}-d_{k})<a_{k}\hskip 8.5359pt;\hskip 8.5359pt\forall i>j,(-1)^{i}(d^{\prime}_{i}-d_{i})\leqslant a_{i} |  |

We deduce :

 | ∑ i = j + 2 ∞ ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 < ∑ i = j + 2 ∞ a i ​ δ i − 1 = ∑ i = j + 2 ∞ ( δ i − 2 − δ i) = δ j + 1 + δ j \sum\limits_{i=j+2}^{\infty}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}<\sum\limits_{i=j+2}^{\infty}a_{i}\delta_{i-1}=\sum\limits_{i=j+2}^{\infty}(\delta_{i-2}-\delta_{i})=\delta_{j+1}+\delta_{j} |  |

We conclude :

 | ∑ i = j + 1 ∞ ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 < a j + 1 ​ δ j + δ j + 1 = δ j − 1 \sum\limits_{i=j+1}^{\infty}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}<a_{j+1}\delta_{j}+\delta_{j+1}=\delta_{j-1} |  |

▶ \blacktriangleright Case 2 : if ( − 1) j + 1 ​ ( d j + 1 ′ − d j + 1) = a j + 1 (-1)^{j+1}(d^{\prime}_{j+1}-d_{j+1})=a_{j+1}.
▶ ⁣ ▶ \blacktriangleright\blacktriangleright Subcase 1 : if j j is even, d j + 1 ′ = 0 d^{\prime}_{j+1}=0 and d j + 1 = a j + 1 d_{j+1}=a_{j+1}.
We can not have d j ′ = a j d^{\prime}_{j}=a_{j}, for ( − 1) j − 1 ​ d j < ( − 1) j − 1 ​ d j ′ (-1)^{j-1}d_{j}<(-1)^{j-1}d^{\prime}_{j}, so d i ′ = 0 d^{\prime}_{i}=0 for all i > j i>j and, since d d does not end with ( max, 0) ∞ (\max,0)^{\infty}, then :

 | ∑ i = j + 1 ∞ ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 = a j + 1 ​ δ j − ∑ i = j + 2 ∞ ( − 1) i ​ d i ​ δ i − 1 < ∑ p = 0 ∞ a j + 2 ​ p + 1 ​ δ j + 2 ​ p \sum\limits_{i=j+1}^{\infty}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}=a_{j+1}\delta_{j}-\sum_{i=j+2}^{\infty}(-1)^{i}d_{i}\delta_{i-1}<\sum_{p=0}^{\infty}a_{j+2p+1}\delta_{j+2p} |  |

Indeed, ( − 1) j + 2 ​ p ​ d j + 2 ​ p ​ δ j + 2 ​ p − 1 ⩾ 0 (-1)^{j+2p}d_{j+2p}\delta_{j+2p-1}\geqslant 0, for all p ∈ ℕ p\in\mathbb{N}, since j j is even. So :

 | ∑ i = j + 1 ∞ ( − 1) i ​ ( d i ′ − d i) ​ δ i − 1 < ∑ p = 0 ∞ ( δ j + 2 ​ p − 1 − δ j + 2 ​ p + 1) = δ j − 1 \sum\limits_{i=j+1}^{\infty}(-1)^{i}(d^{\prime}_{i}-d_{i})\delta_{i-1}<\sum_{p=0}^{\infty}(\delta_{j+2p-1}-\delta_{j+2p+1})=\delta_{j-1} |  |

▶ ⁣ ▶ \blacktriangleright\blacktriangleright Subcase 2 : if j j is odd, similar arguments lead to the same conclusion ( we swap d d and d ′ d^{\prime}). ■ \blacksquare

∙ \bullet Now, we define two maps on these sets :

###### Proposition 4

.
(i) the map Ψ α \Psi_{\alpha} ( defined below) is an order isomorphism from ( E ( α), ⩽ R) (E_{(\alpha)},\leqslant_{R}) to ( ℕ, ⩽) (\mathbb{N},\leqslant).

 | Ψ α: { E ( α) → ℕ d → ∑ j = 1 ∞ d j ​ q j − 1 \Psi_{\alpha}:\begin{cases}E_{(\alpha)}\to\mathbb{N}\\ d\to\sum\limits_{j=1}^{\infty}d_{j}q_{j-1}\end{cases} |  |

(ii) the map Λ α \Lambda_{\alpha} ( defined below) is an order isomorphism from ( E α, ⩽ A) (E_{\alpha},\leqslant_{A}) to ( [0, 1 [, ⩽) ([0,1[,\leqslant). :

 | Λ α: { E α → [0, 1) d → ∑ j = 1 ∞ d j ​ ( − 1) j − 1 ​ δ j − 1 \Lambda_{\alpha}:\begin{cases}E_{\alpha}\to[0,1)\\ d\to\sum\limits_{j=1}^{\infty}d_{j}(-1)^{j-1}\delta_{j-1}\end{cases} |  |

(iii) we have :

 | ∀ n ∈ ℕ, { n ​ α } = Λ α ​ ( Ψ α − 1 ​ ( n)) \forall n\in\mathbb{N},\{n\alpha\}=\Lambda_{\alpha}(\Psi_{\alpha}^{-1}(n)) |  |

Remark 1 : the infinite sum in the definition of Ψ α \Psi_{\alpha} is in fact a finite one. The infinite sum in the definition of Λ α \Lambda_{\alpha} is well defined since :

 | ∀ j ∈ ℕ ∗, 0 ⩽ d j ​ δ j − 1 ⩽ a j ​ δ j − 1 = δ j − 2 − δ j \forall j\in\mathbb{N}^{*},0\leqslant d_{j}\delta_{j-1}\leqslant a_{j}\delta_{j-1}=\delta_{j-2}-\delta_{j} |  |

Remark 2 : if we had defined E α E_{\alpha} without the restriction about the ending of the sequences, then the result about Λ α \Lambda_{\alpha} would have been valid, except that : for x ∈ { { n ​ α }, n ∈ ℕ } x\in\{\{n\alpha\},n\in\mathbb{N}\}, x x would have three ( two for 0 0) preimages : the one in E ( α) E_{(\alpha)} and those that end with ( max, 0) ∞ (\max,0)^{\infty}, an infinite sequence of ” a k, 0 a_{k},0 ”.

Proof :
(i) see proof of Lemma 3 and proof of Algorithm 1.
(ii) first, we will prove that Λ α \Lambda_{\alpha} is increasing : let d, d ′ ∈ E α d,d^{\prime}\in E_{\alpha} such that d < A d ′ d<_{A}d^{\prime}. Then, we have j ∈ ℕ ∗ j\in\mathbb{N}^{*} such that :

 | ( − 1) j − 1 ​ d j < ( − 1) j − 1 ​ d j ′ ​ and ​ ∀ i < j, d i = d i ′ (-1)^{j-1}d_{j}<(-1)^{j-1}d^{\prime}_{j}\hskip 8.5359pt\text{ and }\hskip 8.5359pt\forall i<j,d_{i}=d^{\prime}_{i} |  |

So :

 | Λ α ​ ( d ′) − Λ α ​ ( d) = ( − 1) j − 1 ​ ( d j ′ − d j) ​ δ j − 1 + ∑ i = j + 1 ∞ ( − 1) i − 1 ​ ( d i ′ − d i) ​ δ i − 1 \Lambda_{\alpha}(d^{\prime})-\Lambda_{\alpha}(d)=(-1)^{j-1}(d^{\prime}_{j}-d_{j})\delta_{j-1}+\sum_{i=j+1}^{\infty}(-1)^{i-1}(d^{\prime}_{i}-d_{i})\delta_{i-1} |  |

But, ( − 1) j − 1 ​ ( d j ′ − d j) ​ δ j − 1 ⩾ δ j − 1 (-1)^{j-1}(d^{\prime}_{j}-d_{j})\delta_{j-1}\geqslant\delta_{j-1}, so with Lemma 5, we obtain : Λ α ​ ( d ′) − Λ α ​ ( d) > 0 \Lambda_{\alpha}(d^{\prime})-\Lambda_{\alpha}(d)>0.
Now that we have proved that Λ α \Lambda_{\alpha} is increasing, we can easily deduce that Λ α ( E α) ⊂ [0, 1 [\Lambda_{\alpha}(E_{\alpha})\subset[0,1[: first, remark that ( 0, ⋯, 0) (0,\cdots,0) is the lowest element of E α E_{\alpha} ( with ALO), so Λ α ​ ( d) ⩾ 0 \Lambda_{\alpha}(d)\geqslant 0 for all d ∈ E α d\in E_{\alpha}. In addition, if j j is even ( − 1) j − 1 ​ d j ​ δ j − 1 ⩽ 0 (-1)^{j-1}d_{j}\delta_{j-1}\leqslant 0 and if j j is odd, say j = 2 ​ p + 1 j=2p+1, with p p a non negative integer, then ( − 1) j − 1 ​ d j ​ δ j − 1 ⩽ a 2 ​ p + 1 ​ δ 2 ​ p (-1)^{j-1}d_{j}\delta_{j-1}\leqslant a_{2p+1}\delta_{2p}, this inequality being strict for at least one p p, so :

 | ∀ d ∈ E α, Λ α ​ ( d) < ∑ p = 0 ∞ a 2 ​ p + 1 ​ δ 2 ​ p = ∑ p = 0 ∞ ( δ 2 ​ p − 1 − δ 2 ​ p + 1) = δ − 1 = 1 \forall d\in E_{\alpha},\Lambda_{\alpha}(d)<\sum_{p=0}^{\infty}a_{2p+1}\delta_{2p}=\sum_{p=0}^{\infty}(\delta_{2p-1}-\delta_{2p+1})=\delta_{-1}=1 |  |

For the surjectivity, we refer to Algorithm 3(ii) below.
(iii) see proof of Proposition 3(ii). ■ \blacksquare

###### Algorithm 3

.
(i) the inverse function of Ψ α \Psi_{\alpha} is defined by the following algorithm :
Let n ∈ ℕ n\in\mathbb{N} and r = max ⁡ ( { k ∈ ℕ, n < q k + q k − 1 }) r=\max(\{k\in\mathbb{N},n<q_{k}+q_{k-1}\}). We define d d by : ∀ k > r, d k = 0 \forall k>r,d_{k}=0 and

Input : n n Output : ( d i) i ∈ { 1 ⋯ r } (d_{i})_{i\in\{1\cdots r\}} for k = r k=r to k = 1 k=1 with step − 1 -1: { d k = max ⁡ ( 0, ⌊ n − q k − 2 q k − 1 ⌋) n ← n − d k ​ q k − 1 \begin{cases}d_{k}=\max\left(0,\left\lfloor\frac{n-q_{k-2}}{q_{k-1}}\right\rfloor\right)\\ n\leftarrow n-d_{k}q_{k-1}\end{cases}

(ii) the inverse function of Λ α \Lambda_{\alpha} is defined by the following ( infinite) ” algorithm” :
Let β ∈ [0, 1 [\beta\in[0,1[. We denote β 0 = β \beta_{0}=\beta and define the sequences b = ( b k) k ∈ ℕ ∗ b=(b_{k})_{k\in\mathbb{N}^{*}} and ( β k) k ∈ ℕ ∗ (\beta_{k})_{k\in\mathbb{N}^{*}} by :

Input : β \beta Output : ( b i) i ∈ ℕ ∗ (b_{i})_{i\in\mathbb{N}^{*}} for k = 1 k=1 to k = ∞ k=\infty with step 1 1: { b k = min ⁡ ( a k, ⌈ β k − 1 δ k − 1 ⌉) β k = b k ​ δ k − 1 − β k − 1 \begin{cases}b_{k}=\min\left(a_{k},\left\lceil\frac{\beta_{k-1}}{\delta_{k-1}}\right\rceil\right)\\ \beta_{k}=b_{k}\delta_{k-1}-\beta_{k-1}\end{cases}

Proof :
(i) see proof of Algorithm 1.
(ii) the proof that b ∈ E α b\in E_{\alpha} is the same as the proof of Algorithm 2, with the additional argument : b b does not end with ( max, 0) ∞ (\max,0)^{\infty}, an infinite sequence of ” ( a k, 0) (a_{k},0) ”, that will be shown below.
First, we remark that ( β k) k (\beta_{k})_{k} converges towards 0 0, for ( − 1) k ​ β k − ( − 1) k − 1 ​ β k − 1 = ( − 1) k ​ b k ​ δ k − 1 (-1)^{k}\beta_{k}-(-1)^{k-1}\beta_{k-1}=(-1)^{k}b_{k}\delta_{k-1} is the general term of a convergent serie. We can define β ′ = ∑ j = 1 ∞ b j ​ ( − 1) j − 1 ​ δ j − 1 \beta^{\prime}=\sum\limits_{j=1}^{\infty}b_{j}(-1)^{j-1}\delta_{j-1} and verify that β ′ = β \beta^{\prime}=\beta:

 | β ′ = ∑ j = 1 ∞ ( − 1) j − 1 ​ ( β j + β j − 1) = β 0 = β \beta^{\prime}=\sum_{j=1}^{\infty}(-1)^{j-1}(\beta_{j}+\beta_{j-1})=\beta_{0}=\beta |  |

Suppose that b b ends with ( max, 0) ∞ (\max,0)^{\infty}: this means that, we have r ∈ ℕ ∗ r\in\mathbb{N}^{*}, such that :

 | ( r = 1 ​ or ​ b r − 1 ≠ 0); ∀ p ∈ ℕ, b r + 2 ​ p = a r + 2 ​ p; b r + 2 ​ p + 1 = 0 (r=1\text{ or }b_{r-1}\not=0)\hskip 8.5359pt;\hskip 8.5359pt\forall p\in\mathbb{N},b_{r+2p}=a_{r+2p}\hskip 8.5359pt;\hskip 8.5359ptb_{r+2p+1}=0 |  |

So :

 | β = ∑ j = 1 r − 1 b j ​ ( − 1) j − 1 ​ δ j − 1 + ( − 1) r − 1 ​ ∑ p = 0 ∞ a r + 2 ​ p ​ δ r + 2 ​ p − 1 = ∑ j = 1 r − 1 b j ​ ( − 1) j − 1 ​ δ j − 1 + ( − 1) r − 1 ​ δ r − 2 \beta=\sum\limits_{j=1}^{r-1}b_{j}(-1)^{j-1}\delta_{j-1}+(-1)^{r-1}\sum_{p=0}^{\infty}a_{r+2p}\delta_{r+2p-1}=\sum\limits_{j=1}^{r-1}b_{j}(-1)^{j-1}\delta_{j-1}+(-1)^{r-1}\delta_{r-2} |  |

If r = 1 r=1, then β = δ − 1 = 1 \beta=\delta_{-1}=1, so r ⩾ 2 r\geqslant 2 and we recognize β = Λ α ​ ( b ′) \beta=\Lambda_{\alpha}(b^{\prime}), where b ′ = ( b 1, ⋯, b r − 2, b r − 1 − 1) ∈ E ( α) b^{\prime}=(b_{1},\cdots,b_{r-2},b_{r-1}-1)\in E_{(\alpha)}. Using the proof of Algorithm 2, we obtain β r − 1 = 0 \beta_{r-1}=0, so b b ends with an infinite sequence of ” 0 0 ”. ■ \blacksquare

We can sum up these formulae : for all non negative integers n n, if we denote d = Ψ α − 1 ​ ( n) d=\Psi_{\alpha}^{-1}(n):

 | n = ∑ j = 1 ∞ d j ​ q j − 1; ⌊ n ​ α ⌋ = ∑ j = 1 ∞ d j ​ p j − 1; { n ​ α } = ∑ j = 1 ∞ ( − 1) j − 1 ​ d j ​ δ j − 1 n=\sum_{j=1}^{\infty}d_{j}q_{j-1}\hskip 8.5359pt;\hskip 8.5359pt\lfloor n\alpha\rfloor=\sum_{j=1}^{\infty}d_{j}p_{j-1}\hskip 8.5359pt;\hskip 8.5359pt\{n\alpha\}=\sum_{j=1}^{\infty}(-1)^{j-1}d_{j}\delta_{j-1} |  |

Notations : if no ambiguity, we will denote n = ( d 1, d 2, ⋯, d s) α n=(d_{1},d_{2},\cdots,d_{s})_{\alpha} the Ψ α \Psi_{\alpha} -numeration of an integer n n and β = ( b 1, ⋯) α \beta=(b_{1},\cdots)_{\alpha} the Λ α \Lambda_{\alpha} -numeration of a real β \beta of [0, 1 [[0,1[.

Remark 1 : we denote ℕ α \mathbb{N}_{\alpha} the completion of ( ℕ, D) (\mathbb{N},D), where D D is the distance defined by :

 | ∀ n, n ′ ∈ ℕ, D ⁡ ( n, n ′) = | { n ′ ​ α } − { n ​ α } | \forall n,n^{\prime}\in\mathbb{N},\hskip 8.5359ptD(n,n^{\prime})=|\{n^{\prime}\alpha\}-\{n\alpha\}| |  |

Proposition 4 proves that ℕ α \mathbb{N}_{\alpha} can be represented ( bijectively) by E α E_{\alpha}: if n ∈ ℕ α n\in\mathbb{N}_{\alpha} is represented by d ∈ E α d\in E_{\alpha} then we could define : { n ​ α }:= ∑ j = 1 ∞ ( − 1) j − 1 ​ d j ​ δ j − 1 \{n\alpha\}:=\sum\limits_{j=1}^{\infty}(-1)^{j-1}d_{j}\delta_{j-1}. We obtain a bijective map :

 | ℕ α → [0, 1 [; n → { n α } \mathbb{N}_{\alpha}\to[0,1[\hskip 8.5359pt;\hskip 8.5359ptn\to\{n\alpha\} |  |

Remark 2 : in next subsection, we will study the effect of the symmetry β → 1 − β \beta\to 1-\beta on α \alpha -numeration of reals of [0, 1 [[0,1[. But now, we are interested in this symmetry acting both on α \alpha and β \beta, which gives a much simpler result :
- first, let α \alpha be a real in ] 0, 1 / 2 []0,1/2[and let us consider the CFE of α \alpha and 1 − α 1-\alpha:

 | α = [a k] k ∈ ℕ ⇒ 1 − α = [0, 1, a 1 − 1, a [2, ∞]] \alpha=[a_{k}]_{k\in\mathbb{N}}\hskip 8.5359pt\Rightarrow\hskip 8.5359pt1-\alpha=[0,1,a_{1}-1,a_{[2,\infty]}] |  |

Indeed, if we denote 1 − α = [a k ′] k ∈ ℕ, α 1 = [a [2, ∞]] 1-\alpha=[a^{\prime}_{k}]_{k\in\mathbb{N}},\alpha_{1}=[a_{[2,\infty]}] and α 1 ′ = [a [2, ∞] ′] \alpha^{\prime}_{1}=[a^{\prime}_{[2,\infty]}], then a 0 ′ = a 0 = 0, a 1 ′ = 1 a^{\prime}_{0}=a_{0}=0,a^{\prime}_{1}=1 and :

 | α = 1 a 1 + α 1; 1 − α = 1 1 + α 1 ′ \alpha=\frac{1}{a_{1}+\alpha_{1}}\hskip 8.5359pt;\hskip 8.5359pt1-\alpha=\frac{1}{1+\alpha^{\prime}_{1}} |  |

So :

 | α 1 ′ = 1 1 − α − 1 = 1 1 α − 1 = 1 a 1 − 1 + α 1 \alpha^{\prime}_{1}=\frac{1}{1-\alpha}-1=\frac{1}{\frac{1}{\alpha}-1}=\frac{1}{a_{1}-1+\alpha_{1}} |  |

- secondly : let α ∈] 0, 1 / 2 [, β ∈] 0, 1 [\alpha\in]0,1/2[,\beta\in]0,1[and ( b k) k (b_{k})_{k} its α \alpha -numeration, then :

 | 1 − β = ( 1, b 1 − 1, b [2, ∞]) 1 − α 1-\beta=(1,b_{1}-1,b_{[2,\infty]})_{1-\alpha} |  |

Indeed : if we denote δ i ′ \delta^{\prime}_{i} the analoguous of δ i \delta_{i} ( related to α \alpha) for 1 − α 1-\alpha ( see above), then :

 | δ − 1 ′ = 1; δ 0 ′ = 1 − α; ∀ i ⩾ 1, δ i ′ = δ i − 1 \delta^{\prime}_{-1}=1\hskip 8.5359pt;\hskip 8.5359pt\delta^{\prime}_{0}=1-\alpha\hskip 8.5359pt;\hskip 8.5359pt\forall i\geqslant 1,\hskip 8.5359pt\delta^{\prime}_{i}=\delta_{i-1} |  |

The last equality is obtained with obvious induction and previous result on CFE. Now, we just have to verify that :

 | δ 0 ′ − ( b 1 − 1) ​ δ 1 ′ + ∑ i ⩾ 2 ( − 1) i − 1 ​ b i − 1 ​ δ i − 1 ′ = 1 − β \delta^{\prime}_{0}-(b_{1}-1)\delta^{\prime}_{1}+\sum_{i\geqslant 2}(-1)^{i-1}b_{i-1}\delta^{\prime}_{i-1}=1-\beta |  |

that is an easy calculation…

### 2.4 α \alpha -numeration of negative integers

Let α \alpha be an irrational in ] 0, 1 []0,1[and [a k] k ∈ ℕ [a_{k}]_{k\in\mathbb{N}} its CFE. We have seen at 2.3 that E α E_{\alpha}, the set of α \alpha -admissible sequences is in bijective correspondance with [0, 1 [[0,1[, via the following map :

 | Λ α: d = ( d k) k ∈ ℕ ∗ → ∑ k = 1 ∞ d k ​ δ k − 1 ′ \Lambda_{\alpha}\hskip 8.5359pt:\hskip 8.5359ptd=(d_{k})_{k\in\mathbb{N}^{*}}\to\sum_{k=1}^{\infty}d_{k}\delta^{\prime}_{k-1} |  |

where δ ′ \delta^{\prime} is the sequence defined by :

 | δ − 1 ′ = − 1; δ 0 ′ = α; ∀ k ∈ ℕ ∗, δ k ′ = a k ​ δ k − 1 ′ + δ k − 2 ′ \delta^{\prime}_{-1}=-1\hskip 8.5359pt;\hskip 8.5359pt\delta^{\prime}_{0}=\alpha\hskip 8.5359pt;\hskip 8.5359pt\forall k\in\mathbb{N}^{*},\hskip 8.5359pt\delta^{\prime}_{k}=a_{k}\delta^{\prime}_{k-1}+\delta^{\prime}_{k-2} |  |

with notations of 2.3, we have :

 | ∀ k ∈ { − 1 ⋯ + ∞ }, δ k ′ = q k α − p k = ( − 1) k δ k \forall k\in\{-1\cdots+\infty\},\hskip 8.5359pt\delta^{\prime}_{k}=q_{k}\alpha-p_{k}=(-1)^{k}\delta_{k} |  |

In addition δ ′ \delta^{\prime} converges towards 0 0 and we could set δ ∞ ′ = 0 \delta^{\prime}_{\infty}=0.

In order to define the α \alpha -numeration of negative integers, we consider the natural involution of [0, 1 [[0,1[, that we denote C C: the complement to 1 1.

 | C: { C ⁡ ( 0) = 0 ∀ x ∈] 0, 1 [, C ⁡ ( x) = 1 − x C:\begin{cases}C(0)=0\\ \forall x\in]0,1[,C(x)=1-x\end{cases} |  |

We also have : ∀ x ∈ [0, 1 [, C ( x) = { − x } \forall x\in[0,1[,C(x)=\{-x\}. We can see C C as the usual conjugacy over the unit circle 𝕌 \mathbb{U}, the set of complex of moduli one, via the bijection : [0, 1 [→ 𝕌, x → e 2 ​ i ​ π ​ x [0,1[\to\mathbb{U},x\to e^{2i\pi x}. C C is decreasing, when restricted to ] 0, 1 []0,1[.

Question : is there a simple and natural expression of conjugate involution C α C_{\alpha} of E α E_{\alpha}, induced by C C, via Λ α \Lambda_{\alpha}, that is :

 | C α = Λ α − 1 ∘ C ∘ Λ α C_{\alpha}=\Lambda_{\alpha}^{-1}\circ C\circ\Lambda_{\alpha} |  |

Thinking of the analoguous problem for usual ( b k) k (b^{k})_{k} basis-numeration, where b b is an integer bigger than 1 1, we could try to use a kind of ” complement to ( a k) k ∈ ℕ ∗ (a_{k})_{k\in\mathbb{N}^{*}} ” transformation. Indeed, ( a k) k ∈ ℕ ∗ (a_{k})_{k\in\mathbb{N}^{*}} is the biggest sequence in E α E_{\alpha} for the usual lexicographic order. But, we also have to add 1 to the first digit, so, let m m be the following sequence :

 | m 1 = a 1 + 1; ∀ k > 1, m k = a k m_{1}=a_{1}+1\hskip 8.5359pt;\hskip 8.5359pt\forall k>1,\hskip 8.5359ptm_{k}=a_{k} |  |

We extend the definition of Ψ α \Psi_{\alpha} to all real sequences in l 1 ( δ ′) = { u ∈ ℝ ℕ ∗, ∑ k | u k δ k ′ | < + ∞ } l^{1}(\delta^{\prime})=\{u\in\mathbb{R}^{\mathbb{N}^{*}},\sum_{k}|u_{k}\delta^{\prime}_{k}|<+\infty\}.

 | L α: l 1 ​ ( δ ′) → ℝ; d → ∑ k = 1 ∞ d k ​ δ k − 1 ′ L_{\alpha}:l^{1}(\delta^{\prime})\to\mathbb{R};\hskip 8.5359ptd\to\sum_{k=1}^{\infty}d_{k}\delta^{\prime}_{k-1} |  |

Then, L α ​ ( m) = 1 L_{\alpha}(m)=1, for :

 | ∑ k = 1 ∞ m k ​ δ k − 1 ′ = α + ∑ k = 1 ∞ a k ​ δ k − 1 ′ = α + ∑ k = 1 ∞ ( δ k ′ − δ k − 2 ′) = α − δ − 1 ′ − δ 0 ′ = 1 \sum_{k=1}^{\infty}m_{k}\delta^{\prime}_{k-1}=\alpha+\sum_{k=1}^{\infty}a_{k}\delta^{\prime}_{k-1}=\alpha+\sum_{k=1}^{\infty}(\delta^{\prime}_{k}-\delta^{\prime}_{k-2})=\alpha-\delta^{\prime}_{-1}-\delta^{\prime}_{0}=1 |  |

Since L α L_{\alpha} is linear, we have :

 | ∀ d ∈ l 1 ​ ( δ ′), L α ​ ( m − d) = 1 − L α ​ ( d) \forall d\in l^{1}(\delta^{\prime}),\hskip 8.5359ptL_{\alpha}(m-d)=1-L_{\alpha}(d) |  |

In particular, for d ∈ E α d\in E_{\alpha}, we obtain : L α ​ ( m − d) = 1 − Ψ α ​ ( d) L_{\alpha}(m-d)=1-\Psi_{\alpha}(d). So, the question is : do we always have m − d ∈ E α m-d\in E_{\alpha}? Unfortunately, no. But, m − d ∈ E α m-d\in E_{\alpha} in most cases.
First, since d d does not end with ( max, 0) ∞ (\max,0)^{\infty} ( see 1.2), that is also the case for m − d m-d.
Secondly, if d d is not the null sequence, then m k − d k ∈ { 0 ⋯ a k } m_{k}-d_{k}\in\{0\cdots a_{k}\} for all k ∈ ℕ ∗ k\in\mathbb{N}^{*}, and m 1 − d 1 > 0 m_{1}-d_{1}>0.
Finally, the only case where d ∈ E α d\in E_{\alpha} and m − d ∉ E α m-d\not\in E_{\alpha} is when m − d m-d contains a finite word of consecutive 0 0, that is not preceeded by a maximal digit ( say d k = a k d_{k}=a_{k}) and that is not succeeded by a 0 0. We will name such a word, a *not admissible word*. Such a word can appear in m − d m-d, for d d can contain a word with consecutive maximal digits.
We will see below how to convert such a sequence into an α \alpha -admissible sequence. First, let ∼ \sim denote the equivalence relation on l 1 ​ ( δ ′) l^{1}(\delta^{\prime}), induced by L α L_{\alpha}:

 | ∀ u, v ∈ l 1 ​ ( δ ′), u ∼ v ⇔ L α ​ ( u) = L α ​ ( v) \forall u,v\in l^{1}(\delta^{\prime}),\hskip 8.5359ptu\sim v\Leftrightarrow L_{\alpha}(u)=L_{\alpha}(v) |  |

This relation ∼ \sim is compatible with the linear structure of l 1 ​ ( δ ′) l^{1}(\delta^{\prime}).

We have, for all r, s ∈ ℕ ∗ r,s\in\mathbb{N}^{*}:

 | ( 0 r, 1, ( max, 0) s − 1, max, − 1, 0 ∞) ∼ 0 ∞ ( 𝟏) (0^{r},1,(\max,0)^{s-1},\max,-1,0^{\infty})\sim 0^{\infty}\hskip 8.5359pt\hskip 8.5359pt\mathbf{(1)} |  |

Indeed :

 | L α ​ ( (,,,,,,,,,,,)) = δ r ′ + ∑ k = 1 s a r + 2 ​ k ​ δ r + 2 ​ k − 1 ′ − δ r + 2 ​ s ′ = L_{\alpha}((0^{r},1,(\max,0)^{s-1},\max,-1,0^{\infty}))=\delta^{\prime}_{r}+\sum_{k=1}^{s}a_{r+2k}\delta^{\prime}_{r+2k-1}-\delta^{\prime}_{r+2s}= |  |

 | = δ r ′ + ∑ k = 1 s ( δ r + 2 ​ k ′ − δ r + 2 ​ k − 2 ′) − δ r + 2 ​ s ′ = 0 =\delta^{\prime}_{r}+\sum_{k=1}^{s}(\delta^{\prime}_{r+2k}-\delta^{\prime}_{r+2k-2})-\delta^{\prime}_{r+2s}=0 |  |

Case 1 : a list of an even number of consecutive 0 0 ( not preceeded by a maximal digit and not succeeded by a 0 0). So, if we have a sequence ( e k) k (e_{k})_{k}, such that e [1, r] = [e 1, ⋯, e r] e_{[1,r]}=[e_{1},\cdots,e_{r}] only contains admissible words and such that e r ≠ a r, e r + 2 ​ s + 1 ≠ 0 e_{r}\not=a_{r},e_{r+2s+1}\not=0 and e k = 0 e_{k}=0 for k ∈ { r + 1 ⋯ r + 2 s } k\in\{r+1\cdots r+2s\} ( where r, s ∈ ℕ ∗ r,s\in\mathbb{N}^{*}).
Then, adding ( e k) k (e_{k})_{k} to relation (1), we obtain :

 | ( e k) k ⩾ 1 ∼ ( e [1, r], 1, ( max, 0) s − 1, max, e r + 2 ​ s + 1 − 1, e [r + 2 ​ s + 2, ∞]) (e_{k})_{k\geqslant 1}\sim(e_{[1,r]},1,(\max,0)^{s-1},\max,e_{r+2s+1}-1,e_{[r+2s+2,\infty]}) |  |

Thus, the new sequence ( e k ′) k (e^{\prime}_{k})_{k} only contains admissible words in its first r + 2 ​ s + 1 r+2s+1 digits.

Case 2 : a list of an odd number of consecutive 0 0 ( not preceeded by a maximal digit and not succeeded by a 0 0). So, if we have a sequence ( e k) k (e_{k})_{k}, such that e [1, r] e_{[1,r]} only contains admissible words and such that e r ≠ a r, e r + 2 ​ s ≠ 0 e_{r}\not=a_{r},e_{r+2s}\not=0 and e k = 0 e_{k}=0 for k ∈ { r + 1 ⋯ r + 2 s − 1 } k\in\{r+1\cdots r+2s-1\} ( r, s ∈ ℕ ∗ r,s\in\mathbb{N}^{*}).
Then, adding ( e k) k (e_{k})_{k} to relation (1) ( with r − 1 r-1 instead of r r), we obtain :

 | ( e k) k ⩾ 1 ∼ ( e [1, r − 1], e r + 1, ( max, 0) s − 1, max, e r + 2 ​ s − 1, e [r + 2 ​ s + 1, ∞]) (e_{k})_{k\geqslant 1}\sim(e_{[1,r-1]},e_{r}+1,(\max,0)^{s-1},\max,e_{r+2s}-1,e_{[r+2s+1,\infty]}) |  |

Thus, the new sequence ( e k ′) k (e^{\prime}_{k})_{k} does not contain any not admissible word in its first r + 2 ​ s r+2s digits.

In both cases, we have converted the not admissible word of ( e k) k (e_{k})_{k} into an admissible word, giving the same image for L α L_{\alpha}. This provides a ( possibly infinite) process to convert any not admissible element of m − E α m-E_{\alpha} into an element of E α E_{\alpha}. We only have to browse once the sequence ( e k) k (e_{k})_{k} to convert it into an equivalent α \alpha -admissible sequence :

Process of conversion :

let d d denote an α \alpha -admissible sequence that is not the null sequence and e = m − d e=m-d. Then e ∈ { 1 ⋯ a 1 } × ∏ k > 1 { 0 ⋯ a k } e\in\{1\cdots a_{1}\}\times\prod_{k>1}\{0\cdots a_{k}\}. We denote ( r j) j (r_{j})_{j} and ( s j) j (s_{j})_{j} the sequences of positive integers such that, the finite lists of consecutive 0 0 in e e are for indices from r j + 1 r_{j}+1 to r j + 2 ​ s j r_{j}+2s_{j} or r j + 2 ​ s j − 1 r_{j}+2s_{j}-1, depending on the parity of the lengths ( l j) j (l_{j})_{j} of these lists. We apply then the inductive following process : We suppose that we have converted the digits of e e for the indices k ⩽ r j k\leqslant r_{j}. Then : we can suppose that e r j < a j e_{r_{j}}<a_{j} ( if e r j = a j e_{r_{j}}=a_{j}, then we change r j ← r j + 1 r_{j}\leftarrow r_{j}+1) and e r + l j + 1 > 0 e_{r+l_{j}+1}>0. - Case 1 : if l j l_{j} is even, then : e ← ( e [1, r j], 1, ( max, 0) s j − 1, max, e r j + 2 ​ s j + 1 − 1, e [r j + 2 ​ s j + 2, ∞]) e\leftarrow(e_{[1,r_{j}]},1,(\max,0)^{s_{j}-1},\max,e_{r_{j}+2s_{j}+1}-1,e_{[r_{j}+2s_{j}+2,\infty]}) - Case 2 : if l j l_{j} is odd, then : e ← ( e [1, r j − 1], e r j + 1, ( max, 0) s j − 1, max, e r j + 2 ​ s j − 1, e [r j + 2 ​ s j + 1, ∞]) e\leftarrow(e_{[1,r_{j}-1]},e_{r_{j}}+1,(\max,0)^{s_{j}-1},\max,e_{r_{j}+2s_{j}}-1,e_{[r_{j}+2s_{j}+1,\infty]})

So, this process explicits the map C α C_{\alpha}, that is the relation between the α \alpha -numerations of β \beta and 1 − β 1-\beta for a real β ∈] 0, 1 [\beta\in]0,1[. We will name this map : *CFE-complement*.
Now, let us consider the particular case of β = { n ​ α } \beta=\{n\alpha\}, where n ∈ ℕ ∗ n\in\mathbb{N}^{*}. We have seen in 2.3 that n n and β \beta have the same α \alpha -numeration. Since { − n ​ α } = 1 − β \{-n\alpha\}=1-\beta, it is natural to define the α \alpha -numeration of − n -n as follows :

###### Definition 5 ( α \alpha -numeration of a negative integer)

.
for any positive integer n n, we define the α \alpha -numeration of − n -n as the CFE-complement of the α \alpha -numeration of n n.

Notations : we denote E ( α) c E^{c}_{(\alpha)} the subset of E α E_{\alpha} of sequences ending with max ∞ \max^{\infty}, that is to say :

 | E ( α) c = { e ∈ E α, ∃ k ∈ ℕ, ∀ i > k, e i = a i } E^{c}_{(\alpha)}=\{e\in E_{\alpha},\exists k\in\mathbb{N},\forall i>k,\hskip 8.5359pte_{i}=a_{i}\} |  |

We have then E ( α) c = C α ​ ( E ( α)) E^{c}_{(\alpha)}=C_{\alpha}(E_{(\alpha)}) and E ( α) c E^{c}_{(\alpha)} is the set of α \alpha -admissible sequences that ” α \alpha -numerate” negative integers ( see Proposition below).
We will also denote F α = E ( α) ∪ E ( α) c F_{\alpha}=E_{(\alpha)}\cup E^{c}_{(\alpha)} and we extend RLO, that we defined on E ( α) E_{(\alpha)}, to F α F_{\alpha}:

 | ∀ d, d ′ ∈ F α, d < R d ′ ⇔ ∃ k ∈ ℕ ∗, ( ( d k < d k ′, ∀ i > k, d i = d i ′) or ( ∀ i ⩾ k, d i = a i, d i ′ = 0)) \forall d,d^{\prime}\in F_{\alpha},\hskip 8.5359ptd<_{R}d^{\prime}\Leftrightarrow\exists k\in\mathbb{N}^{*},((d_{k}<d^{\prime}_{k},\forall i>k,d_{i}=d^{\prime}_{i})\text{ or }(\forall i\geqslant k,d_{i}=a_{i},d^{\prime}_{i}=0)) |  |

Remark : the above process of conversion is, in that frame, an algorithm, since an element of E ( α) c E^{c}_{(\alpha)} only contains a finite number of lists of consecutive 0 0.

###### Proposition 5

we can extend Ψ α \Psi_{\alpha} from E ( α) E_{(\alpha)} to F α F_{\alpha} as follows :

 | ∀ e ∈ E ( α) c, Ψ ~ α ​ ( e) = − 1 − ∑ k = 1 ∞ ( a k − e k) ​ q k − 1 \forall e\in E^{c}_{(\alpha)},\hskip 8.5359pt\widetilde{\Psi}_{\alpha}(e)=-1-\sum_{k=1}^{\infty}(a_{k}-e_{k})q_{k-1} |  |

hence, Ψ ~ α \widetilde{\Psi}_{\alpha} is an order isomorphisme from ( F α, ⩽ R) (F_{\alpha},\leqslant_{R}) to ( ℤ, ⩽) (\mathbb{Z},\leqslant) and we still have :

 | ∀ n ∈ ℤ, Λ α ​ ( Ψ ~ α − 1 ​ ( n)) = { n ​ α } \forall n\in\mathbb{Z},\hskip 8.5359pt\Lambda_{\alpha}(\widetilde{\Psi}_{\alpha}^{-1}(n))=\{n\alpha\} |  |

Proof :
- Formula and injectivity : let e ∈ E ( α) c e\in E^{c}_{(\alpha)}. First, we remark that the sum in the definition of Ψ ~ α ​ ( e) \widetilde{\Psi}_{\alpha}(e) is finite, since e k = a k e_{k}=a_{k} for k k large enough. Let denote d = m − e d=m-e and :

 | n = ∑ k = 1 ∞ d k ​ q k − 1; β = ∑ k = 1 ∞ d k ​ δ k − 1 ′ n=\sum_{k=1}^{\infty}d_{k}q_{k-1}\hskip 8.5359pt;\hskip 8.5359pt\beta=\sum_{k=1}^{\infty}d_{k}\delta^{\prime}_{k-1} |  |

Now, Ψ ~ α ​ ( e) = − n \widetilde{\Psi}_{\alpha}(e)=-n and n n is a positive integer ( d d ends with 0 ∞ 0^{\infty} and d 1 > 0 d_{1}>0), so Ψ ~ α ​ ( e) ∈ ℤ − ∗ \widetilde{\Psi}_{\alpha}(e)\in\mathbb{Z}_{-}^{*}.
But d d is not always in E ( α) E_{(\alpha)}. Nevertheless β ∈] 0, 1 [\beta\in]0,1[for :

 | β = L α ​ ( d) = L α ​ ( m) − L α ​ ( e) = 1 − Λ α ​ ( e) \beta=L_{\alpha}(d)=L_{\alpha}(m)-L_{\alpha}(e)=1-\Lambda_{\alpha}(e) |  |

indeed, e ∈ E α e\in E_{\alpha}. Finally :

 | n ​ α − β = ∑ k = 1 ∞ d k ​ p k − 1 ∈ ℕ n\alpha-\beta=\sum_{k=1}^{\infty}d_{k}p_{k-1}\in\mathbb{N} |  |

so : β = { n ​ α } \beta=\{n\alpha\}. We obtain : Λ α ​ ( e) = 1 − β = { − n ​ α } \Lambda_{\alpha}(e)=1-\beta=\{-n\alpha\}. We can conclude :

 | ∀ e ∈ F ( α), Λ α ​ ( e) = { Ψ ~ α ​ ( e) ​ α } ​ ( 1) \forall e\in F_{(\alpha)},\hskip 8.5359pt\Lambda_{\alpha}(e)=\{\widetilde{\Psi}_{\alpha}(e)\alpha\}\hskip 8.5359pt(1) |  |

Since, Λ α \Lambda_{\alpha} is injective, we deduce that Ψ ~ α \widetilde{\Psi}_{\alpha} is injective.
- Surjectivity : let n ∈ ℕ ∗, d = Ψ α − 1 ​ ( n) n\in\mathbb{N}^{*},d=\Psi_{\alpha}^{-1}(n) and e = Λ α − 1 ​ ( 1 − { n ​ α }) e=\Lambda_{\alpha}^{-1}(1-\{n\alpha\}). Then, e ∈ E ( α) c e\in E^{c}_{(\alpha)} ( see the beginning of this section) and, with (1) :

 | Λ α ​ ( e) = { Ψ ~ α ​ ( e) ​ α } = 1 − { n ​ α } = { − n ​ α } \Lambda_{\alpha}(e)=\{\widetilde{\Psi}_{\alpha}(e)\alpha\}=1-\{n\alpha\}=\{-n\alpha\} |  |

So, Ψ ~ α ​ ( e) = − n \widetilde{\Psi}_{\alpha}(e)=-n, for Ψ ~ α ​ ( e) ∈ ℤ \widetilde{\Psi}_{\alpha}(e)\in\mathbb{Z}. So, Ψ ~ α \widetilde{\Psi}_{\alpha} is surjective.
- Increase : let e, e ′ ∈ E ( α) c e,e^{\prime}\in E^{c}_{(\alpha)} such that e < R e ′ e<_{R}e^{\prime}.
— Case 1 : if e ∈ E ( α) c e\in E^{c}_{(\alpha)} and e ′ ∈ E ( α) e^{\prime}\in E_{(\alpha)}, then Ψ ~ α ​ ( e) < 0 ⩽ Ψ ~ α ​ ( e ′) \widetilde{\Psi}_{\alpha}(e)<0\leqslant\widetilde{\Psi}_{\alpha}(e^{\prime}).
— Case 2 : if e, e ′ ∈ E ( α) e,e^{\prime}\in E_{(\alpha)}, we have proved in Proposition 2 that Ψ α ​ ( e) < Ψ α ​ ( e ′) \Psi_{\alpha}(e)<\Psi_{\alpha}(e^{\prime}).
— Case 3 : if e, e ′ ∈ E ( α) c e,e^{\prime}\in E^{c}_{(\alpha)}, then :

 | Ψ ~ α ​ ( e ′) − Ψ ~ α ​ ( e) = ∑ k = 1 ∞ ( e k ′ − e k) ​ q k − 1 = Ψ α ​ ( d ′) − Ψ α ​ ( d) \widetilde{\Psi}_{\alpha}(e^{\prime})-\widetilde{\Psi}_{\alpha}(e)=\sum_{k=1}^{\infty}(e^{\prime}_{k}-e_{k})q_{k-1}=\Psi_{\alpha}(d^{\prime})-\Psi_{\alpha}(d) |  |

where d = ( ( e k) k ∈ { 1 ⋯ r }, 0 ∞) d=((e_{k})_{k\in\{1\cdots r\}},0^{\infty}) and d ′ = ( ( e k ′) k ∈ { 1 ⋯ r }, 0 ∞) d^{\prime}=((e^{\prime}_{k})_{k\in\{1\cdots r\}},0^{\infty}), the integer r r being such that e i ′ = e i = a i e^{\prime}_{i}=e_{i}=a_{i} for i > r i>r. Since e, e ′ e,e^{\prime} are α \alpha -admissible, we can claim that d, d ′ ∈ E ( α) d,d^{\prime}\in E_{(\alpha)}. So, with Proposition 2, Ψ α ​ ( d ′) − Ψ α ​ ( d) > 0 \Psi_{\alpha}(d^{\prime})-\Psi_{\alpha}(d)>0. So, Ψ ~ α ​ ( e ′) − Ψ ~ α ​ ( e) > 0 \widetilde{\Psi}_{\alpha}(e^{\prime})-\widetilde{\Psi}_{\alpha}(e)>0.
We have proved that Ψ ~ α \widetilde{\Psi}_{\alpha} is increasing on F α F_{\alpha}. ■ \blacksquare

Note that the definition of Ψ ~ α \widetilde{\Psi}_{\alpha} in Proposition 5 could be given by the same formula for d d in E ( α) E_{(\alpha)} and for d d in E ( α) c E^{c}_{(\alpha)}, with the following convention : + ∞ = 0 +\infty=0, so that q n → n → ∞ 0 q_{n}\xrightarrow[n\to\infty]{}0. Indeed, if we define :

 | ∀ d ∈ F α, Ψ α ​ ( d) = ∑ k = 1 ∞ d k ​ q k − 1 \forall d\in F_{\alpha},\hskip 8.5359pt\Psi_{\alpha}(d)=\sum_{k=1}^{\infty}d_{k}q_{k-1} |  |

then, it is convenient, since :

 | ∑ k = 1 ∞ a k ​ q k − 1 = ∑ k = 1 ∞ ( q k − q k − 2) = 0 + 0 − q 0 − q − 1 = − 1 \sum_{k=1}^{\infty}a_{k}q_{k-1}=\sum_{k=1}^{\infty}(q_{k}-q_{k-2})=0+0-q_{0}-q_{-1}=-1 |  |

We also have, with this convention a coherent result for both ” improper expansions” of an integer n n, herited from improper expansions of { n ​ α } \{n\alpha\} ( see remark 2, below Proposition 4), whose proper expansion is ( d 1, d 2, ⋯, d r) (d_{1},d_{2},\cdots,d_{r}) with d r > 0 d_{r}>0. Indeed, these improper expansions are ( d [1, r], 1, ( max, 0) ∞) (d_{[1,r]},1,(\max,0)^{\infty}) and ( d [1, r − 1], d r + 1, ( max, 0) ∞) (d_{[1,r-1]},d_{r}+1,(\max,0)^{\infty}) ( if d r < a r d_{r}<a_{r}) or ( d [1, r], 0, 1, ( max, 0) ∞) (d_{[1,r]},0,1,(\max,0)^{\infty}) ( if d r = a r d_{r}=a_{r}). Moreover :

 | ∀ s ∈ ℕ, ∑ j = 0 ∞ a s + 2 ​ j + 1 ​ q s + 2 ​ j = ∑ j = 0 ∞ ( q s + 2 ​ j + 1 − q s + 2 ​ j − 1) = 0 − q s − 1 \forall s\in\mathbb{N},\hskip 8.5359pt\sum_{j=0}^{\infty}a_{s+2j+1}q_{s+2j}=\sum_{j=0}^{\infty}(q_{s+2j+1}-q_{s+2j-1})=0-q_{s-1} |  |

## 3 Complements

### 3.1 dynamic generating α \alpha -numeration

∙ \bullet What follows is inspired by the analoguous result for the usual Ostrowski numeration made by Ito in [5]:

###### Proposition 6

let α \alpha be an irrational and [a k] k ∈ ℕ [a_{k}]_{k\in\mathbb{N}} its CFE. Let β ∈ [0, 1 [\beta\in[0,1[and ( b k) k (b_{k})_{k} its α \alpha -numeration. We have :

 | ∀ k ∈ ℕ ∗, ( a k, b k) = A ​ H k − 1 ​ ( α, β) \forall k\in\mathbb{N}^{*},\hskip 8.5359pt(a_{k},b_{k})=AH^{k-1}(\alpha,\beta) |  |

where H H is a self map of the open trapezoid U U defined by : for ( x, y) ∈ ℝ 2 (x,y)\in\mathbb{R}^{2}

 | ( x, y) ∈ U ⇔ { 0 < x < 1 − x < y < 1 (x,y)\in U\Leftrightarrow\begin{cases}0<x<1\\ -x<y<1\end{cases} |  |

 | H: ( x, y) → ( { 1 x }, min ⁡ ( ⌊ 1 x ⌋, ⌈ y x ⌉) − y x) H:(x,y)\to\left(\left\{\frac{1}{x}\right\},\min\left(\left\lfloor\frac{1}{x}\right\rfloor,\left\lceil\frac{y}{x}\right\rceil\right)-\frac{y}{x}\right) |  |

 | A: ( x, y) → ( ⌊ 1 x ⌋, min ⁡ ( ⌊ 1 x ⌋, ⌈ y x ⌉)) A:(x,y)\to\left(\left\lfloor\frac{1}{x}\right\rfloor,\min\left(\left\lfloor\frac{1}{x}\right\rfloor,\left\lceil\frac{y}{x}\right\rceil\right)\right) |  |

Remark 1 : we could prefer the following expressions, distinguishing two cases :

 | ∀ ( x, y) ∈ U, { A ( x, y) = ( ⌊ 1 / x ⌋, ⌈ y / x ⌉); H ( x, y) = ( { 1 / x }, { − y / x }) if y ⩽ x ⌊ 1 / x ⌋ A ( x, y) = ( ⌊ 1 / x ⌋, ⌊ 1 / x ⌋); H ( x, y) = ( { 1 / x }, { − y / x } − 1) else \forall(x,y)\in U,\hskip 8.5359pt\begin{cases}A(x,y)=(\lfloor 1/x\rfloor,\lceil y/x\rceil)\hskip 8.5359pt;\hskip 8.5359ptH(x,y)=(\{1/x\},\{-y/x\})\text{ if }y\leqslant x\lfloor 1/x\rfloor\\ A(x,y)=(\lfloor 1/x\rfloor,\lfloor 1/x\rfloor)\hskip 8.5359pt;\hskip 8.5359ptH(x,y)=(\{1/x\},\{-y/x\}-1)\text{ else }\end{cases} |  |

Indeed, if y > x ​ ⌊ 1 / x ⌋ y>x\lfloor 1/x\rfloor, then : ⌊ 1 / x ⌋ < y / x < 1 / x \lfloor 1/x\rfloor<y/x<1/x, so ⌊ 1 / x ⌋ = ⌈ y / x ⌉ − 1 \lfloor 1/x\rfloor=\lceil y/x\rceil-1.

Remark 2 : let us verify that H ⁡ ( U) ⊂ U H(U)\subset U: if y ⩽ x ​ ⌊ 1 / x ⌋ y\leqslant x\lfloor 1/x\rfloor, that is obvious. Else, { − y / x } − 1 = − { y / x } > − { 1 / x } \{-y/x\}-1=-\{y/x\}>-\{1/x\}, for ⌊ 1 / x ⌋ < y / x < 1 / x \lfloor 1/x\rfloor<y/x<1/x and so { y / x } < { 1 / x } \{y/x\}<\{1/x\} ( see remark 1).

Proof :
we denote ( α k, γ k) = H k ​ ( α, β) (\alpha_{k},\gamma_{k})=H^{k}(\alpha,\beta) for all k ∈ ℕ k\in\mathbb{N}. We avoid here the notation β k \beta_{k} for it is used below as reference to Algorithm 3.
We already know that a k = p x ​ ( A ​ H k − 1 ​ ( α, β)) a_{k}=p_{x}(AH^{k-1}(\alpha,\beta)), where p x: ( x, y) → x p_{x}:(x,y)\to x, since T ⁡ ( x) = p x ​ ( H ⁡ ( x, y)) T(x)=p_{x}(H(x,y)) for all x, y ∈] 0, 1 [x,y\in]0,1[( T T is the Gauss map, see 1.3). By definition, we have :

 | γ 0 = β; ∀ k ∈ ℕ ∗, γ k = min ⁡ ( a k, ⌈ γ k − 1 / α k − 1 ⌉) − γ k − 1 α k − 1 \gamma_{0}=\beta\hskip 8.5359pt;\hskip 8.5359pt\forall k\in\mathbb{N}^{*},\hskip 8.5359pt\gamma_{k}=\min(a_{k},\lceil\gamma_{k-1}/\alpha_{k-1}\rceil)-\frac{\gamma_{k-1}}{\alpha_{k-1}} |  |

We denote γ k ′ = β k δ k − 1 \gamma^{\prime}_{k}=\frac{\beta_{k}}{\delta_{k-1}}, with notations of Algorithm 3 ( see 2.3). We also have :

 | ∀ i ∈ ℕ, α i = T i ​ ( α) = δ i δ i − 1 ​ so ​ γ i ′ α i = β i δ i \forall i\in\mathbb{N},\hskip 8.5359pt\alpha_{i}=T^{i}(\alpha)=\frac{\delta_{i}}{\delta_{i-1}}\hskip 8.5359pt\text{ so }\hskip 8.5359pt\frac{\gamma^{\prime}_{i}}{\alpha_{i}}=\frac{\beta_{i}}{\delta_{i}} |  |

Thus, according to Algorithm 3 on reals :

 | ∀ k ∈ ℕ ∗, b k = min ⁡ ( a k, ⌈ β k − 1 / δ k − 1 ⌉); β k = b k ​ δ k − 1 − β k − 1 \forall k\in\mathbb{N}^{*},\hskip 8.5359ptb_{k}=\min(a_{k},\lceil\beta_{k-1}/\delta_{k-1}\rceil)\hskip 8.5359pt;\hskip 8.5359pt\beta_{k}=b_{k}\delta_{k-1}-\beta_{k-1} |  |

We deduce :

 | ∀ k ∈ ℕ ∗, γ k ′ = b k − γ k − 1 ′ α k − 1 \forall k\in\mathbb{N}^{*},\hskip 8.5359pt\gamma^{\prime}_{k}=b_{k}-\frac{\gamma^{\prime}_{k-1}}{\alpha_{k-1}} |  |

Yet, γ 0 ′ = β = γ 0 \gamma^{\prime}_{0}=\beta=\gamma_{0} and we obtain, by obvious induction : γ k = γ k ′ \gamma_{k}=\gamma^{\prime}_{k} for all integer k ∈ ℕ k\in\mathbb{N}. Then :

 | ∀ k ∈ ℕ ∗, b k = min ⁡ ( a k, ⌈ γ k − 1 / α k − 1 ⌉) \forall k\in\mathbb{N}^{*},\hskip 8.5359ptb_{k}=\min(a_{k},\lceil\gamma_{k-1}/\alpha_{k-1}\rceil) |  |

This ends the proof. ■ \blacksquare

### 3.2 α \alpha -germs and orbits of α \alpha -rotation

Our α \alpha -numeration is related to f α f_{\alpha}, the rotation on the circle ℝ / ℤ \mathbb{R}/\mathbb{Z} defined by :

 | ∀ x ∈ ℝ / ℤ, f α ​ ( x) = α + x ⁡ ( mod ​ 1) \forall x\in\mathbb{R}/\mathbb{Z},\hskip 8.5359ptf_{\alpha}(x)=\alpha+x\hskip 8.5359pt(\text{ mod }1) |  |

Let α \alpha be an irrational and [a k] k [a_{k}]_{k} its CFE. We know that f α f_{\alpha} is topologically transitive : its orbits are dense in X = ℝ / ℤ X=\mathbb{R}/\mathbb{Z}. Moreover, it is uniquely ergodic : there is only one f α f_{\alpha} -invariant ( and ergodic) measure on X X: the Lebesgue measure.
Now, we will explicit the conjugate of f α f_{\alpha} on E α E_{\alpha}, namely the map g α: E α → E α g_{\alpha}:E_{\alpha}\to E_{\alpha}, such that :

 | Λ α ∘ g α = f α ∘ Λ α \Lambda_{\alpha}\circ g_{\alpha}=f_{\alpha}\circ\Lambda_{\alpha} |  |

We remind some notations : E α E_{\alpha} is the set of α \alpha -admissible sequences and F α = E ( α) ∪ E ( α) c F_{\alpha}=E_{(\alpha)}\cup E^{c}_{(\alpha)}, where

 | E ( α) = { ( d k) k ∈ E α, ∃ n ∈ ℕ, ∀ k > n, d k = 0 }; E ( α) c = { ( d k) k ∈ E α, ∃ n ∈ ℕ, ∀ k > n, d k = a k } E_{(\alpha)}=\{(d_{k})_{k}\in E_{\alpha},\exists n\in\mathbb{N},\forall k>n,d_{k}=0\}\hskip 8.5359pt;\hskip 8.5359ptE^{c}_{(\alpha)}=\{(d_{k})_{k}\in E_{\alpha},\exists n\in\mathbb{N},\forall k>n,d_{k}=a_{k}\} |  |

We will use an equivalence relation on E α E_{\alpha}, that defines the notion of *germ*of a sequence :

 | ∀ d, d ′ ∈ E α, d ≂ d ′ ⇔ ∃ k ∈ ℕ, ∀ i > k, d i = d i ′ \forall d,d^{\prime}\in E_{\alpha},\hskip 8.5359ptd\eqsim d^{\prime}\Leftrightarrow\exists k\in\mathbb{N},\forall i>k,d_{i}=d^{\prime}_{i} |  |

We remark that the class of ( 0) (0) is E ( α) E_{(\alpha)} and that the class of ( a k) k ∈ ℕ ∗ (a_{k})_{k\in\mathbb{N}^{*}} is E ( α) c E^{c}_{(\alpha)}.
More generally, we can extend RLO to each class of germs of E α E_{\alpha}, as follows :

 | ( d k) k < R ( d k ′) k ⇔ ∃ j ∈ ℕ ∗, { d j < d j ′ ∀ k > j, d k = d k ′ (d_{k})_{k}<_{R}(d^{\prime}_{k})_{k}\Leftrightarrow\exists j\in\mathbb{N}^{*},\begin{cases}d_{j}<d^{\prime}_{j}\\ \forall k>j,d_{k}=d^{\prime}_{k}\end{cases} |  |

Remark : for each class of germs of E α E_{\alpha}, RLO is a total order and every element of the class has a successor ( except for E ( α) c E^{c}_{(\alpha)}, where ( a k) k ∈ ℕ ∗ (a_{k})_{k\in\mathbb{N}^{*}} is the maximal element) and a predecessor ( except for E ( α) E_{(\alpha)}, where ( 0) (0) is the minimal element).

∙ \bullet The following Proposition explicits the orbits of g α g_{\alpha}. Before that, we remark that : for β, β ′ ∈ ℝ / ℤ \beta,\beta^{\prime}\in\mathbb{R}/\mathbb{Z}, β \beta and β ′ \beta^{\prime} are in the same orbit of f α f_{\alpha} if and only if it exists n ∈ ℤ n\in\mathbb{Z}, such that β ′ − β = n ​ α \beta^{\prime}-\beta=n\alpha mod 1 1. So, an orbit of g α g_{\alpha} is the set of α \alpha -numerations of the { β + n ​ α }, n ∈ ℤ \{\beta+n\alpha\},n\in\mathbb{Z}, for some β ∈ [0, 1 [\beta\in[0,1[.

###### Proposition 7

Let α \alpha be an irrational, [a k] k [a_{k}]_{k} its CFE and g α g_{\alpha} defined as above, then :
(i) the orbits of g α g_{\alpha} are exactly the classes of germs of E α E_{\alpha}, except for the orbit of ( 0) (0), that is F α F_{\alpha}.
(ii) g α g_{\alpha} is the successor map on each of theses classes ( with RLO).

Proof :
First, the class of ( 0) (0), via g α g_{\alpha}, is F α F_{\alpha}, the set of α \alpha -numerations of the { n ​ α }, n ∈ ℤ \{n\alpha\},n\in\mathbb{Z}, as we have seen in previous subsection 3.1.
Let β ∈ [0, 1 [\beta\in[0,1[such that β ∉ { { n ​ α }, n ∈ ℤ } \beta\not\in\{\{n\alpha\},n\in\mathbb{Z}\}. We denote b = ( b k) k b=(b_{k})_{k} its α \alpha -numeration and C C the class of germ of b b in E α E_{\alpha}.
If b ′ ∈ C b^{\prime}\in C, then we have an integer r ∈ ℕ r\in\mathbb{N}, such that b i ′ = b i b^{\prime}_{i}=b_{i} for all integer i > r i>r. We denote β ′ = Λ α ​ ( b ′) \beta^{\prime}=\Lambda_{\alpha}(b^{\prime}), then :

 | β ′ − β = ∑ k = 1 r ( b k ′ − b k) ​ δ k − 1 ′ \beta^{\prime}-\beta=\sum_{k=1}^{r}(b^{\prime}_{k}-b_{k})\delta^{\prime}_{k-1} |  |

but, δ i ′ = α ​ q i − p i \delta^{\prime}_{i}=\alpha q_{i}-p_{i} and q i, p i q_{i},p_{i} are integer for all i ∈ ℕ i\in\mathbb{N}. So, β ′ − β ∈ ℤ + α ​ ℤ \beta^{\prime}-\beta\in\mathbb{Z}+\alpha\mathbb{Z} and we conclude that β ′ \beta^{\prime} is in the f α f_{\alpha} -orbit of β \beta and that b ′ b^{\prime} is in the g α g_{\alpha} -orbit of b b.
Conversely, suppose that b ′ b^{\prime} is in the g α g_{\alpha} -orbit of b b. We want to show that b b and b ′ b^{\prime} have the same germ. By obvious induction, it suffices to show that this is the case for b ′ = g α ​ ( b) b^{\prime}=g_{\alpha}(b), that is to say for β ′ = β + α \beta^{\prime}=\beta+\alpha. But, since b b is not ( a k) k (a_{k})_{k}, then there exists an index r r such that b r < a r b_{r}<a_{r}. We denote d = ( b [1, r], 0 ∞) d=(b_{[1,r]},0^{\infty}). Then, the successor of d d in ( E ( α), R ​ L ​ O) (E_{(\alpha)},RLO) is d ′ d^{\prime} such that d i ′ = 0 d^{\prime}_{i}=0 for all i > r i>r. We claim now that b ′ = ( d ( 1, r] ′, b [r + 1, ∞]) b^{\prime}=(d^{\prime}_{(1,r]},b_{[r+1,\infty]}). Indeed, b ′ ∈ E α b^{\prime}\in E_{\alpha} and :

 | Λ α ​ ( b ′) − Λ α ​ ( b) = Λ α ​ ( d ′) − Λ α ​ ( d) = α \Lambda_{\alpha}(b^{\prime})-\Lambda_{\alpha}(b)=\Lambda_{\alpha}(d^{\prime})-\Lambda_{\alpha}(d)=\alpha |  |

So, b ′ b^{\prime} and b b have the same germ.
By the way, we have also proved that g α g_{\alpha} is the successor map on the class of germ of b b. ■ \blacksquare

Remark 1 : this proves that ℝ / ( ℤ + α ​ ℤ) \mathbb{R}/(\mathbb{Z}+\alpha\mathbb{Z}) is represented, via our α \alpha -numeration Λ α \Lambda_{\alpha}, by germs of sequences of E α E_{\alpha}.

Remark 2 : we can define, on each orbit X X of f α f_{\alpha}, a natural order, which makes them isomorphic to ( ℤ, ⩽) (\mathbb{Z},\leqslant) ( but not canonically) :

 | ∀ x, x ′ ∈ X, x ⩽ x ′ ⇔ ∃ n ∈ ℕ, x ′ = f α n ​ ( x) \forall x,x^{\prime}\in X,x\leqslant x^{\prime}\Leftrightarrow\exists n\in\mathbb{N},x^{\prime}=f_{\alpha}^{n}(x) |  |

In the same way, each class of germ of ( E α, R ​ L ​ O) (E_{\alpha},RLO) ( except for the class of ( 0) (0), where we consider F α F_{\alpha}) is isomorphic to ( ℤ, ⩽) (\mathbb{Z},\leqslant).

∙ \bullet Now, we define, for any x x in ℝ, ‖ x ‖ \mathbb{R},||x||, the distance of x x to ℤ \mathbb{Z}. We also have : ‖ x ‖ = min ⁡ ( { x }, { − x }) ||x||=\min(\{x\},\{-x\}). Later, we define several maps on ℝ \mathbb{R} by : for all β ∈ ℝ \beta\in\mathbb{R}

 | D α ​ ( β) = lim inf n → + ∞ ​ ( n ​ ‖ n ​ α − β ‖); D α + ​ ( β) = lim inf n → + ∞ ​ ( n ⁡ { n ​ α − β }); D α − ​ ( β) = lim inf n → + ∞ ​ ( n ⁡ { β − n ​ α }) D_{\alpha}(\beta)=\underset{n\to+\infty}{\liminf}(n||n\alpha-\beta||)\hskip 8.5359pt;\hskip 8.5359ptD^{+}_{\alpha}(\beta)=\underset{n\to+\infty}{\liminf}(n\{n\alpha-\beta\})\hskip 8.5359pt;\hskip 8.5359ptD^{-}_{\alpha}(\beta)=\underset{n\to+\infty}{\liminf}(n\{\beta-n\alpha\}) |  |

Remark 3 : D α = min ⁡ ( D α +, D α −) D_{\alpha}=\min(D^{+}_{\alpha},D^{-}_{\alpha}), for lim inf \liminf ” respects” the min \min.

Remark 4 : these 3 maps are f α f_{\alpha} -invariant. Indeed, if x ∈ ℝ x\in\mathbb{R}, then :

 | ∀ n ∈ ℕ ∗, n ⁡ { n ​ α − ( x + α) } = { ( n − 1) ​ α − x } = j + 1 j × j ⁡ { j ​ α − x } \forall n\in\mathbb{N}^{*},\hskip 8.5359ptn\{n\alpha-(x+\alpha)\}=\{(n-1)\alpha-x\}=\frac{j+1}{j}\times j\{j\alpha-x\} |  |

where j = n − 1 j=n-1. But, j + 1 j \frac{j+1}{j} converges to 1 as j j tends to infinity, so the lim inf \liminf is the same…
This proves that these maps could be defined on ℝ / ( ℤ + α ​ ℤ) \mathbb{R}/(\mathbb{Z}+\alpha\mathbb{Z}), the additive group of orbits of f α f_{\alpha} and so they only depend on the germ of the α \alpha -numeration of β ∈ ℝ / ℤ \beta\in\mathbb{R}/\mathbb{Z}. In other words, these maps only depand on the asymptotic behaviour of the α \alpha -numeration of β \beta.

It is well known that D α ​ ( 0) D_{\alpha}(0) is null if and only if the sequence of partial quotients of α \alpha is unbounded and that D α ​ ( 0) D_{\alpha}(0) can be defined, restricting n n to the denominators of convergents of α \alpha. But, we have more precise results :

 | lim inf n → + ∞ ​ ( 1 a n + 2) ⩽ D α ​ ( 0) ⩽ lim inf n → + ∞ ​ ( 1 a n) \underset{n\to+\infty}{\liminf}\left(\frac{1}{a_{n}+2}\right)\leqslant D_{\alpha}(0)\leqslant\underset{n\to+\infty}{\liminf}\left(\frac{1}{a_{n}}\right) |  |

Moreover, Dirichlet’s theorem on diophantine approximation gives ( see [4]) :

 | ∀ β ∈ ℝ, D α ​ ( β) ⩽ 1 \forall\beta\in\mathbb{R},\hskip 8.5359ptD_{\alpha}(\beta)\leqslant 1 |  |

And Minkowski has proved that ( see [4] again) :

 | ∀ β ∈ ℝ \ ( ℤ + α ​ ℤ), min ⁡ ( D α ​ ( β), D α ​ ( 1 − β)) ⩽ 1 4 \forall\beta\in\mathbb{R}\backslash(\mathbb{Z}+\alpha\mathbb{Z}),\hskip 8.5359pt\min(D_{\alpha}(\beta),D_{\alpha}(1-\beta))\leqslant\frac{1}{4} |  |

In 4.3, we give some results that helps to compute D α + ​ ( β) D_{\alpha}^{+}(\beta) and D α − ​ ( β) D_{\alpha}^{-}(\beta), in relation to the α \alpha -numeration of β \beta.

### 3.3 shift and inductive structure

∙ \bullet Let α \alpha be a real in [0, 1 [[0,1[and [0, a 1, a 2, ⋯] [0,a_{1},a_{2},\cdots] its CFE. We denote a = ( a 1, ⋯) a=(a_{1},\cdots) and σ \sigma the usual shift on sequences. We have seen that : if α \alpha is not null, then [0, σ ⁡ ( a)] [0,\sigma(a)] is the CFE of T 1 ​ ( α) T_{1}(\alpha), where T 1 T_{1} is an extension of the Gauss map, described in 1.3. We recall that μ ⁡ ( α) = + ∞ \mu(\alpha)=+\infty if α \alpha is not rational and μ ⁡ ( α) = r \mu(\alpha)=r if α \alpha is rational and its CFE is [0, a 1, ⋯, a r, 1] [0,a_{1},\cdots,a_{r},1]. We define inductively the sequence : ( α k) k (\alpha_{k})_{k} by :

 | α 0 = α; ∀ k ∈ { 1 ⋯ μ ( α) }, α k = { 1 α k − 1 } \alpha_{0}=\alpha\hskip 8.5359pt;\hskip 8.5359pt\forall k\in\{1\cdots\mu(\alpha)\},\hskip 8.5359pt\alpha_{k}=\left\{\frac{1}{\alpha_{k-1}}\right\} |  |

With the remark above, we obtain :

 | ∀ k ∈ { 0 ⋯ μ ( α) − 1 }, α k = [0, a k + 1, ⋯] = [0, σ k ( a)] \forall k\in\{0\cdots\mu(\alpha)-1\},\hskip 8.5359pt\alpha_{k}=[0,a_{k+1},\cdots]=[0,\sigma^{k}(a)] |  |

Moreover, if α \alpha is rational and r = μ ⁡ ( α) r=\mu(\alpha), then α r = 0 \alpha_{r}=0, for α r − 1 = [0, a r, 1] = 1 a r + 1 \alpha_{r-1}=[0,a_{r},1]=\frac{1}{a_{r}+1}.

According to the definition of the sets ( E α k) k (E_{\alpha_{k}})_{k}, we can claim :

 | ∀ b ∈ E α, ∀ k ∈ ℕ, ( σ k ( b) ∈ E α k ⇔ b k + 1 ≠ 0 or σ k ( b) = ( 0)) \forall b\in E_{\alpha},\forall k\in\mathbb{N},(\sigma^{k}(b)\in E_{\alpha_{k}}\Leftrightarrow b_{k+1}\not=0\text{ or }\sigma^{k}(b)=(0)) |  |

In particular :

 | E T ⁡ ( α) ⊂ σ ⁡ ( E α) ​ and ​ σ ​ ( E α) \ E T ⁡ ( α) = { 0 } × ( E T 2 ​ ( α) \ { ( 0) }) E_{T(\alpha)}\subset\sigma(E_{\alpha})\hskip 8.5359pt\text{ and }\hskip 8.5359pt\sigma(E_{\alpha})\backslash E_{T(\alpha)}=\{0\}\times(E_{T^{2}(\alpha)}\backslash\{(0)\}) |  |

In addition, if we denote for any k ∈ { 0 ⋯ a 1 − 1 } k\in\{0\cdots a_{1}-1\}:
- E α, k E_{\alpha,k}: the set of α \alpha -admissible sequences whose first digit is k k. We have E α, 0 = { ( 0) } E_{\alpha,0}=\{(0)\}.
- E α, a 1 E_{\alpha,a_{1}}: the set of α \alpha -admissible sequences whose first digit is a 1 a_{1} and second is non null, except for ( a 1, 0, 0, ⋯) (a_{1},0,0,\cdots), that is in this set.
- E α, a 1 ′ E^{\prime}_{\alpha,a_{1}}: the set of α \alpha -admissible sequences whose first digit is a 1 a_{1} and second is null, except for ( a 1, 0, 0, ⋯) (a_{1},0,0,\cdots), that is not in this set.

( E α, k) k ∈ { 0 ⋯ a 1 } ∪ E α, a 1 ′ (E_{\alpha,k})_{k\in\{0\cdots a_{1}\}}\cup E^{\prime}_{\alpha,a_{1}} is clearly a partition of E α E_{\alpha} and ALO induces an order on these subsets : ( where B < A B ′ B<_{A}B^{\prime} means that for every b ∈ B b\in B and b ′ ∈ B ′ b^{\prime}\in B^{\prime}, we have b < A b ′ b<_{A}b^{\prime})

 | E α, 0 < A E α, 1 < A E α, 2 < A ⋯ < A E α, a 1 < A E ′ α, a 1 E_{\alpha,0}<_{A}E_{\alpha,1}<_{A}E_{\alpha,2}<_{A}\cdots<_{A}E_{\alpha,a_{1}}<_{A}E^{\prime}_{\alpha,a_{1}} |  |

###### Lemma 6

.
(i) for any k ∈ { 1 ⋯ a 1 } k\in\{1\cdots a_{1}\}, the map ( see below) is a bijective decreasing map ( induced by σ \sigma).

 | σ k: { ( E α, k, ⩽ A) → ( E T ⁡ ( α), ⩽ A) ( k, d [2, ∞]) → ( d [2, ∞]) \sigma_{k}:\begin{cases}(E_{\alpha,k},\leqslant_{A})\to(E_{T(\alpha)},\leqslant_{A})\\ (k,d_{[2,\infty]})\to(d_{[2,\infty]})\end{cases} |  |

(ii) the map ( see below) is a bijective increasing map ( induced by σ 2 \sigma^{2}).

 | σ ( 2): { ( E ′ α, a 1, ⩽ A) → ( E T 2 ​ ( α) \ { ( 0) }, ⩽ A) ( a 1, 0, d [3, ∞]) → ( d [3, ∞]) \sigma^{(2)}:\begin{cases}(E^{\prime}_{\alpha,a_{1}},\leqslant_{A})\to(E_{T^{2}(\alpha)}\backslash\{(0)\},\leqslant_{A})\\ (a_{1},0,d_{[3,\infty]})\to(d_{[3,\infty]})\end{cases} |  |

Proof :
direct consequence of former remarks and definition of sets E α E_{\alpha} and ALO. ■ \blacksquare

So to say, ( E α, < A) (E_{\alpha},<_{A}) consists in one null element, followed by a 1 a_{1} ordered copies of ( E T ⁡ ( α), < A ′) (E_{T(\alpha)},<_{A^{\prime}}) and, at the end a copy of ( E T 2 ​ ( α) \ { ( 0) }, < A) (E_{T^{2}(\alpha)}\backslash\{(0)\},<_{A}), where < A ′ <_{A^{\prime}} denotes inversed ALO.

We deduce a result on Kronecker sequences :

###### Corollary 3

let α \alpha be a real in [0, 1 [[0,1[, T T the usual Gauss map x → { 1 / x } x\to\{1/x\}.
We denote a 1 = ⌊ 1 / α ⌋ a_{1}=\lfloor 1/\alpha\rfloor and K α = { { k ​ α }, k ∈ ℕ } K_{\alpha}=\{\{k\alpha\},k\in\mathbb{N}\}.
The following union are disjoint :

 | K α = α ( { 0 } ∪ ⋃ j ∈ { 1 ⋯ a 1 } ( j − K T ⁡ ( α)) ∪ ( a 1 + T ( α) ( K T 2 ​ ( α) \ { 0 })) K_{\alpha}=\alpha\left(\{0\}\cup\bigcup_{j\in\{1\cdots a_{1}\}}(j-K_{T(\alpha)})\cup(a_{1}+T(\alpha)(K_{T^{2}(\alpha)}\backslash\{0\})\right) |  |

Proof :
direct consequence of Lemma 6 ■ \blacksquare

∙ \bullet Now, we would like to specify the effect of the shift on the integers and reals of [0, 1 [[0,1[, via their α \alpha or T ⁡ ( α) T(\alpha) -numerations.

We define a sequence of integers ( ν k) k (\nu_{k})_{k} by :

 | ν 0 = ν; ∀ k ∈ { 1 ⋯ μ ( α) − 2 }, ν k = { ⌊ ν k − 1 ​ α k − 1 ⌋ ​ if ​ n k + 1 ≠ 0 ​ or ​ σ k ​ ( n) = ( 0) ⌊ ν k − 1 ​ α k − 1 ⌋ + 1 ​ else \nu_{0}=\nu\hskip 8.5359pt;\hskip 8.5359pt\forall k\in\{1\cdots\mu(\alpha)-2\},\hskip 8.5359pt\nu_{k}=\begin{cases}\lfloor\nu_{k-1}\alpha_{k-1}\rfloor\text{ if }n_{k+1}\not=0\text{ or }\sigma^{k}(n)=(0)\\ \lfloor\nu_{k-1}\alpha_{k-1}\rfloor+1\text{ else }\end{cases} |  |

###### Lemma 7

let k ∈ { 0 ⋯ μ ( α) − 2 } k\in\{0\cdots\mu(\alpha)-2\} and n = ( n i) i n=(n_{i})_{i} the α \alpha -numeration of ν \nu ( we denote ν = ( n) α \nu=(n)_{\alpha} for example these numeration…)
⊳ \triangleright Case 1 : if n k + 1 ≠ 0 n_{k+1}\not=0 or σ k ​ ( n) = ( 0) \sigma^{k}(n)=(0), then ν k = ( n [k + 1, ∞]) α k = σ k ​ ( n) α k \nu_{k}=(n_{[k+1,\infty]})_{\alpha_{k}}=\sigma^{k}(n)_{\alpha_{k}}.
⊳ \triangleright Case 2 : else ν k = ( 1, n [k + 2, ∞]) α k = ( 1, σ k + 1 ​ ( n)) α k \nu_{k}=(1,n_{[k+2,\infty]})_{\alpha_{k}}=(1,\sigma^{k+1}(n))_{\alpha_{k}}.

Proof :
we will denote p k ​ ( x) p_{k}(x) and q k ​ ( x) q_{k}(x) for the reduced of the k t ​ h k^{th} convergent of a real x x, for any non negative integer k k and [a 0 ​ ( x), a 1 ​ ( x), ⋯, a k ​ ( x), …] [a_{0}(x),a_{1}(x),\cdots,a_{k}(x),...] its CFE. We have remarked that, if we denote T ⁡ ( x) = { 1 { x } } T(x)=\left\{\frac{1}{\{x\}}\right\}, then :

 | ∀ j ∈ ℕ ∗, a j ​ ( T ⁡ ( x)) = a j + 1 ​ ( x) \forall j\in\mathbb{N}^{*},a_{j}(T(x))=a_{j+1}(x) |  |

By obvious induction, we can deduce that :

 | ∀ x ∈ [0, 1 [, ∀ j ∈ ℕ, q j − 1 ( T ( x)) = p j ( x) ( 1) \forall x\in[0,1[,\forall j\in\mathbb{N},\hskip 8.5359ptq_{j-1}(T(x))=p_{j}(x)\hskip 8.5359pt\hskip 8.5359pt(1) |  |

We denote r = μ ⁡ ( α) r=\mu(\alpha). Now, we will use an induction on k ∈ { 0 ⋯ r − 2 } k\in\{0\cdots r-2\}. Result (i) is true for k = 0 k=0 ( we are in Case 1) . Suppose it is true for k − 1 k-1, where k ∈ { 1 ⋯ r − 2 } k\in\{1\cdots r-2\}, then :

 | ν k − 1 = ( n k ′, n [k + 1, r]) α k − 1 = ( n k ′, σ k ​ ( n)) \nu_{k-1}=(n^{\prime}_{k},n_{[k+1,r]})_{\alpha_{k-1}}=(n^{\prime}_{k},\sigma^{k}(n)) |  |

with n k ′ = 1 n^{\prime}_{k}=1 or n k n_{k}, but n k ′ > 0 n^{\prime}_{k}>0 in all cases.
▶ \blacktriangleright Case 1 : if n k + 1 ≠ 0 n_{k+1}\not=0 or σ k ​ ( n) = ( 0) \sigma^{k}(n)=(0), then : with the formula that follows the proof of Algorithm 3 and ( 1) (1):

 | ν k = ⌊ ν k − 1 ​ α k − 1 ⌋ = n k ′ ​ p 0 ​ ( α k − 1) + ∑ j = k + 1 r n j ​ p j − k ​ ( α k − 1) = ∑ j = k + 1 r n j ​ q j − k − 1 ​ ( α k) \nu_{k}=\lfloor\nu_{k-1}\alpha_{k-1}\rfloor=n^{\prime}_{k}p_{0}(\alpha_{k-1})+\sum_{j=k+1}^{r}n_{j}p_{j-k}(\alpha_{k-1})=\sum_{j=k+1}^{r}n_{j}q_{j-k-1}(\alpha_{k}) |  |

For p 0 ​ ( α k − 1) = 0 p_{0}(\alpha_{k-1})=0. So we obtain the α k \alpha_{k} -numeration of ν k \nu_{k}: it is σ k ​ ( n) \sigma^{k}(n) for σ k ​ ( n) ∈ E ( α k) \sigma^{k}(n)\in E_{(\alpha_{k})}.

▶ \blacktriangleright Case 2 : if n k + 1 = 0 n_{k+1}=0 and n k + 2 ≠ 0 n_{k+2}\not=0, then ( n [k + 1, ∞]) ∉ E α k (n_{[k+1,\infty]})\not\in E_{\alpha_{k}}, but :

 | ν k = q 0 + ∑ j = k + 2 r n j ​ q j − k − 1 ​ ( α k) \nu_{k}=q_{0}+\sum_{j=k+2}^{r}n_{j}q_{j-k-1}(\alpha_{k}) |  |

So we obtain the α k \alpha_{k} -numeration of ν k \nu_{k}: it is ( 1, n [k + 2, ∞]) (1,n_{[k+2,\infty]}) for it is in E ( α k) E_{(\alpha_{k})}. ■ \blacksquare

We also define a sequence ( γ k) k (\gamma_{k})_{k} of reals :

 | γ 0 = β; ∀ k ∈ { 1 ⋯ μ ( α) }, γ k = 1 α k − 1 ( b k α k − 1 − γ k − 1) \gamma_{0}=\beta\hskip 8.5359pt;\hskip 8.5359pt\forall k\in\{1\cdots\mu(\alpha)\},\gamma_{k}=\frac{1}{\alpha_{k-1}}(b_{k}\alpha_{k-1}-\gamma_{k-1}) |  |

###### Lemma 8

let k ∈ { 0 ⋯ μ ( α) − 2 } k\in\{0\cdots\mu(\alpha)-2\}.
⊳ \triangleright Case 1 : if b k + 1 ≠ 0 b_{k+1}\not=0 or σ k ​ ( b) = ( 0) \sigma^{k}(b)=(0), then γ k = ( b [k + 1, ∞]) α k = σ k ​ ( b) α k \gamma_{k}=(b_{[k+1,\infty]})_{\alpha_{k}}=\sigma^{k}(b)_{\alpha_{k}}.
⊳ \triangleright Case 2 : else γ k < 0 \gamma_{k}<0 and γ k + 1 = ( b [k + 2, ∞]) α k + 1 = σ k + 1 ​ ( b) α k + 1 \gamma_{k+1}=(b_{[k+2,\infty]})_{\alpha_{k+1}}=\sigma^{k+1}(b)_{\alpha_{k+1}}.

Proof :
we will use same notations as in previous proof. First, we remark that ( by obvious induction) :

 | ∀ x ∈] 0, 1 [, ∀ i ∈ ℕ, q i ​ ( x) = a 1 ​ ( x) ​ q i − 1 ​ ( T ⁡ ( x)) + p i − 1 ​ ( T ⁡ ( x)); p i ​ ( x) = q i − 1 ​ ( T ⁡ ( x)) \forall x\in]0,1[,\forall i\in\mathbb{N},\hskip 8.5359ptq_{i}(x)=a_{1}(x)q_{i-1}(T(x))+p_{i-1}(T(x))\hskip 8.5359pt;\hskip 8.5359ptp_{i}(x)=q_{i-1}(T(x)) |  |

We denote r = μ ⁡ ( α) r=\mu(\alpha) and argue with induction on k k. It is clear for k = 0 k=0. Suppose it is true for k − 1 k-1, with k ∈ { 1 ⋯ r − 2 } k\in\{1\cdots r-2\}.
— if b k ≠ 0 b_{k}\not=0 or σ k − 1 ​ ( b) = ( 0) \sigma^{k-1}(b)=(0), then γ k − 1 = ( b [k, ∞]) α k − 1 \gamma_{k-1}=(b_{[k,\infty]})_{\alpha_{k-1}}. So :

 | γ k − 1 = ∑ j = k r b j ​ [α k − 1 ​ q j − k ​ ( α k − 1) − p j − k ​ ( α k − 1)] = ∑ j = k r b j ​ [α k − 1 ​ ( a k ​ q j − k − 1 ​ ( α k) + p j − k − 1 ​ ( α k)) − q j − k − 1 ​ ( α k)] \gamma_{k-1}=\sum_{j=k}^{r}b_{j}[\alpha_{k-1}q_{j-k}(\alpha_{k-1})-p_{j-k}(\alpha_{k-1})]=\sum_{j=k}^{r}b_{j}[\alpha_{k-1}(a_{k}q_{j-k-1}(\alpha_{k})+p_{j-k-1}(\alpha_{k}))-q_{j-k-1}(\alpha_{k})] |  |

The term of the above sum for j = k j=k is equal to b k ​ α k − 1 b_{k}\alpha_{k-1}, so :

 | γ k = 1 α k − 1 ​ ( b k ​ α k − 1 − γ k − 1) = ∑ j = k + 1 r b j ​ [q j − k − 1 ​ ( α k) α k − 1 − ( a k ​ q j − k − 1 ​ ( α k) + p j − k − 1 ​ ( α k))] \gamma_{k}=\frac{1}{\alpha_{k-1}}(b_{k}\alpha_{k-1}-\gamma_{k-1})=\sum_{j=k+1}^{r}b_{j}\left[\frac{q_{j-k-1}(\alpha_{k})}{\alpha_{k-1}}-(a_{k}q_{j-k-1}(\alpha_{k})+p_{j-k-1}(\alpha_{k}))\right] |  |

But, 1 α k − 1 = a k + α k \frac{1}{\alpha_{k-1}}=a_{k}+\alpha_{k}, so :

 | γ k = ∑ j = k + 1 r b j ​ [α k ​ q j − k − 1 ​ ( α k) − p j − k − 1 ​ ( α k)] \gamma_{k}=\sum_{j=k+1}^{r}b_{j}[\alpha_{k}q_{j-k-1}(\alpha_{k})-p_{j-k-1}(\alpha_{k})] |  |

Case 1 : b k + 1 ≠ 0 b_{k+1}\not=0 or b k + 2 = 0 b_{k+2}=0: we recognize the α k \alpha_{k} -numeration of γ k \gamma_{k}, since ( b [k + 1, r]) ∈ E α k (b_{[k+1,r]})\in E_{\alpha_{k}}, with our hypothesis.
Case 2 : b k + 1 = 0 b_{k+1}=0 and b k + 2 ≠ 0 b_{k+2}\not=0, then ( b [k + 1, r]) ∉ E α k (b_{[k+1,r]})\not\in E_{\alpha_{k}} and :

 | γ k = ∑ j = k + 2 r b j ​ [α k ​ q j − k − 1 ​ ( α k) − p j − k − 1 ​ ( α k)] \gamma_{k}=\sum_{j=k+2}^{r}b_{j}[\alpha_{k}q_{j-k-1}(\alpha_{k})-p_{j-k-1}(\alpha_{k})] |  |

so :

 | γ k + 1 = − γ k α k = ∑ j = k + 2 r b j ​ [p j − k − 1 ​ ( α k) α k − q j − k − 1 ​ ( α k)] = ∑ j = k + 2 r b j ​ [α k + 1 ​ q j − k − 2 ​ ( α k + 1) − p j − k − 2 ​ ( α k + 1)] \gamma_{k+1}=-\frac{\gamma_{k}}{\alpha_{k}}=\sum_{j=k+2}^{r}b_{j}\left[\frac{p_{j-k-1}(\alpha_{k})}{\alpha_{k}}-q_{j-k-1}(\alpha_{k})\right]=\sum_{j=k+2}^{r}b_{j}[\alpha_{k+1}q_{j-k-2}(\alpha_{k+1})-p_{j-k-2}(\alpha_{k+1})] |  |

the last equality is obtained as above in Case 1…
Now, ( b [k + 2, r]) ∈ E α k + 1 (b_{[k+2,r]})\in E_{\alpha_{k+1}} and γ k + 1 = ( b [k + 2, r]) α k + 1 \gamma_{k+1}=(b_{[k+2,r]})_{\alpha_{k+1}}. We deduce that γ k + 1 ∈] 0, 1 [\gamma_{k+1}\in]0,1[and γ k < 0 \gamma_{k}<0.

— if b k = 0 b_{k}=0 and b k + 1 ≠ 0 b_{k+1}\not=0, then, with induction hypothesis, we obtain the result since we are in Case 1. ■ \blacksquare

## 4 Order properties of Kronecker sequences

### 4.1 a one-page proof of the ”three distance theorem”

In this section, we will be interested in lengths of subdivisions of [0, 1] [0,1] by finite sets { { k α }, k ∈ { 1 ⋯ N − 1 } } \{\{k\alpha\},k\in\{1\cdots N-1\}\}, where α \alpha is a real in [0, 1 [[0,1[and N N a positive integer.
Let us remark that, if we consider subdivisions of the circle S 1 S^{1}, that is to say of ℝ / ℤ \mathbb{R}/\mathbb{Z}, then their lengths are invariant by translations. In that case, subdivisions by sets like { { k α + β }, k ∈ { 0 ⋯ N − 1 } } \{\{k\alpha+\beta\},k\in\{0\cdots N-1\}\} are the same, from a metric point of view, for all real β \beta.

The well known 3 distance theorem ( see [7]) claims that these subdivisions are quite simple : they all contains at most 3 different lengths, one being the sum of the others :

Let α \alpha be a real in [0, 1 [[0,1[, with CFE [a k] k [a_{k}]_{k}. We denote, as usual, p n / q n p_{n}/q_{n} the reduced fraction of the convergent [a 0, ⋯, a n] [a_{0},\cdots,a_{n}] and δ n = ( − 1) n ​ ( α ​ q n − p n) \delta_{n}=(-1)^{n}(\alpha q_{n}-p_{n}). We remind that ( δ n) n (\delta_{n})_{n} is a positive and decreasing sequence that converges towards 0 0 ( if α \alpha is irrational).
Let N N be a positive integer. If α \alpha is rational, we suppose that N ⩽ q N\leqslant q, where q q is the denominator of the reduced fraction of α \alpha. So, the set { { k α }, k ∈ { 0 ⋯ N − 1 } } \{\{k\alpha\},k\in\{0\cdots N-1\}\} contains exactly N N elements.

###### Theorem 1 ( 3 distance theorem)

.
the set { { k α }, k ∈ { 1 ⋯ N − 1 } } \{\{k\alpha\},k\in\{1\cdots N-1\}\} divides [0, 1] [0,1] into N N intervals of length taking at most 3 values, one being the sum of the others.
We can precise a bit : let s s be the lowest integer such that N ⩽ q s + q s − 1 N\leqslant q_{s}+q_{s-1}, then :
- if N = q s + ( 1 − i) ​ q s − 1 N=q_{s}+(1-i)q_{s-1}, with i ∈ { 0 ⋯ a s − 1 } i\in\{0\cdots a_{s}-1\}, the lengths of above intervals take 2 values :

 | δ s + i ​ δ s − 1 ​ and ​ δ s − 1 \delta_{s}+i\delta_{s-1}\text{ and }\delta_{s-1} |  |

- if N ≠ q s + ( 1 − i) ​ q s − 1 N\not=q_{s}+(1-i)q_{s-1}, with i ∈ { 0 ⋯ a s − 1 } i\in\{0\cdots a_{s}-1\}, the lengths of above intervals take 3 values :

 | δ s − 1, δ s + i ​ δ s − 1 ​ and ​ δ s + ( i + 1) ​ δ s − 1 \delta_{s-1},\delta_{s}+i\delta_{s-1}\text{ and }\delta_{s}+(i+1)\delta_{s-1} |  |

Proof :
According to propositions 2 and 4, algorithm 1 and 3, we can write : N − 1 = ( n 1, ⋯, n s) α N-1=(n_{1},\cdots,n_{s})_{\alpha}, with n s ≠ 0 n_{s}\not=0. Let denote ( u j) j ∈ { 0 ⋯ N − 1 } (u_{j})_{j\in\{0\cdots N-1\}} the increasing sequence that enumerates our set { { k α }, k ∈ { 0 ⋯ N − 1 } } \{\{k\alpha\},k\in\{0\cdots N-1\}\}. We have u 0 = 0 u_{0}=0 and denote u N = 1 u_{N}=1. The aim of this result is to prove that u j − u j − 1 u_{j}-u_{j-1} take at most 3 values, when j j ranges over { 1 ⋯ N } \{1\cdots N\}.
We will denote E ⁡ ( N) E(N) the set of α \alpha -admissible sequences that are lower or equal, for RLO, than ( n i) i (n_{i})_{i}. These sequences are the α \alpha -numeration of integers of { 0 ⋯ N − 1 } \{0\cdots N-1\}. Let k ∈ { 1 ⋯ N − 1 } k\in\{1\cdots N-1\}, then k = ( k 1, ⋯, k r) α k=(k_{1},\cdots,k_{r})_{\alpha}, ( k i) i ∈ E ⁡ ( N) (k_{i})_{i}\in E(N) and k r > 0 k_{r}>0. So, 1 ⩽ r ⩽ s 1\leqslant r\leqslant s.
We denote j j the integer such that u j = { k ​ α } u_{j}=\{k\alpha\}. Then u j − 1 = { k ′ ​ α } u_{j-1}=\{k^{\prime}\alpha\}, where k ′ = ( ( k i ′) i) α k^{\prime}=((k^{\prime}_{i})_{i})_{\alpha} and ( k i ′) i (k^{\prime}_{i})_{i} is the predecessor of ( k i) i (k_{i})_{i} in ( E ⁡ ( N), A ​ L ​ O) (E(N),ALO). In a similar way u j + 1 = { k ​ " ​ α } u_{j+1}=\{k"\alpha\}, where k ​ " = ( ( k ​ " i) i) α k"=((k"_{i})_{i})_{\alpha} and ( k ​ " i) i (k"_{i})_{i} is the successor of ( k i) i (k_{i})_{i} in ( E ⁡ ( N), A ​ L ​ O) (E(N),ALO).
We will suppose that s s is even, because the other case can easily be deduced ( see end of the proof).

▶ \blacktriangleright Case 1 : if r r is odd. Then k ′ = ( k [1, r], 1, ( max, 0) ν) α k^{\prime}=(k_{[1,r]},1,(\max,0)^{\nu})_{\alpha}, where ν = s − r − 1 2 \nu=\frac{s-r-1}{2}. So, more explicitly :

 | ( k i ′) i = ( k 1, ⋯, k r − 1, k r, 1, a r + 2, 0, a r + 4, 0, ⋯, a s − 1, 0) (k^{\prime}_{i})_{i}=(k_{1},\cdots,k_{r-1},k_{r},1,a_{r+2},0,a_{r+4},0,\cdots,a_{s-1},0) |  |

So :

 | u j − u j − 1 = δ r − ∑ i = r + 2; i ​ odd s − 1 a i ​ δ i − 1 = δ r − ∑ i = r + 2; i ​ odd s − 1 ( δ i − 2 − δ i) = δ s − 1 u_{j}-u_{j-1}=\delta_{r}-\sum_{i=r+2;i\text{ odd}}^{s-1}a_{i}\delta_{i-1}=\delta_{r}-\sum_{i=r+2;i\text{ odd}}^{s-1}(\delta_{i-2}-\delta_{i})=\delta_{s-1} |  |

▶ \blacktriangleright Case 2 : if r r is even. Then, we define K = ( k [1, r − 1], k r + 1, ( max, 0) ν) K=(k_{[1,r-1]},k_{r}+1,(\max,0)^{\nu}), where ν = s − r 2 \nu=\frac{s-r}{2}.
▶ ⁣ ▶ \blacktriangleright\blacktriangleright subcase 1 : if K ∈ E ⁡ ( N) K\in E(N), then K K is the predecessor of ( k i) i (k_{i})_{i} in ( E ⁡ ( N), A ​ L ​ O) (E(N),ALO) and :

 | u j − u j − 1 = δ r − 1 − ∑ i = r + 1; i ​ odd s − 1 a i ​ δ i − 1 = δ r − 1 − ∑ i = r + 1; i ​ odd s − 1 ( δ i − 2 − δ i) = δ s − 1 u_{j}-u_{j-1}=\delta_{r-1}-\sum_{i=r+1;i\text{ odd}}^{s-1}a_{i}\delta_{i-1}=\delta_{r-1}-\sum_{i=r+1;i\text{ odd}}^{s-1}(\delta_{i-2}-\delta_{i})=\delta_{s-1} |  |

▶ ⁣ ▶ \blacktriangleright\blacktriangleright subcase 2 : if K ∉ E ⁡ ( N) K\not\in E(N). We have then 2 subsubcases :
▶ ▶ ▶ \blacktriangleright\blacktriangleright\blacktriangleright subsubcase 1 : if r < s r<s, then k r = a r k_{r}=a_{r}. We denote K ′ = ( k [1, r], 0, 1, ( max, 0) ν) α K^{\prime}=(k_{[1,r]},0,1,(\max,0)^{\nu})_{\alpha}, where ν = s − r − 2 2 \nu=\frac{s-r-2}{2}. Then, K ′ ∈ E ⁡ ( N) K^{\prime}\in E(N) and K ′ K^{\prime} is the predecessor of ( k i) i (k_{i})_{i} in ( E ⁡ ( N), A ​ L ​ O) (E(N),ALO). So :

 | u j − u j − 1 = δ r + 1 − ∑ i = r + 3; i ​ odd s − 1 a i ​ δ i − 1 = δ r + 1 − ∑ i = r + 3; i ​ odd s − 1 ( δ i − 2 − δ i) = δ s − 1 u_{j}-u_{j-1}=\delta_{r+1}-\sum_{i=r+3;i\text{ odd}}^{s-1}a_{i}\delta_{i-1}=\delta_{r+1}-\sum_{i=r+3;i\text{ odd}}^{s-1}(\delta_{i-2}-\delta_{i})=\delta_{s-1} |  |

▶ ▶ ▶ \blacktriangleright\blacktriangleright\blacktriangleright subsubcase 2 : if r = s r=s then k s = n s k_{s}=n_{s} or ( k s = n s − 1 k_{s}=n_{s}-1 and ( k [1, s − 1]) > R ( n [1, s − 1]) (k_{[1,s-1]})>_{R}(n_{[1,s-1]}).
We denote t t the greatest odd integer i i such that k i > 0 k_{i}>0. So k = ( k [1, t], ( max, 0) ν, k s) α k=(k_{[1,t]},(\max,0)^{\nu},k_{s})_{\alpha}, where ν = s − t − 1 2 \nu=\frac{s-t-1}{2}. Then, the predecessor of ( k i) i (k_{i})_{i} in ( E ⁡ ( N), A ​ L ​ O) (E(N),ALO) is ( k [1, t − 1], k t − 1) (k_{[1,t-1]},k_{t}-1). So :

 | u j − u j − 1 = δ t − 1 − k s ​ δ s − 1 − ∑ i = t + 1; i ​ even s − 2 a i ​ δ i − 1 = δ t − 1 − k s ​ δ s − 1 − ∑ i = t + 1; i ​ even s − 2 ( δ i − 2 − δ i) = δ s − 2 − k s ​ δ s − 1 u_{j}-u_{j-1}=\delta_{t-1}-k_{s}\delta_{s-1}-\sum_{i=t+1;i\text{ even}}^{s-2}a_{i}\delta_{i-1}=\delta_{t-1}-k_{s}\delta_{s-1}-\sum_{i=t+1;i\text{ even}}^{s-2}(\delta_{i-2}-\delta_{i})=\delta_{s-2}-k_{s}\delta_{s-1} |  |

N.B : r = s r=s and k s = n s k_{s}=n_{s} is valid for k = N − 1 k=N-1. But, r = s, k s = n s − 1 r=s,k_{s}=n_{s}-1 and ( k [1, s − 1]) > R ( n [1, s − 1]) (k_{[1,s-1]})>_{R}(n_{[1,s-1]}) is possible for at least one k < N k<N if and only if ( n [1, s − 1]) ≠ ( max s − 1) (n_{[1,s-1]})\not=(\max^{s-1}). That is to say if and only if : N ≠ q s + q s − 1 − ( a s − n s) ​ q s − 1 = q s − 2 + ( n s + 1) ​ q s − 1 N\not=q_{s}+q_{s-1}-(a_{s}-n_{s})q_{s-1}=q_{s-2}+(n_{s}+1)q_{s-1}.
So, the length δ s − 2 − n s ​ δ s − 1 \delta_{s-2}-n_{s}\delta_{s-1} always occur in our subdivision, but the length δ s − 2 − ( n s − 1) ​ δ s − 1 \delta_{s-2}-(n_{s}-1)\delta_{s-1} occur if and only if N ≠ q s − 2 + ( n s + 1) ​ q s − 1 N\not=q_{s-2}+(n_{s}+1)q_{s-1}. We put i = a s − n s i=a_{s}-n_{s} and obtain the conditions of Theorem 1.

▶ \blacktriangleright Case 3 : the last interval. What about 1 − u j 1-u_{j}, where j = ( K) α j=(K)_{\alpha} and K K is the greatest element of ( E ⁡ ( N), A ​ L ​ O) (E(N),ALO)? Then K = ( ( max, 0) s / 2) K=((\max,0)^{s/2}), so :

 | 1 − u j = 1 − ∑ i = 1; i ​ odd s − 1 a i ​ δ i − 1 = 1 − ∑ i = 1; i ​ odd s − 1 ( δ i − 2 − δ i) = 1 − δ − 1 + δ s − 1 = δ s − 1 1-u_{j}=1-\sum_{i=1;i\text{ odd}}^{s-1}a_{i}\delta_{i-1}=1-\sum_{i=1;i\text{ odd}}^{s-1}(\delta_{i-2}-\delta_{i})=1-\delta_{-1}+\delta_{s-1}=\delta_{s-1} |  |

So, the case s s even is proven !

If s s is odd, we use similar arguments, replacing ”predecessor” by ” successor” and ” u j − u j − 1 u_{j}-u_{j-1} ” by ” u j + 1 − u j u_{j+1}-u_{j} ”. ■ \blacksquare

### 4.2 order coincidence of ( { n ​ α }) n (\{n\alpha\})_{n} and ( { n ​ α ′ }) n (\{n\alpha^{\prime}\})_{n}

∙ \bullet Let α \alpha and α ′ \alpha^{\prime} be two different reals in [0, 1) [0,1). We look for the greatest N N such that ( { n α }) n ∈ { 0 ⋯ N − 1 } (\{n\alpha\})_{n\in\{0\cdots N-1\}} and ( { n α ′ }) n ∈ { 0 ⋯ N − 1 } (\{n\alpha^{\prime}\})_{n\in\{0\cdots N-1\}} are in the same order in the following meaning :

 | ( { n α }) n ∈ I is in the same order than ( { n α ′ }) n ∈ I if and only if ( ∀ n, n ′ ∈ I, { n α } < { n ′ α } ⇔ { n α ′ } < { n ′ α ′ }) (\{n\alpha\})_{n\in I}\text{ is in the same order than }(\{n\alpha^{\prime}\})_{n\in I}\text{ if and only if }(\forall n,n^{\prime}\in I,\{n\alpha\}<\{n^{\prime}\alpha\}\Leftrightarrow\{n\alpha^{\prime}\}<\{n^{\prime}\alpha^{\prime}\}) |  |

where I I is an interval of ℤ \mathbb{Z}.
This property is related with another one, concerning integral parts :

###### Lemma 9

let α, α ′ ∈ ℝ \alpha,\alpha^{\prime}\in\mathbb{R} and N N a positive integer. The following assertions are equivalent :
(i) ( { n α }) n ∈ { 0 ⋯ N − 1 } (\{n\alpha\})_{n\in\{0\cdots N-1\}} and ( { n α ′ }) n ∈ { 0 ⋯ N − 1 } (\{n\alpha^{\prime}\})_{n\in\{0\cdots N-1\}} are in the same order.
(ii) ∀ n ∈ { 0 ⋯ N − 1 }, ⌊ n α ⌋ = ⌊ n α ′ ⌋ \forall n\in\{0\cdots N-1\},\lfloor n\alpha\rfloor=\lfloor n\alpha^{\prime}\rfloor

Proof :
Let n, n ′ ∈ { 0 ⋯ N − 1 } n,n^{\prime}\in\{0\cdots N-1\} such that n < n ′ n<n^{\prime}. We denote d = n ′ − n ∈ { 0 ⋯ N − 1 } d=n^{\prime}-n\in\{0\cdots N-1\}. Then :

 | ⌊ n ′ ​ α ⌋ = ⌊ d ​ α ⌋ + ⌊ n ​ α ⌋ + ϵ ​ where ​ ϵ ∈ { 0, 1 } \lfloor n^{\prime}\alpha\rfloor=\lfloor d\alpha\rfloor+\lfloor n\alpha\rfloor+\epsilon\hskip 8.5359pt\text{ where }\epsilon\in\{0,1\} |  |

so :

 | { n ′ ​ α } − { n ​ α } = { d ​ α } − ϵ \{n^{\prime}\alpha\}-\{n\alpha\}=\{d\alpha\}-\epsilon |  |

thus, the sign of { n ′ ​ α } − { n ​ α } \{n^{\prime}\alpha\}-\{n\alpha\} only depends on ϵ \epsilon. We have the same equalities and remark with α ′ \alpha^{\prime} and ϵ ′ \epsilon^{\prime} instead of α \alpha and ϵ \epsilon.
( i ​ i) ⇒ ( i): (ii)\Rightarrow(i): suppose that (ii) is true. Then, with above notations, we have ϵ = ϵ ′ \epsilon=\epsilon^{\prime}, so { n ′ ​ α } − { n ​ α } \{n^{\prime}\alpha\}-\{n\alpha\} and { n ′ ​ α ′ } − { n ​ α ′ } \{n^{\prime}\alpha^{\prime}\}-\{n\alpha^{\prime}\} have the same sign.
( i) ⇒ ( i ​ i): (i)\Rightarrow(ii): suppose that (ii) is false. Then we have an integer ν ∈ { 1 ⋯ N − 1 } \nu\in\{1\cdots N-1\} such that :

 | ∀ k ∈ { 0 ⋯ ν − 1 }, ⌊ k α ⌋ = ⌊ k α ′ ⌋ and ⌊ ν α ⌋ ≠ ⌊ ν α ′ ⌋ \forall k\in\{0\cdots\nu-1\},\lfloor k\alpha\rfloor=\lfloor k\alpha^{\prime}\rfloor\text{ and }\lfloor\nu\alpha\rfloor\not=\lfloor\nu\alpha^{\prime}\rfloor |  |

suppose that α < α ′ \alpha<\alpha^{\prime}, then : ⌊ ν ​ α ⌋ < ⌊ ν ​ α ′ ⌋ \lfloor\nu\alpha\rfloor<\lfloor\nu\alpha^{\prime}\rfloor. If we denote n ′ = ν, n = ν − 1 n^{\prime}=\nu,n=\nu-1 and d = 1 d=1, then, with above notations : ϵ = 0 \epsilon=0 and ϵ ′ = 1 \epsilon^{\prime}=1, so { n ′ ​ α } − { n ​ α } \{n^{\prime}\alpha\}-\{n\alpha\} and { n ′ ​ α ′ } − { n ​ α ′ } \{n^{\prime}\alpha^{\prime}\}-\{n\alpha^{\prime}\} do not have the same sign. ■ \blacksquare

∙ \bullet Suppose that α \alpha is a real and p / q p/q is a convergent of α \alpha. We claim that :

 | ∀ n ∈ { 0 ⋯ q − 1 }, ⌊ n α ⌋ = ⌊ n ​ p q ⌋ \forall n\in\{0\cdots q-1\},\hskip 8.5359pt\lfloor n\alpha\rfloor=\left\lfloor\frac{np}{q}\right\rfloor |  |

Indeed : | α − p q | < 1 q 2 \left|\alpha-\frac{p}{q}\right|<\frac{1}{q^{2}}, so : ∀ n ∈ { 1 ⋯ q − 1 }, | n α − n p q | < 1 q \forall n\in\{1\cdots q-1\},\left|n\alpha-n\frac{p}{q}\right|<\frac{1}{q}. But, { n ​ p q } ∈ [1 q, 1 − 1 q] \{n\frac{p}{q}\}\in[\frac{1}{q},1-\frac{1}{q}], since p p and q q are coprime, so ⌊ n ​ α ⌋ = ⌊ n ​ p q ⌋ \lfloor n\alpha\rfloor=\left\lfloor\frac{np}{q}\right\rfloor.

∙ \bullet Is this result still valid for semi-convergents instead of convergents ? for other reduced rationals ? The following result gives the answer…and a bit more.

###### Proposition 8

.
(i) let α \alpha and α ′ \alpha^{\prime} be two reals such that 0 < α < α ′ < 1 0<\alpha<\alpha^{\prime}<1. We denote γ \gamma the best rational in ] α, α ′]]\alpha,\alpha^{\prime}] and q q the denominator of its reduced fraction. Then

 | q = max { N ∈ ℕ, ∀ n ∈ { 0 ⋯ N − 1 }, ⌊ n α ⌋ = ⌊ n α ′ ⌋ } q=\max\{N\in\mathbb{N},\forall n\in\{0\cdots N-1\},\lfloor n\alpha\rfloor=\lfloor n\alpha^{\prime}\rfloor\} |  |

(ii) let α \alpha be a real in [0, 1) [0,1) and p / q p/q a reduced fraction, with q ∈ ℕ ∗ q\in\mathbb{N}^{*}, such that α \alpha is not the nearest left strict convergent of p / q p/q.

 | p / q is a semi-convergent of α ⇔ ∀ k ∈ { 0 ⋯ q − 1 }, ⌊ k α ⌋ = ⌊ k p / q ⌋ p/q\text{ is a semi-convergent of }\alpha\Leftrightarrow\forall k\in\{0\cdots q-1\},\lfloor k\alpha\rfloor=\lfloor kp/q\rfloor |  |

Remark : for a positive integer n n, we have ⌊ n ​ α ⌋ < ⌊ n ​ α ′ ⌋ \lfloor n\alpha\rfloor<\lfloor n\alpha^{\prime}\rfloor if and only if there exists an integer p p such that α < p / n ⩽ α ′ \alpha<p/n\leqslant\alpha^{\prime}.

Proof :
(i) is a consequence of the remark.
(ii) the best rational in [α, p / q] ⟷ \overset{\longleftrightarrow}{[\alpha,p/q]} is the common semi-convergent of α \alpha and p / q p/q, that has the greatest denominator ( see Proposition 1 (iii)). But, semi-convergents of p / q p/q are either p / q p/q or p ′ / q ′ p^{\prime}/q^{\prime} where p ′, q ′ p^{\prime},q^{\prime} are integers such that 1 ⩽ q ′ < q 1\leqslant q^{\prime}<q. So, we have two cases.
If p / q p/q is a semi-convergent of α \alpha, then there are no integers a, b a,b such that b ∈ { 1 ⋯ q − 1 } b\in\{1\cdots q-1\} and α < a / b ⩽ p / q \alpha<a/b\leqslant p/q or p / q < a / b ⩽ α p/q<a/b\leqslant\alpha. The previous remark implies ⇒ \Rightarrow of (ii).
If p / q p/q is not a semi-convergent of α \alpha, then the best rational in [α, p / q] ⟷ \overset{\longleftrightarrow}{[\alpha,p/q]} is p ′ / q ′ p^{\prime}/q^{\prime} with p ′, q ′ p^{\prime},q^{\prime} two integers such that 0 < q ′ < q 0<q^{\prime}<q. If p / q < α p/q<\alpha then p / q < p ′ / q ′ ⩽ α p/q<p^{\prime}/q^{\prime}\leqslant\alpha and we use remark 2. Else, since α \alpha is not the nearest left strict convergent of p / q p/q, we have p ​ ", q ​ " p",q" two integers such that α < p ​ " / q ​ " < p / q \alpha<p"/q"<p/q and 0 < q ​ " < q 0<q"<q. We conclude with remark 2. ■ \blacksquare

∙ \bullet We also have direct consequences for sums of ⌊ k ​ α ⌋ \lfloor k\alpha\rfloor and { k ​ α } \{k\alpha\}: we will denote

 | ∀ n ∈ ℕ, ∀ x ∈ ℝ, I n ​ ( x) = ∑ k = 0 n − 1 ⌊ k ​ x ⌋; F n ​ ( x) = ∑ k = 0 n − 1 { k ​ x } \forall n\in\mathbb{N},\forall x\in\mathbb{R},\hskip 8.5359ptI_{n}(x)=\sum_{k=0}^{n-1}\lfloor kx\rfloor\hskip 8.5359pt;\hskip 8.5359ptF_{n}(x)=\sum_{k=0}^{n-1}\{kx\} |  |

Obviously, F n F_{n} is 1-periodic, I n I_{n} is non decreasing and :

 | ∀ n ∈ ℕ, ∀ x ∈ ℝ, I n ​ ( x) + F n ​ ( x) = n ⁡ ( n − 1) ​ x 2 ​ ( 1) \forall n\in\mathbb{N},\forall x\in\mathbb{R},\hskip 8.5359ptI_{n}(x)+F_{n}(x)=\frac{n(n-1)x}{2}\hskip 8.5359pt(1) |  |

Moreover, let p, n p,n be 2 positive integers and d = gcd ⁡ ( p, n) d=\gcd(p,n). We denote n ′ = n / d n^{\prime}=n/d and p ′ = p / d p^{\prime}=p/d. Then n ′ n^{\prime} and p ′ p^{\prime} are coprime, so { { k ​ p ′ n ′ }, k ∈ { 0 ⋯ n ′ − 1 } } = { j n ′, j ∈ { 0 ⋯ n ′ − 1 } } \left\{\left\{\frac{kp^{\prime}}{n^{\prime}}\right\},k\in\{0\cdots n^{\prime}-1\}\right\}=\left\{\frac{j}{n^{\prime}},j\in\{0\cdots n^{\prime}-1\}\right\}. So, we have, since ( { k ​ p ′ n ′ }) k \left(\left\{\frac{kp^{\prime}}{n^{\prime}}\right\}\right)_{k} is n ′ n^{\prime} -periodic :

 | ∀ p, n ∈ ℕ ∗, F n ​ ( p n) = n − gcd ⁡ ( p, n) 2 ​ ( 2) \forall p,n\in\mathbb{N}^{*},\hskip 8.5359ptF_{n}\left(\frac{p}{n}\right)=\frac{n-\gcd(p,n)}{2}\hskip 8.5359pt(2) |  |

We also have, for two reals x x and x ′ x^{\prime}:

 | I n ( x) = I n ( x ′) ⇔ ∀ k ∈ { 0 ⋯ n − 1 }, ⌊ k x ⌋ = ⌊ k x ′ ⌋ I_{n}(x)=I_{n}(x^{\prime})\Leftrightarrow\forall k\in\{0\cdots n-1\},\lfloor kx\rfloor=\lfloor kx^{\prime}\rfloor |  |

So, Proposition 8 gives : I n ​ ( x) = I n ​ ( x ′) I_{n}(x)=I_{n}(x^{\prime}) if and only if n n is lower or equal to the denominator of the reduced best rational in ] x, x ′]]x,x^{\prime}], if x < x ′ x<x^{\prime}.
In [2], we can find an expression of I n ​ ( x) I_{n}(x) and F n ​ ( x) F_{n}(x) in terms of the Ostrowski x x -numeration of n n. In what follows, we restrict ourselves to a special case :

###### Corollary 4

Let α \alpha be a real and p / q p/q a fraction of integers, such that α \alpha is not the nearest left strict convergent of p / q p/q.

 | p q ​ a reduced semi-convergent of ​ α ⇔ ∑ k = 0 q − 1 ⌊ k ​ α ⌋ = ( p − 1) ​ ( q − 1) 2 \frac{p}{q}\text{ a reduced semi-convergent of }\alpha\hskip 8.5359pt\Leftrightarrow\hskip 8.5359pt\sum_{k=0}^{q-1}\lfloor k\alpha\rfloor=\frac{(p-1)(q-1)}{2} |  |

Proof :
direct consequence (1),(2) and Proposition 8 (ii). ■ \blacksquare

Remark : we deduce an expression of the mean value of ( { k ​ α }) 1 ⩽ k < q (\{k\alpha\})_{1\leqslant k<q} if p q \frac{p}{q} is a reduced semi-convergent of α \alpha:

 | 1 q − 1 ​ ∑ k = 1 q − 1 { k ​ α } = 1 2 + q ​ α − p 2 \frac{1}{q-1}\sum\limits_{k=1}^{q-1}\{k\alpha\}=\frac{1}{2}+\frac{q\alpha-p}{2} |  |

### 4.3 best left or right α \alpha -approximation of a real in [0, 1 [[0,1[

Let α \alpha be a real, [a k] k ∈ ℕ ∗ [a_{k}]_{k\in\mathbb{N}^{*}} its CFE and r = μ ⁡ ( α) r=\mu(\alpha), the CFE-depth of α \alpha. So, we denote [a 0, a 1, ⋯, a r, 1] [a_{0},a_{1},\cdots,a_{r},1] the CFE of α \alpha if α \alpha is rational. We also denote ( p n / q n) n (p_{n}/q_{n})_{n} the usual sequence of convergents of α \alpha. We consider points of ℝ 2 \mathbb{R}^{2} with the product order : ( x, y) ⩽ ( x ′, y ′) (x,y)\leqslant(x^{\prime},y^{\prime}) if and only if x ⩽ x ′ x\leqslant x^{\prime} and y ⩽ y ′ y\leqslant y^{\prime}.
We recall some notations mentioned at 3.2 : for any x x in ℝ, ‖ x ‖ \mathbb{R},||x||, the distance of x x to ℤ \mathbb{Z}. We also have : ‖ x ‖ = min ⁡ ( { x }, { − x }) ||x||=\min(\{x\},\{-x\}).

###### Definition 6 ( best α \alpha -approximation of a real)

.
let α \alpha and β \beta be two reals in [0, 1 [[0,1[and n n a non negative integer.
⊳ \triangleright { n ​ α } \{n\alpha\} is a *best α \alpha -approximation*of β \beta if and only if :

 | ∀ k ∈ { 0 ⋯ n − 1 }, | | n α − β | | < | | k α − β | | \forall k\in\{0\cdots n-1\},\hskip 8.5359pt||n\alpha-\beta||<||k\alpha-\beta|| |  |

⊳ \triangleright { n ​ α } \{n\alpha\} is a *best right ( resp. left) α \alpha -approximation*of β \beta if and only if :

 | ∀ k ∈ { 0 ⋯ n − 1 }, { n α − β } < { k α − β } ( resp. { β − n α } < { β − k α }) \forall k\in\{0\cdots n-1\},\hskip 8.5359pt\{n\alpha-\beta\}<\{k\alpha-\beta\}\hskip 8.5359pt(\text{ resp. }\{\beta-n\alpha\}<\{\beta-k\alpha\}) |  |

Remarks : we could also consider approximations of β \beta by n ​ α n\alpha mod 1, for negative integers n n.
Best sided α \alpha -approximations of a real are easier to describe than best α \alpha -approximations. But, there is a simple relation : a best α \alpha -approximation is also a best right or left α \alpha -approximation of β \beta.
First, we remark that these notions are closely related to minimal points in ℝ 2 \mathbb{R}^{2} of sequences ( { n ​ α − β }, n) n ∈ ℕ (\{n\alpha-\beta\},n)_{n\in\mathbb{N}} and ( { β − n ​ α }, n) n ∈ ℕ (\{\beta-n\alpha\},n)_{n\in\mathbb{N}}: best right ( resp. left) α \alpha -approximations of β \beta are obtained for the values of n n such that ( { n ​ α − β }, n) (\{n\alpha-\beta\},n) ( resp. ( { β − n ​ α }, n) (\{\beta-n\alpha\},n)) is a minimal point of the sequence ( { k ​ α − β }, k) k ∈ ℕ (\{k\alpha-\beta\},k)_{k\in\mathbb{N}} ( resp. ( { β − k ​ α }, k) k ∈ ℕ (\{\beta-k\alpha\},k)_{k\in\mathbb{N}}).
Moreover :

 | ∀ x ∈ ℝ, { x − β } = { { x } − β ∈ [0, 1 − β [if { x } ⩾ β { x } + 1 − β ∈ [1 − β, 1 [if { x } < β \forall x\in\mathbb{R},\{x-\beta\}=\begin{cases}\{x\}-\beta\in[0,1-\beta[\text{ if }\{x\}\geqslant\beta\\ \{x\}+1-\beta\in[1-\beta,1[\text{ if }\{x\}<\beta\end{cases} |  |

Finally : ( 1 − β, 0) (1-\beta,0) is a trivial minimal point of ( { n ​ α − β }, n) n ∈ ℕ (\{n\alpha-\beta\},n)_{n\in\mathbb{N}}, so the other minimal points must verify { n ​ α } ⩾ β \{n\alpha\}\geqslant\beta.

###### Proposition 9 (best right ( positive) α \alpha -approximations)

.
⊳ \triangleright Case 1: α \alpha is rational and [0, a 1, ⋯, a r, 1] [0,a_{1},\cdots,a_{r},1] is its CFE. We suppose that β ∈ { { n ​ α }, n ∈ ℕ } \beta\in\{\{n\alpha\},n\in\mathbb{N}\} and denote ( b 1, b 2, ⋯, b r) (b_{1},b_{2},\cdots,b_{r}) the α \alpha -numeration of β \beta ( see 2.2).
Best right ( positive) α \alpha -approximations of β \beta are the { n ​ α } \{n\alpha\} for n = 0 n=0, for n = ∑ i = 1 r b i ​ q i − 1 n=\sum\limits_{i=1}^{r}b_{i}q_{i-1} and for the following n n:

 | n = ∑ i = 1 2 ​ k − 1 b i q i − 1 + j q 2 ​ k − 1; j ∈ { 0 ⋯ b 2 ​ k − 1 }; k ∈ { 1 ⋯ ⌊ r / 2 ⌋ } n=\sum_{i=1}^{2k-1}b_{i}q_{i-1}+jq_{2k-1}\hskip 8.5359pt;\hskip 8.5359ptj\in\{0\cdots b_{2k}-1\}\hskip 8.5359pt;\hskip 8.5359ptk\in\{1\cdots\lfloor r/2\rfloor\} |  |

⊳ \triangleright Case 2 : if α \alpha is irrational and [a k] k ∈ ℕ [a_{k}]_{k\in\mathbb{N}} is its CFE. Let β \beta be a real in [0, 1 [[0,1[and ( b k) k ∈ ℕ ∗ (b_{k})_{k\in\mathbb{N}^{*}} its α \alpha -numeration. ( see 2.3)
Best right ( positive) α \alpha -approximations of β \beta are the { n ​ α } \{n\alpha\} for n = 0 n=0, for n = ∑ i = 1 s b i ​ q i − 1 n=\sum\limits_{i=1}^{s}b_{i}q_{i-1}, if b k = 0 b_{k}=0 for all integer k > s k>s, and for the following n n:

 | n = ∑ i = 1 2 ​ k − 1 b i q i − 1 + j q 2 ​ k − 1; j ∈ { 0 ⋯ b 2 ​ k − 1 }; k ∈ ℕ ∗ n=\sum_{i=1}^{2k-1}b_{i}q_{i-1}+jq_{2k-1}\hskip 8.5359pt;\hskip 8.5359ptj\in\{0\cdots b_{2k}-1\}\hskip 8.5359pt;\hskip 8.5359ptk\in\mathbb{N}^{*} |  |

Proof :
We denote t = min ⁡ ( { i, b 2 ​ i ≠ 0 }) t=\min(\{i,b_{2i}\not=0\}), except if all b 2 ​ i b_{2i} are null : we then denote t t the greatest integer i i such that b 2 ​ i − 1 ≠ 0 b_{2i-1}\not=0: so we have, in that case, b = ( max, 0) t b=(\max,0)^{t}. Then, for all cases ( see definition of E ( α) E_{(\alpha)}), we have :

 | b 2 ​ t − 1 ≠ 0; b = ( ( max, 0) t − 1, b [2 ​ t − 1, ∞]) b_{2t-1}\not=0\hskip 8.5359pt;\hskip 8.5359ptb=((\max,0)^{t-1},b_{[2t-1,\infty]}) |  |

Following last remarks above Proposition 9, we need the α \alpha -numeration, say ν \nu, of the least integer n n such that { n ​ α } ⩾ β \{n\alpha\}\geqslant\beta. According to Proposition 2,3,4, it is the minimum of elements d d of E ( α) E_{(\alpha)} for RLO, such that d ⩾ A b d\geqslant_{A}b. We claim that ν = b [1, 2 ​ t − 1] \nu=b_{[1,2t-1]}. Indeed, the condition d ⩾ A b d\geqslant_{A}b implies that

 | d [1, 2 ​ t − 2] = ( m ​ a ​ x, 0) t − 1 = b [1, 2 ​ t − 2] ​ and ​ d 2 ​ t − 1 ⩾ b 2 ​ t − 1 d_{[1,2t-2]}=(max,0)^{t-1}=b_{[1,2t-2]}\hskip 8.5359pt\text{ and }\hskip 8.5359ptd_{2t-1}\geqslant b_{2t-1} |  |

But, b [1, 2 ​ t − 1] b_{[1,2t-1]} is minimal ( for RLO) among these one and satisfies ν ⩾ A b \nu\geqslant_{A}b.
Now, if we denote n 1 = Ψ α ​ ( ν) n_{1}=\Psi_{\alpha}(\nu) this least integer n n such that { n ​ α } ⩾ β \{n\alpha\}\geqslant\beta, then :

 | ∀ n < n 1, { n α − β } ∈ [1 − β, 1 [; { n 1 α − β } ∈ [0, 1 − β [\forall n<n_{1},\hskip 8.5359pt\{n\alpha-\beta\}\in[1-\beta,1[\hskip 8.5359pt;\hskip 8.5359pt\{n_{1}\alpha-\beta\}\in[0,1-\beta[ |  |

So, for the product order in ℤ 2 \mathbb{Z}^{2}:

 | ∀ n ∈ { 1 ⋯ n 1 − 1 }, ( 1 − β, 0) < ( { n α − β }, n) \forall n\in\{1\cdots n_{1}-1\},\hskip 8.5359pt(1-\beta,0)<(\{n\alpha-\beta\},n) |  |

Hence, no points ( { n ​ α − β }, n) (\{n\alpha-\beta\},n) is minimal, for n ∈ { 1 ⋯ n 1 − 1 } n\in\{1\cdots n_{1}-1\}.
If b k = 0 b_{k}=0 for all integer k ⩾ 2 ​ t k\geqslant 2t, then ν = b \nu=b and { n 1 ​ α − β } = 0 \{n_{1}\alpha-\beta\}=0, so this gives the only minimal point ( with n = 0 n=0).
For the other cases : if n ⩾ n 1 n\geqslant n_{1}, let denote d d its α \alpha -numeration. Then, the minimality condition for ( { n ​ α − β }, n) (\{n\alpha-\beta\},n) is equivalent to : d ⩾ A b d\geqslant_{A}b and d d is minimal among these ( elements of E α E_{\alpha} greater than b b for ALO) for the product of orders (ALO,RLO).
Of course, ν \nu is the first ( for RLO) of these minimal ( for (ALO,RLO)) elements. The next one ( for RLO) must satisfy : d < A ν d<_{A}\nu and d d is minimal for RLO : it gives the successive ( b [1, 2 ​ t − 1], j), j ∈ { 0 ⋯ b 2 ​ t − 1 } (b_{[1,2t-1]},j),j\in\{0\cdots b_{2t}-1\} and then ( b [1, 2 ​ t + 1], j), j ∈ { 0 ⋯ b 2 ​ t + 2 − 1 } (b_{[1,2t+1]},j),j\in\{0\cdots b_{2t+2}-1\} if b 2 ​ t + 2 ≠ 0 b_{2t+2}\not=0 ( but this is still true, if b 2 ​ t + 2 = 0 b_{2t+2}=0!), and so on… ■ \blacksquare

∙ \bullet we have a similar result for best left ( positive) α \alpha -approximations :

###### Proposition 10 (best left ( positive) α \alpha -approximations)

.
⊳ \triangleright Case 1: α \alpha is rational and [0, a 1, ⋯, a r, 1] [0,a_{1},\cdots,a_{r},1] is its CFE. We suppose that β ∈ { { n ​ α }, n ∈ ℕ } \beta\in\{\{n\alpha\},n\in\mathbb{N}\} and denote ( b 1, b 2, ⋯, b r) (b_{1},b_{2},\cdots,b_{r}) the α \alpha -numeration of β \beta.
Best left ( positive) α \alpha -approximations of β \beta are the { n ​ α } \{n\alpha\} for n = ∑ i = 1 r b i ​ q i − 1 n=\sum\limits_{i=1}^{r}b_{i}q_{i-1} and for the following n n:

 | n = ∑ i = 1 2 ​ k b i q i − 1 + j q 2 ​ k; j ∈ { 0 ⋯ b 2 ​ k + 1 − 1 }; k ∈ { 0 ⋯ ⌊ ( r − 1) / 2 ⌋ } n=\sum_{i=1}^{2k}b_{i}q_{i-1}+jq_{2k}\hskip 8.5359pt;\hskip 8.5359ptj\in\{0\cdots b_{2k+1}-1\}\hskip 8.5359pt;\hskip 8.5359ptk\in\{0\cdots\lfloor(r-1)/2\rfloor\} |  |

⊳ \triangleright Case 2 : α \alpha is an irrational and [a k] k ∈ ℕ [a_{k}]_{k\in\mathbb{N}} is its CFE. Let β \beta be a real in [0, 1 [[0,1[and ( b k) k ∈ ℕ ∗ (b_{k})_{k\in\mathbb{N}^{*}} its α \alpha -numeration.
Best left ( positive) α \alpha -approximations of β \beta are the { n ​ α } \{n\alpha\} for n = ∑ i = 1 s b i ​ q i − 1 n=\sum\limits_{i=1}^{s}b_{i}q_{i-1}, if b k = 0 b_{k}=0 for all integer k > s k>s, and the following n n:

 | n = ∑ i = 1 2 ​ k b i q i − 1 + j q 2 ​ k; j ∈ { 0 ⋯ b 2 ​ k + 1 − 1 }; k ∈ ℕ n=\sum_{i=1}^{2k}b_{i}q_{i-1}+jq_{2k}\hskip 8.5359pt;\hskip 8.5359ptj\in\{0\cdots b_{2k+1}-1\}\hskip 8.5359pt;\hskip 8.5359ptk\in\mathbb{N} |  |

Proof :
the proof is similar to those of previous Proposition. ■ \blacksquare

### 4.4 measure of repartition of ( { k ​ α }) 0 ⩽ k < ν (\{k\alpha\})_{0\leqslant k<\nu}

∙ \bullet If α \alpha is an irrational, we know that the sequence of probability measures ( μ n) n (\mu_{n})_{n} defined as below converges ( for weak-star topology) to the Lebesgue measure.

 | ∀ ν ∈ ℕ ∗, μ ν = 1 ν ​ ∑ k = 0 ν − 1 D { k ​ α } \forall\nu\in\mathbb{N}^{*},\hskip 8.5359pt\mu_{\nu}=\frac{1}{\nu}\sum_{k=0}^{\nu-1}D_{\{k\alpha\}} |  |

where D x D_{x} is the Dirac-measure in x x.
Can we precise these measures ? That is the aim of the following study. It is sufficient to give an expression of μ ν ( [0, β [) \mu_{\nu}([0,\beta[), where β \beta is any real of [0, 1 [[0,1[. So, we want to count integers k k in { 0 ⋯ ν − 1 } \{0\cdots\nu-1\}, such that, given a real β \beta in [0, 1 [[0,1[, we have { k ​ α } < β \{k\alpha\}<\beta.

∙ \bullet Another approach of this question is the following : note L L the lattice in ℝ 2 \mathbb{R}^{2} generated by ( 1, 0) (1,0) and ( α, 1) (\alpha,1). What is the cardinality of L ∩ R L\cap R, if R R is the rectangle : R = [0, β [× [0, ν [R=[0,\beta[\times[0,\nu[?

∙ \bullet For two reals α \alpha and β \beta in [0, 1 [[0,1[and for a positive integer ν \nu, we denote n = ( n k) k n=(n_{k})_{k} and b = ( b k) k b=(b_{k})_{k} the respective α \alpha -numeration of ν \nu and β \beta. We denote σ \sigma the usual shift on sequences. We will also use the two total orders on finite sequences of reals : RLO, denoted ⩽ R \leqslant_{R} and ALO, denoted ⩽ A \leqslant_{A} ( see 1.2 and 2.3).
We also denote :

 | N ( α, β, ν) = { k ∈ { 0 ⋯ ν − 1 }, { k α } < β }; E ( α, β, ν) = { d ∈ E ( α), d < R n and d < A b } N(\alpha,\beta,\nu)=\{k\in\{0\cdots\nu-1\},\{k\alpha\}<\beta\}\hskip 8.5359pt;\hskip 8.5359ptE(\alpha,\beta,\nu)=\{d\in E_{(\alpha)},d<_{R}n\text{ and }d<_{A}b\} |  |

With the results of section 2.3. we can claim that : Ψ α \Psi_{\alpha} gives a one to one correspondance between N ⁡ ( α, β, ν) N(\alpha,\beta,\nu) and E ⁡ ( α, β, ν) E(\alpha,\beta,\nu). We will denote C ⁡ ( α, β, ν) C(\alpha,\beta,\nu) the cardinality of these finite sets.
We will denote α = [a k] k ∈ ℕ \alpha=[a_{k}]_{k\in\mathbb{N}} the CFE of α \alpha ( with a 0 = 0 a_{0}=0) and r r the CFE depth of α \alpha ( r = + ∞ r=+\infty if and only if α \alpha is irrational). We suppose ν ⩽ q \nu\leqslant q if α \alpha is a rational and p / q p/q is a reduced fraction that represents α \alpha. As in section 3.3, we use the following notations :

 | α 0 = α; ∀ k ∈ { 1 ⋯ r }, α k = { 1 α k − 1 } \alpha_{0}=\alpha\hskip 8.5359pt;\hskip 8.5359pt\forall k\in\{1\cdots r\},\alpha_{k}=\left\{\frac{1}{\alpha_{k-1}}\right\} |  |

 | ν 0 = ν; ∀ k ∈ { 1 ⋯ r − 2 }, ν k = { ⌊ ν k − 1 ​ α k − 1 ⌋ ​ if ​ n k ≠ 0 ​ or ​ n k + 1 = 0 ⌊ ν k − 1 ​ α k − 1 ⌋ + 1 ​ else \nu_{0}=\nu\hskip 8.5359pt;\hskip 8.5359pt\forall k\in\{1\cdots r-2\},\nu_{k}=\begin{cases}\lfloor\nu_{k-1}\alpha_{k-1}\rfloor\text{ if }n_{k}\not=0\text{ or }n_{k+1}=0\\ \lfloor\nu_{k-1}\alpha_{k-1}\rfloor+1\text{ else }\end{cases} |  |

 | β 0 = β; ∀ k ∈ { 1 ⋯ r }, β k = 1 α k − 1 ( b k α k − 1 − β k − 1) \beta_{0}=\beta\hskip 8.5359pt;\hskip 8.5359pt\forall k\in\{1\cdots r\},\beta_{k}=\frac{1}{\alpha_{k-1}}(b_{k}\alpha_{k-1}-\beta_{k-1}) |  |

Remark 1 :

 | d ∈ E ( α) ⇔ d = ( 0) ​ or ​ { d 1 ∈ { 1 ⋯ a 1 } σ ⁡ ( d) ∈ E ( α 1) ​ or ​ { d 1 = a 1 d 2 = 0 σ 2 ​ ( d) ∈ E ( α 2) \ { ( 0) } d\in E_{(\alpha)}\Leftrightarrow d=(0)\text{ or }\begin{cases}d_{1}\in\{1\cdots a_{1}\}\\ \sigma(d)\in E_{(\alpha_{1})}\end{cases}\text{ or }\begin{cases}d_{1}=a_{1}\\ d_{2}=0\\ \sigma^{2}(d)\in E_{(\alpha_{2})}\backslash\{(0)\}\end{cases} |  |

These three cases are exclusive.

Remark 2 : let d ∈ E ( α) d\in E_{(\alpha)}, then :

 | d < R n ⇔ σ ( d) < R σ ( n) or ( σ ( d) = σ ( n) and d 1 < n 1) d<_{R}n\Leftrightarrow\sigma(d)<_{R}\sigma(n)\text{ or }(\sigma(d)=\sigma(n)\text{ and }d_{1}<n_{1}) |  |

 | d < A b ⇔ d 1 < b 1 or ( d 1 = b 1 and σ ( b) < A σ ( d)) d<_{A}b\Leftrightarrow d_{1}<b_{1}\text{ or }(d_{1}=b_{1}\text{ and }\sigma(b)<_{A}\sigma(d)) |  |

###### Proposition 11

we denote n = ( n k) k n=(n_{k})_{k} the α \alpha -numeration of ν \nu and b = ( b k) k b=(b_{k})_{k} the α \alpha -numeration of β \beta. We denote s s the minimum of the lengths of n n and b b, when we drop the eventual infinite ” 0 0 -tail”. So, n s n_{s} or b s b_{s} is not null, but σ s ​ ( n) \sigma^{s}(n) or σ s ​ ( b) \sigma^{s}(b) is the null sequence.

 | C ⁡ ( α, β, ν) = ∑ i = 1 s ( − 1) i − 1 ​ [b i ​ ν i + τ i + ϵ i − ϵ i ′] C(\alpha,\beta,\nu)=\sum_{i=1}^{s}(-1)^{i-1}[b_{i}\nu_{i}+\tau_{i}+\epsilon_{i}-\epsilon^{\prime}_{i}] |  |

τ i = { 1 ​ if ​ n i ​ n i + 1 = 0 ​ and ​ σ i ​ ( n) ≠ ( 0) min ⁡ ( b i, n i) ​ else \tau_{i}=\begin{cases}1\text{ if }n_{i}n_{i+1}=0\text{ and }\sigma^{i}(n)\not=(0)\\ \min(b_{i},n_{i})\text{ else}\end{cases}
ϵ i = { 1 if b i < n i and σ i ( b) < A σ i ( n) 0 ​ else \epsilon_{i}=\begin{cases}1\text{ if }b_{i}<n_{i}\text{ and }\sigma^{i}(b)<_{A}\sigma^{i}(n)\\ 0\text{ else }\end{cases} ϵ i ′ = { 1 if σ i ( b) < R σ i ( n) 0 ​ else \epsilon^{\prime}_{i}=\begin{cases}1\text{ if }\sigma^{i}(b)<_{R}\sigma^{i}(n)\\ 0\text{ else }\end{cases}

Proof :
we want to enumerate sequences d d of E ( α) E_{(\alpha)} such that d < R n d<_{R}n and d < A b d<_{A}b. We will consider several cases and subcases, depending on the cancellation of the b i b_{i} and n i n_{i} …
First, we remark that b 1 > 0 b_{1}>0 and n 1 > 0 n_{1}>0, for we can suppose that b ≠ ( 0) b\not=(0) and n ≠ ( 0) n\not=(0).
▶ \blacktriangleright Case 1 : b 2 > 0 b_{2}>0.
▶ ⁣ ▶ \blacktriangleright\blacktriangleright subcase 1 : n 2 > 0 n_{2}>0 or σ ⁡ ( n) = ( 0) \sigma(n)=(0). Let us count sequences d d as follows :
— if d 1 = 0 d_{1}=0, then d = ( 0) ∈ E ⁡ ( α, β, ν) d=(0)\in E(\alpha,\beta,\nu) for n ≠ ( 0) n\not=(0) and b ≠ ( 0) b\not=(0): 1 sequence.
— if 0 < d 1 < b 1 0<d_{1}<b_{1}. Then d < A b d<_{A}b. So d ∈ E ⁡ ( α, β, ν) d\in E(\alpha,\beta,\nu) if and only if d < R n d<_{R}n.
—— if σ ⁡ ( d) = σ ⁡ ( n) ​ and ​ d 1 < n 1 \sigma(d)=\sigma(n)\text{ and }d_{1}<n_{1}, this gives, exactly min ⁡ ( b 1, n 1) − 1 \min(b_{1},n_{1})-1 sequences d d.
—— if σ ( d) < R σ ( n) \sigma(d)<_{R}\sigma(n), this gives, for every d 1 ∈ { 1 ⋯ b 1 − 1 } d_{1}\in\{1\cdots b_{1}-1\}, ν 1 \nu_{1} possible sequences d d, according to Lemma 6 : so, we have ν 1 ​ ( b 1 − 1) \nu_{1}(b_{1}-1) sequences d d for this subcase.
— if d 1 = b 1 d_{1}=b_{1}, then, d ∈ E ⁡ ( α, β, ν) d\in E(\alpha,\beta,\nu) if and only if d < R n d<_{R}n and σ ( d) > A σ ( b) \sigma(d)>_{A}\sigma(b).
—— if σ ⁡ ( d) = σ ⁡ ( n) \sigma(d)=\sigma(n), this gives a unique sequence d = ( b 1, σ ⁡ ( n)) d=(b_{1},\sigma(n)) if and only if b 1 < n 1 b_{1}<n_{1} and σ ( n) > A σ ( b) \sigma(n)>_{A}\sigma(b) ( because n 2 ≠ 0 n_{2}\not=0, so ( b 1) ⊔ σ ⁡ ( n) ∈ E ( α) (b_{1})\sqcup\sigma(n)\in E_{(\alpha)}) and no sequences d d else. This gives ϵ 1 \epsilon_{1} sequences.
—— if σ ( d) < R σ ( n) \sigma(d)<_{R}\sigma(n). Since d 1 d_{1} is fixed ( OPEN d 1 = b 1) d_{1}=b_{1}), counting these sequences is the same, according to Lemma 6, as counting sequences u u of E ( α 1) E_{(\alpha_{1})} ( since d 2 d_{2} can not be null if σ ( d) > A σ ( b) \sigma(d)>_{A}\sigma(b)) such that u < R σ ( n) u<_{R}\sigma(n) and u > A σ ( b) u>_{A}\sigma(b). But, σ ⁡ ( n) \sigma(n) is the α 1 \alpha_{1} - numeration of ν 1 \nu_{1} ( see Lemma 7) and σ ⁡ ( b) \sigma(b) is the α 1 \alpha_{1} -numeration of β 1 \beta_{1} ( see Lemma 8). So, we obtain ν 1 − C ⁡ ( α 1, β 1, ν 1) − ϵ 1 ′ \nu_{1}-C(\alpha_{1},\beta_{1},\nu_{1})-\epsilon^{\prime}_{1} sequences d d for this subcase, where ϵ 1 ′ = 1 \epsilon^{\prime}_{1}=1 if and only if u u can be equal to σ ⁡ ( b) \sigma(b), so if and only if σ ( b) < R σ ( n) \sigma(b)<_{R}\sigma(n) and 0 0 else.

If we summarize this subcase, we obtain :

 | C ⁡ ( α 0, β 0, ν 0) = ν 1 ​ b 1 + min ⁡ ( b 1, n 1) + ϵ 1 − ϵ 1 ′ − C ⁡ ( α 1, β 1, ν 1) C(\alpha_{0},\beta_{0},\nu_{0})=\nu_{1}b_{1}+\min(b_{1},n_{1})+\epsilon_{1}-\epsilon^{\prime}_{1}-C(\alpha_{1},\beta_{1},\nu_{1}) |  |

▶ ⁣ ▶ \blacktriangleright\blacktriangleright subcase 2 : n 2 = 0 n_{2}=0 and σ ⁡ ( n) ≠ ( 0) \sigma(n)\not=(0).
— if d 1 = 0 d_{1}=0: 1 sequence for d = ( 0) d=(0).
— if 0 < d 1 < b 1 0<d_{1}<b_{1}, this is the same count as in the previous subcase, except that : we have σ ⁡ ( n) = ( 0, n [3, ∞]) \sigma(n)=(0,n_{[3,\infty]}) with n 3 ≠ 0 n_{3}\not=0, so σ ⁡ ( n) \sigma(n) is not a possible value for σ ⁡ ( d) ∈ E ( α 1) \sigma(d)\in E_{(\alpha_{1})} if d 1 < b 1 d_{1}<b_{1} ( for b 1 ⩽ a 1 b_{1}\leqslant a_{1}). So, we must replace min ⁡ ( b 1, n 1) \min(b_{1},n_{1}) by 1 1: this is the role of τ 1 \tau_{1}. Furthermore, the condition σ ( d) < R σ ( n) \sigma(d)<_{R}\sigma(n) is equivalent to σ ( d) < R ( 1, n [3, ∞]) = ( 1, σ 2 ( n)) \sigma(d)<_{R}(1,n_{[3,\infty]})=(1,\sigma^{2}(n)) that is the α 1 \alpha_{1} -numeration of ν 1 \nu_{1}: so this gives τ 1 − 1 + ν 1 ​ ( b 1 − 1) \tau_{1}-1+\nu_{1}(b_{1}-1) sequences.
— if d 1 = b 1 d_{1}=b_{1}, we have n 2 = 0 n_{2}=0, so u < R σ ( n) u<_{R}\sigma(n) is equivalent to u < R ( 1, σ 2 ( n)) u<_{R}(1,\sigma^{2}(n)) and ( 1, σ 2 ​ ( n)) (1,\sigma^{2}(n)) is the α 1 \alpha_{1} - numeration of ν 1 \nu_{1}. As above, we obtain ν 1 − C ⁡ ( α 1, β 1, ν 1) − ϵ 1 ′ \nu_{1}-C(\alpha_{1},\beta_{1},\nu_{1})-\epsilon^{\prime}_{1} sequences d d for this subcase. Now, with all previous arguments, we obtain C ⁡ ( α 1, β 1, ν 1) = ν 2 ​ b 2 + τ 2 + ϵ 2 − ϵ 2 ′ − C ⁡ ( α 2, β 2, ν 2) C(\alpha_{1},\beta_{1},\nu_{1})=\nu_{2}b_{2}+\tau_{2}+\epsilon_{2}-\epsilon^{\prime}_{2}-C(\alpha_{2},\beta_{2},\nu_{2}), but ν 1 = ( 1, σ 2 ​ ( n)) α 1 \nu_{1}=(1,\sigma^{2}(n))_{\alpha_{1}} and n 2 = 0 n_{2}=0, so we must replace 0 0 by 1 1 for the value of n 2 n_{2} in the formula for τ 2 \tau_{2} and ϵ 2 \epsilon_{2}. But, it does not change the result, for b 2 ≠ 0 b_{2}\not=0! At the end, ν 2 = ( σ 2 ​ ( n)) α 2 \nu_{2}=(\sigma^{2}(n))_{\alpha_{2}}, so the induction goes on.

If we summarize this subcase, we obtain ( here ϵ 1 = 0 \epsilon_{1}=0) :

 | C ⁡ ( α 0, β 0, ν 0) = ν 1 ​ b 1 + τ 1 + ϵ 1 − ϵ 1 ′ − ( ν 2 ​ b 2 + τ 2 + ϵ 2 − ϵ 2 ′) + C ⁡ ( α 2, β 2, ν 2) C(\alpha_{0},\beta_{0},\nu_{0})=\nu_{1}b_{1}+\tau_{1}+\epsilon_{1}-\epsilon^{\prime}_{1}-(\nu_{2}b_{2}+\tau_{2}+\epsilon_{2}-\epsilon^{\prime}_{2})+C(\alpha_{2},\beta_{2},\nu_{2}) |  |

▶ \blacktriangleright Case 2 : if b 2 = 0 b_{2}=0 and σ ⁡ ( b) ≠ 0 \sigma(b)\not=0. Then b 1 = a 1 b_{1}=a_{1}. We can copy all arguments given in Case 1, except if d 1 = b 1 d_{1}=b_{1} and σ ( d) < R σ ( n) \sigma(d)<_{R}\sigma(n): indeed, σ ⁡ ( b) \sigma(b) is not the α 1 \alpha_{1} -numeration of β 1 \beta_{1} ( for β 1 < 0 \beta_{1}<0 and σ ⁡ ( b) ∉ E α 1 \sigma(b)\not\in E_{\alpha_{1}}). But, σ 2 ​ ( b) \sigma^{2}(b) is the α 2 \alpha_{2} -numeration of β 2 \beta_{2} ( see Lemma …). So, we must look for a formula between C ⁡ ( α 0, β 0, ν 0) C(\alpha_{0},\beta_{0},\nu_{0}) and C ⁡ ( α 2, β 2, ν 2) C(\alpha_{2},\beta_{2},\nu_{2}). Moreover, σ ( d) > A σ ( b) \sigma(d)>_{A}\sigma(b) if and only if d 2 > 0 d_{2}>0 or ( d 2 = 0 d_{2}=0 and σ 2 ( d) < A σ 2 ( b) \sigma^{2}(d)<_{A}\sigma^{2}(b)).
— if d 2 > 0 d_{2}>0, then counting these sequences is the same as counting sequences d d such that d 2 > 0 d_{2}>0 and σ ( d) < R σ ( n) \sigma(d)<_{R}\sigma(n), so counting sequences u ∈ E ( α 1) u\in E_{(\alpha_{1})} such that u ≠ ( 0) u\not=(0) and u < R σ ( n) u<_{R}\sigma(n). With the same arguments as in Case 1 ( separating 2 cases : if n 2 n_{2} is null or not), we obtain ν 1 − 1 \nu_{1}-1 such sequences.
— if d 2 = 0 d_{2}=0. We will study 3 subcases, depending on n 2 n_{2} and n 3 n_{3}:
▶ ⁣ ▶ \blacktriangleright\blacktriangleright subcase 1 : if n 2 = 0 n_{2}=0, then we count sequences d d such that σ 2 ( d) < R σ 2 ( n) \sigma^{2}(d)<_{R}\sigma^{2}(n) and σ 2 ( d) < A σ 2 ( b) \sigma^{2}(d)<_{A}\sigma^{2}(b). So, we obtain C ⁡ ( α 2, β 2, ν 2) C(\alpha_{2},\beta_{2},\nu_{2}) such sequences, because σ 2 ​ ( n) \sigma^{2}(n) and σ 2 ​ ( b) \sigma^{2}(b) are the α 2 \alpha_{2} -numeration of ν 2 \nu_{2} and β 2 \beta_{2} respectively.
▶ ⁣ ▶ \blacktriangleright\blacktriangleright subcase 2 : if n 2 ≠ 0 n_{2}\not=0 and ( n 3 ≠ 0 n_{3}\not=0 or σ 2 ​ ( n) = ( 0) \sigma^{2}(n)=(0)), then we count sequences d d such that σ 2 ( d) ⩽ R σ 2 ( n) \sigma^{2}(d)\leqslant_{R}\sigma^{2}(n): we obtain C ⁡ ( α 2, β 2, ν 2) + ϵ ​ " 1 C(\alpha_{2},\beta_{2},\nu_{2})+\epsilon"_{1} such sequences, with ϵ ​ " 1 = 1 \epsilon"_{1}=1 if σ 2 ( n) < A σ 2 ( b) \sigma^{2}(n)<_{A}\sigma^{2}(b), ϵ ​ " 1 = 0 \epsilon"_{1}=0 else…( σ 2 ​ ( n) \sigma^{2}(n) and σ 2 ​ ( b) \sigma^{2}(b) are still the α 2 \alpha_{2} -numeration of ν 2 \nu_{2} and β 2 \beta_{2} respectively).
▶ ⁣ ▶ \blacktriangleright\blacktriangleright subcase 3 : if n 2 ≠ 0, n 3 = 0 n_{2}\not=0,n_{3}=0 and σ 3 ​ ( n) ≠ ( 0) \sigma^{3}(n)\not=(0), then σ 2 ​ ( n) \sigma^{2}(n) is not the α 2 \alpha_{2} -numeration of ν 2 \nu_{2}: it is ( 1, σ 3 ​ ( n)) (1,\sigma^{3}(n)). Now, σ 2 ( d) ⩽ R σ 2 ( n) \sigma^{2}(d)\leqslant_{R}\sigma^{2}(n) is equivalent to σ 2 ( d) < R ( 1, σ 3 ( n)) \sigma^{2}(d)<_{R}(1,\sigma^{3}(n)), so we obtain C ⁡ ( α 2, β 2, ν 2) C(\alpha_{2},\beta_{2},\nu_{2}) sequences d d ( see Lemma 7 again).

If we summarize this case 2 :

 | C ⁡ ( α 0, β 0, ν 0) = ν 1 ​ b 1 + τ 1 + ϵ 1 − 1 + ϵ ​ " 1 + C ⁡ ( α 2, β 2, ν 2) C(\alpha_{0},\beta_{0},\nu_{0})=\nu_{1}b_{1}+\tau_{1}+\epsilon_{1}-1+\epsilon"_{1}+C(\alpha_{2},\beta_{2},\nu_{2}) |  |

where ϵ ​ " 1 = 1 \epsilon"_{1}=1 if n 2 ≠ 0, ( n 3 ≠ 0 CLOSE n_{2}\not=0,(n_{3}\not=0 or σ 2 ​ ( n) = ( 0) \sigma^{2}(n)=(0)) and σ 2 ( n) < A σ 2 ( b) \sigma^{2}(n)<_{A}\sigma^{2}(b). ϵ ​ " 1 = 0 \epsilon"_{1}=0 else.

Now, let us summarize and generalize all cases :

for all i ∈ { 1 ⋯ s − 1 } i\in\{1\cdots s-1\}: ( we have σ i ​ ( b) ≠ ( 0) \sigma^{i}(b)\not=(0))
- if b i + 1 > 0 b_{i+1}>0, then : C ⁡ ( α i − 1, β i − 1, ν i − 1) = ν i ​ b i + τ i + ϵ i − ϵ i ′ − C ⁡ ( α i, β i, ν i) C(\alpha_{i-1},\beta_{i-1},\nu_{i-1})=\nu_{i}b_{i}+\tau_{i}+\epsilon_{i}-\epsilon^{\prime}_{i}-C(\alpha_{i},\beta_{i},\nu_{i}).
- if b i + 1 = 0 b_{i+1}=0 and σ i ​ ( b) ≠ ( 0) \sigma^{i}(b)\not=(0), then : C ⁡ ( α i − 1, β i − 1, ν i − 1) = ν i ​ b i + τ i + ϵ i + ϵ ​ " i + C ⁡ ( α i + 1, β i + 1, ν i + 1) − 1 C(\alpha_{i-1},\beta_{i-1},\nu_{i-1})=\nu_{i}b_{i}+\tau_{i}+\epsilon_{i}+\epsilon"_{i}+C(\alpha_{i+1},\beta_{i+1},\nu_{i+1})-1,
where ϵ ​ " i = 1 \epsilon"_{i}=1 if n i + 1 ≠ 0, ( n i + 2 ≠ 0 CLOSE n_{i+1}\not=0,(n_{i+2}\not=0 or σ i + 1 ​ ( n) = ( 0) \sigma^{i+1}(n)=(0)) and σ i + 1 ( n) < A σ i + 1 ( b) \sigma^{i+1}(n)<_{A}\sigma^{i+1}(b) and 0 0 else.
We claim that :

 | ϵ ​ " i − 1 = − ϵ i ′ + ϵ i + 1 ′ − ϵ i + 1 − τ i + 1 \epsilon"_{i}-1=-\epsilon^{\prime}_{i}+\epsilon^{\prime}_{i+1}-\epsilon_{i+1}-\tau_{i+1} |  |

— if n i + 1 = 0 n_{i+1}=0, then ϵ i + 1 = 0, τ i + 1 = 1 \epsilon_{i+1}=0,\tau_{i+1}=1 and σ i ( b) < R σ i ( n) ⇔ σ i + 1 ( b) < R σ i + 1 ( n) \sigma^{i}(b)<_{R}\sigma^{i}(n)\Leftrightarrow\sigma^{i+1}(b)<_{R}\sigma^{i+1}(n), so ϵ i ′ = ϵ i + 1 ′ \epsilon^{\prime}_{i}=\epsilon^{\prime}_{i+1}. Moreover, ϵ ​ " i = 0 \epsilon"_{i}=0, so the equality is true.
— if n i + 1 > 0 n_{i+1}>0, then σ i ( b) < R σ i ( n) ⇔ σ i + 1 ( b) ⩽ R σ i + 1 ( n) \sigma^{i}(b)<_{R}\sigma^{i}(n)\Leftrightarrow\sigma^{i+1}(b)\leqslant_{R}\sigma^{i+1}(n).
If σ i + 1 ​ ( b) = σ i + 1 ​ ( n) \sigma^{i+1}(b)=\sigma^{i+1}(n), then ϵ i + 1 = 0, τ i + 1 = 0, ϵ i ′ = 1, ϵ i + 1 ′ = 0 \epsilon_{i+1}=0,\tau_{i+1}=0,\epsilon^{\prime}_{i}=1,\epsilon^{\prime}_{i+1}=0 and ϵ ​ " i = 0 \epsilon"_{i}=0, so the equality is true.
If σ i + 1 ​ ( b) ≠ σ i + 1 ​ ( n) \sigma^{i+1}(b)\not=\sigma^{i+1}(n), then ϵ i ′ = ϵ i + 1 ′ \epsilon^{\prime}_{i}=\epsilon^{\prime}_{i+1}. If n i + 2 ≠ 0 n_{i+2}\not=0 or σ i + 1 ​ ( n) = ( 0) \sigma^{i+1}(n)=(0) then ϵ ​ " i = 1 − ϵ i + 1 \epsilon"_{i}=1-\epsilon_{i+1} and τ i + 1 = 0 \tau_{i+1}=0. Else, ϵ i + 1 = 0 \epsilon_{i+1}=0 ( for b i + 2 ≠ 0 b_{i+2}\not=0), ϵ ​ " i = 0 \epsilon"_{i}=0 and τ i + 1 = 1 \tau_{i+1}=1. In both cases, the equality is true.

From this equality, we deduce that : if b i + 1 = 0 b_{i+1}=0, and σ i ​ ( b) ≠ ( 0) \sigma^{i}(b)\not=(0), then

 | C ⁡ ( α i − 1, β i − 1, ν i − 1) = ν i ​ b i + τ i + ϵ i − ϵ i ′ − ( ν i + 1 ​ b i + 1 + τ i + 1 + ϵ i + 1 − ϵ i + 1 ′) + C ⁡ ( α i + 1, β i + 1, ν i + 1) C(\alpha_{i-1},\beta_{i-1},\nu_{i-1})=\nu_{i}b_{i}+\tau_{i}+\epsilon_{i}-\epsilon^{\prime}_{i}-(\nu_{i+1}b_{i+1}+\tau_{i+1}+\epsilon_{i+1}-\epsilon^{\prime}_{i+1})+C(\alpha_{i+1},\beta_{i+1},\nu_{i+1}) |  |

So, the induction formula for b i + 1 > 0 b_{i+1}>0 can be generalized to all cases and we conclude with : if s = 1 s=1, then n = ( n 1) n=(n_{1}) or b = ( b 1) b=(b_{1}). In the first case, ν 1 = 0 \nu_{1}=0 and C ⁡ ( α, β, ν) C(\alpha,\beta,\nu) counts the d = ( d 1) d=(d_{1}) such that 0 ⩽ d 1 < n 1 0\leqslant d_{1}<n_{1} and d 1 < b 1 d_{1}<b_{1}. So C ⁡ ( α, β, ν) = min ⁡ ( b 1, n 1) = τ 1 C(\alpha,\beta,\nu)=\min(b_{1},n_{1})=\tau_{1} and ϵ 1 = 0 = ϵ 1 ′ \epsilon_{1}=0=\epsilon^{\prime}_{1}, since σ ⁡ ( n) = ( 0) \sigma(n)=(0). In the second case, we have σ ⁡ ( b) = ( 0) ≠ σ ⁡ ( n) \sigma(b)=(0)\not=\sigma(n). Our former arguments give : C ⁡ ( α, β, ν) = b 1 ​ ν 1 + τ 1 + ϵ 1 − 1 C(\alpha,\beta,\nu)=b_{1}\nu_{1}+\tau_{1}+\epsilon_{1}-1 and ϵ 1 ′ = 1 \epsilon^{\prime}_{1}=1. This is the initialization of our induction. ■ \blacksquare

∙ \bullet We can deduce similar results for conditions with large inequalities instead of strict ones.
For example : if we denote C ′ ( α, β, ν) = #{ k ∈ { 0 ⋯ ν }, { k α } ⩽ β } C^{\prime}(\alpha,\beta,\nu)=\#\{k\in\{0\cdots\nu\},\{k\alpha\}\leqslant\beta\}, then :

 | C ′ ​ ( α, β, ν) = C ⁡ ( α, β, ν) + D C^{\prime}(\alpha,\beta,\nu)=C(\alpha,\beta,\nu)+D |  |

where :

 | D = 1 n ⩽ A b + 1 b ⩽ R n − 1 n = b D=\textbf{1}_{n\leqslant_{A}b}+\textbf{1}_{b\leqslant_{R}n}-\textbf{1}_{n=b} |  |

Indeed, if we denote E ′ ( α, β, ν) = { d ∈ E ( α), d ⩽ R n, d ⩽ A b } E^{\prime}(\alpha,\beta,\nu)=\{d\in E_{(\alpha)},d\leqslant_{R}n,d\leqslant_{A}b\}, then C ′ ​ ( α, β, ν) C^{\prime}(\alpha,\beta,\nu) is the number of elements of E ′ ​ ( α, β, ν) E^{\prime}(\alpha,\beta,\nu). This set is E ⁡ ( α, β, ν) E(\alpha,\beta,\nu) plus the element n n if and only if n ⩽ A b n\leqslant_{A}b, plus the element b b if and only if b ⩽ R n b\leqslant_{R}n … if n = b n=b, we have to count once this element.

## 5 References

[1] V Berthé : ” autour du système de numération d’Ostrowski”, Bull. Belg. Math. Soc. 8 (2001), 209-238

[2] T.C. Brown and P.J.-S. Shiue : ” sums of fractional parts of integer multiples of an irrational”, J.Number Theory 50 (1995), 181-192.

[3] E.Cabanillas : ” quotients of numerical semigroups generated by two numbers”, hal-02097473 and Arxiv 1904.08240 ( 2019)

[4] J. W. S. Cassels : ” an introduction to Diophantine approximation”, Cambridge, Cambridge University Press, 1957.

[5] S. Ito : ”some skew product transformations associated with continued fractions and their invariant measures” , Tokyo J. Math. 9 (1986), 115-133.

[6] Ostrowski : ” bemerkungen zur Theorie der Diophantischen Approximationnen I,II” , Abh. Math. Sem Hamburg I ( 1922), 77-98 and 250-251

[7] V. T. S Sòs : ”on the distribution mod 1 of the sequence n α \alpha ”, Ann. Univ. Sci. Budapest, Eotvos Sect. Math. 1 (1958), 127-134.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1904.01873
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1904.01874
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1904.01874
[7]: https://arxiv.org/abs/1904.01874
[8]: /html/1904.01876
