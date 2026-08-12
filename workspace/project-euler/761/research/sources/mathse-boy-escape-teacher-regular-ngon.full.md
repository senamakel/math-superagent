<!-- source: https://web.archive.org/web/2023/https://math.stackexchange.com/questions/1762665/can-the-boy-escape-the-teacher-for-a-regular-n-gon | converted from HTML -->

geometry - Can the boy escape the teacher for a regular $n$-gon? - Mathematics Stack Exchange

Mathematics Stack Exchange is a question and answer site for people studying math at any level and professionals in related fields. It only takes a minute to sign up.

[Sign up to join this community][1]

Anybody can ask a question

Anybody can answer

The best answers are voted up and rise to the top

**Teams**

Q&A for work

Connect and share knowledge within a single location that is structured and easy to search.

[Learn more][2]

# [Can the boy escape the teacher for a regular $n$-gon?][3]

[Ask Question][4]

Asked 5 years ago

Active [3 years, 6 months ago][5]

Viewed 586 times

14

10

[6]

$\begingroup$

This is related to [Prove that the boy cannot escape the teacher][7]

Suppose there is a boy in the center of a regular $n$-gon. The teacher is on the edge of the $n$-gon (but cannot leave the edge) and wants to capture the boy. At the beginning he is on a vertex. The teacher is $v(n)$ times faster than the boy. Which is the maximum $v(n)$ such that the boy can escape? (By escaping means he reaches the edge of the $n$-gon and the teacher is not there)

From the linked question we know $3 \le v(4) < 6$, and for $n= \infty$ (a circle) then I know a strategy such that $v(\infty) = \pi + 1$ suffice; I don't know if this is optimal. I also put convergence in the tags because my wild hypothesis is that the maximum $v(n)$ will converge to some value and it would be interesting to know which one!

Any cool way to solve this?

[geometry][8] [convergence-divergence][9] [analytic-geometry][10] [curves][11]

[Share][12]

Cite

Follow

[edited Apr 13 '17 at 12:21][13]

[14]

[Community][14] ♦

1

asked Apr 28 '16 at 13:16

[15]

[Ant][15] Ant

20.2k 4 4 gold badges 38 38 silver badges 94 94 bronze badges

$\endgroup$

4

-

1

$\begingroup$ The [optimal strategy for the circular case][16] works for any $v(\infty)$ up to a value slightly greater than $4.6$. $\endgroup$ – [David K][17] Jun 24 '16 at 13:23

-

$\begingroup$ @ARi interesting! Can you provide a proof of your claim? :-) $\endgroup$ – [Ant][15] Jan 28 '17 at 22:33

-

$\begingroup$ @ARi that is also interesting, but I would also be interested in the proof to your solution for the regular $n$-gon case :) $\endgroup$ – [Ant][15] Jan 29 '17 at 9:37

-

$\begingroup$ What you want to look up is 'Dog curve' or 'Escape curves' $\endgroup$ – [ARi][18] Apr 24 '17 at 20:59

Add a comment |

## 4 Answers 4

[Active][19] [Oldest][20] [Votes][21]

5

[22]

$\begingroup$

This is an interesting question! I thought I would get the ball rolling by looking first at the case for the square pool (4-gon).

A diagram:

[image: Basic diagram] [23]

The teacher is located at point $A$, the boy is in the center of the pool at point $E$. The square has the size $2x2$, the speed of the boy is arbitrarily set at $1$ and the speed of the teacher is $K > 1$.

It is easy to check that if the boy swims directly to the corner furthest from the teacher (point $C$), $K=2 \sqrt2 \approx 2.83$ is sufficient for the teacher to catch the boy. A slightly better strategy for the boy is to swim perpendicular to the nearest pool side (furthest from $A$) which requires $K=3$.

A much better strategy (although not quite the optimal, as I will show later) is the one illustrated in green in the diagram. The boy starts off by heading for the point furthest from the teacher (point $C$). The teacher must now also head for $C$ and can either go left towards $D$ or down towards $B$. Both paths are equally long. Let's assume he goes down (red line in diagram). The boy continues heading for $C$ *until*the teacher reaches point $G$. At this time, the boy and the teacher are equidistant from the horizontal centerline of the pool. More importantly, the teacher is now at the maximum distance from the point $H$ (mirror point of $G$). The boy now heads for $H$. It doesn't matter at this time whether the teacher turns around or continues in the direction he was going. The point $H$ is equally far away.

Let us set up the equations for this scenario. Let $d_1$ be the distance to the horizontal centerline at the moment the boy heads for $H$. Let $t_1$ be the time since start. Then, for the teacher $$t_1 = \frac{1-d_1}{K}$$

and for the boy $$t_1= \frac{d_1}{\frac{1}{\sqrt2}}= \sqrt2d_1$$

Let the time for the boy to swim from $F$ to $H$ be $t_2$. Then $$t_2 = 1-d_1$$

For the teacher, the time to reach $H$ from $G$ would be $$t_2 = \frac{4}{K}$$

Solving these equations for $d_1$ and $K$, we find that $$K=2+\sqrt{2+2\sqrt2}\approx4.61$$

A substantial improvement of $K=3$. However, as I mentioned earlier, a further improvement exists.

Suppose the boy doesn't wait for the teacher to reach $G$ before changing direction, but changes his direction as soon as he sees whether the teacher moves left towards $D$ or down towards $B$. Suppose he changes his direction (continuously) such that he is always heading towards the point on the square furthest from the teacher. The boy thus starts heading for the point $C$ but then heads more and more towards the pool side $CD$. What can the teacher do? He can turn around and head for the pool side $CD$ as well, but if he does, the boy will again change direction and head for the pool side $CB$, always aiming for the point on the square furthest from the teacher. The teacher gains nothing and is best served continuing his progress towards $B$.

It was not intuitively clear to me what form the boy's curve would take in this scenario, so I simulated it. A close-up of the new path of the boy is shown below:

[image: New path] [24]

The green curve is the same as the green curve in the first diagram, while the purple curve is the new scenario.

The result of the simulation is that in this scenario, $K\approx4.782$.

