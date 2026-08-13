<!-- source: https://institucional.us.es/blogimus/en/2020/07/gilbreaths-conjecture/ | converted from HTML -->

Gilbreath’s conjecture – Blog del Instituto de Matemáticas de la Universidad de Sevilla

We consider the sequence of primes in a row. Below we write the differences between them:

$$\begin{array}{ccccc cccccccccc} 2&&3&&5&&7&&11&&13&&17&&19\\ &1&&2&&2&&4&&2&&4&&2\\&&1&&0&&2&&2&&2&&2\\&&&1&&2&&0&&0&&0\\&&&&1&&2&&0&&0\\&&&&&1&&2&&0\\&&&&&&1&&2\\&&&&&&&1\end{array}$$

We continue the process by forming a third row, but subtracting the smaller from the larger, so that they are all non-negative. We repeat this process indefinitely. Proth in 1878 observed that all rows obtained in this way start with a 1. Many sources report that Proth thought he had a proof, which was not correct. I will return to this later to avoid interrupting the discussion now.

The third row as far as we have written it down is formed by the \(1\) at the beginning and then all \(0\) and \(2\). This implies that the remaining rows of the whole triangle of numbers will be made up of zeros and twos except for the ones at the beginning. This observation is key, but we must note that in any row, if we continue it for long enough, we will find numbers other than \(0\) and \(2\).

## To what degree are we convinced of the conjecture?

The first reaction we may have is one of disbelief. We take the sequence of primes. We form the successive differences, changing their sign when they go negative and after all we get a row of ones! Why?

So we undertake the task of proving the conjecture. Simple mathematical ideas spontaneously reappear. In 1958 Norman L. Gilbreath, a mathematics student at the University of California, trying to find a method of generating primes, constructed the absolute value difference table and again noticed the property of the first row of ones. Two other colleagues, R. B. Kilgrove and K. E. Ralston, took advantage of the fact that one of the first computers, the SWAC, was located at UCLA and proved the conjecture for the row of the first 63419 primes. They already noticed that if in a row all numbers up to the \(n\)-th, except the first one which is a 1, are equal to \(0\) or \(2\) then the next \(n-1\) rows start with a \(1\). This greatly reduces the number of operations needed to confirm the conjecture. Their feat is all the more remarkable if we look at what computers were like in the 1950s.

[image: The SWAC computer] [1] The SWAC computer where Kilgrove and Ralston tested the conjecture.

### Odlyzko’s results

Computers were considerably more powerful in 1993. Odlyzko succeeded in proving that the conjecture is true for all primes \(<10^{13}\), approximately \(3.4\times10^{11}\) primes.

Let us consider the row of the first \(n\) primes and form rows until we reach a row \(k\) which except for the first element \(=1\) consists of \(0\) and \(2\). We will say that \(G(n)=k\). For example the table we formed before proves that \(G(8)=2\). This function grows very slowly, Odlyzko notes that \(G(\pi(10^{13}))=635\). That is, only 635 rows of differences need to be calculated to show that all primes \(p\le 10^{13}\) satisfy Gilbreath’s conjecture.

So, although we must be very cautious with primes, yes, the calculations lead us to believe that Gilbreath’s conjecture is true.

## What do prime numbers have to do with this?

Gilbreath is also known as a magician. There is a method of card shuffling named after him. Another magician, Martin Gardner, ran a section on mathematical games in Scientific American magazine. In 1980 one of Gardner’s articles was devoted to Gilbreath’s conjecture. He surprised there by presenting the ideas of Hallard Croft. This mathematician maintained that the property does not have much to do with the primes. Given an arbitrary sequence \((a_n)\) of integers we can construct a new transformed sequence \((b_n)\) by the process of successive differences in absolute value. For example $$\begin{array}{ccccc ccccc ccccc} 5&&8&&9&&11&&27&&33&&71&&75\\ &3&&1&&2&&16&&6&&38&&4\\ &&2&&1&&14&&10&&32&&34\\ &&&1&&13&&4&&22&&2\\ &&&&12&&9&&18&&20\\ &&&&&3&&9&&2\\ &&&&&&6&&7\\ &&&&&&&1 \end{array}$$ the transformed succession \((b_n)\) is in this case \(5\), \(3\), \(2\), \(1\), \(12\), \(3\), \(6\), \(1\), …which obviously does not satisfy the conjecture, as the original is pretty arbitrary.

Croft claimed that any sequence starting with \(2\) and continuing with odd numbers in increasing order and such that the first differences are not very large will satisfy the same property as the primes: the transformed sequence will verify that \(b_n=1\) for \(n>1\). That is, what Proth and Gilbreath observed is practically not a property of the primes.

