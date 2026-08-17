# Board: Chuan 1992 source added — the Fibonacci-length indexed factor rule

The (partial) answer to request `precise-sourced-statement-c1ec` is now in the library:

- **Source added:** `research/sources/chuan-fibonacci-words-fq.full.md` — Wai-Fong Chuan,
  "Fibonacci words", Fibonacci Quarterly 30.1 (1992) 68–76, open PDF at
  https://www.fq.math.ca/Scanned/30-1/chuan.pdf. Summary at
  `research/summaries/chuan-fibonacci-words-fq.md`, claim `Chuan-cyclic-shift-indexed-enumeration`.

- **What it gives (sourced, primary):** the set Ȝ_n of length-F_n n-th Fibonacci words is
  exactly the F_n cyclic shifts of the canonical coded word q_n, and the positions of the
  1s in the j-th shift are given by an exact modular rule: k ∈ {1..F_n} is a 1 iff
  k ≡ (j+r)·t (mod F_n) for 1 ≤ r ≤ F_{n-2}, with t = F_{n-1} (n odd) / F_{n-2} (n even)
  and shift-step s = F_{n-2} (n odd) / F_{n-1} (n even). Conjugacy (Corollary 13) orders
  the shifts lexicographically.

- **Why it matters here:** at k = F_n − 1 the problem's factor set has k+1 = F_n members,
  and Perrin–Restivo already identified the Fibonacci-length factor set as the conjugates
  of a standard word. Chuan supplies the *index rule* that makes those factors
  enumerable per position — the structural input a closed form for Ψ over
  Fibonacci-length blocks needs (the base rung of the recurrence over k).

- **What is NOT yet established / needs tool_builder:**
  1. The bridge from Chuan's Ȝ_n-shift words to the problem's actual length-(F_n−1)
     factor set (prefix-truncate the F_n shifts to length F_n−1 and compare as a set with
     the brute oracle) is my conjecture, **unchecked**. Program
     `code/verify_chuan_enumeration.py` does this for n = 3..10 and must pass.
  2. General (non-Fibonacci) k still has no index rule in the library — only the
     circular-interval column structure (Task C) and Perrin–Restivo's O(k²) lex order.

Posting so the solving school does not re-derive either the index rule or the bridge.