The above is not a proof that no better scenario is possible and I invite suggestions on how such a proof could be made. And if anyone can work out what the analytical form of the curve is (it doesn't seem to be a circle or a parabola) that would also be much appreciated.

The above scenario, by the way, would be directly applicable to all regular polygons with an even number of sides.

**EDIT**

An old question revived!

After reading the link provided by @David K in the comments, I think I can improve on my answer above.

Suppose we make an inner square in the pool with side length $\frac{2}{K}-\epsilon$, where $\epsilon$ approaches $0$. The boy's angular speed along the perimeter of this inner square will slightly outpace the teacher's angular speed along the perimeter of the outer square. Suppose further that the boy swims to the midpoint of a side on this inner square. The teacher will then run to the matching midpoint on the outer square and thus be as close to the boy as possible. If the boy now starts swimming along the perimeter of the inner square, he will slightly outpace the teacher as the teacher attempts to match the boy's position on the outer square. In fact, the boy can make shortcuts within the inner square which are not available to the teacher on the outer square. It therefore seems clear that the boy can eventually position himself wherever he wants on the perimeter of the inner square, in relation to where the teacher is. Let us now consider two scenarios for the teacher's position:

1. The teacher is at the midpoint of side

The boy then positions himself at the midpoint of the inner square's side which is furthest from the teacher. The boy then swims straight for the nearest poolside. The time it takes him to reach this is: $$t_3 = 1-\frac{1}{K}$$

The time it takes for the teacher to reach the boy is: $$t_3= \frac{4}{K}$$

Setting these two equal gives: $$K=5$$

An improvement of my previous answer!

1. The teacher is at a corner

The boy then positions himself at the opposite corner on the inner square. He then uses the basic strategy I gave in my old answer, i.e. he swims straight for the corner until the teacher reaches a position which is equidistant from the boy's nearest poolside, and then the boy swims straight for this poolside. Looking at the equations from my old answer, only one needs to be changed, namely the one for $t_1$: $$t_1=\frac{d_1-\frac{1}{K}}{\frac{1}{\sqrt{2}}}$$

which results in $$K^2-5K-\frac{4}{\sqrt{2}}=0$$

which gives a value of $K\gt 5$. The teacher will therefore not position himself at a corner.

Summing up, the optimal answer for a square pool appears to be $$K = 5$$

[Share][25]

Cite

Follow

[edited Jan 29 '17 at 3:02][26]

answered Jun 24 '16 at 1:38

[27]

[Jens][27] Jens

5,239 2 2 gold badges 14 14 silver badges 35 35 bronze badges

$\endgroup$

6

-

$\begingroup$ Indeed, some of the answers provided at the google discussions webpage are fascinating! To extend it to the square (or $n$-gon) though I don't see why you would make the inner, smaller region a square (or $n$-gon) as well - why not let the boy run around in a circle in the interior, before sprinting towards the edge? If the inner circle has radius $4/(\pi K) - \varepsilon$ then he can always position himself opposite the teacher, which for the case (1.) above translates to $K = 4 + 4/\pi > 5$. I'm not sure about case (2.) then as he would be further from either edge. $\endgroup$ – [TMM][28] Jan 31 '17 at 15:53

-

$\begingroup$ (continued) I believe the optimal strategy for the square should ultimately be such that no matter whether the teacher is at a corner, or on the center of an edge, or anywhere else on the edge, the same optimal value $K$ should come out. So probably the "optimal" strategy involves creating an inner region which is neither a circle nor a square, but such that on any point on the boundary of this region, the same value $K$ comes out. Finding this optimal shape may be incredibly hard though... $\endgroup$ – [TMM][28] Jan 31 '17 at 15:56

-

$\begingroup$ Thanks for the effort! This is indeed a very interesting approach. I have to say that I was hoping for a more general and less "case-checking" approach but I guess that takes too much effort, if at all possible :) Thank you anyhow! $\endgroup$ – [Ant][15] Feb 1 '17 at 21:09

-

$\begingroup$ I think I have a strategy for the boy that yields $v(4)>5.78,$ which I've written up as an answer. There are a number of non-obvious things about the strategy for the circular pool that carry over to the square pool (for example, the teacher must run much further than half of the pool's perimeter to cut off all avenues of earlier escape) but also some non-obvious differences. I have not worked out other polygons yet. $\endgroup$ – [David K][17] Aug 23 '17 at 1:54

-

$\begingroup$ Hi! Since you spent some time with the problem, you may be interested in the answer by @stewbasic that solves the problem (I did not double check the results though) :) $\endgroup$ – [Ant][15] Oct 25 '17 at 22:35

| Show **1**more comment

3

[29]

$\begingroup$

See all the [details here][30]; they are too long for a MSE answer. In summary, suppose the pool occupies a regular $n$-gon $P$. Let $\theta=\pi/n$, and let $K$ be the largest integer between $0$ and $n$ such that $$ \sin(K\theta)-(K+n)\tan\theta\cos(K\theta) $$ is negative. Equivalently, $K$ is the floor of the unique root of $\tan(x\theta)-(x+n)\tan\theta$ in $[1,n/2)$. Then $$ \cos((K+2)\theta)\leq\frac{2\sin(K\theta)}{(K+n)\tan\theta}-\cos(K\theta)<\cos(K\theta) $$ so we can define $$ \alpha=\frac12\left(K\theta+\cos^{-1}\left( \frac{2\sin(K\theta)}{(K+n)\tan\theta}-\cos(K\theta)\right)\right), $$ Then the cutoff speed is $\lambda=1/\cos\alpha$. Explicitly, for speeds $<\lambda$ the student wins regardless of starting positions. For speeds $>\lambda$ the teacher wins provided the student starts in a regular $n$-gon $Q$, where $Q$ is obtained from $P$ by rotating by $K\theta$ and scaling by $$ s=\frac{\cos\alpha}{\cos(\alpha-K\theta)} $$ about the center of $P$.

As for a circular pool, the student must consider two cases in which the teacher chases clockwise or anti-clockwise, and find the optimal path in each. In fact from each vertex of $Q$ there are two equally optimal paths in each direction, as shown below (follow the link for other values of $n$).

[image: Regular hexagon] [31]

For a square we have $K=1$, $\alpha\approx1.397$ and $\lambda\approx5.789$.

For large $n$, $\theta$ is small and $n\tan\theta\approx\pi$. Thus $\alpha\approx K\theta\approx\mu$, where $\mu$ satisfies $$ \tan\mu=\mu+\pi. $$ This agrees with the cutoff for a circular pool.

[Share][32]

Cite

Follow

answered Oct 24 '17 at 21:22

[33]

[stewbasic][33] stewbasic

5,911 1 1 gold badge 11 11 silver badges 28 28 bronze badges

$\endgroup$

1

-

$\begingroup$ Fantastic work! Thank you for the time you took :) You could even make it a paper and publish it on arXiv or some journals :D I will need to study the proof now... :D $\endgroup$ – [Ant][15] Oct 25 '17 at 8:02

Add a comment |

2

+100

[34]

$\begingroup$

I'll start with the case $n = 4$ below, and further down I'll touch on the generalization to arbitrary $n$.

---

# The case $n = 4$ (square)

This is building upon the answer by Jens for the square, and upon the strategies provided in the linked [Google discussions topic][16]. It does not provide a full answer yet but aims to give sharper bounds on $v(n)$.

Terminology: as depicted below, we consider a regular $4$-gon or square (for now) with side length $2$. The teacher moves along the edge at speed $v$, the boy moves in the interior at speed $1$. As already described by others, there is a small region in the middle where the boy can move in such a way that he can always make sure that the teacher is at the far opposite end, i.e. such that the center is on the line between the boy and the teacher. For this inner region we can take various shapes.

## Attempt 1: Inner circle