Strictly speaking Croft’s statement is false. In fact Odlyzko is more cautious and only states that a sequence starting with \(2\) followed by an increasing sequence of odd numbers generated with small random increments will have a transformed sequence \((b_n)\) such that \(b_n=1\) for \(n\ge n_0\), being \(n_0\) dependent on the chosen sequence. That is, the conjecture will hold from a certain term onwards.

## Ways to approach the conjecture

Erdös once said that Gilbreath’s conjecture was true but that it would take at least 200 years to prove. A surprising statement since there are many paths to explore. For example given a finite sequence $$p_1, p_2,\dots, p_n, q$$ where the \(p_j\) are the first primes, what values of \(q\) satisfy the conjecture? My experiments show me that any odd \(q\) in a certain interval satisfies the conjecture. For example, taking all primes up to \(p_{4000}=37813\) any odd number \(q\) such that \(33667\le q\le 41959\) would satisfy the conjecture. One knows that the next prime is \(\le p_n+p_n^{0.525}<38067\).

This indicates one possible way to attack the conjecture.

Another possibility is to attack a more affordable variant. A very attractive proposal is that of David Eppstein: [the Gilbreath conjecture for practical numbers][2].

I have sometimes proposed to my students in Number Theory the task of estimating the probability that a sequence such as the primes verifies the conjecture.

What do we know about the primes? A lot, but in principle we know that a large number \(x\) has probability \(1/\log x\) of being prime. This statement needs an explanation. If the number is even and large its probability of being prime is zero. What the previous statement means is that if we take all the numbers up to \(x\) there are \(\pi(x)\) primes less than or equal to \(x\). Then if we understand the probability as the quotient between favourable cases divided by the total of cases, the probability is

$$\frac{\pi(x)}{x}\approx\frac{1}{\log x}.$$ We can also say that if the number is even its probability of being prime is \(0\) and if it is odd it is \(\approx 2/\log x\).

Thus we can imagine a probabilistic model for the primes.

We construct a sequence \((a_n)\) of pseudo primes. We will set \(a_1=2\), \(a_2=3\) and for each \(n\ge3\), we will set \(a_n=a_{n-1}+2u_n\) where \(u_n\) is chosen from the set \(\{1,2,3,\dots \lfloor \log n\rfloor\}\) randomly with equal probability. Stopping at \(\lfloor\log n\rfloor\) we obtain that the average value of \(a_n\) is \(n\log n\), as well as the approximate value of the \(n\)-th prime is \(n\log n\).

What I asked my students to do was to estimate the probability that these pseudo primes verify Gilbreath’s conjecture. By the simple method of generating many sufficiently long sequences of pseudo primes and seeing how many satisfy the conjecture. With \(10000\) tests we found the probability \(0.499\) of fulfilling Gilbreath with this model. Odlyzko expected rather that there exists a \(M\) such that the transformed sequence satisfies that \(b_n=1\) for \(n_n=1\) for \(n\ge M\). Testing with our model we found that the probability that \(b_n=1\) for \(n>10\) goes up to \(0.9916\). Finally, among the \(10000\) tests we found none that did not satisfy the conjecture for \(n>40\).

## The work of Zachary Chase

Until last May all that was known about Gilbreath’s conjecture were numerical checks and conjectures about probabilities based on intuition. May saw the publication of Chase’s paper *A Random analogue of Gilbreath’s conjecture*. Zachary Chase is a postgraduate at Oxford University, directed by Prof. Ben Green, who with Terry Tao proved the existence of arithmetic progressions of primes of arbitrary length.

[3] Zachary Chase

Chase uses pseudo primes as we did above, \(a_{n+1}=a_n+2u_n\), choosing \(u_n\) randomly from a set \(\{1,2,\dots, f(n)\}\), and proves that with probability \(1\) there exists one \(M\) such that the transformed sequence verifies \(b_n=1\) for \(n>M\).

In other words, Chase has almost proved what Odlyzko said. The only difference is that Chase needs to assume that \(f(n)\le \frac{1}{100}\frac{\log\log n}{\log\log\log n}\). The prime number model took \(f(n)=\lfloor\log n\rfloor\). We should be able to improve Chase’s theorem to admit larger \(f(n)\) functions.

How does Chase’s proof work? Numerical experiments show that the conjecture is true because the rightmost terms apart from the \(1\) at the beginning are always \(0\) or \(2\). What Chase proves is that this occurs with probability \(1\) from one term onwards.

