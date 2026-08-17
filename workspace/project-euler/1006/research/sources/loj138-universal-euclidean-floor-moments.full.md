<!-- source: https://www.cnblogs.com/AThousandMoons/p/13129167.html | converted from HTML -->

LOJ138 类欧几里得算法【万能欧几里得】 - mizu164 - 博客园

[image: 返回主页] [1]

# [2]

##

- [博客园][3]
- [首页][1]
- [新随笔][4]
- [联系][5]
- 订阅 -->
- [管理][6]

# [LOJ138 类欧几里得算法【万能欧几里得】][7]

[题目链接][8]

题目描述：求

\[\sum_{x=0}^n\lfloor\frac{px+r}{q}\rfloor^{k_1}x^{k_2} \bmod (10^9+7) \]

数据范围：数据组数 \(T=1000\) ， \(n,p,q,r\le 10^9\) ， \(k_1,k_2\ge 0,k_1+k_2\le 10\) 。

[真正的类欧几里得][9] ，过于令人自闭了。

所以把刚学的 [万能欧几里得][10] 用一用，设`Node`结构体为 \((cnt_1,cnt_2,ans_{i,j})\) ，表示 \(\text{U,R}\) 的个数，和 \(k_1=i,k_2=j\) 时的答案。所以若 \(C=A+B\) ，则

\[\begin{aligned} C.cnt_1&=A.cnt_1+B.cnt_1 \\ C.cnt_2&=A.cnt_2+B.cnt_2 \\ C.ans_{a,b}&=A.ans_{a,b}+\sum_{i=0}^a\sum_{j=0}^b\binom{a}{i}\binom{b}{j}A.cnt_1^iA.cnt_2^jB.ans_{a-i,b-j} \end{aligned} \]

其中第三个柿子把 \((y+A.cnt_1)^a(x+A.cnt_2)^b\) 展开就可以得到。

再把那个模板原封不动地套一遍，时间复杂度 \(O(225\log\max\{p,q\})\) 。

```
#include<bits/stdc++.h>
#define Rint register int
#define MP make_pair
#define PB push_back
#define fi first
#define se second
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;
const int mod = 1000000007;
template<typename T>
inline void read(T &x){
	int ch = getchar(); x = 0; bool f = false;
	for(;ch < '0' || ch > '9';ch = getchar()) f |= ch == '-';
	for(;ch >= '0' && ch <= '9';ch = getchar()) x = x * 10 + ch - '0';
	if(f) x = -x;
}
inline void qmo(int &x){x += (x >> 31) & mod;}
template<typename T>
inline bool chmax(T &a, const T &b){if(a < b) return a = b, 1; return 0;}
template<typename T>
inline bool chmin(T &a, const T &b){if(a > b) return a = b, 1; return 0;}
int T, C[11][11];
LL n, p, q, r, k1, k2;
struct Node {
	LL cnt1, cnt2;
	int ans[11][11];
	Node(){cnt1 = cnt2 = 0; memset(ans, 0, sizeof ans);}
	Node operator = (const Node &o){cnt1 = o.cnt1; cnt2 = o.cnt2; memcpy(ans, o.ans, sizeof ans); return *this;}
	Node operator * (const Node &o) const {
		Node res;
		res.cnt1 = cnt1 + o.cnt1;
		res.cnt2 = cnt2 + o.cnt2;
		memcpy(res.ans, ans, sizeof res.ans);
		int x = cnt1 % mod, y = cnt2 % mod;
		for(Rint al = 0;al <= k1;++ al)
			for(Rint be = 0;be <= k2;++ be)
				for(Rint i = 0, t1 = 1;i <= al;++ i, t1 = (LL) t1 * x % mod)
					for(Rint j = 0, t2 = 1;j <= be;++ j, t2 = (LL) t2 * y % mod)
						qmo(res.ans[al][be] += (LL) C[al][i] * C[be][j] % mod * o.ans[al - i][be - j] % mod * t1 % mod * t2 % mod - mod);
		return res;
	}
};
template<typename T>
T ksm(T a, LL b){
	T res;
	for(;b;b >>= 1, a = a * a) if(b & 1) res = res * a;
	return res;
}
Node calc(LL p, LL q, LL r, LL n, const Node &a, const Node &b){
	LL m = (p * n + r) / q;
	if(!m) return ksm(b, n);
	if(p >= q) return calc(p % q, q, r, n, a, ksm(a, p / q) * b);
	return ksm(b, (q - r - 1) / p) * a * calc(q, p, (q - r - 1) % p, m - 1, b, a) * ksm(b, n - (m * q - r - 1) / p);
}
inline void work(){
	Node res, A, B; read(n); read(p); read(r); read(q); read(k2); read(k1);
	A.cnt1 = 1; B.cnt2 = 1; for(Rint i = 0;i <= k2;++ i) B.ans[0][i] = 1;
	res.cnt1 = r / q; for(Rint i = 0, t = 1;i <= k1;++ i, t = (LL) t * res.cnt1 % mod) res.ans[i][0] = t;
	res = res * calc(p, q, r % q, n, A, B);
	printf("%d\n", res.ans[k1][k2]);
}
int main(){
	read(T);
	for(Rint i = 0;i <= 10;++ i){
		C[i][0] = 1;
		for(Rint j = 1;j <= i;++ j) qmo(C[i][j] = C[i - 1][j] + C[i - 1][j - 1] - mod);
	}
	while(T --) work();
}
```

posted @ 2020-06-15 09:29 [mizu164][2] 阅读( 580) 评论( 0) 收藏 [举报][11]

刷新页面 返回顶部

[12]

### 公告

[博客园][3] &copy; 2004-2026
[浙公网安备 33010602011771号][13] [浙ICP备2021040463号-3][14]


## Links

[1]: https://www.cnblogs.com/AThousandMoons/
[2]: https://www.cnblogs.com/AThousandMoons
[3]: https://www.cnblogs.com/
[4]: https://i.cnblogs.com/EditPosts.aspx?opt=1
[5]: https://msg.cnblogs.com/send/mizu164
[6]: https://i.cnblogs.com/
[7]: https://www.cnblogs.com/AThousandMoons/p/13129167.html
[8]: https://loj.ac/problem/138
[9]: https://www.cnblogs.com/zzqsblog/p/8904010.html
[10]: https://www.cnblogs.com/AThousandMoons/p/13129093.html
[11]: https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2FAThousandMoons%2Fp%2F13129167.html&targetId=13129167&targetType=0
[12]: https://harmonyos.cnblogs.com/p/31505
[13]: http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771
[14]: https://beian.miit.gov.cn
