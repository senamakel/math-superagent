> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/loj138-universal-euclidean-floor-moments.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.cnblogs.com/AThousandMoons/p/13129167.html | converted from HTML -->

## What is in it

- [2]
- [LOJ138 类欧几里得算法【万能欧几里得】][7]
    - 公告


## What it claims

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
		memcpy(res.ans, ans, sizeof…

posted…

*[digest of a 4225 character source; every section, statement, and proof in full at `research/sources/loj138-universal-euclidean-floor-moments.full.md`]*