He first observes that if \(a_{n+1}=a_n+2u_n\) then the first differences are \(1\), \(2u_2\), \(2u_3\), … We can forget about the first \(1\) and divide everything by \(2\). We must prove that after a certain number of iterations from the sequence \((u_n)\) chosen randomly and independently, we will arrive at a sequence of \(0\) and \(1\).

The basic result is proving that if we take \(M\) and \(C\) such that \(3\le C\le \frac{1}{100}\frac{\log\log M}{\log\log\log M}\) and we randomly take \(u_1\), \(u_2\), …, \(u_M\) independently from among \(\{0, \dots, C-1\}\), then, with a very large probability (at least \(1-e^{-e^{\sqrt[20]{\log M}}}\)), in a not very far apart row (the row \(e^{\sqrt[5]{\log M}}\)) from the process, all is reduced to \(0\) and \(1\).

The proof is an outstanding example of how pure mathematics works. We are sharpening our weapons to face the unknown. This is a tricky problem of probability that would throw even the most experienced mathematician for a loop. The interest goes beyond proving Gilbreath’s conjecture. It is a difficult problem and therefore worthy of attack. We are improving our ability to calculate probabilities. It is not surprising then that when a physicist or engineer is confronted with a problem, the mathematician has solved it sometimes hundreds of years ahead. Mathematics is always on the lookout to attack problems that are complicated.

I will highlight a lemma from Chase’s proof that I think is a gem. How it turns the problem into something finite and combinatorial.

**Lemma.**Suppose that \(a_1\), \(a_2\),…. \(a_n\) are chosen randomly and independently from among \(\{0,1,\dots, C-1\}\) being \(n\ge (200C^2)^{2C}\) and we perform the process of successive differences in absolute value until only one number remains. The probability that this number is a \(0\) is at least \(\frac{1}{200C^2}\).

## *Nouvelle Correspondance Mathématique*

We turn now again to Proth, the first to note the property. *Nouvelle correspondence Mathématique*was a Belgian journal published from 1874 to 1880. It was founded by [Eugene Catalan][4] y [Paul Mansion][5]. Its aim was the dissemination of mathematics; it published problems and solutions at the level of the French aggregation (i.e. the examination for secondary school teachers). The aim was also to disseminate knowledge, but not to publish original results.

The type of magazine reminds me of a tradition that goes back a long way. Diophantus’ *Arithmetic*is a collection of problems, all with a certain style, and their solutions. Reading Diophantus, one imagines a group of mathematics lovers posing problems and challenging each other to solve them. It is in a similar environment, the one created by the journal Nouvelle Correspondance, that the idea of Proth arose. As a problem beyond the capabilities of the group. Proth was nothing more than a farmer with an interest in mathematics. Self-taught and certainly not very sophisticated. He is remembered for a primality criterion for numbers of the form \(N=2^n h+1\), primes which are called Proth primes. We also owe him Gilbreath’s conjecture and the beautiful theorem that if we put \begin{align*} x&=a^2+b^2+ab\\ y&=c^2+d^2+cd\\ z&= (a+c)^2+(b+d)^2+(a+c)(b+d)\\ t&=a^2+c^2+ac\\ u&=b^2+d^2+bd\\ v&=(a+b)^2+(c+d)^2+(a+b)(c+d) \end{align*} then \begin{align*} x+y+z&=t+u+v\\ x^2+y^2+z^2&=t^2+u^2+v^2\\ xy+xz+yz&=tu+uv+vt \end{align*} By the way, the problem of finding numbers \(x\), \(y\), \(z\), \(t\), \(u\), \(v\) that verify the above three equations has all the style of Diophantus’ problems. All this is no small souvenir for a farmer.

Nevertheless, the conjecture is remembered as the Gilbreath conjecture and there is no one who presents it who does not say that Proth thought he had a proof that was not correct. In writing the entry, because of Chase’s result, I was interested to see what Proth’s failed proof was. I was in for a surprise. Those who talk about the failed proof cite one of the following two papers:

**F. Proth**, *Théorèmes sur les nombres premiers*, Comp. Rend. Acad. Sci. Paris, **85**(1877), 329-331.

**F. Proth**, *Sur la série des nombres premiers*, Nouvelle Correspondance Mathématique, **4 **(1878) 236-240.

Pero si uno busca el tomo y la página de la primera referencia encuentra otro artículo

**F. Pepin**, *Sur la formule \(2^{2^n}+1\)*, Comp. Rend. Acad. Sci. Paris, **85**(1877), 329-331.

which has nothing to do with what we are discussing here. The second reference is indeed devoted to the conjecture. It is true that Proth presents it as a theorem, but he does not present any proof. Instead Proth devotes himself to drawing some consequences from his “theorem”. At the end of the article we find a note signed by E. C. (no doubt the editor of the journal Eugene Catalan) saying “is it not true that the theorems of Mr. Proth which we have just read are, rather, postulates?”.

