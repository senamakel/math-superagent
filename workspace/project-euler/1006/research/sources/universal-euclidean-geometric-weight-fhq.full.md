<!-- source: https://www.cnblogs.com/dixiao/p/15719155.html | converted from HTML -->

[学习笔记]万能欧几里得 - fhq_treap - 博客园

[image: 返回主页] [1]

# [fhq_treap][2]

## 很多时候你要够努力，你要做的是往前走，去100分的位置，而不是在0分位置就此停止

- [博客园][3]
- [首页][1]
- [新随笔][4]
-
- -->
- [管理][5]

# [[学习笔记]万能欧几里得][6]

要对得起你的苦难

万能欧几里得对比类欧几里得的优势在于其对于一类差分影响线性问题给出了一个通用方法。

### 问题形式

对于求下列问题 \(y = \lfloor\frac{px + r}{q}\rfloor\)

求该类形式 \(\sum f(x) a^x g(y)b^y\)

我们考虑将其丢到 \(y = \frac{px + r}{q}\) 的几何上思考，如果其与网格线交于横线，则其需对 \(y\) 进行一个加操作，遇到竖线则需要加入贡献。

我们维护一个列向量，遇到横线就乘上一个 \(U\) (考虑维护 \(y\) 加这一操作),遇到竖线就乘一个 \(R\) (贡献)，这也是为什么要求差分影响线性的原因。

比如若求 \(\sum y\)
则取 \((v,U,R)\) 为
\(\begin{bmatrix}\sum_x y\\y\\1\end{bmatrix}\) \(\begin{bmatrix}1&0&0\\0&1&1\\0&0&1\end{bmatrix}\) \(\begin{bmatrix}1&1&0\\0&1&0\\0&0&1\end{bmatrix}\)

我们只要快速乘出该矩阵即可。

### 解决该问题

我们形式化的描述该问题有 \(n个R的U,R\) 矩阵，以 \(R\) 结尾，第 \(x\) 个 \(R\) 前有 \(y = \lfloor\frac{px + r}{q}\rfloor\) ，求矩阵乘积。

#### 合并

所以我们考虑 \(q \leq p\) ，则每个 \(R\) 前都有 \(\lfloor\frac{p}{q}\rfloor\) 个连续 \(U\),我们将其合并，那么每个 \(R\) 前的数还有
\(\lfloor\frac{px + r}{q}\rfloor - x\lfloor\frac{p}{q}\rfloor = \lfloor\frac{px - px + (p\ mod\ q)x + r}{q}\rfloor = \lfloor\frac{(p\ mod\ q)x + r}{q}\rfloor\)

于是有 \(sol(p,q,r,n,U,R) = sol(p\ mod\ q,q,r,n,U,U^{\lfloor\frac{p}{q}\rfloor}R)\)

#### 翻转

我们考虑第 \(y\) 个 \(U\) 前有多少个 \(R\)
即 \(y > \lfloor\frac{px + r}{q}\rfloor\) 的最大整数解。
我们类似于类欧操作我们改写不等式为 \(x \leq \lfloor\frac{qy - r - 1}{p}\rfloor\)

此时 \(U\) 的个数 \(m = \lfloor\frac{pn + r}{q}\rfloor\)

但是我们还要处理两个问题

- 新的 \(r\) 应在 \([0,p)\) 间
- 原序列以R结尾，我们理应不改变其性质。

对于第一个问题，我们把第一个 \(U\) 和他前面所有 \(R\) 拿出来单独算，那么后面的第 \(y\) 个 \(U\),在原来这个数列中是第 \(y+ 1\) 个，所以其改写为 \(\lfloor\frac{qy + (q - r - 1)}{p}\rfloor\)

第二个问题，我们把最后一段 \(R\) 单独计算，则共有 \(n - \lfloor\frac{qm - r - 1}{p}\rfloor\)

所以我们得到了 \(sol(p,q,r,n,U,R) = R^{\lfloor\frac{q - r - 1}{p}\rfloor}U\times sol(q,p,(q - r - 1)\ mod\ p,m - 1,R,U) \times R ^ {(n - \lfloor\frac{qm - r - 1}{p}\rfloor )}\)

如果 \(m = 0\) 则
\(sol(p,q,r,n,U,R) = R^n\)

#### 合并