Let us first consider the case where the inner region is a circle of some radius $r$ as depicted below. For the case the pool is circular, this choice was optimal as described [somewhere in this topic][16].

[image: enter image description here] [35]

Now, to see what the radius $r$ is, we basically need to make sure that moving along the perimeter takes as much time for the boy as moving along the edge of the pool for the teacher. The circumference of the circle is $2 \pi r$, the pool has a perimeter of $8$, and equating these, taking into account the velocities, gives $2 \pi r = 8 / v$ or \begin{align} r = \frac{4}{\pi v} \end{align}

Next, although the boy can keep the center between him and the teacher at all times, he cannot force the teacher to make a choice as to whether the teacher waits at a corner for the boy to exit this region, or sits at the middle of the edge, or anywhere else along the edge. We will analyze two specific cases similar to Jens (middle of edge and corner), but note that one would have to consider the teacher being on any point of the perimeter of the square to show that he can never catch the boy. On the other hand, the corner and center of an edge intuitively feel like "extreme" cases and one of them is likely the best strategy for the teacher.

**Case 1: Center of an edge**

The easy case, and the case where we mostly improve upon Jens' analysis with an inner square instead of an inner circle. In this case the teacher patiently waits at the center of one of the edges until the boy exits the inner circle, after which the teacher goes after him. A straightforward strategy now is to just make a run straight for the edge, and see if it works. At the boy is already at distance $r = 4 / (\pi v)$ from the center, he still has to traverse $1 - r = 1 - 4 / (\pi v)$. The teacher has to go half the perimeter to make it to the other side, in time $4 / v$. So the boy gets away if \begin{align} 1 - \frac{4}{\pi v} < \frac{4}{v}. \end{align} Solving for $v$ leads to $v < 4 + \frac{4}{\pi} \approx \color{blue}{\mathbf{5.27}}$, so in this case the boy "survives" if the teacher is no more than $5.27$ times faster than the boy.

**Case 2: The corner**

The hardest case to analyze. We follow the boy strategy outlined by Jens: run towards the opposite corner, and as soon as we hit a point where the closest point on the boundary would be the mirrored opposite of where the teacher is at that point, we make a run for it straight towards the boundary.

[image: enter image description here] [36]

As in this figure, the boy starts at the point $(-r/\sqrt{2}, -r/\sqrt{2})$ and the teacher starts at point $(1, 1)$ if we take the center of the pool as $(0,0)$. The boy swims straight towards $(-1, -1)$, until at a certain point $A = (-R/\sqrt{2}, -R/\sqrt{2})$ at some distance $R$ from the center, when the teacher is at the point $B = (1, R/\sqrt{2})$. This occurs at time $t_1$, satisfying the following equalities in terms of the distance/velocity traversed by the boy and teacher: \begin{align} t_1 &= (R - r) \cdot 1, \\ t_1 &= \left(1 - \frac{R}{\sqrt{2}}\right) \cdot \frac{1}{v}. \end{align} Then, from this point on, the boy has a distance $1 - R/\sqrt{2}$ to traverse towards the edge, while the teacher (who is at the far opposite end) has a distance $4$ to traverse. So after $t_2$ more units of time, the boy escapes if: \begin{align} t_2 &= \left(1 - \frac{R}{\sqrt{2}}\right) \cdot 1, \\ t_2 &< 4 \cdot \frac{1}{v}. \end{align} From the second set of equations we can solve for $R$ to obtain $ R > \sqrt{2} (1 - \frac{4}{v})$. (If $v < 4$ then clearly the condition is always satisfied, so only $v \geq 4$ is interesting.) Solving the first set of equations for $v$, plugging in the bound on $R$ and $r = 4 / (\pi v)$, we obtain: \begin{align} \sqrt{2} \left(1 - \frac{4}{v}\right) - \frac{4}{\pi v} < \frac{4}{v^2}. \end{align} Solving for $v$ leads to $v < \frac{\sqrt{2} + 2\pi + \sqrt{2 + 4 \sqrt{2} \pi + 2 (2 + \sqrt{2}) \pi^2}}{\pi} \approx \color{blue}{\mathbf{5.42}}$, so the boy gets away if the speed of the teacher is no more than $5.42$ times the speed of the boy.

**Preliminary conclusion**

Based on these two cases, one might hope that for the square, the velocity needed for the teacher to catch the boy using any possible strategy is at least \begin{align} \Large\boxed{v(4) \stackrel{?}{\geq} 4 + \frac{4}{\pi} \approx 5.27}, \end{align} where the best strategy for the teacher based on our particular strategy for the boy would be to wait at the center of an edge. To prove this, however, one would also have to consider cases where the teacher waits at some other particular point along one of the edges until the boy leaves the inner circle. As argued before, the two considered cases may be the "best" strategies for the teacher, so one might hope that in those other cases the teacher needs a velocity $v \geq 5.27$ as well to catch the boy.

## Attempt 2: Inner diamond

From the above analysis, we note that the boy is more resistant against a teacher starting in a corner than a teacher starting at the middle of an edge. This suggests that the optimal "inner shape" should actually be more "pointy" down in the middle, so that the boy gets a further head-start when going straight for the edge, at the cost of starting a bit further from the corner when the teacher is in the opposite corner. So as an alternative, consider an inner shape in the form of a diamond, like below.

[image: enter image description here] [37]

Now as before, the perimeter of the inner region should be a factor $v$ smaller than the perimeter of the outer region, hence the edge length $2/v$. We now again consider the same two special cases, hoping that other cases in between are worse for the teacher. The figure again depicts the boy's strategies for both these cases, similar to the circular case.

**Case 1: Center of an edge**

In this case, the boy starts at distance $\sqrt{2}/v$ from the center, and distance $1 - \sqrt{2}/v$ from the edge. When he makes a run for it, he succeeds if $1 - \sqrt{2}/v$ is less than $4/v$, the time it takes the teacher to run around the pool. This leads to the condition on $v$ of $v < 4 + \sqrt{2} \approx \color{blue}{\mathbf{5.41}}$.

**Case 2: The corner**

We can reuse the previous analysis for the circular inner region, where the boy now starts at a radius $r = 1/v$ from the center, rather than $r = 4/(\pi v)$. Note that the boy is now closer to the center, and so we expect the teacher to have a better chance of catching the boy.

Redoing the same analysis, we get the following condition on the value $v$ for which the teacher is just in time: \begin{align} \sqrt{2} \left(1 - \frac{4}{v}\right) - \frac{1}{v} < \frac{4}{v^2}. \end{align} This has a solution at $v = \tfrac{1}{4} (8 + \sqrt{2} + \sqrt{66 + 48 \sqrt{2}}) \approx \color{blue}{\mathbf{5.25}}$. So indeed, the teacher needs a slightly lower speed to catch the boy.

Based on this analysis, the teacher would wait in a corner, and only need a velocity of $v \approx 5.25$ to catch the boy. This is slightly worse than the circular inner region, which required the teacher to have speed $v \approx 5.27$.

