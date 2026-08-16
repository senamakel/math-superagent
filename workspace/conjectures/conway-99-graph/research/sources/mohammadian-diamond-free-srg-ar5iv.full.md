<!-- source: https://ar5iv.labs.arxiv.org/html/1303.0473 | converted from HTML -->

[1303.0473] On a family of diamond-free strongly regular graphs

# On a family of diamond-free strongly regular graphs

A. Mohammadian B. Tayfeh-Rezaie Affiliation: School of Mathematics, Institute for Research in Fundamental Sciences (IPM), Affiliation: P.O. Box 19395-5746, Tehran, Iran Affiliation: 𝖺𝗅𝗂 ​ _ ​ 𝗆 ​ @ ​ 𝗂𝗉𝗆. 𝗂𝗋 \mathsf{ali\_m@ipm.ir} 𝗍𝖺𝗒𝖿𝖾𝗁 \mathsf{tayfeh} - 𝗋 ​ @ ​ 𝗂𝗉𝗆. 𝗂𝗋 \mathsf{r@ipm.ir}

###### Abstract

The existence of a partial quadrangle 𝖯𝖰 ⁡ ( s, t, μ) {\mathsf{PQ}}(s,t,\mu) is equivalent to the existence of a diamond-free strongly regular graph 𝖲𝖱𝖦 ⁡ ( 1 + s ⁡ ( t + 1) + s 2 ​ t ​ ( t + 1) / μ, s ⁡ ( t + 1), s − 1, μ) {\mathsf{SRG}}(1+s(t+1)+s^{2}t(t+1)/\mu,s(t+1),s-1,\mu). Recently, it is shown that there exists a 𝖯𝖰 ⁡ ( 2, ( n 3 + 3 ​ n 2 − 2) / 2, n 2 + n) {\mathsf{PQ}}(2,(n^{3}+3n^{2}-2)/2,n^{2}+n) if and only if n ∈ { 1, 2, 4 } n\in\{1,2,4\}. Let 𝒮 \mathcal{S} be a 𝖯𝖰 ⁡ ( 3, ( n + 3) ​ ( n 2 − 1) / 3, n 2 + n) {\mathsf{PQ}}(3,(n+3)(n^{2}-1)/3,n^{2}+n) such that for every two non-collinear points p 1 p_{1} and p 2 p_{2}, there is a point q q non-collinear with p 1 p_{1}, p 2 p_{2}, and all points collinear with both p 1 p_{1} and p 2 p_{2}. In this article, we establish that 𝒮 \mathcal{S} exists only for n ∈ { − 2, 2, 3 } n\in\{-2,2,3\} and probably n = 10 n=10.

Key words and phrases: adjacency matrix, eigenvalue multiplicity, automorphism group, diamond-free graph, negative Latin square graph, partial quadrangle, strongly regular graph, transitive graph.

AMS Mathematics Subject Classification (2010): 05B25, 05C25, 05C50, 05E30.

## I. Introduction

A strongly regular graph with parameters ( ν, k, λ, μ) (\nu,k,\lambda,\mu), denoted by 𝖲𝖱𝖦 ⁡ ( ν, k, λ, μ) {\mathsf{SRG}}(\nu,k,\lambda,\mu), is a regular graph of order ν \nu and valency k k such that ( 𝗂) \mathsf{(i)} it is not complete or edgeless, ( 𝗂𝗂) \mathsf{(ii)} every two adjacent vertices have λ \lambda common neighbors, and ( 𝗂𝗂𝗂) \mathsf{(iii)} every two non-adjacent vertices have μ \mu common neighbors. The concept of strongly regular graphs was first introduced by Bose and Shimamoto in [4]. Strongly regular graphs form an important class of graphs and lie somewhere between highly structured graphs and apparently random graphs. They often appear in different areas such as coding theory, design theory, discrete geometry, group theory, and so on. Obviously, complete multipartite graphs with equal part sizes and their complements are trivial examples of strongly regular graphs. To exclude these examples, we assume that a strongly regular graph and its complement are connected; or equivalently, 0 < μ < k < ν − 1 0<\mu<k<\nu-1.

The adjacency matrix of a graph G G, denoted by 𝒜 G \mathcal{A}_{G}, has its rows and columns indexed by the vertex set of G G and its ( i, j) (i,j) -entry is 1 1 if the vertices i i and j j are adjacent and 0 0 otherwise. The zeros of the characteristic polynomial of 𝒜 G \mathcal{A}_{G} are called the eigenvalues of G G. The statement that G G is an 𝖲𝖱𝖦 ⁡ ( ν, k, λ, μ) {\mathsf{SRG}}(\nu,k,\lambda,\mu) is equivalent to

 | 𝒜 G ​ J ν = k ​ J ν and 𝒜 G 2 + ( μ − λ) ​ 𝒜 G + ( μ − k) ​ I ν = μ ​ J ν, \mathcal{A}_{G}J_{\nu}=kJ_{\nu}\quad\text{and}\quad\mathcal{A}_{G}^{2}+(\mu-\lambda)\mathcal{A}_{G}+(\mu-k)I_{\nu}=\mu J_{\nu}, |  |

where I t I_{t} and J t J_{t} are the t × t t\times t identity matrix and the t × t t\times t all one matrix, respectively. It is easy to verify that the eigenvalues of an 𝖲𝖱𝖦 ⁡ ( ν, k, λ, μ) {\mathsf{SRG}}(\nu,k,\lambda,\mu) are

 |  | k, with the multiplicity ​ 1; \displaystyle k,\textrm{ with the multiplicity }1; |  |

 |  | r = λ − μ + Δ 2, with the multiplicity ​ f = ν − 1 2 − 2 ​ k + ( ν − 1) ​ ( λ − μ) 2 ​ Δ; \displaystyle r=\frac{\lambda-\mu+\mathnormal{\Delta}}{2},\textrm{ with the multiplicity }f=\frac{\nu-1}{2}-\frac{2k+(\nu-1)(\lambda-\mu)}{2\mathnormal{\Delta}}; |  |

 |  | s = λ − μ − Δ 2, with the multiplicity ​ g = ν − 1 2 + 2 ​ k + ( ν − 1) ​ ( λ − μ) 2 ​ Δ, \displaystyle s=\frac{\lambda-\mu-\mathnormal{\Delta}}{2},\textrm{ with the multiplicity }g=\frac{\nu-1}{2}+\frac{2k+(\nu-1)(\lambda-\mu)}{2\mathnormal{\Delta}}, |  |

where Δ = ( λ − μ) 2 + 4 ​ ( k − μ) \mathnormal{\Delta}=\sqrt{(\lambda-\mu)^{2}+4(k-\mu)}. It is well known that the second largest eigenvalue of a graph G G is non-positive if and only if the non-isolated vertices of G G form a complete multipartite graph. Also, it is a known fact that the smallest eigenvalue of a graph G G is at least − 1 -1 if and only if G G is a disjoint union of some complete graphs. So, for any 𝖲𝖱𝖦 ⁡ ( ν, k, λ, μ) {\mathsf{SRG}}(\nu,k,\lambda,\mu), we necessarily have r > 0 r>0 and s < − 1 s<-1.

The diamond is the graph on four vertices with five edges. A graph with no diamond as an induced subgraph is called diamond-free. It is straightforward to see that a graph is diamond-free if and only if the neighborhood of any vertex is a disjoint union of some complete graphs. Furthermore, an 𝖲𝖱𝖦 ⁡ ( ν, k, λ, μ) {\mathsf{SRG}}(\nu,k,\lambda,\mu) is diamond-free if and only if λ + 1 | k \lambda+1\,|\,k and the neighborhood of each vertex is k λ + 1 ​ K λ + 1 \tfrac{k}{\lambda+1}K_{\lambda+1}.

A partial quadrangle with parameters ( s, t, μ) (s,t,\mu), denoted by 𝖯𝖰 ⁡ ( s, t, μ) {\mathsf{PQ}}(s,t,\mu), is an incidence structure ( 𝒫, ℒ, ℐ) (\mathcal{P},\mathcal{L},\mathcal{I}) in which 𝒫 \mathcal{P} and ℒ \mathcal{L} are disjoint non-empty sets of elements called points and lines, respectively, and ℐ ⊆ ( 𝒫 × ℒ) ∪ ( ℒ × 𝒫) \mathcal{I}\subseteq(\mathcal{P}\times\mathcal{L})\cup(\mathcal{L}\times\mathcal{P}) is a symmetric incidence relation satisfying the following conditions:

- ( 𝗂) \mathsf{(i)}

Each line is incident with s + 1 s+1 points and each point is incident with t + 1 t+1 lines.

- ( 𝗂𝗂) \mathsf{(ii)}

Every two distinct points are incident with at most one line.

- ( 𝗂𝗂𝗂) \mathsf{(iii)}

For each non-incident pair ( p, ℓ) ∈ 𝒫 × ℒ (p,\ell)\in\mathcal{P}\times\mathcal{L}, there is at most one pair ( p ′, ℓ ′) ∈ 𝒫 × ℒ (p^{\prime},\ell^{\prime})\in\mathcal{P}\times\mathcal{L} such that the both p, p ′ p,p^{\prime} are incident with ℓ ′ \ell^{\prime} and p ′ p^{\prime} is incident with ℓ \ell.

- ( 𝗂𝗏) \mathsf{(iv)}

For every two non-collinear points, there are exactly μ \mu points collinear with both of them.

Partial quadrangles were firstly introduced by Cameron in [5]. Clearly, for any 𝖯𝖰 ⁡ ( s, t, μ) {\mathsf{PQ}}(s,t,\mu), we necessarily have μ ⩽ t + 1 \mu\leqslant t+1. In the literature, a 𝖯𝖰 ⁡ ( s, t, t + 1) {\mathsf{PQ}}(s,t,t+1) is called a generalized quadrangle and is denoted by 𝖦𝖰 ⁡ ( s, t) {\mathsf{GQ}}(s,t). The collinearity graph of a 𝖯𝖰 ⁡ ( s, t, μ) {\mathsf{PQ}}(s,t,\mu) is the graph whose vertices are the points and two vertices are adjacent if they are collinear. It is straightforward to verify that the collinearity graph of a 𝖯𝖰 ⁡ ( s, t, μ) {\mathsf{PQ}}(s,t,\mu) is a diamond-free

 | 𝖲𝖱𝖦 ⁡ ( 1 + s ⁡ ( t + 1) + s 2 ​ t ​ ( t + 1) μ, s ⁡ ( t + 1), s − 1, μ). {\mathsf{SRG}}\left(1+s(t+1)+\frac{s^{2}t(t+1)}{\mu},s(t+1),s-1,\mu\right). |  |