于是我们得到
\(sol(p,q,r,n,U,R)=\begin{cases} R^n&m = 0\\R^{\lfloor\frac{q - r - 1}{p}\rfloor}U\times sol(q,p,(q - r - 1)\ mod\ p,m - 1,R,U) \times R ^ {(n - \lfloor\frac{qm - r - 1}{p}\rfloor )}&m>0\end{cases}\)

### 实现

#### [【模板】类欧几里得算法][7]

【模板】类欧几里得算法

```
#include<bits/stdc++.h>
#define ll long long
#define N 22
#define P 998244353

ll t,p,q,r,l;

struct Po{
	ll cntu,cntr,sumi,sums,sqrs,prod;
	Po(){cntu = cntr = sumi = sums = sqrs = prod = 0;}
	Po operator + (Po b) {
		Po c;
		c.cntu=(cntu+b.cntu)%P,c.cntr=(cntr+b.cntr)%P;
		c.sumi=(sumi+b.sumi+cntr*b.cntr)%P;
		c.sums=(sums+b.sums+cntu*b.cntr)%P;
		c.sqrs=(sqrs+b.sqrs+((cntu*cntu)%P)*b.cntr+(2*cntu*b.sums)%P)%P;
		c.prod=((prod+b.prod+((cntu*cntr)%P)*b.cntr)%P+cntu*b.sumi+cntr*b.sums)%P;
		return c;
	}
}nu,nr,ans;

inline Po pow(Po a,ll k){
	Po res;
	while(k){
		if(k & 1){res = res + a;}
		a = a + a;
		k >>= 1;
	}
	return res;
}

inline ll div(ll a,ll b,ll c,ll d){return ((long double)1.0 * a * b + c) / d;}

inline Po solve(ll p,ll q,ll r,ll l,Po a,Po b){
	if(!l)return Po();
	if(p >= q)return solve(p % q,q,r,l,a,pow(a,p / q) + b);
	ll m = div(l,p,r,q);
	if(!m)return pow(b,l);
	ll cnt = l - div(q,m,-r - 1,p);
	return pow(b,(q - r - 1) / p) + a + solve(q,p,(q - r - 1) % p,m - 1,b,a) + pow(b,cnt);
}

int main(){
	scanf("%lld",&t);
	while(t -- ){
		scanf("%lld%lld%lld%lld",&l,&p,&r,&q);
		nu.cntu = 1,nu.cntr = nu.sumi = nu.sums = nu.sqrs = nu.prod = 0;
		nr.cntu = nr.sums = nr.sqrs = nr.prod = 0,nr.sumi = nr.cntr = 1;
		ans = pow(nu,r / q) + solve(p,q,r % q,l,nu,nr);
		printf("%lld %lld %lld\n",(ans.sums+r/q)%P,(ans.sqrs+((r/q)%P)*((r/q)%P))%P,ans.prod);
	}
}
```

### 一些特定的问题

万欧不能解决一类问题：
如 \(\sum \sqrt y,\sum x^y,\sum a^{xy},\sum 2^{2^y},\sum Asin(wy + \phi)\),这类单维影响无法差分线性，即我们无法设计出一个好的矩阵来表达其。

posted @ 2021-12-22 13:42 [fhq_treap][2] 阅读( 747) 评论( 1) 收藏 [举报][8]

刷新页面 返回顶部

[9]

### 公告

[博客园][3] &copy; 2004-2026
[浙公网安备 33010602011771号][10] [浙ICP备2021040463号-3][11]


## Links

[1]: https://www.cnblogs.com/dixiao/
[2]: https://www.cnblogs.com/dixiao
[3]: https://www.cnblogs.com/
[4]: https://i.cnblogs.com/EditPosts.aspx?opt=1
[5]: https://i.cnblogs.com/
[6]: https://www.cnblogs.com/dixiao/p/15719155.html
[7]: https://www.luogu.com.cn/problem/P5170
[8]: https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fdixiao%2Fp%2F15719155.html&targetId=15719155&targetType=0
[9]: https://www.volcengine.com/activity/codingplan?amp;utm_content=hw&amp;utm_medium=devrel_tool_web&amp;utm_source=OWO&amp;utm_term=cnblogs
[10]: http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771
[11]: https://beian.miit.gov.cn