## Attempt 3: Inner octagon

The above two cases still seem suboptimal: ideally we would like to balance the two cases to get the best overall complexity. (Note however that again, there is no proof that the best strategy for the teacher is one of these two - the best strategy for the teacher might be to sit at 3/4 of an edge for instance. This is just to simplify the analysis.) To at least balance the two complexities, consider the case where the inner shape is an octagon.

[image: enter image description here] [38]

We denote the bottom point of the octagon by $(0, -y)$ for $y$ to be determined later, and the left bottom corner by $(-r/\sqrt{2}, -r/\sqrt{2})$ again for $r$ to be determined later. Now, based on the perimeter condition, the edge case and the corner case, we obtain three equations (technically inequalities) on the parameters $y, r, v$: \begin{align} 8 \cdot \sqrt{\frac{r^2}{2} + \left(\frac{r}{\sqrt{2}} - y\right)^2} &= \frac{8}{v}, \\ 1 - y &= \frac{4}{v}, \\ \sqrt{2} \left(1 - \frac{4}{v}\right) - r &= \frac{4}{v^2}. \end{align} This is pretty messy, but can be solved for the three variables, leading to: \begin{align} y &\approx 0.256023,\\ r &\approx 0.223696,\\ v &\approx 5.376512. \end{align} In other words, if we simply balance these two cases, the boy can escape teachers sporting a velocity of $v \approx \color{blue}{\mathbf{5.38}}$.

**Conclusion**

Below is an overview of the velocities required for the teacher to catch the boy, for different inner shapes, and for different starting positions.

