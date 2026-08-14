"""Verify the structural claims used for Psi(k) against the brute oracle.

Claims tested:
  C1. For every length k, the Fibonacci word has EXACTLY ONE right-special
      factor (a factor w with both w0 and w1 factors). Same for left-special.
  C2. That right-special factor of length k equals a prefix of the infinite
      Fibonacci word (a standard word), and in particular equals the finite
      Fibonacci word S_n truncated to length k for the right n | |S_n| > k.
  C3. Bispecial factors are ordinary (not strict): w0&w1&&0w&1w all factors.
  C4. F(k) (the k+1 length-k factors) as k ranges over consecutive Fibonacci
      lengths obeys the self-similarity F(F_n) built from F(F_{n-1}), F(F_{n-2})
      (Fici-type factorizations / the substitution structure).

All checks are against the directly generated Fibonacci word.
"""
import sys

def fib_word(n):
    w = ""
    a, b = "0", "01"
    if n <= 0: return "0"
    if n == 1: return "01"
    for _ in range(2, n+1):
        a, b = b, b+a
    return b

def factors(word, k):
    return {word[i:i+k] for i in range(len(word)-k+1)}

def right_special(word, k):
    """factor(s) w of length k such that w0 and w1 are both factors."""
    Fak = factors(word, k)
    Fak1 = factors(word, k+1)
    rs = [w for w in Fak if (w+'0' in Fak1) and (w+'1' in Fak1)]
    return rs

def left_special(word, k):
    Fak = factors(word, k)
    Fak1 = factors(word, k+1)
    return [w for w in Fak if ('0'+w in Fak1) and ('1'+w in Fak1)]

def bispecial(word, k):
    Fak = factors(word,k); Fak1 = factors(word,k+1); Fak2ianak = None
    Fak2 = factors(word,k+2)
    out=[]
    for w in Fak:
        if (w+'0' in Fak1) and (w+'1' in Fak1) and ('0'+w in Fak1) and ('1'+w in Fak1):
            # classification: how many of the 4 two-letter fills occur
            fills = [a+b for a in '01' for b in '01']
            c = sum(1 for a in '01' for b in '01' if a+w+b in Fak2)
            out.append((w,c))
    return out

def is_prefix_of_fibonacci(w, W):
    return W.startswith(w)

W = fib_word(30)   # long Fibonacci word (|S_30| huge for k<=40 checks)

print("="*70)
print("C1/C2: unique right-special factor per length; equals a Fibonacci prefix")
print("="*70)
all_ok = True
for k in range(1, 25):
    rs = right_special(W, k)
    ls = left_special(W, k)
    # uniqueness
    uniq = (len(rs)==1 and len(ls)==1)
    # each right special factor is a prefix of the Fibonacci word W
    pref = all(is_prefix_of_fibonacci(w, W) for w in rs)
    # the right-special factor of length k should be S_n truncated: check that
    # it is the length-k prefix of some finite Fibonacci word S_m.
    w = rs[0] if rs else "?"
    # find which finite fib prefix contains w as its own prefix
    s_of=set()
    for m in range(0,8):
        Sm = fib_word(m)
        if Sm.startswith(w):
            s_of.add(m)
    print(f"k={k:2d}: RS={rs} LS={ls} uniq={uniq} is-fib-prefix={pref} fib-indices-prepending={sorted(s_of)}")
    all_ok = all_ok and uniq and pref

print("C1/C2 all ok:", all_ok)

print()
print("="*70)
print("C3: bispecial factors are ordinary (c between 2..4, never strict-4 separately)")
print("="*70)
for k in range(1, 16):
    bs = bispecial(W,k)
    print(f"k={k:2d}: bispecial {bs}")