Inversely, a diamond-free strongly regular graph is the collinearity graph of a partial quadrangle whose points are vertices of the graph and lines are maximal cliques of the graph. So, an 𝖲𝖱𝖦 ⁡ ( ν, k, λ, μ) {\mathsf{SRG}}(\nu,k,\lambda,\mu) with λ ⩽ 1 \lambda\leqslant 1 or μ = 1 \mu=1 is the collinearity graph of a partial quadrangle.

Recently, Bondarenko and Radchenko showed in [3] that a 𝖯𝖰 ⁡ ( 2, ( n 3 + 3 ​ n 2 − 2) / 2, n 2 + n) {\mathsf{PQ}}(2,(n^{3}+3n^{2}-2)/2,n^{2}+n), or equivalently, an 𝖲𝖱𝖦 ⁡ ( ( n 2 + 3 ​ n − 1) 2, n 2 ​ ( n + 3), 1, n ⁡ ( n + 1)) {\mathsf{SRG}}((n^{2}+3n-1)^{2},n^{2}(n+3),1,n(n+1)), exists if and only if n ∈ { 1, 2, 4 } n\in\{1,2,4\}. Let 𝒮 \mathcal{S} be a 𝖯𝖰 ⁡ ( 3, ( n + 3) ​ ( n 2 − 1) / 3, n 2 + n) {\mathsf{PQ}}(3,(n+3)(n^{2}-1)/3,n^{2}+n) such that for every two non-collinear points p 1 p_{1} and p 2 p_{2}, there is a point q q non-collinear with p 1 p_{1}, p 2 p_{2}, and all points collinear with both p 1 p_{1} and p 2 p_{2}. In this article, we will show that if 𝒮 \mathcal{S} exists, then n ∈ { − 2, 2, 3, 10 } n\in\{-2,2,3,10\}. Equivalently, we will establish the following theorem.

###### Theorem 1

. If there exists a diamond-free 𝖲𝖱𝖦 ⁡ ( ( n 2 + 3 ​ n − 2) 2, n ⁡ ( n 2 + 3 ​ n − 1), 2, n ⁡ ( n + 1)) {\mathsf{SRG}}((n^{2}+3n-2)^{2},n(n^{2}+3n-1),2,n(n+1)), for some integer n n, satisfying the following condition:

 | For every two non-adjacent vertices u and v, there is a vertex that is not adjacent to u, v, and all common neighbors of u and v, \begin{array}[]{cc}\text{For every two non-adjacent vertices $u$ and $v$, there is a vertex that}\\ \text{\hskip-31.29802pt is not adjacent to $u$, $v$, and all common neighbors of $u$ and $v$,}\end{array} |  | (1) |

then n ∈ { − 2, 2, 3, 10 } n\in\{-2,2,3,10\}.

In each of two cases n = − 2 n=-2 and n = 2 n=2, there is a unique diamond-free strongly regular graph [6]. For n = 3 n=3, we are aware of only one diamond-free strongly regular graph which is found in [7]. Note that all these three examples satisfy ( 1). The question whether there exists a diamond-free strongly regular graph for n = 10 n=10 is left as an open problem. Finally, we believe that Theorem 1 holds without assuming the condition ( 1).

## II. Notation and Preliminaries

We first recall some notation from graph theory. For a graph G G, the vertex set of G G is denoted by V ⁡ ( G) V(G). We employ the notation u ∼ v u\thicksim v when two vertices u, v ∈ V ⁡ ( G) u,v\in V(G) are adjacent. For any vertices v 1, …, v t ∈ V ⁡ ( G) v_{1},\ldots,v_{t}\in V(G), we let

 | N ( v 1, …, v t) = { x ∈ V ( G) | x ∼ v i, for i = 1, …, t }. N(v_{1},\ldots,v_{t})=\{x\in V(G)\,|\,x\thicksim v_{i},\text{ for }i=1,\ldots,t\}. |  |

For every two subsets S S and T T of V ⁡ ( G) V(G), we denote by ⟨ S, T ⟩ \langle S,T\rangle the induced subgraph of G G on all edges with one endpoint in S S and the other endpoint in T T. For simplicity, we will use the notation N ⁡ [v] N[v], N ¯ ​ ( v) \overline{N}(v), and ⟨ S ⟩ \langle S\rangle instead of N ⁡ ( v) ∪ { v } N(v)\cup\{v\}, V ⁡ ( G) ∖ ( N ⁡ ( v) ∪ { v }) V(G)\setminus(N(v)\cup\{v\}), and ⟨ S, S ⟩ \langle S,S\rangle, respectively.

It is a simple and well known fact that a strongly regular graph whose valency is equal to the multiplicity of a non-principal eigenvalue is either a conference graph, that is an 𝖲𝖱𝖦 ⁡ ( n, ( n − 1) / 2, ( n − 5) / 4, ( n − 1) / 4) {\mathsf{SRG}}(n,(n-1)/2,(n-5)/4,(n-1)/4), or an

 | 𝖲𝖱𝖦 ⁡ ( ( n 2 + 3 ​ n − λ) 2, n ⁡ ( n 2 + 3 ​ n − λ + 1), λ, n ⁡ ( n + 1)), \displaystyle{\mathsf{SRG}}((n^{2}+3n-\lambda)^{2},n(n^{2}+3n-\lambda+1),\lambda,n(n+1)), |  | (2) |

for some integer n n; depending on f = g f=g or not. Let G G be a graph of the family given by ( 2). The eigenvalues of G G are n n with the multiplicity ν − 1 − k \nu-1-k and λ − n 2 − 2 ​ n \lambda-n^{2}-2n with the multiplicity k k. Traditionally, if n > 0 n>0, then g = k g=k and G G is called a negative Latin square graph and if n < 0 n<0, then f = k f=k and G G is called a pseudo Latin square graph. Note that if n < 0 n<0, then λ − n 2 − 2 ​ n > 0 \lambda-n^{2}-2n>0 and so n > − 1 − 1 + λ n>-1-\sqrt{1+\lambda}. This means that, for a fixed parameter λ \lambda, there are only finitely many strongly regular graphs with f = k f=k. In this article, we only deal with strongly regular graphs with f ≠ g f\neq g and g = k g=k.

Let G G be a diamond-free 𝖲𝖱𝖦 ⁡ ( ν, k, λ, μ) {\mathsf{SRG}}(\nu,k,\lambda,\mu) in the family ( 2) with 0 ⩽ λ ⩽ n − 1 0\leqslant\lambda\leqslant n-1. Fix a vertex u ∈ V ⁡ ( G) u\in V(G) and assume that ⟨ N ⁡ ( u) ⟩ = s ​ K λ + 1 \langle N(u)\rangle=sK_{\lambda+1}, where s = k / ( λ + 1) s=k/(\lambda+1). Letting H = ⟨ N ⁡ [u] ⟩ H=\langle N[u]\rangle, we may write

 | 𝒜 G = [X Y Y ⊤ 𝒜 H ​], \mathcal{A}_{G}=\left[\begin{array}[]{cc}X&Y\\ Y^{\top}&\mathcal{A}_{H}$$\\ \end{array}\right], |  | (3) |

for some matrices X X and Y Y. Since λ ⩽ n − 1 \lambda\leqslant n-1, n n is not an eigenvalue of H H. With an easy calculation, we find that

 | n ​ ( n + 1) 2 ​ ( n − λ) ​ ( n ​ I k + 1 − 𝒜 H) − 1 = [( a ​ I λ + 1 + μ ​ J λ + 1) ⊗ I s b ​ 𝒋 k b ​ 𝒋 k ⊤ c] − J k + 1, n(n+1)^{2}(n-\lambda)(nI_{k+1}-\mathcal{A}_{H})^{-1}=\left[\begin{array}[]{c|c}(aI_{\lambda+1}+\mu J_{\lambda+1})\otimes I_{s}&b\mbox{\boldmath$j$}_{k}\\ \hline\cr b\mbox{\boldmath$j$}_{k}^{\top}&c\\ \end{array}\right]-J_{k+1}, |  | (4) |

where a = μ ⁡ ( n − λ) a=\mu(n-\lambda), b = λ + 1 − n b=\lambda+1-n, c = ( λ + 1 − n) ​ ( n + 1 − λ) c=(\lambda+1-n)(n+1-\lambda), and 𝒋 k \mbox{\boldmath$j$}_{k} is the all one column vector of length k k. For every two vertices v, w ∈ N ¯ ​ ( u) v,w\in\overline{N}(u), let p u ​ ( v, w) = | N ⁡ ( u, v, w) | p_{u}(v,w)=|N(u,v,w)| and q u ​ ( v, w) q_{u}(v,w) be the number of pairs x ∼ y x\thicksim y with x ∈ N ⁡ ( u, v) x\in N(u,v) and y ∈ N ⁡ ( u, w) y\in N(u,w). Since g = k g=k, we have rank ​ ( n ​ I ν − 𝒜 G) = rank ​ ( n ​ I k + 1 − 𝒜 H) \text{\sl rank}\,(nI_{\nu}-\mathcal{A}_{G})=\text{\sl rank}\,(nI_{k+1}-\mathcal{A}_{H}), which implies by ( 3) that

 | n ​ I ν − X = Y ​ ( n ​ I k + 1 − 𝒜 H) − 1 ​ Y ⊤. nI_{\nu}-X=Y(nI_{k+1}-\mathcal{A}_{H})^{-1}Y^{\top}. |  | (5) |