- Inner shape: **Square**(see [Jens' answer][39])

  - Edge center: $5.00$
  - Corner: $5.51$
  - Minimum $v$: (at most) $\color{blue}{\mathbf{5.00}}$

- Inner shape: **Diamond**

  - Edge center: $5.41$
  - Corner: $5.25$
  - Minimum $v$: (at most) $\color{blue}{\mathbf{5.25}}$

- Inner shape: **Circle**

  - Edge center: $5.27$
  - Corner: $5.41$
  - Minimum $v$: (at most) $\color{blue}{\mathbf{5.27}}$

- Inner shape: **Octagon**

  - Edge center: $5.38$
  - Corner: $5.38$
  - Minimum $v$: (at most) $\color{blue}{\mathbf{5.38}}$

Again, I'd like to stress that (1) these are not proven until every single starting position for the teacher has been analyzed, and (2) these still may not be the best strategies for the boy.

**Better strategies for the boy**

As outlined in the [Google discussions topic][16], the optimal strategy for a circular pool involves an ever-updating strategy for the boy, moving along an arc towards the edge of the pool. Similarly one would expect that here, the path for the corner-case may not be optimal, and a smooth curve may lead to better results. When running straight for the edge, moving along an arc seems less tempting; the time lost by the boy will likely be larger than the extra time needed for the teacher to run along the edge.

Furthermore the analysis is now based on various different inner shapes, which were kind of chosen ad-hoc. The best strategy may not be any of these simple shapes, but rather a more complex, smooth symmetric shape.

---

# Arbitrary $n$-gons

As the above analysis likely already does not provide an optimal solution for the case $n = 4$, finding the correct answer for large $n$ is not going to be easy either. I'll just analyze one strategy below, which we can analyze quite easily for arbitrary $n$.

First, as also described in [this post][40], the perimeter $p$ of a regular $n$-gon with "radius" $R$ (corresponding to the distance from the center to any of the corners) is given by \begin{align} p = 2 n R \sin \left( \frac{\pi}{n}\right). \end{align} As a special case, for instance, $n = 4$ with "radius" $\sqrt{2}$ as in the above analysis leads to perimeter $2 \cdot 4 \cdot \sqrt{2} \cdot \frac{1}{2} \sqrt{2} = 8$, as we saw above as well. Also, the shortest distance from the center to the edge (to the middle of any of the edges) is given by \begin{align} h = R \cos \left( \frac{\pi}{n}\right). \end{align} Note that $h = R - O(1/n^2)$ is slightly smaller than the radius; the middle of an edge is slightly closer to the center than a corner.

Now, as for a strategy, consider the simple case where again, the boy first tries to get as far from the teacher as possible (keeping the center of the polygon directly between him and the teacher), and then makes a run straight for the nearest edge or corner. First, as in the previous analysis, we will envision the "safe zone" in the center as a circle of a certain radius $r$, such that traversing the perimeter takes the boy the same amount of time as it takes the teacher to traverse the edge of the pool. This means $r$ is defined by the relation: \begin{align} 2 \pi r = \frac{2 n R}{v} \sin\left(\frac{\pi}{n}\right). \end{align} This can be rewritten as $r = \frac{n R}{\pi v} \sin\left(\frac{\pi}{n}\right)$.

We will again consider two cases, based on whether the teacher decides to hang around in a corner or on the middle of an edge, and whether $n$ is odd or even. The two cases are whether directly opposite the teacher is another corner which the boy makes a run for, or whether opposite the teacher is the middle of an edge.

**Case 1: Going for the center of an edge**

As mentioned, the distance to the center of an edge is $R \cos \frac{\pi}{n}$, of which $r = \frac{n R}{\pi v} \sin\left(\frac{\pi}{n}\right)$ can be traversed for free. After that, a distance $R \cos \frac{\pi}{n} - r$ still needs to be swum, while the teacher traverses half the entire pool at a velocity $v$. So the breaking point of the boy getting away is: \begin{align} R \cos \left(\frac{\pi}{n}\right) - \frac{n R}{\pi v} \sin\left(\frac{\pi}{n}\right) = \frac{n R}{v} \sin\left(\frac{\pi}{n}\right). \end{align} This can be rewritten in terms of a condition on $v$ as: \begin{align} v = \frac{n (\pi + 1) \sin\left(\frac{\pi}{n}\right)}{\pi \cos \left(\frac{\pi}{n}\right)}. \end{align} For $n = 4$ we get the previous result $v(4) \geq 4 + \frac{4}{\pi}$, while for $n \to \infty$ we get the suboptimal result $v(n) \geq (\pi + 1) + O(1/n^2)$.

**Case 2: Going for a corner**

The analysis for this case is very similar, except that the distance traveled by the boy is now slightly longer - a factor $1 / \cos \frac{\pi}{n} > 1$ more. This ultimately leads to the very similar condition: \begin{align} v = \frac{n (\pi + 1) \sin\left(\frac{\pi}{n}\right)}{\pi}. \end{align} For $n = 4$ we get a bad result $v(4) \geq \frac{2 \sqrt{2}}{\pi} (1 + \pi) \approx 3.73$, which you would get if you don't adjust your strategy midway and head for the nearest edge (as you should), while for large $n \to \infty$ you do not really notice a difference with the previous case: $v(n) \geq (\pi + 1) + O(1/n^2)$.

**Conjectured lower bound**

Now, this is completely hand-wavy, but for the square we saw that the worst case (for our analysis and strategy) is when we head straight for the edge; if we first head towards a corner, we can adjust our direction mid-way through and escape even faster teachers than when we had directly towards the sides. If this "trend" continues for arbitrary $n$, then we might hope that the above bound for case (1) is actually a valid lower bound on $v(n)$ for larger $n$ as well: \begin{align} \Large\boxed{v(n) \stackrel{?}{\geq} \frac{n}{\pi} (\pi + 1) \tan\left(\frac{\pi}{n}\right)} \end{align}

To get an idea of how this potential lower bound would scale in terms of $n$, here's a plot of $n$ against the above function $v(n)$:

[image: enter image description here] [41]

But again, to prove these are indeed lower bounds on $v(n)$, you would have to consider arbitrary positions of the teacher, instead of just the corners or the centers of the edges.

**Better strategies**

Again, even if these are valid lower bounds, they are unlikely to be sharp bounds since, as mentioned before, optimal strategies should take into account the teacher's actions and should adjust the direction accordingly. This also explains why the limiting case $n \to \infty$ is off from the real optimum, as the optimal curve towards the edge should converge to a spiral/curve instead of a straight line.

[Share][42]

Cite

Follow

[edited Apr 13 '17 at 12:21][43]

[14]

[Community][14] ♦

1

answered Jan 31 '17 at 18:22

[28]

[TMM][28] TMM

9,624 3 3 gold badges 32 32 silver badges 51 51 bronze badges

$\endgroup$

9

-

$\begingroup$ Great stuff! I was actually thinking about using an inner circle when I did my edit but wanted to keep the symmetry of the inner and outer shape. One point that eludes me: to what degree does the boy's ability to do shortcuts within the inner shape affect the maximum size of this shape? Can the inner shape be larger than expected because of this ability? $\endgroup$ – [Jens][27] Jan 31 '17 at 18:54

-

$\begingroup$ @Jens Thanks! And to answer your question: I think not. Essentially you'll want to consider the scenario where you are already *almost*opposite to the teacher. To really get opposite to him you then have to swim roughly perpendicular to the line from you to the teacher, which roughly means along the edge of the inner circle. I think the shortcuts only help to get to the edge of the inner circle faster, but after that you'll be spiraling almost along the edge of the inner circle. $\endgroup$ – [TMM][28] Jan 31 '17 at 19:04

-

$\begingroup$ You may be right, but I'm not quite convinced. Couldn't the boy be "almost" opposite the teacher, but on a larger circle, such that "almost" was good enough to give the boy less distance to swim to the poolside? $\endgroup$ – [Jens][27] Jan 31 '17 at 19:28

-

$\begingroup$ @Jens If you are at say radius $r - \varepsilon$, you can always improve from *almost*opposite the teacher to *exactly*opposite the teacher, by roughly moving along the edge of this region in the opposite direction compared to the teacher. If the smaller region has radius $r + \varepsilon$, you cannot improve from *almost*opposite to *exactly*opposite as you are not fast enough. In fact, if you try, the teacher will only get closer and closer. Whether a circle is optimal is another thing though - this argumentation works for any region with a perimeter below a certain value. $\endgroup$ – [TMM][28] Jan 31 '17 at 23:00

-

$\begingroup$ To find the optimal shape, (1) for each point inside the square you'd have to compute the minimum $v$ needed for the teacher to catch the boy if he starts running from here, (2) you'd have to look at a "height map" inside the square based on these values $v$ for each point, and (3) you'd have to find the value $v$ for which the circlish shape corresponding to exactly this height has perimeter $p = 8 / v$. $\endgroup$ – [TMM][28] Jan 31 '17 at 23:07

| Show **4**more comments

2

[44]

$\begingroup$

For convenience in notation I will write $v_n$ instead of $v(n).$

Let the teacher be able to run $v$ times as fast as the child can swim. (Note that $v$ without a subscript is an arbitrary ratio of speeds, not necessarily a solution of the problem.) Given an $n$-sided pool, the teacher will follow some strategy for pursuing the child and the child will follow some strategy to try to escape the teacher. Let $\tau$ be the time that passes from the moment the child reaches an edge of the pool at some point $P$ until the moment the teacher reaches the same point $P.$ If $\tau > 0,$ the child has escaped; if $\tau < 0,$ the teacher has caught the child.

We are looking for $v_n$ (if it exists) such that when $v$ is near $v_n,$ at each value of $v$ there is a value of $\tau$ such that the teacher cannot force a lower value of $\tau$ by choosing a different strategy, the child cannot force a higher value of $\tau$ by choosing a different strategy, $\tau > 0$ when $v < v_n,$ $\tau < 0$ when $v > v_n,$ and $\tau$ approaches zero as $v$ approaches $v_n.$

It should also be clear that the in the limiting case, as $v$ approaches $v_n,$ the child's path will not meet the edge of the pool at a right angle, because by turning slightly away from the direction from which the teacher is approaching, the child can lengthen the teacher's path much more than the child's path is lengthened. I claim the child's path will meet the edge of the pool at an angle $\alpha$ such that $\cos\alpha = \frac1{v_n},$ because that is the angle at which any further turn away from the teacher will add less than $v_n$ times as much to the teacher's path as to the child's path, whereas any turn toward the teacher will reduce the teacher's path by more than $v_n$ times as much as the child's path. (Note that [the child's best strategy for a circular pool][16] also approaches the side of the pool at the same angle $\alpha.$)

---

Now let's consider the case $n=4$ (a square pool). The limiting speed ratio $v_4$ is independent of the size of the pool, so we can assume the side of the pool has length $2.$

Let's assume (for now) that the first part of the teacher's strategy is to arbitrarily choose one of the two sides adjacent to the starting vertex and run immediately to the center of that side, as in the solution of " [Prove that the boy cannot escape the teacher][45]." Without loss of generality, we an assume that the vertices of the square pool are at $(1,1),$ $(1,-1),$ $(-1,-1),$ and $(-1,1),$ and that the teacher initially runs to $(0,-1).$ In the time that it takes the teacher to reach $(0,-1),$ the child swims to $\left(0, \frac1v\right).$

The child now swims along the $y$-axis in the positive direction. As soon as the teacher starts to move, the child swims in nearly the opposite direction, along a line with a small slope so that the child's $y$-coordinate slowly increases. For example, if the teacher runs to the right (increasing $x$ coordinate), the child swims left along a line with a small negative slope (decreasing $x$ but slowly increasing $y$).

If the teacher were to start running immediately to the right and continue running around the pool in the same direction, as the teacher passed the vertex $(1,-1)$ the child would change direction to swim along a line of slope $\frac{1}{\sqrt{v^2 - 1}}$ toward the edge at $x=-1.$ The child would reach the side of the pool at a point whose $y$-coordinate was much smaller than $\frac1v.$ In order to reach this point, the teacher would run along half one edge of the pool, two complete edges, and about half of another edge; the teacher's relative speed would need to be $v\approx 5.9$ in order to catch the child. But this is not the best strategy for the teacher.

The teacher's strategy will have to include a run from the edge at $y=-1$ to the edge at $y=1,$ traversing one of the other two edges in order to do so. But suppose (for example) that the teacher runs through the vertex at $(1,-1);$ then if the child was not already close enough to the edge at $y=1$ to escape there, the child will respond by swimming to a point with an $x$-coordinate near $-\frac1v.$ The child can then swim toward the edge at $x=-1$ along a line of slope $\frac{1}{\sqrt{v^2 - 1}}$ if the teacher continues toward the vertex at $(1,1),$ swim toward the edge at $y=1$ if the teacher heads back toward the vertex at $(-1,-1),$ or swim toward the vertex at $(-1,1)$ if the teacher remains at $(1,-1).$ The last two maneuvers increase the child's "lead," so the teacher must accept that at some point, the teacher will pass one of the two vertices on the edge at $y=-1,$ and if that vertex is $(1,-1)$ (for example) the child will swim toward the side at $x=-1,$ forcing the teacher to run "the long way around."

The teacher's best strategy is to force the child to reach one of the edges at $x=1$ or $x=-1$ at as great a $y$-coordinate as possible without making it more advantageous for the child to escape at the edge at $y=1.$ To do so, the teacher can simply stay still for a period of time while the child swims along the $y$-axis, running to the left or right only if the child swims to the left or right. During this "midgame" phase, neither the teacher nor the child has a motivation to unilaterally move away from the $y$-axis. The child is deterred because the teacher will move in the same direction and reduce the maximum $\tau$ the child can achieve without returning to the $y$-axis; the teacher is deterred because the child will move in the opposite direction and be closer to being able to trap the teacher into running the "long way around" while that way is still longer than it needs to be.

When the child reaches the point $\left(0, \frac{2}{\sqrt{v^2 - 1} + 1}\right),$ it becomes possible for the child to achieve the same $\tau$ by swimming toward the edge at $y=1$ (at an angle $\alpha,$ of course) as if the child could force the teacher to "run the long way around" while the child swamp to the edge at either $x=1$ or $x=-1.$ The teacher therefore has nothing to lose by immediately running around the edge of the pool (clockwise or counterclockwise), and so the teacher will do that. Supposing the teacher initially runs toward $(-1,-1),$ the child will swim to $P = \left(\frac{\sqrt{v^2 - 1} - 1}{(\sqrt{v^2 - 1} + 1)\sqrt{v^2 - 1}}, 1\right).$ The child therefore swims a distance $d_1 = \frac{v(\sqrt{v^2 - 1} - 1)}{(\sqrt{v^2 - 1} + 1)\sqrt{v^2 - 1}}$ while the teacher runs a distance $d_2 = 4 + \frac{\sqrt{v^2 - 1} - 1}{(\sqrt{v^2 - 1} + 1)\sqrt{v^2 - 1}}.$ We have $\tau = 0$ when $d_2 = vd_1;$ [solving for $v,$][46] we find that $$ v = \sqrt{\frac52\left(7+\sqrt{41}\right)} > 5.788593. $$ Unless there is a better strategy for the teacher, $v_4 > 5.788593.$

It does not seem there is a better strategy for the teacher, since allowing the child to reach either the line $y = \frac{2}{\sqrt{v^2 - 1} + 1} + \frac{x}{\sqrt{v^2 - 1}}$ or $y = \frac{2}{\sqrt{v^2 - 1} + 1} - \frac{x}{\sqrt{v^2 - 1}}$ at $\left(x, \frac{2}{\sqrt{v^2 - 1} + 1} - \frac{|x|}{\sqrt{v^2 - 1}}\right)$ while the teacher is at $(-vx, -1)$ allows the child to escape to the edge $y=1$ whenever $v \leq \sqrt{\frac52\left(7+\sqrt{41}\right)},$ and any strategy except running to the center of an adjacent edge and matching the "left" or "right" movement of the child (in order to cut off escape routes on either side) seems to allow the child to reach such a point relative to whichever side of the square the teacher is on at the time. This is a few steps short of a proof, however.

[Share][47]

Cite

Follow

answered Aug 21 '17 at 0:01

[17]

[David K][17] David K

77k 5 5 gold badges 61 61 silver badges 165 165 bronze badges

$\endgroup$

1

-

$\begingroup$ Hi! Since you spent some time with the problem, you may be interested in the answer by @stewbasic that solves the problem (I did not double check the results though) :) $\endgroup$ – [Ant][15] Oct 25 '17 at 8:03

Add a comment |

## Not the answer you're looking for? Browse other questions tagged [geometry][8] [convergence-divergence][9] [analytic-geometry][10] [curves][11] or [ask your own question][4].

The Overflow Blog

-

[Find knowledge faster: New Articles features][48]

Featured on Meta

-

[Testing three-vote close and reopen on 13 network sites][49]

-

[We're switching to system fonts on May 10, 2021][50]

-

[Enforcement of Quality Standards][51]

#### Linked

[9][52] [The Fox and the Duck in a Square Pond][53]

[23][54] [Prove that the boy cannot escape the teacher][55]

[0][56] [Calculating perimeter of n-sided regular polygons using only height?][57]

[1][58] [Will the boy outwit the teacher in this way?][59]

#### Related

[6][60] [The largest regular m-gon that fits inside a regular n-gon][61]

[0][62] [Algorithm - the longest chord whose supporting line contains a given point, in a convex polygon][63]

[1][64] [If I have an $n$-gon, for odd $n\geq5$ with all angles equal to the angles of the regular $n$-gon, is my $n$-gon necessarily regular?][65]

[23][54] [Prove that the boy cannot escape the teacher][66]

[3][67] [How does the area of a regular n-gon compare to the area of a non-regular n-gon?][68]

[0][69] [Regular n-gon diagonal length][70]

[0][71] [Regular $n$-gon sidelength][72]

#### [Hot Network Questions][73]

-

[How could the blood be improved so that it can carry more oxygen?][74]
-

[Should I be worried that bitcoincore.org now suddenly only provides an "unsigned" Bitcoin Core installer?][75]
-

[Sitecore containers exit with "Failed to update IIS configuration" error][76]
-

[Convince my wife that the flu vaccine is good for our child][77]
-

[Is this pairing-based signature scheme secure?][78]
-

[Meaning of the phrase "If ever a man leaped across time into the raw..."][79]
-

[What's wrong with being wise and learned that warrants being denied by God the secrets of His kingdom? Luke 10:21][80]
-

[How to safely and legally join building wire behind drywall][81]
-

[How bad is switching derailleur gears under load?][82]
-

[What was the "Favorable result" that the German admiralty was expecting from the naval attack on the Royal Navy in 1918?][83]
-

[How should we compensate for lack of friction for vehicles on the moon?][84]
-

[I got a very bad review, but the paper is not rejected][85]
-

[Is there a catalog of Lego building techniques?][86]
-

[Why do banks seem to be indifferent about identity theft?][87]
-

[Spurious 0.0000000000001 added to formula result][88]
-

[If I touched a black hole with a small mass (the mass of an apple), would I die?][89]
-

[How to smoothly move down in Z-index a curved object][90]
-

[How can draw an area under a thermodynamic graph?][91]
-

[secp256k1: is it theoretically possible to generate same signature with different key, message hash and k?][92]
-

[How would you describe this not-quite-a-triplet rhythm?][93]
-

[HR suggested 1:1 talk - how to address potential topics?][94]
-

[What are the "Big 13" critical contingency spacewalks on the ISS? Have any actually been performed?][95]
-

[How can the title "13" be so common?][96]
-

[Does use of a Fireball Necklace count as 'casting a spell'?][97]

more hot questions

[Question feed][98]

Your privacy

By clicking “Accept all cookies”, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our [Cookie Policy][99].

Accept all cookies Customize settings


## Links

[1]: /web/20210506134248/https://math.stackexchange.com/users/signup?ssrc=hero&amp;returnurl=https%3a%2f%2fmath.stackexchange.com%2fquestions%2f1762665%2fcan-the-boy-escape-the-teacher-for-a-regular-n-gon
[2]: https://web.archive.org/web/20210506134248/https://stackoverflow.com/teams
[3]: /web/20210506134248/https://math.stackexchange.com/questions/1762665/can-the-boy-escape-the-teacher-for-a-regular-n-gon
[4]: /web/20210506134248/https://math.stackexchange.com/questions/ask
[5]: ?lastactivity
[6]: /web/20210506134248/https://math.stackexchange.com/posts/1762665/timeline
[7]: https://web.archive.org/web/20210506134248/https://math.stackexchange.com/questions/1555855/prove-that-the-boy-cannot-escape-the-teacher
[8]: /web/20210506134248/https://math.stackexchange.com/questions/tagged/geometry
[9]: /web/20210506134248/https://math.stackexchange.com/questions/tagged/convergence-divergence
[10]: /web/20210506134248/https://math.stackexchange.com/questions/tagged/analytic-geometry
[11]: /web/20210506134248/https://math.stackexchange.com/questions/tagged/curves
[12]: /web/20210506134248/https://math.stackexchange.com/q/1762665
[13]: /web/20210506134248/https://math.stackexchange.com/posts/1762665/revisions
[14]: /web/20210506134248/https://math.stackexchange.com/users/-1/community
[15]: /web/20210506134248/https://math.stackexchange.com/users/66711/ant
[16]: https://web.archive.org/web/20210506134248/https://groups.google.com/forum/#!msg/rec.puzzles/cC332o0Ha88/nzEAcWhWessJ
[17]: /web/20210506134248/https://math.stackexchange.com/users/139123/david-k
[18]: /web/20210506134248/https://math.stackexchange.com/users/82412/ari
[19]: /web/20210506134248/https://math.stackexchange.com/questions/1762665/can-the-boy-escape-the-teacher-for-a-regular-n-gon?answertab=active#tab-top
[20]: /web/20210506134248/https://math.stackexchange.com/questions/1762665/can-the-boy-escape-the-teacher-for-a-regular-n-gon?answertab=oldest#tab-top
[21]: /web/20210506134248/https://math.stackexchange.com/questions/1762665/can-the-boy-escape-the-teacher-for-a-regular-n-gon?answertab=votes#tab-top
[22]: /web/20210506134248/https://math.stackexchange.com/posts/1837688/timeline
[23]: https://web.archive.org/web/20210506134248/https://i.stack.imgur.com/lgsXa.png
[24]: https://web.archive.org/web/20210506134248/https://i.stack.imgur.com/Hn5jb.gif
[25]: /web/20210506134248/https://math.stackexchange.com/a/1837688
[26]: /web/20210506134248/https://math.stackexchange.com/posts/1837688/revisions
[27]: /web/20210506134248/https://math.stackexchange.com/users/307210/jens
[28]: /web/20210506134248/https://math.stackexchange.com/users/11176/tmm
[29]: /web/20210506134248/https://math.stackexchange.com/posts/2488286/timeline
[30]: https://web.archive.org/web/20210506134248/https://drive.google.com/file/d/0ByRo3goCgoh7OFJCQ2RiUzEycVE/view?usp=sharing
[31]: https://web.archive.org/web/20210506134248/https://ggbm.at/dXkrt9pb
[32]: /web/20210506134248/https://math.stackexchange.com/a/2488286
[33]: /web/20210506134248/https://math.stackexchange.com/users/197161/stewbasic
[34]: /web/20210506134248/https://math.stackexchange.com/posts/2122862/timeline
[35]: https://web.archive.org/web/20210506134248/https://i.stack.imgur.com/RCIfO.png
[36]: https://web.archive.org/web/20210506134248/https://i.stack.imgur.com/0EXe2.png
[37]: https://web.archive.org/web/20210506134248/https://i.stack.imgur.com/gbM56.png
[38]: https://web.archive.org/web/20210506134248/https://i.stack.imgur.com/gi9Td.png
[39]: https://web.archive.org/web/20210506134248/https://math.stackexchange.com/a/1837688/11176
[40]: https://web.archive.org/web/20210506134248/https://math.stackexchange.com/questions/669373/calculating-perimeter-of-n-sided-regular-polygons-using-only-height
[41]: https://web.archive.org/web/20210506134248/https://i.stack.imgur.com/d8xYq.png
[42]: /web/20210506134248/https://math.stackexchange.com/a/2122862
[43]: /web/20210506134248/https://math.stackexchange.com/posts/2122862/revisions
[44]: /web/20210506134248/https://math.stackexchange.com/posts/2400756/timeline
[45]: https://web.archive.org/web/20210506134248/https://math.stackexchange.com/questions/1555855
[46]: https://web.archive.org/web/20210506134248/http://www.wolframalpha.com/input/?i=%28v%5E2%2Fsqrt%28v%5E2-1%29%29%2A%28sqrt%28v%5E2-1%29-1%29%2F%28sqrt%28v%5E2-1%29%2B1%29+%3D+4+%2B+%281%2Fsqrt%28v%5E2-1%29%29%2A%28sqrt%28v%5E2-1%29-1%29%2F%28sqrt%28v%5E2-1%29%2B1%29
[47]: /web/20210506134248/https://math.stackexchange.com/a/2400756
[48]: https://web.archive.org/web/20210506134248/https://stackoverflow.blog/2021/05/03/find-knowledge-faster-new-articles-features/
[49]: https://web.archive.org/web/20210506134248/https://meta.stackexchange.com/questions/364007/testing-three-vote-close-and-reopen-on-13-network-sites
[50]: https://web.archive.org/web/20210506134248/https://meta.stackexchange.com/questions/364048/were-switching-to-system-fonts-on-may-10-2021
[51]: https://web.archive.org/web/20210506134248/https://math.meta.stackexchange.com/questions/33508/enforcement-of-quality-standards
[52]: /web/20210506134248/https://math.stackexchange.com/q/2394785
[53]: /web/20210506134248/https://math.stackexchange.com/questions/2394785/the-fox-and-the-duck-in-a-square-pond?noredirect=1
[54]: /web/20210506134248/https://math.stackexchange.com/q/1555855
[55]: /web/20210506134248/https://math.stackexchange.com/questions/1555855/prove-that-the-boy-cannot-escape-the-teacher?noredirect=1
[56]: /web/20210506134248/https://math.stackexchange.com/q/669373
[57]: /web/20210506134248/https://math.stackexchange.com/questions/669373/calculating-perimeter-of-n-sided-regular-polygons-using-only-height?noredirect=1
[58]: /web/20210506134248/https://math.stackexchange.com/q/1762499
[59]: /web/20210506134248/https://math.stackexchange.com/questions/1762499/will-the-boy-outwit-the-teacher-in-this-way?noredirect=1
[60]: /web/20210506134248/https://math.stackexchange.com/q/605126
[61]: /web/20210506134248/https://math.stackexchange.com/questions/605126/the-largest-regular-m-gon-that-fits-inside-a-regular-n-gon
[62]: /web/20210506134248/https://math.stackexchange.com/q/958187
[63]: /web/20210506134248/https://math.stackexchange.com/questions/958187/algorithm-the-longest-chord-whose-supporting-line-contains-a-given-point-in-a
[64]: /web/20210506134248/https://math.stackexchange.com/q/1514325
[65]: /web/20210506134248/https://math.stackexchange.com/questions/1514325/if-i-have-an-n-gon-for-odd-n-geq5-with-all-angles-equal-to-the-angles-of-th
[66]: /web/20210506134248/https://math.stackexchange.com/questions/1555855/prove-that-the-boy-cannot-escape-the-teacher
[67]: /web/20210506134248/https://math.stackexchange.com/q/1682465
[68]: /web/20210506134248/https://math.stackexchange.com/questions/1682465/how-does-the-area-of-a-regular-n-gon-compare-to-the-area-of-a-non-regular-n-gon
[69]: /web/20210506134248/https://math.stackexchange.com/q/1953074
[70]: /web/20210506134248/https://math.stackexchange.com/questions/1953074/regular-n-gon-diagonal-length
[71]: /web/20210506134248/https://math.stackexchange.com/q/3433030
[72]: /web/20210506134248/https://math.stackexchange.com/questions/3433030/regular-n-gon-sidelength
[73]: https://web.archive.org/web/20210506134248/https://stackexchange.com/questions?tab=hot
[74]: https://web.archive.org/web/20210506134248/https://worldbuilding.stackexchange.com/questions/202043/how-could-the-blood-be-improved-so-that-it-can-carry-more-oxygen
[75]: https://web.archive.org/web/20210506134248/https://bitcoin.stackexchange.com/questions/106038/should-i-be-worried-that-bitcoincore-org-now-suddenly-only-provides-an-unsigned
[76]: https://web.archive.org/web/20210506134248/https://sitecore.stackexchange.com/questions/28675/sitecore-containers-exit-with-failed-to-update-iis-configuration-error
[77]: https://web.archive.org/web/20210506134248/https://parenting.stackexchange.com/questions/41583/convince-my-wife-that-the-flu-vaccine-is-good-for-our-child
[78]: https://web.archive.org/web/20210506134248/https://crypto.stackexchange.com/questions/89813/is-this-pairing-based-signature-scheme-secure
[79]: https://web.archive.org/web/20210506134248/https://literature.stackexchange.com/questions/18526/meaning-of-the-phrase-if-ever-a-man-leaped-across-time-into-the-raw
[80]: https://web.archive.org/web/20210506134248/https://hermeneutics.stackexchange.com/questions/59906/whats-wrong-with-being-wise-and-learned-that-warrants-being-denied-by-god-the-s
[81]: https://web.archive.org/web/20210506134248/https://diy.stackexchange.com/questions/223588/how-to-safely-and-legally-join-building-wire-behind-drywall
[82]: https://web.archive.org/web/20210506134248/https://bicycles.stackexchange.com/questions/76570/how-bad-is-switching-derailleur-gears-under-load
[83]: https://web.archive.org/web/20210506134248/https://history.stackexchange.com/questions/63820/what-was-the-favorable-result-that-the-german-admiralty-was-expecting-from-the
[84]: https://web.archive.org/web/20210506134248/https://worldbuilding.stackexchange.com/questions/202085/how-should-we-compensate-for-lack-of-friction-for-vehicles-on-the-moon
[85]: https://web.archive.org/web/20210506134248/https://academia.stackexchange.com/questions/167153/i-got-a-very-bad-review-but-the-paper-is-not-rejected
[86]: https://web.archive.org/web/20210506134248/https://bricks.stackexchange.com/questions/16183/is-there-a-catalog-of-lego-building-techniques
[87]: https://web.archive.org/web/20210506134248/https://money.stackexchange.com/questions/140472/why-do-banks-seem-to-be-indifferent-about-identity-theft
[88]: https://web.archive.org/web/20210506134248/https://superuser.com/questions/1646546/spurious-0-0000000000001-added-to-formula-result
[89]: https://web.archive.org/web/20210506134248/https://physics.stackexchange.com/questions/634080/if-i-touched-a-black-hole-with-a-small-mass-the-mass-of-an-apple-would-i-die
[90]: https://web.archive.org/web/20210506134248/https://blender.stackexchange.com/questions/221611/how-to-smoothly-move-down-in-z-index-a-curved-object
[91]: https://web.archive.org/web/20210506134248/https://tex.stackexchange.com/questions/595881/how-can-draw-an-area-under-a-thermodynamic-graph
[92]: https://web.archive.org/web/20210506134248/https://crypto.stackexchange.com/questions/89809/secp256k1-is-it-theoretically-possible-to-generate-same-signature-with-differen
[93]: https://web.archive.org/web/20210506134248/https://music.stackexchange.com/questions/114238/how-would-you-describe-this-not-quite-a-triplet-rhythm
[94]: https://web.archive.org/web/20210506134248/https://workplace.stackexchange.com/questions/172104/hr-suggested-11-talk-how-to-address-potential-topics
[95]: https://web.archive.org/web/20210506134248/https://space.stackexchange.com/questions/51948/what-are-the-big-13-critical-contingency-spacewalks-on-the-iss-have-any-actua
[96]: https://web.archive.org/web/20210506134248/https://law.stackexchange.com/questions/64740/how-can-the-title-13-be-so-common
[97]: https://web.archive.org/web/20210506134248/https://rpg.stackexchange.com/questions/184767/does-use-of-a-fireball-necklace-count-as-casting-a-spell
[98]: /web/20210506134248/https://math.stackexchange.com/feeds/question/1762665
[99]: https://web.archive.org/web/20210506134248/https://stackoverflow.com/legal/cookie-policy
