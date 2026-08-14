# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive oracle for PE 351. hidden_literal(n) is the mechanical definition scan (closer collinear point exists; O(N²), N=3n²+3n+1); hidden_gcd(n) is the equivalent gcd(|q|,|r|)>=2 count (O(n²) gcds). Established correct: reproduces the statement's H(5)=30, H(10)=138, H(1000)=1177848; both methods agree on n≤10; H(1..8) matches OEIS A216453. Self-capped at n≤1000; literal scan capped at n≤10. |