Using ( 4) and ( 5), it is not hard to see that

 | ( n − λ + 1) ​ p u ​ ( v, w) + q u ​ ( v, w) = { λ ⁡ ( n + 1), if v ∼ w; μ, otherwise, \displaystyle(n-\lambda+1)p_{u}(v,w)+q_{u}(v,w)=\left\{\begin{array}[]{ll}\lambda(n+1),&\text{if $v\thicksim w$};\\ \mu,&\text{otherwise},\end{array}\right. |  |

for every two vertices v, w ∈ N ¯ ​ ( u) v,w\in\overline{N}(u).

Now, fix a vertex v ∈ N ¯ ​ ( u) v\in\overline{N}(u) and set t = ⌊ μ / ( n − λ + 1) ⌋ t=\lfloor\mu/(n-\lambda+1)\rfloor. For i = 0, 1, …, t i=0,1,\ldots,t, let M i ​ ( u, v) M_{i}(u,v) be the set of all vertices x ∉ N ⁡ [u] ∪ N ⁡ [v] x\not\in N[u]\cup N[v] with p u ​ ( v, x) = i p_{u}(v,x)=i, and put m i ​ ( u, v) = | M i ​ ( u, v) | m_{i}(u,v)=|M_{i}(u,v)|. By a double counting argument, it is straightforward to find that

 | { ∑ i = 0 t m i ​ ( u, v) = ν − 2 ​ k + μ − 2; ∑ i = 0 t i ​ m i ​ ( u, v) = μ ⁡ ( k − 2 ​ λ − 2); ∑ i = 0 t ( i 2) ​ m i ​ ( u, v) = ( μ − 2) ​ ( μ 2). \displaystyle\left\{\begin{array}[]{l}\displaystyle{\sum_{i=0}^{t}m_{i}(u,v)=\nu-2k+\mu-2};\\ \\ \displaystyle{\sum_{i=0}^{t}im_{i}(u,v)=\mu(k-2\lambda-2)};\\ \\ \displaystyle{\sum_{i=0}^{t}{{i}\choose{2}}m_{i}(u,v)=(\mu-2){{\mu}\choose{2}}}.\end{array}\right. |  |

Notice that G G satisfies ( 1) if and only if m 0 ​ ( u, v) ≠ 0 m_{0}(u,v)\neq 0 for every two non-adjacent vertices u, v ∈ V ⁡ ( G) u,v\in V(G).

## III. The Proof of Theorem 1

In this section, we give a proof of Theorem 1. Let 𝔾 \mathbb{G} be a diamond-free 𝖲𝖱𝖦 ⁡ ( ( n 2 + 3 ​ n − 2) 2, n ⁡ ( n 2 + 3 ​ n − 1), 2, n ⁡ ( n + 1)) {\mathsf{SRG}}((n^{2}+3n-2)^{2},n(n^{2}+3n-1),2,n(n+1)), for some integer n ⩾ 3 n\geqslant 3, satisfying ( 1). We will demonstrate that either n = 3 n=3 or n = 10 n=10. In the following lemma, we solve the system ( II. Notation and Preliminaries) for each pair u ≁ v u\nsim v of vertices of 𝔾 \mathbb{G}. For any vertex u ∈ V ⁡ ( 𝔾) u\in V(\mathbb{G}), we denote by Φ ⁡ ( u) \mathnormal{\Phi}(u) the partition of N ⁡ ( u) N(u) into cliques of size 3 3.

###### Lemma 2

. For every two non-adjacent vertices u, v ∈ V ⁡ ( 𝔾) u,v\in V(\mathbb{G}), the system ( II. Notation and Preliminaries) has the unique solution

 | { m 0 ​ ( u, v) = 2; m 1 ​ ( u, v) = ⋯ = m n − 1 ​ ( u, v) = 0; m n ​ ( u, v) = n ⁡ ( n + 2) ​ ( n 2 − 1); m n + 1 ​ ( u, v) = 2 ​ n ​ ( n 2 − 4); m n + 2 ​ ( u, v) = n ⁡ ( n + 1). \displaystyle\left\{\begin{array}[]{l}m_{0}(u,v)=2;\\ m_{1}(u,v)=\cdots=m_{n-1}(u,v)=0;\\ m_{n}(u,v)=n(n+2)(n^{2}-1);\\ m_{n+1}(u,v)=2n(n^{2}-4);\\ m_{n+2}(u,v)=n(n+1).\end{array}\right. |  |

Moreover, if M 0 ​ ( u, v) = { a, b } M_{0}(u,v)=\{a,b\}, for some vertices a, b ∈ V ⁡ ( 𝔾) a,b\in V(\mathbb{G}), then a ≁ b a\nsim b, p u ​ ( a, b) = 0 p_{u}(a,b)=0, and any element of Φ ⁡ ( u) \mathnormal{\Phi}(u) which meets N ⁡ ( v) N(v), also meets both N ⁡ ( a) N(a) and N ⁡ ( b) N(b).

###### Proof.

Fix two non-adjacent vertices u, v ∈ V ⁡ ( 𝔾) u,v\in V(\mathbb{G}). Since 𝔾 \mathbb{G} satisfies ( 1), there exists a vertex a ∈ M 0 ​ ( u, v) a\in M_{0}(u,v). We first establish the following steps.

Step 1. ⟨ M 0 ​ ( u, v), M n + 2 ​ ( u, v) ⟩ \langle M_{0}(u,v),M_{n+2}(u,v)\rangle is complete bipartite.

By contrary, suppose that x ∈ M 0 ​ ( u, v) x\in M_{0}(u,v) is not adjacent to y ∈ M n + 2 ​ ( u, v) y\in M_{n+2}(u,v). Since q u ​ ( v, x) = μ q_{u}(v,x)=\mu, p u ​ ( v, y) = 2 p_{u}(v,y)=2, and q u ​ ( v, y) = n + 2 q_{u}(v,y)=n+2, one can easily deduce that q u ​ ( x, y) ⩾ n + 2 q_{u}(x,y)\geqslant n+2 and p u ​ ( x, y) + q u ​ ( x, y) = n + 4 p_{u}(x,y)+q_{u}(x,y)=n+4. Further, we have from ( II. Notation and Preliminaries) that ( n − 1) ​ p u ​ ( x, y) + q u ​ ( x, y) = μ (n-1)p_{u}(x,y)+q_{u}(x,y)=\mu. These two equalities yield that q u ​ ( x, y) = 2 q_{u}(x,y)=2, a contradiction.

Step 2. ⟨ N ⁡ ( u, a), N ⁡ ( v, a) ⟩ \langle N(u,a),N(v,a)\rangle is 1 1 -regular.

Consider an arbitrary vertex x ∈ N ⁡ ( v, a) x\in N(v,a). Since ⟨ N ⁡ [v] ⟩ \langle N[v]\rangle is a disjoint union of triangles, p u ​ ( v, x) = 1 p_{u}(v,x)=1 and so ( II. Notation and Preliminaries) implies that q u ​ ( v, x) = n + 3 q_{u}(v,x)=n+3. This shows that p u ​ ( a, x) + q u ​ ( a, x) = n + 4 p_{u}(a,x)+q_{u}(a,x)=n+4. Again, ( II. Notation and Preliminaries) yields that p u ​ ( a, x) = 1 p_{u}(a,x)=1, as required.

Step 3. m n + 2 ​ ( u, v) ⩽ μ m_{n+2}(u,v)\leqslant\mu.

Consider an arbitrary vertex x ∈ M n + 2 ​ ( u, v) x\in M_{n+2}(u,v). Since q u ​ ( v, a) = μ q_{u}(v,a)=\mu, p u ​ ( v, x) = n + 2 p_{u}(v,x)=n+2, and q u ​ ( v, x) = 2 q_{u}(v,x)=2, we conclude that p u ​ ( a, x) + q u ​ ( a, x) = n + 4 p_{u}(a,x)+q_{u}(a,x)=n+4. By Step 1 and ( II. Notation and Preliminaries), we find that p u ​ ( a, x) = 1 p_{u}(a,x)=1 and similarly, p v ​ ( a, x) = 1 p_{v}(a,x)=1. Let N ⁡ ( u, a, x) = { u ′ } N(u,a,x)=\{u^{\prime}\} and N ⁡ ( v, a, x) = { v ′ } N(v,a,x)=\{v^{\prime}\}. Since 𝔾 \mathbb{G} is diamond-free, u ′ ∼ v ′ u^{\prime}\thicksim v^{\prime}. It follows from Step 2 that m n + 2 ​ ( u, v) ⩽ μ m_{n+2}(u,v)\leqslant\mu, as desired.

Step 4. m 0 ​ ( u, v) ⩽ 2 m_{0}(u,v)\leqslant 2 and the ‘Moreover’ statement holds.

For every two vertices x, y ∈ M 0 ​ ( u, v) x,y\in M_{0}(u,v), we have p u ​ ( x, y) + q u ​ ( x, y) = μ p_{u}(x,y)+q_{u}(x,y)=\mu and by ( II. Notation and Preliminaries), ( n − 1) ​ p u ​ ( x, y) + q u ​ ( x, y) = ϵ ⁡ ( n + 1) (n-1)p_{u}(x,y)+q_{u}(x,y)=\epsilon(n+1), where ϵ ∈ { 2, n } \epsilon\in\{2,n\}. This yields that p u ​ ( x, y) = 0 p_{u}(x,y)=0 and x ≁ y x\nsim y. Since ⟨ N ⁡ [u] ⟩ \langle N[u]\rangle is a disjoint union of triangles, we must have m 0 ​ ( u, v) ⩽ 2 m_{0}(u,v)\leqslant 2. If M 0 ​ ( u, v) = { a, b } M_{0}(u,v)=\{a,b\}, then ( II. Notation and Preliminaries) forces that q u ​ ( v, a) = q u ​ ( v, b) = μ q_{u}(v,a)=q_{u}(v,b)=\mu. This shows clearly that the ‘Moreover’ statement is valid.

Step 5. Let { u, v 1, w 1 } \{u,v_{1},w_{1}\} be an independent set with p u ​ ( v 1, w 1) ≠ 0 p_{u}(v_{1},w_{1})\neq 0. Then p u ​ ( v 1, w 1) ⩾ n p_{u}(v_{1},w_{1})\geqslant n.

Let v 2 ∈ M 0 ​ ( u, v 1) v_{2}\in M_{0}(u,v_{1}) and w 2 ∈ M 0 ​ ( u, w 1) w_{2}\in M_{0}(u,w_{1}). Since p u ​ ( v 1, w 1) ≠ 0 p_{u}(v_{1},w_{1})\neq 0, Step 4 shows that v 2 ≠ w 2 v_{2}\neq w_{2}. Let t t denote the number of elements in Φ ⁡ ( u) \mathnormal{\Phi}(u) meeting both N ⁡ ( v 1) N(v_{1}) and N ⁡ ( w 1) N(w_{1}). Using Step 4 and ( II. Notation and Preliminaries), we have

 | ( n − 1) ​ p u ​ ( v i, w j) + ( t − p u ​ ( v i, w j)) = ϵ i ​ j ​ ( n + 1), for ​ i, j ∈ { 1, 2 }, \displaystyle(n-1)p_{u}(v_{i},w_{j})+\big(t-p_{u}(v_{i},w_{j})\big)=\epsilon_{ij}(n+1),\quad\text{ for }i,j\in\{1,2\}, |  | (21) |

where ϵ i ​ j = 2 \epsilon_{ij}=2, if v i ∼ w j v_{i}\thicksim w_{j} and ϵ i ​ j = n \epsilon_{ij}=n, otherwise. Since n ⩾ 3 n\geqslant 3 and p u ​ ( v 1, w 1) + p u ​ ( v 1, w 2) + p u ​ ( v 2, w 1) + p u ​ ( v 2, w 2) = t p_{u}(v_{1},w_{1})+p_{u}(v_{1},w_{2})+p_{u}(v_{2},w_{1})+p_{u}(v_{2},w_{2})=t, summing up the four formulae given in ( 21), we obtain that t ⩽ 4 ​ μ / ( n + 2) t\leqslant 4\mu/(n+2). The equality ( 21) for i = j = 1 i=j=1 yields that p u ​ ( v 1, w 1) ⩾ μ / ( n + 2) > n − 1 p_{u}(v_{1},w_{1})\geqslant\mu/(n+2)>n-1, as we wanted to prove.

We are now prepared to solve the system ( II. Notation and Preliminaries) for 𝔾 \mathbb{G}. Obviously, Step 5 means that m 1 ​ ( u, v) = ⋯ = m n − 1 ​ ( u, v) = 0 m_{1}(u,v)=\cdots=m_{n-1}(u,v)=0. Solving the system ( II. Notation and Preliminaries) in terms of m n ​ ( u, v), m_{n}(u,v), m n + 1 ​ ( u, v), m_{n+1}(u,v), m n + 2 ​ ( u, v) m_{n+2}(u,v), we obtain that

 |  | m n ​ ( u, v) = ( n + 1) ​ ( n + 2) ​ ( n 2 − n + 1) − ( n + 2 2) ​ m 0 ​ ( u, v); \displaystyle m_{n}(u,v)=(n+1)(n+2)(n^{2}-n+1)-{n+2\choose 2}m_{0}(u,v); |  | (22) |

 |  | m n + 1 ​ ( u, v) = 2 ​ n ​ ( n + 2) ​ ( n − 3) + n ⁡ ( n + 2) ​ m 0 ​ ( u, v); \displaystyle m_{n+1}(u,v)=2n(n+2)(n-3)+n(n+2)m_{0}(u,v); |  | (23) |

 |  | m n + 2 ​ ( u, v) = 2 ​ n ​ ( n + 1) − ( n + 1 2) ​ m 0 ​ ( u, v). \displaystyle m_{n+2}(u,v)=2n(n+1)-{n+1\choose 2}m_{0}(u,v). |  | (24) |

 | { \displaystyle\left\{\begin{array}[]{l}${}$\hskip 284.52756pt${}$\vskip 62.59596pt${}$\end{array}\right. |  |

From ( 24) and using Steps 3 and 4, we deduce that m 0 ​ ( u, v) = 2 m_{0}(u,v)=2 and m n + 2 ​ ( u, v) = n ⁡ ( n + 1) m_{n+2}(u,v)=n(n+1). Now, the solution ( 2) is clearly obtained from ( 22) and ( 23). □ \square

Consider a vertex u ∈ V ⁡ ( 𝔾) u\in V(\mathbb{G}). Obviously, Lemma 2 shows that N ¯ ​ ( u) \overline{N}(u) has a partition Ψ ⁡ ( u) \mathnormal{\Psi}(u) into independent sets of size 3 3 such that p u ​ ( x, y) = 0 p_{u}(x,y)=0, for every two distinct vertices x x and y y belonging to an element of Ψ ⁡ ( u) \mathnormal{\Psi}(u). Notice that for every subsets ϕ ∈ Φ ⁡ ( u) \phi\in\mathnormal{\Phi}(u) and ψ ∈ Ψ ⁡ ( u) \psi\in\mathnormal{\Psi}(u), ⟨ ϕ, ψ ⟩ \langle\phi,\psi\rangle is either edgeless or 1 1 -regular. In the latter case, we say that ϕ \phi and ψ \psi are matched together.

###### Lemma 3

. Let u ∈ V ⁡ ( 𝔾) u\in V(\mathbb{G}) and let ψ, ψ ′ \psi,\psi^{\prime} be two distinct elements of Ψ ⁡ ( u) \mathnormal{\Psi}(u). Then ⟨ ψ, ψ ′ ⟩ \langle\psi,\psi^{\prime}\rangle is r r -regular with r ∈ { 0, 1, 2 } r\in\{0,1,2\}. Moreover, for every two vertices v ∈ ψ v\in\psi and w ∈ ψ ′ w\in\psi^{\prime},

 | p u ​ ( v, w) = { max ⁡ { 0, r − 1 }, if v ∼ w; n + r, otherwise. \displaystyle p_{u}(v,w)=\left\{\begin{array}[]{ll}\max\{0,r-1\},&\text{if $v\thicksim w$};\\ n+r,&\text{otherwise}.\end{array}\right. |  |

###### Proof.

Let v ∈ ψ v\in\psi, ψ ′ = { w 1, w 2, w 3 } \psi^{\prime}=\{w_{1},w_{2},w_{3}\}, and t = p u ​ ( v, w 1) + p u ​ ( v, w 2) + p u ​ ( v, w 3) t=p_{u}(v,w_{1})+p_{u}(v,w_{2})+p_{u}(v,w_{3}). By Lemma 2, t t is independent of the choice of v v in ψ \psi and q u ​ ( v, w i) = t − p u ​ ( v, w i) q_{u}(v,w_{i})=t-p_{u}(v,w_{i}), for i = 1, 2, 3 i=1,2,3. Applying ( II. Notation and Preliminaries), we find for each i i that ( n − 2) ​ p u ​ ( v, w i) = ϵ i ​ ( n + 1) − t (n-2)p_{u}(v,w_{i})=\epsilon_{i}(n+1)-t, where ϵ i = 2 \epsilon_{i}=2, if v ∼ w i v\thicksim w_{i} and ϵ i = n \epsilon_{i}=n, otherwise. Summing up these three formulae, we obtain that ϵ 1 + ϵ 2 + ϵ 3 = t \epsilon_{1}+\epsilon_{2}+\epsilon_{3}=t. It follows from n ⩾ 3 n\geqslant 3 that the degrees of the elements in ψ \psi as some vertices of ⟨ ψ, ψ ′ ⟩ \langle\psi,\psi^{\prime}\rangle are the same. Clearly, a similar property holds for the elements of ψ ′ \psi^{\prime}. This shows that ⟨ ψ, ψ ′ ⟩ \langle\psi,\psi^{\prime}\rangle is r r -regular, for some r r. By Lemma 2, m 2 ​ ( u, v) = 0 m_{2}(u,v)=0 and so r ∈ { 0, 1, 2 } r\in\{0,1,2\}. The rest of the proof is straightforward. □ \square

###### Lemma 4

. Let u ∈ V ⁡ ( 𝔾) u\in V(\mathbb{G}) and let ψ = { v 1, v 2, v 3 } \psi=\{v_{1},v_{2},v_{3}\}, ψ ′ = { w 1, w 2, w 3 } \psi^{\prime}=\{w_{1},w_{2},w_{3}\} be two distinct elements of Ψ ⁡ ( u) \mathnormal{\Psi}(u) in which ⟨ ψ, ψ ′ ⟩ \langle\psi,\psi^{\prime}\rangle is 2 2 -regular and v i ≁ w i v_{i}\nsim w_{i}, for i = 1, 2, 3 i=1,2,3. Then for any element { a 1, a 2, a 3 } ∈ Φ ⁡ ( u) \{a_{1},a_{2},a_{3}\}\in\mathnormal{\Phi}(u) matched to both ψ \psi and ψ ′ \psi^{\prime}, there is an permutation π ∈ ⟨ ( 1 2 3) ⟩ \pi\in\langle(1\,2\,3)\rangle such that a i ∼ v i a_{i}\thicksim v_{i} and a i ∼ w π ⁡ ( i) a_{i}\thicksim w_{\pi(i)}, for i = 1, 2, 3 i=1,2,3.

###### Proof.

By the contrary and with no loss of generality, suppose that there is an element { a 1, a 2, a 3 } ∈ Φ ⁡ ( u) \{a_{1},a_{2},a_{3}\}\in\mathnormal{\Phi}(u) with a 1 ∈ N ⁡ ( v 1, w 1) a_{1}\in N(v_{1},w_{1}), a 2 ∈ N ⁡ ( v 2, w 3) a_{2}\in N(v_{2},w_{3}), and a 3 ∈ N ⁡ ( v 3, w 2) a_{3}\in N(v_{3},w_{2}). Since the neighborhood of each vertex of 𝔾 \mathbb{G} is a disjoint union of triangles, there is a vertex x ∈ N ⁡ ( a 2, v 2, w 3) x\in N(a_{2},v_{2},w_{3}). Since { a 2, w 3, x } ∈ Φ ⁡ ( v 2) \{a_{2},w_{3},x\}\in\mathnormal{\Phi}(v_{2}), { u, v 1, v 3 } ∈ Ψ ⁡ ( v 2) \{u,v_{1},v_{3}\}\in\mathnormal{\Psi}(v_{2}), a 2 ∼ u a_{2}\thicksim u, and w 3 ∼ v 1 w_{3}\thicksim v_{1}, we deduce that x ∼ v 3 x\thicksim v_{3}. Also, since { a 2, v 2, x } ∈ Φ ⁡ ( w 3) \{a_{2},v_{2},x\}\in\mathnormal{\Phi}(w_{3}), { u, w 1, w 2 } ∈ Ψ ⁡ ( w 3) \{u,w_{1},w_{2}\}\in\mathnormal{\Psi}(w_{3}), a 2 ∼ u a_{2}\thicksim u, and v 2 ∼ w 1 v_{2}\thicksim w_{1}, we conclude that x ∼ w 2 x\thicksim w_{2}. Thus ⟨ { a 3, v 3, w 2, x } ⟩ \langle\{a_{3},v_{3},w_{2},x\}\rangle contains a diamond as a subgraph, which forces that x ∼ a 3 x\thicksim a_{3}. However, this is impossible, since { u, a 1, x } ⊆ N ⁡ ( a 2, a 3) \{u,a_{1},x\}\subseteq N(a_{2},a_{3}). □ \square

###### Lemma 5

. Let u ∈ V ⁡ ( 𝔾) u\in V(\mathbb{G}) and let ϕ, ϕ ′ \phi,\phi^{\prime} be two distinct elements of Φ ⁡ ( u) \mathnormal{\Phi}(u). Then there is a suitable labeling ϕ = { a 1, a 2, a 3 } \phi=\{a_{1},a_{2},a_{3}\} and ϕ ′ = { b 1, b 2, b 3 } \phi^{\prime}=\{b_{1},b_{2},b_{3}\} such that for any element { v 1, v 2, v 3 } ∈ Ψ ⁡ ( u) \{v_{1},v_{2},v_{3}\}\in\mathnormal{\Psi}(u) matched to both ϕ \phi and ϕ ′ \phi^{\prime}, the relations a i ∼ v i a_{i}\thicksim v_{i} and b i ∼ v π ⁡ ( i) b_{i}\thicksim v_{\pi(i)} hold, for any i ∈ { 1, 2, 3 } i\in\{1,2,3\} and some permutation π ∈ ⟨ ( 1 2 3) ⟩ \pi\in\langle(1\,2\,3)\rangle.

###### Proof.

Let ℛ i ​ j ​ ℓ = { { v 1, v 2, v 3 } ∈ Ψ ( u) | v 1 ∈ N ( a 1, b i), v 2 ∈ N ( a 2, b j), v 3 ∈ N ( a 3, b ℓ) } \mathcal{R}_{ij\ell}=\{\{v_{1},v_{2},v_{3}\}\in\mathnormal{\Psi}(u)\,|\,v_{1}\in N(a_{1},b_{i}),v_{2}\in N(a_{2},b_{j}),v_{3}\in N(a_{3},b_{\ell})\}, for every i, j, ℓ i,j,\ell with { i, j, ℓ } = { 1, 2, 3 }. \{i,j,\ell\}=\{1,2,3\}. Since each pair a i ≁ b j a_{i}\nsim b_{j} has μ − 1 \mu-1 common neighbors except u u, it is easily seen that | ℛ 123 | = | ℛ 231 | = | ℛ 312 | |\mathcal{R}_{123}|=|\mathcal{R}_{231}|=|\mathcal{R}_{312}| and | ℛ 132 | = | ℛ 321 | = | ℛ 213 | = μ − 1 − | ℛ 123 | |\mathcal{R}_{132}|=|\mathcal{R}_{321}|=|\mathcal{R}_{213}|=\mu-1-|\mathcal{R}_{123}|. Let 𝒮 = ℛ 123 ∪ ℛ 231 ∪ ℛ 312 \mathcal{S}=\mathcal{R}_{123}\cup\mathcal{R}_{231}\cup\mathcal{R}_{312} and 𝒯 = ℛ 132 ∪ ℛ 321 ∪ ℛ 213 \mathcal{T}=\mathcal{R}_{132}\cup\mathcal{R}_{321}\cup\mathcal{R}_{213}. The assertion of the lemma is equivalent to that either 𝒮 = ∅ \mathcal{S}=\varnothing or 𝒯 = ∅ \mathcal{T}=\varnothing. By contrary, suppose that both 𝒮 \mathcal{S} and 𝒯 \mathcal{T} are not empty. We show that the degree of each vertex of ⟨ 𝒮 ⟩ \langle\mathcal{S}\rangle is at least 2 ​ n 2n. With no loss of generality, consider x ∈ 𝒮 ∩ N ⁡ ( a 1, b 1) x\in\mathcal{S}\cap N(a_{1},b_{1}). It is easily checked by Lemmas 3 and 4 that ⟨ 𝒮, 𝒯 ⟩ \langle\mathcal{S},\mathcal{T}\rangle is edgeless. Since b 2 ∼ b 3 b_{2}\thicksim b_{3}, at least one set in each of pairs { N ⁡ ( x, a 2, b 2), N ⁡ ( x, a 2, b 3) } \{N(x,a_{2},b_{2}),N(x,a_{2},b_{3})\} and { N ⁡ ( x, a 3, b 2), N ⁡ ( x, a 3, b 3) } \{N(x,a_{3},b_{2}),N(x,a_{3},b_{3})\} is not empty. On the other hand, it follows from ( 2) that either p x ​ ( a i, b j) = 0 p_{x}(a_{i},b_{j})=0 or p x ​ ( a i, b j) ⩾ n p_{x}(a_{i},b_{j})\geqslant n, for every indices i, j ∈ { 2, 3 } i,j\in\{2,3\}. This clearly means that the degree of x x as a vertex of ⟨ 𝒮 ⟩ \langle\mathcal{S}\rangle is at least 2 ​ n 2n, as desired. Obviously, the similar property holds for ⟨ 𝒯 ⟩ \langle\mathcal{T}\rangle. So, the second largest eigenvalue of ⟨ 𝒮, 𝒯 ⟩ = ⟨ 𝒮 ⟩ ∪ ⟨ 𝒯 ⟩ \langle\mathcal{S},\mathcal{T}\rangle=\langle\mathcal{S}\rangle\cup\langle\mathcal{T}\rangle would be at least 2 ​ n 2n. This is a contradiction by the interlacing theorem, since the second largest eigenvalue of 𝔾 \mathbb{G} is r = n r=n. □ \square

We now proceed to define a permutation σ u \sigma_{u} on V ⁡ ( 𝔾) V(\mathbb{G}) of order 3 3 and then demonstrate that σ u \sigma_{u} is in fact an automorphism of 𝔾 \mathbb{G}. Put σ u ​ ( u) = u \sigma_{u}(u)=u. Fix an element ζ = { z 1, z 2, z 3 } \zeta=\{z_{1},z_{2},z_{3}\} of Φ ⁡ ( u) \mathnormal{\Phi}(u) and define σ u ​ ( z 1) = z 2 \sigma_{u}(z_{1})=z_{2}, σ u ​ ( z 2) = z 3 \sigma_{u}(z_{2})=z_{3}, and σ u ​ ( z 3) = z 1 \sigma_{u}(z_{3})=z_{1}. We repeatedly do the following process until σ u \sigma_{u} is defined on the whole V ⁡ ( 𝔾) V(\mathbb{G}):

Assume that { a 1, a 2, a 3 } ∈ Φ ⁡ ( u) \{a_{1},a_{2},a_{3}\}\in\mathnormal{\Phi}(u) and { v 1, v 2, v 3 } ∈ Ψ ⁡ ( u) \{v_{1},v_{2},v_{3}\}\in\mathnormal{\Psi}(u) form a matched pair with a i ∼ v i a_{i}\thicksim v_{i}, for i = 1, 2, 3 i=1,2,3. If σ u \sigma_{u} is already defined on only one of the two triples, then we define σ u \sigma_{u} on the other one such that σ u \sigma_{u} induces the same permutation on indices of elements of the two triples.

Note that we may first define σ u \sigma_{u} on the all elements of Ψ ⁡ ( u) \mathnormal{\Psi}(u) matched with ζ \zeta and then we can proceed to define σ u \sigma_{u} on each element of Φ ⁡ ( u) \mathnormal{\Phi}(u), since μ > 1 \mu>1. Finally, σ u \sigma_{u} is defined on each element of Ψ ⁡ ( u) \mathnormal{\Psi}(u). We show that σ u \sigma_{u} is a well defined permutation. For this, it suffices to demonstrate that

- ( 𝗂) \mathsf{(i)}

if σ u \sigma_{u} is defined on two elements ψ = { v 1, v 2, v 3 } \psi=\{v_{1},v_{2},v_{3}\} and ψ ′ = { w 1, w 2, w 3 } \psi^{\prime}=\{w_{1},w_{2},w_{3}\} in Ψ ⁡ ( u) \mathnormal{\Psi}(u) and ϕ = { a 1, a 2, a 3 } ∈ Φ ⁡ ( u) \phi=\{a_{1},a_{2},a_{3}\}\in\mathnormal{\Phi}(u) is matched to ψ \psi and ψ ′ \psi^{\prime}, then the definitions of σ u \sigma_{u} forced by ψ \psi and ψ ′ \psi^{\prime} on ϕ \phi are the same;

- ( 𝗂𝗂) \mathsf{(ii)}

if σ u \sigma_{u} is defined on two elements ϕ = { a 1, a 2, a 3 } \phi=\{a_{1},a_{2},a_{3}\} and ϕ ′ = { b 1, b 2, b 3 } \phi^{\prime}=\{b_{1},b_{2},b_{3}\} of Φ ⁡ ( u) \mathnormal{\Phi}(u) and ψ = { v 1, v 2, v 3 } ∈ Ψ ⁡ ( u) \psi=\{v_{1},v_{2},v_{3}\}\in\mathnormal{\Psi}(u) is matched to ϕ \phi and ϕ ′ \phi^{\prime}, then the definitions of σ u \sigma_{u} forced by ϕ \phi and ϕ ′ \phi^{\prime} on ψ \psi are the same.

The assertions ( 𝗂) \mathsf{(i)} and ( 𝗂𝗂) \mathsf{(ii)} are direct consequences of Lemmas 4 and 5, respectively. For ( 𝗂) \mathsf{(i)}, note that we may assume that ζ \zeta is matched to ψ \psi and ψ ′ \psi^{\prime}. For ( 𝗂𝗂) \mathsf{(ii)}, note that z 1 ∈ M i ​ ( a 1, b 1) z_{1}\in M_{i}(a_{1},b_{1}), for some i ⩾ 1 i\geqslant 1, and so there is a vertex w ∈ N ⁡ ( z 1, a 1, b 1) w\in N(z_{1},a_{1},b_{1}). This shows that there is an element in Ψ ⁡ ( u) \mathnormal{\Psi}(u) containing w w which matches to ζ \zeta, ψ \psi, and ψ ′ \psi^{\prime}.

The above discussion implies that σ u \sigma_{u} is well defined. Also, from the definition of σ u \sigma_{u}, we easily see that the subgraphs ⟨ N ⁡ [u] ⟩ \langle N[u]\rangle and ⟨ N ​ [u], N ¯ ​ ( u) ⟩ \langle N[u],\overline{N}(u)\rangle are fixed by σ u \sigma_{u}. Therefore, applying ( 5), ⟨ N ¯ ​ ( u) ⟩ \langle\overline{N}(u)\rangle is fixed by σ u \sigma_{u} and hence σ u \sigma_{u} is an automorphism of 𝔾 \mathbb{G}.

As we saw in the above, for each vertex u ∈ V ⁡ ( 𝔾) u\in V(\mathbb{G}), we can associate to u u two automorphisms of 𝔾 \mathbb{G} of order 3 3, that are the inverse of each other. Fix a vertex 𝓏 ∈ 𝒱 ⁡ ( 𝔾) \mathpzc{z}\in V(\mathbb{G}) and also fix σ ​ z \sigma{z} to be one of the two automorphisms associated to 𝓏 \mathpzc{z}. Now, for any arbitrary vertex u ∈ V ⁡ ( 𝔾) u\in V(\mathbb{G}), let σ u \sigma_{u} be that automorphism associated to u u satisfying σ u ​ ( 𝓏) = σ − 1 ​ 𝓏 ​ ( 𝓊) \sigma_{u}(\mathpzc{z})=\sigma^{-1}{z}(u).

###### Lemma 6

. For every two vertices u, v ∈ V ⁡ ( 𝔾) u,v\in V(\mathbb{G}), σ u ​ ( v) = σ v − 1 ​ ( u) \sigma_{u}(v)=\sigma^{-1}_{v}(u).

###### Proof.

In order to prove the lemma, we need to establish a more general result. For any vertex u ∈ V ⁡ ( 𝔾) u\in V(\mathbb{G}), fix τ u u {}^{u}\tau_{u} to be one of the two automorphisms which perviously defined at u u. Also, for each other vertex v ∈ V ⁡ ( 𝔾) v\in V(\mathbb{G}), let τ v u {}^{u}\tau_{v} be that automorphism defined at v v satisfying τ v u ​ ( u) = τ u − 1 u ​ ( v) {}^{u}\tau_{v}(u)={{}^{u}}\tau^{-1}_{u}(v). Consequently, we have τ v − 1 u ​ ( u) = τ u u ​ ( v) {}^{u}\tau^{-1}_{v}(u)={{}^{u}}\tau_{u}(v), for every vertices u, v ∈ V ⁡ ( 𝔾) u,v\in V(\mathbb{G}). We claim that τ b a ​ ( c) = τ c − 1 a ​ ( b) {}^{a}\tau_{b}(c)={{}^{a}}\tau^{-1}_{c}(b), for every vertices a, b, c ∈ V ⁡ ( 𝔾) a,b,c\in V(\mathbb{G}). This clearly implies the assertion of the lemma, if we consider 𝓏 \mathpzc{z} instead of a a. We will just prove the claim when a, b, c a,b,c are mutually distinct, since otherwise the claim follows from the definition. We consider the following seven cases.

Case 1. a ∼ b a\thicksim b, a ∼ c a\thicksim c, b ∼ c b\thicksim c.

In this case, the claim is easily checked from the definition.

Case 2. a ∼ b a\thicksim b, a ∼ c a\thicksim c, b ≁ c b\nsim c.

Let { b, u, u ′ }, { c, v, v ′ } ∈ Φ ⁡ ( a) \{b,u,u^{\prime}\},\{c,v,v^{\prime}\}\in\mathnormal{\Phi}(a) and M 0 ​ ( b, c) = { w, w ′ } M_{0}(b,c)=\{w,w^{\prime}\}. From N ⁡ ( b, c, w) = N ⁡ ( b, c, w ′) = ∅ N(b,c,w)=N(b,c,w^{\prime})=\varnothing, we find that a ≁ w a\nsim w and a ≁ w ′ a\nsim w^{\prime}. Also, from a ∉ M 0 ​ ( w, w ′) = { b, c } a\not\in M_{0}(w,w^{\prime})=\{b,c\}, one concludes that M 0 ​ ( a, w) M_{0}(a,w) and M 0 ​ ( a, w ′) M_{0}(a,w^{\prime}) are disjoint. Let M 0 ​ ( a, w) = { x, x ′ } M_{0}(a,w)=\{x,x^{\prime}\} and M 0 ​ ( a, w ′) = { y, y ′ } M_{0}(a,w^{\prime})=\{y,y^{\prime}\}. Since { a, u, u ′ } ∈ Φ ⁡ ( b) \{a,u,u^{\prime}\}\in\mathnormal{\Phi}(b), { c, w, w ′ } ∈ Ψ ⁡ ( b) \{c,w,w^{\prime}\}\in\mathnormal{\Psi}(b), and a ∼ c a\thicksim c, we may, with no loss of generality, assume that u ∼ w u\thicksim w and u ′ ∼ w ′ u^{\prime}\thicksim w^{\prime}. Similarly, let v ∼ w v\thicksim w and v ′ ∼ w ′ v^{\prime}\thicksim w^{\prime}. Without loss of generality, assume that τ a a ​ ( b) = u {}^{a}\tau_{a}(b)=u and b ∼ x b\thicksim x. Then τ b a ​ ( a) = τ a − 1 a ​ ( b) = u ′ {}^{a}\tau_{b}(a)={{}^{a}}\tau^{-1}_{a}(b)=u^{\prime}, which yields that τ b a ​ ( c) = w ′ {}^{a}\tau_{b}(c)=w^{\prime}. Consider two elements { a, x, x ′ }, { b, c, w ′ } ∈ Ψ ⁡ ( w) \{a,x,x^{\prime}\},\{b,c,w^{\prime}\}\in\mathnormal{\Psi}(w). Since a ∈ N ⁡ ( b, c) a\in N(b,c), Lemma 3 yields that ⟨ { a, x, x ′ }, { b, c, w ′ } ⟩ \langle\{a,x,x^{\prime}\},\{b,c,w^{\prime}\}\rangle is 2 2 -regular and so we conclude from b ∼ x b\thicksim x that c ∼ x ′ c\thicksim x^{\prime}. Therefore, x ∼ v ′ x\thicksim v^{\prime}. Since τ a a ​ ( b) {}^{a}\tau_{a}(b) has cycle ( b ​ u ​ u ′) (b\,u\,u^{\prime}), it also has cycles ( x ​ w ​ x ′) (x\,w\,x^{\prime}) and ( v ′ ​ v ​ c) (v^{\prime}\,v\,c). Hence τ a a ​ ( c) = v ′ {}^{a}\tau_{a}(c)=v^{\prime}, which in turn implies that τ c − 1 a ​ ( a) = τ a a ​ ( c) = v ′ {}^{a}\tau^{-1}_{c}(a)={{}^{a}}\tau_{a}(c)=v^{\prime}. So τ c a {}^{a}\tau_{c} has cycle ( v ′ ​ a ​ v) (v^{\prime}\,a\,v) and so it also has cycle ( w ′ ​ b ​ w) (w^{\prime}\,b\,w). Thus τ c − 1 a ​ ( b) = w ′, {}^{a}\tau^{-1}_{c}(b)=w^{\prime}, as desired.

Case 3. a ∼ b a\thicksim b, a ≁ c a\nsim c, b ∼ c b\thicksim c.

By the definition, either τ a b = τ a a {}^{b}\tau_{a}={{}^{a}}\tau_{a} or τ a b = τ a − 1 a {}^{b}\tau_{a}={{}^{a}}\tau^{-1}_{a}. We only consider the first equality. The argument is similar, if the second equality occurs. We have τ b a ​ ( a) = τ a − 1 a ​ ( b) = τ a − 1 b ​ ( b) = τ b b ​ ( a) {}^{a}\tau_{b}(a)={{}^{a}}\tau^{-1}_{a}(b)={{}^{b}}\tau^{-1}_{a}(b)={{}^{b}}\tau_{b}(a). Since τ b a {}^{a}\tau_{b} and τ b b {}^{b}\tau_{b} are coincide on { a, b } \{a,b\}, we conclude from the definition that τ b a = τ b b {}^{a}\tau_{b}={{}^{b}}\tau_{b}. Also, Case 2 implies that τ c b ​ ( a) = τ a − 1 b ​ ( c) = τ a − 1 a ​ ( c) = τ c a ​ ( a) {}^{b}\tau_{c}(a)={{}^{b}}\tau^{-1}_{a}(c)={{}^{a}}\tau^{-1}_{a}(c)={{}^{a}}\tau_{c}(a), which yields that τ c b = τ c a {}^{b}\tau_{c}={{}^{a}}\tau_{c}. Therefore, τ b a ​ ( c) = τ b b ​ ( c) = τ c − 1 b ​ ( b) = τ c − 1 a ​ ( b) {}^{a}\tau_{b}(c)={{}^{b}}\tau_{b}(c)={{}^{b}}\tau^{-1}_{c}(b)={{}^{a}}\tau^{-1}_{c}(b), as required.

Case 4. N ⁡ ( a, b, c) ≠ ∅ N(a,b,c)\neq\varnothing.

Consider a vertex x ∈ N ⁡ ( a, b, c) x\in N(a,b,c). We assume that τ a x = τ a a {}^{x}\tau_{a}={{}^{a}}\tau_{a}. The argument is similar when τ a x = τ a − 1 a {}^{x}\tau_{a}={{}^{a}}\tau^{-1}_{a}. Using Cases 1 and 2, we can write τ b x ​ ( a) = τ a − 1 x ​ ( b) = τ a − 1 a ​ ( b) = τ b a ​ ( a) {}^{x}\tau_{b}(a)={{}^{x}}\tau^{-1}_{a}(b)={{}^{a}}\tau^{-1}_{a}(b)={{}^{a}}\tau_{b}(a). Hence τ b x = τ b a {}^{x}\tau_{b}={{}^{a}}\tau_{b}, and similarly, τ c x = τ c a {}^{x}\tau_{c}={{}^{a}}\tau_{c}. Therefore, by Cases 1 and 2, we find that τ b a ​ ( c) = τ b x ​ ( c) = τ c − 1 x ​ ( b) = τ c − 1 a ​ ( b) {}^{a}\tau_{b}(c)={{}^{x}}\tau_{b}(c)={{}^{x}}\tau^{-1}_{c}(b)={{}^{a}}\tau^{-1}_{c}(b), as we wanted to prove.

Case 5. a ≁ b a\nsim b, a ≁ c a\nsim c, b ≁ c b\nsim c.

If a ∈ M 0 ​ ( b, c) a\in M_{0}(b,c), then the claim is easily checked from the definition. So, let a ∉ M 0 ​ ( b, c) a\not\in M_{0}(b,c), which means that there exists a vertex x ∈ N ⁡ ( a, b, c) x\in N(a,b,c). Now we are done by Case 4.

Case 6. a ≁ b a\nsim b, a ≁ c a\nsim c, b ∼ c b\thicksim c.

It suffices by Case 4 to assume that N ⁡ ( a, b, c) = ∅ N(a,b,c)=\varnothing. Let y, y ′ ∈ N ⁡ ( a, b) y,y^{\prime}\in N(a,b) and z ∈ N ⁡ ( b, y ′) z\in N(b,y^{\prime}). Since a ≁ b a\nsim b, we have y ≁ y ′ y\nsim y^{\prime}. We assume that τ y a = τ y y {}^{a}\tau_{y}={{}^{y}}\tau_{y}. The argument is similar when τ y a = τ y − 1 y {}^{a}\tau_{y}={{}^{y}}\tau^{-1}_{y}. By Case 3, we obtain that τ b a ​ ( y) = τ y − 1 a ​ ( b) = τ y − 1 y ​ ( b) = τ b y ​ ( y) {}^{a}\tau_{b}(y)={{}^{a}}\tau^{-1}_{y}(b)={{}^{y}}\tau^{-1}_{y}(b)={{}^{y}}\tau_{b}(y), which yields that τ b a = τ b y {}^{a}\tau_{b}={{}^{y}}\tau_{b}. Since ⟨ N ⁡ ( b) ⟩ \langle N(b)\rangle and ⟨ N ⁡ ( y ′) ⟩ \langle N(y^{\prime})\rangle are disjoint unions of triangles, z ∉ N ⁡ ( a) ∪ N ⁡ ( c) ∪ N ⁡ ( y) z\not\in N(a)\cup N(c)\cup N(y). It follows from y ′ ∈ N ⁡ ( a, b, z) y^{\prime}\in N(a,b,z) and Cases 3 and 4 that τ z y ​ ( b) = τ b − 1 y ​ ( z) = τ b − 1 a ​ ( z) = τ z a ​ ( b) {}^{y}\tau_{z}(b)={{}^{y}}\tau^{-1}_{b}(z)={{}^{a}}\tau^{-1}_{b}(z)={{}^{a}}\tau_{z}(b) and thus τ z y = τ z a {}^{y}\tau_{z}={{}^{a}}\tau_{z}. Moreover, it follows from b ∈ N ⁡ ( c, y, z) b\in N(c,y,z) and Cases 4 and 5 that τ c y ​ ( z) = τ z − 1 y ​ ( c) = τ z − 1 a ​ ( c) = τ c a ​ ( z) {}^{y}\tau_{c}(z)={{}^{y}}\tau^{-1}_{z}(c)={{}^{a}}\tau^{-1}_{z}(c)={{}^{a}}\tau_{c}(z) and hence τ c y = τ c a {}^{y}\tau_{c}={{}^{a}}\tau_{c}. Since N ⁡ ( a, b, c) = ∅ N(a,b,c)=\varnothing, we have c ≁ y c\nsim y, which together Case 3 imply that τ b a ​ ( c) = τ b y ​ ( c) = τ c − 1 y ​ ( b) = τ c − 1 a ​ ( b) {}^{a}\tau_{b}(c)={{}^{y}}\tau_{b}(c)={{}^{y}}\tau_{c}^{-1}(b)={{}^{a}}\tau^{-1}_{c}(b), as desired.

Case 7. a ∼ b a\thicksim b, a ≁ c a\nsim c, b ≁ c b\nsim c.

We assume that τ a c = τ a a {}^{c}\tau_{a}={{}^{a}}\tau_{a}. The argument for the case τ a c = τ a − 1 a {}^{c}\tau_{a}={{}^{a}}\tau^{-1}_{a} is similar. We have τ c a ​ ( a) = τ a − 1 a ​ ( c) = τ a − 1 c ​ ( c) = τ c c ​ ( a) {}^{a}\tau_{c}(a)={{}^{a}}\tau^{-1}_{a}(c)={{}^{c}}\tau^{-1}_{a}(c)={{}^{c}}\tau_{c}(a), which implies that τ c a = τ c c {}^{a}\tau_{c}={{}^{c}}\tau_{c}. Using Case 6, τ b c ​ ( a) = τ a − 1 c ​ ( b) = τ a − 1 a ​ ( b) = τ b a ​ ( a) {}^{c}\tau_{b}(a)={{}^{c}}\tau^{-1}_{a}(b)={{}^{a}}\tau^{-1}_{a}(b)={{}^{a}}\tau_{b}(a) and so τ b c = τ b a {}^{c}\tau_{b}={{}^{a}}\tau_{b}. Now, we find that τ b a ​ ( c) = τ b c ​ ( c) = τ c − 1 c ​ ( b) = τ c − 1 a ​ ( b) {}^{a}\tau_{b}(c)={{}^{c}}\tau_{b}(c)={{}^{c}}\tau^{-1}_{c}(b)={{}^{a}}\tau^{-1}_{c}(b), as required.

The proof of the claim is now completed and so the assertion of the lemma follows. □ \square

In order to continue, we need the following result.

###### Theorem 7

. [1, Theorem 3.2] If π \pi is a non-trivial automorphism of an 𝖲𝖱𝖦 ⁡ ( ν, k, λ, μ) {\mathsf{SRG}}(\nu,k,\lambda,\mu) with the second largest eigenvalue r r, then the number of fixed points of π \pi is at most

 | ν k − r ​ max ⁡ ( λ, μ). \frac{\nu}{k-r}\max(\lambda,\mu). |  |

###### Corollary 8

. Each non-trivial automorphism of 𝔾 \mathbb{G} has at most ν / 4 \nu/4 fixed points.

###### Lemma 9

. For every two vertices u 1, u 2 ∈ V ⁡ ( 𝔾) u_{1},u_{2}\in V(\mathbb{G}), ( σ u 1 ​ σ u 2 − 1) 2 (\sigma_{u_{1}}\sigma^{-1}_{u_{2}})^{2} is equal to the identity.

###### Proof.

For four distinct vertices a, b, c, d ∈ V ⁡ ( 𝔾) a,b,c,d\in V(\mathbb{G}), we call the set { a, b, c, d } \{a,b,c,d\} to be related if either it is a clique or it is an independent set with M 0 ​ ( a, b) = { c, d } M_{0}(a,b)=\{c,d\}. Note that every two distinct vertices of 𝔾 \mathbb{G} is contained in a unique related set. Let U = { u 1, u 2, u 3, u 4 } U=\{u_{1},u_{2},u_{3},u_{4}\} be a related set and let ρ i ​ j = σ u i ​ σ u j − 1 \rho_{ij}=\sigma_{u_{i}}\sigma^{-1}_{u_{j}}, for every i, j ∈ { 1, 2, 3, 4 } i,j\in\{1,2,3,4\}. Consider a vertex x ∈ V ⁡ ( 𝔾) ∖ U x\in V(\mathbb{G})\setminus U. By Lemma 6, we find that σ σ u i − 1 ​ ( x) − 1 ​ ( U) = { ρ 1 ​ i ​ ( x), ρ 2 ​ i ​ ( x), ρ 3 ​ i ​ ( x), ρ 4 ​ i ​ ( x) } \sigma^{-1}_{\sigma^{-1}_{u_{i}}(x)}(U)=\{\rho_{1i}(x),\rho_{2i}(x),\rho_{3i}(x),\rho_{4i}(x)\} and σ u j ​ σ x ​ ( U) = { ρ j ​ 1 ​ ( x), ρ j ​ 2 ​ ( x), ρ j ​ 3 ​ ( x), ρ j ​ 4 ​ ( x) } \sigma_{u_{j}}\sigma_{x}(U)=\{\rho_{j1}(x),\rho_{j2}(x),\rho_{j3}(x),\rho_{j4}(x)\} are related, for every i, j ∈ { 1, 2, 3, 4 } i,j\in\{1,2,3,4\}. Since every two distinct vertices of 𝔾 \mathbb{G} is contained in a unique related set, it is easily seen that σ σ u i − 1 ​ ( x) − 1 ​ ( U) = σ u j ​ σ x ​ ( U) \sigma^{-1}_{\sigma^{-1}_{u_{i}}(x)}(U)=\sigma_{u_{j}}\sigma_{x}(U), for every indices i ≠ j i\neq j. It follows that the eight sets which we associated to x x in the above are the same. Denote the common set by ℋ x \mathcal{H}_{x}. Note that if y ∈ ℋ x y\in\mathcal{H}_{x}, then ℋ x = ℋ y \mathcal{H}_{x}=\mathcal{H}_{y}. Therefore, 𝒫 = { ℋ x | x ∈ V ⁡ ( 𝔾) ∖ U } \mathscr{P}=\{\mathcal{H}_{x}\,|\,x\in V(\mathbb{G})\setminus U\} is clearly a partition of V ⁡ ( 𝔾) ∖ U V(\mathbb{G})\setminus U into related sets.

Working towards a contradiction, suppose that ρ 12 ≠ ρ 21 \rho_{12}\neq\rho_{21}. Consider an arbitrary element ℋ x ∈ 𝒫 \mathcal{H}_{x}\in\mathscr{P}. Since ρ 12 2 \rho^{2}_{12} is a permutation on ℋ x \mathcal{H}_{x}, | ℋ x | = 4 |\mathcal{H}_{x}|=4, and ρ 12 ​ ( x) ≠ x \rho_{12}(x)\neq x, we obviously deduce that either ρ 12 2 \rho^{2}_{12} has no fixed point in ℋ x \mathcal{H}_{x} or ρ 12 2 \rho^{2}_{12} is the identity on ℋ x \mathcal{H}_{x}. Thus, Corollary 8 shows that ρ 12 2 \rho^{2}_{12} has no fixed point in at least 3 16 ​ ν − 1 \frac{3}{16}\nu-1 elements of 𝒫 \mathscr{P}.

Assume that ρ 12 2 \rho^{2}_{12} fixes no element of ℋ x = { x, ρ 12 ​ ( x), ρ 13 ​ ( x), ρ 14 ​ ( x) } \mathcal{H}_{x}=\{x,\rho_{12}(x),\rho_{13}(x),\rho_{14}(x)\}. So ρ 12 ​ ( x) ≠ ρ 21 ​ ( x) \rho_{12}(x)\neq\rho_{21}(x). We claim that one of ρ 12 ​ ρ 13 \rho_{12}\rho_{13} or ρ 12 ​ ρ 14 \rho_{12}\rho_{14} is the identity on ℋ x \mathcal{H}_{x}. Note that by Lemma 6, ρ i ​ j ​ ( x) ≠ ρ i ​ j ′ ​ ( x) \rho_{ij}(x)\neq\rho_{ij^{\prime}}(x) and ρ i ​ j ​ ( x) ≠ ρ i ′ ​ j ​ ( x) \rho_{ij}(x)\neq\rho_{i^{\prime}j}(x) whenever i ≠ i ′ i\neq i^{\prime} and j ≠ j ′ j\neq j^{\prime}. We clearly have ρ 21 ​ ( x) ∈ { ρ 13 ​ ( x), ρ 14 ​ ( x) } \rho_{21}(x)\in\{\rho_{13}(x),\rho_{14}(x)\}. Suppose that ρ 21 ​ ( x) = ρ 13 ​ ( x) \rho_{21}(x)=\rho_{13}(x). Since the eight sets which we associated to x x in the first paragraph of the proof are equal, one concludes that the elements of ℋ x ∖ { x } \mathcal{H}_{x}\setminus\{x\} are

 | { ρ 12 ​ ( x) = ρ 24 ​ ( x) = ρ 31 ​ ( x), ρ 13 ​ ( x) = ρ 21 ​ ( x) = ρ 34 ​ ( x), ρ 14 ​ ( x) = ρ 23 ​ ( x) = ρ 32 ​ ( x). \displaystyle\left\{\begin{array}[]{ccc}\rho_{12}(x)=\rho_{24}(x)=\rho_{31}(x),\\ \rho_{13}(x)=\rho_{21}(x)=\rho_{34}(x),\\ \rho_{14}(x)=\rho_{23}(x)=\rho_{32}(x).\end{array}\right. |  |

It is then easy to check that ρ 12 ​ ρ 13 \rho_{12}\rho_{13} is the identity on ℋ x \mathcal{H}_{x}. With a similar argument, one deduces that if ρ 21 ​ ( x) = ρ 14 ​ ( x) \rho_{21}(x)=\rho_{14}(x), then ρ 12 ​ ρ 14 \rho_{12}\rho_{14} is the identity on ℋ x \mathcal{H}_{x}. This establishes the claim.

Note that none of ρ 12 ​ ρ 13 \rho_{12}\rho_{13} and ρ 12 ​ ρ 14 \rho_{12}\rho_{14} are trivial. For instance, if ρ 12 ​ ρ 13 ​ ( u 1) = u 1 \rho_{12}\rho_{13}(u_{1})=u_{1}, then σ u 2 − 1 ​ σ u 1 ​ σ u 3 − 1 ​ ( u 1) = u 1 \sigma^{-1}_{u_{2}}\sigma_{u_{1}}\sigma^{-1}_{u_{3}}(u_{1})=u_{1} and so by Lemma 6, we find that σ u 2 ​ ( u 1) = σ u 1 ​ σ u 3 − 1 ​ ( u 1) = σ u 1 − 1 ​ ( u 3) = σ u 3 ​ ( u 1) \sigma_{u_{2}}(u_{1})=\sigma_{u_{1}}\sigma^{-1}_{u_{3}}(u_{1})=\sigma^{-1}_{u_{1}}(u_{3})=\sigma_{u_{3}}(u_{1}), which means that u 2 = u 3 u_{2}=u_{3}, a contradiction. Therefore, one of ρ 12 ​ ρ 13 \rho_{12}\rho_{13} or ρ 12 ​ ρ 14 \rho_{12}\rho_{14} is a non-trivial automorphism of 𝔾 \mathbb{G} which is the identity on at least 3 32 ​ ν − 1 2 \frac{3}{32}\nu-\frac{1}{2} elements of 𝒫 \mathscr{P}. It follows from Corollary 8 that 3 8 ​ ν − 2 ⩽ 1 4 ​ ν \frac{3}{8}\nu-2\leqslant\frac{1}{4}\nu, which it contradicts n ⩾ 3 n\geqslant 3. □ \square

###### Lemma 10

. The group Γ \mathnormal{\Gamma} generated by { σ u σ v − 1 | u, v ∈ V ( 𝔾) } \{\sigma_{u}\sigma^{-1}_{v}\,|\,u,v\in V(\mathbb{G})\} is Abelian and it acts transitively on V ⁡ ( 𝔾) V(\mathbb{G}).

###### Proof.

Consider the arbitrary vertices u, v, x, y ∈ V ⁡ ( 𝔾) u,v,x,y\in V(\mathbb{G}). By Lemma 6, σ v ​ σ σ u − 1 ​ ( v) − 1 ​ ( u) = v \sigma_{v}\sigma^{-1}_{\sigma^{-1}_{u}(v)}(u)=v, meaning that Γ \mathnormal{\Gamma} acts transitively on V ⁡ ( 𝔾) V(\mathbb{G}). Applying Lemma 9, we have ( σ u ​ σ v − 1) ​ ( σ x ​ σ y − 1) = σ u ​ σ x − 1 ​ σ v ​ σ y − 1 = σ x ​ σ u − 1 ​ σ y ​ σ v − 1 = ( σ x ​ σ y − 1) ​ ( σ u ​ σ v − 1) (\sigma_{u}\sigma^{-1}_{v})(\sigma_{x}\sigma^{-1}_{y})=\sigma_{u}\sigma^{-1}_{x}\sigma_{v}\sigma^{-1}_{y}=\sigma_{x}\sigma^{-1}_{u}\sigma_{y}\sigma^{-1}_{v}=(\sigma_{x}\sigma^{-1}_{y})(\sigma_{u}\sigma^{-1}_{v}). So, Γ \mathnormal{\Gamma} is Abelian. □ \square

###### Lemma 11

. The order of 𝔾 \mathbb{G} is either 256 256 or 16384 16384.

###### Proof.

Applying Lemmas 9 and 10, we find that 𝔾 \mathbb{G} admits a transitive automorphism group whose order is a power of 2 2. It follows from the orbit-stabilizer theorem that n 2 + 3 ​ n − 2 = 2 t n^{2}+3n-2=2^{t}, for some integer t t. We have ( 2 ​ n + 3) 2 = 2 t + 2 + 17 (2n+3)^{2}=2^{t+2}+17. Using a result in [2, p. 401], we obtain that ( n, t) ∈ { ( 1, 1), ( 2, 3), ( 3, 4), ( 10, 7) } (n,t)\in\{(1,1),(2,3),(3,4),(10,7)\}. Since n ⩾ 3 n\geqslant 3, we conclude that ( n, ν) ∈ { ( 3,256), ( 10, 16384) } (n,\nu)\in\{(3,256),(10,16384)\}. □ \square

Now, the proof of Theorem 1 is finally completed after proving Lemma 11. Notice that we employed the assumption ( 1) only in the proof of Lemma 2. As mentioned before, we believe that ( 1) automatically holds for any diamond-free 𝖲𝖱𝖦 ⁡ ( ( n 2 + 3 ​ n − 2) 2, n ⁡ ( n 2 + 3 ​ n − 1), 2, n ⁡ ( n + 1)) {\mathsf{SRG}}((n^{2}+3n-2)^{2},n(n^{2}+3n-1),2,n(n+1)).

## IV. Partial Quadrangle PQ (3, 35, 20)

In the following, we demonstrate that there exists no 𝖯𝖰 ⁡ ( 3, 35, 20) {\mathsf{PQ}}(3,35,20), or equivalently, there is no diamond-free 𝖲𝖱𝖦 ⁡ ( 676,108, 2, 20) {\mathsf{SRG}}(676,108,2,20). Notice that this strongly regular graph belongs to the family ( 2) with n = 4 n=4 and λ = 2 \lambda=2.

###### Theorem 12

. There exists no diamond-free 𝖲𝖱𝖦 ⁡ ( 676,108, 2, 20) {\mathsf{SRG}}(676,108,2,20).

###### Proof.

Suppose, toward a contradiction, that G G is a diamond-free 𝖲𝖱𝖦 ⁡ ( 676,108, 2, 20) {\mathsf{SRG}}(676,108,2,20). Consider two non-adjacent vertices u, v ∈ V ⁡ ( G) u,v\in V(G). Since G G is diamond-free, there are vertices w ∈ N ⁡ ( u) w\in N(u) and v ′, v ′′ ∈ N ¯ ​ ( u) v^{\prime},v^{\prime\prime}\in\overline{N}(u) such that { v, v ′, v ′′, w } \{v,v^{\prime},v^{\prime\prime},w\} is a clique. For i = 0, 1, 2, 3 i=0,1,2,3, assume that s i s_{i} is the number of cliques Ω \mathnormal{\Omega} in N ⁡ ( u) N(u) of size 3 3 such that ⟨ Ω, { v, v ′, v ′′ } ⟩ \langle\mathnormal{\Omega},\{v,v^{\prime},v^{\prime\prime}\}\rangle has i i edges. By a double counting argument, we find that

 | { s 0 + s 1 + s 2 + s 3 = 35; s 1 + 2 ​ s 2 + 3 ​ s 3 = 57; s 2 + 3 ​ s 3 = 21, \displaystyle\left\{\begin{array}[]{l}s_{0}+s_{1}+s_{2}+s_{3}=35;\\ s_{1}+2s_{2}+3s_{3}=57;\\ s_{2}+3s_{3}=21,\end{array}\right. |  |

which gives s 0 = − s 3 − 1 s_{0}=-s_{3}-1, a contradiction. □ \square

## Acknowledgements

The research of the first author was in part supported by a grant from IPM (No. 91050405).

## References

- [1] M. Behbahani and C. Lam, Strongly regular graphs with non-trivial automorphisms, Discrete Math. 311 (2011), 132 – 144.
- [2] F. Beukers, On the generalized Ramanujan-Nagell equation, I, Acta Arith. 38 (1980/81), 389 – 410.
- [3] A.V. Bondarenko and D.V. Radchenko, On a family of strongly regular graphs with λ = 1 \lambda=1, preprint.
- [4] R.C. Bose and T. Shimamoto, Classification and analysis of partially balanced incomplete block designs with two associate classes, J. Amer. Statist. Assoc. 47 (1952), 151 – 184.
- [5] P.J. Cameron, Partial quadrangles, Quart. J. Math. Oxford Ser. (2) 26 (1975), 61 – 73.
- [6] W.H. Haemers and E. Spence, The pseudo-geometric graphs for generalized quadrangles of order ( 3, t) (3,t), European J. Combin. 22 (2001), 839 – 845.
- [7] J.H. van Lint and A. Schrijver, Construction of strongly regular graphs, two-weight codes and partial geometries by finite fields, Combinatorica 1 (1981), 63 – 73.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1303.0472
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1303.0473
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1303.0473
[7]: https://arxiv.org/pdf/1303.0473
[8]: /html/1303.0474