Rummaging through the volumes of Comptes Rendus we find a note:

**F. Proth**, *Théorèmes sur les nombres premiers*, Comp. Rend. Acad. Sci. Paris, **87**(1878), 926.

but it deals with primality criteria. Finally, in volume **84**(1877) 259 it says: [E. Proth submits some new theorems on numbers to the judgement of the Academy.][6] On page 92 we can read: [E. Lucas addresses some critical remarks on the subject of the theorems on numbers which were communicated by F. Proth at the session of 27 December 1876][7].

Lucas probably noticed that, although not a theorem, Proth did have an interesting observation. That is why he allowed publication in the minor journal although he did not allow the academy to publish Proth’s article.

It is a little unfair not to talk about Proth’s intuition, which without computers has more merit than we suppose, and to insist that his proof was wrong. As far as I know, no one has seen any wrong proof. And besides, no one has any proof to offer.

## Learn more

The Gilbreath conjecture is a popular topic in mathematics. For example, we find it featured in the [pages on primes by Chris K. Caldwell][8], or in [Wikipedia][9].

Experimental papers have a lot of information and are accessible on the internet.

**R. B. Killgrove and K. E. Ralston**, [On a conjecture concerning the primes][10], Math. Comp. **13**(1959), 121-122.

**A. M. Odlyzko**, [Iterated absolute values of differences of consecutive primes][11], Math. Comp. **61**(1993), 373–380.

And Zachary Chase’s paper is available on arXiv:

**Zachary Chase**, [A Random Analogue of Gilbreath’s Conjecture][12], arXiv:2005.00530, mayo (2020).

The volumes of the journal **[Nouvelles Correspondances Mathematiques][13] can be found on the internet. Proth’s article concerning our question appeared in volume 4.

The best source I have found for the journal is at the University of Göttingen and allows downloading pdfs of the *[Nouvelles Correspondances Mathématiques][13] volumes*. Some separate volumes can also be found in other sources: [Tomo 1, 1874-1875][14], [Tomo 4 1878][15], [Tome 5, 1879][16].

**

- [number theory][17]
- [prime][18]
- [probability][19]

#### Be the first to comment

### Leave a Reply [Cancel reply][20]

Copyright &copy; 2026 | WordPress Theme by [MH Themes][21]

#### Uso de cookies

Este sitio web utiliza cookies para que usted tenga la mejor experiencia de usuario. Si continúa navegando está dando su consentimiento para la aceptación de las mencionadas cookies y la aceptación de nuestra [política de cookies][22], pinche el enlace para mayor información. ACEPTAR

Aviso de cookies


## Links

[1]: https://institucional.us.es/blogimus/wp-content/uploads/2020/07/SWAC_Dec50.jpg
[2]: https://11011110.github.io/blog/2011/02/19/gilbreath-made-practical.html
[3]: https://institucional.us.es/blogimus/wp-content/uploads/2020/07/ZacharyChase.png
[4]: https://en.wikipedia.org/wiki/Eugène_Charles_Catalan
[5]: https://en.wikipedia.org/wiki/Paul_Mansion
[6]: https://gallica.bnf.fr/ark:/12148/bpt6k30410/f258.item.r=proth
[7]: https://gallica.bnf.fr/ark:/12148/bpt6k30410/f91.item.r=proth
[8]: https://primes.utm.edu/glossary/page.php?sort=GilbreathsConjecture
[9]: https://en.wikipedia.org/wiki/Gilbreath%27s_conjecture
[10]: https://www.ams.org/journals/mcom/1959-13-066/S0025-5718-59-99262-2/
[11]: https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1182247-7/
[12]: https://arxiv.org/abs/2005.00530
[13]: https://gdz.sub.uni-goettingen.de/id/PPN598948236
[14]: https://archive.org/details/nouvellecorresp01mansgoog/page/n7/mode/2up
[15]: https://play.google.com/books/reader?id=10A0AQAAMAAJ&amp;hl=en_GB&amp;pg=GBS.PP2
[16]: https://archive.org/details/nouvellecorresp00mansgoog/page/n6/mode/2up
[17]: https://institucional.us.es/blogimus/en/tag/number-theory/
[18]: https://institucional.us.es/blogimus/en/tag/prime/
[19]: https://institucional.us.es/blogimus/en/tag/probability/
[20]: /blogimus/en/2020/07/gilbreaths-conjecture/#respond
[21]: https://www.mhthemes.com/
[22]: https://institucional.us.es/blogimus/politica-de-cookies/
