"""Position analysis of length-k factors of the infinite Fibonacci word.

Builds the infinite Fibonacci word f as S_n iterated until length >= 20000
(reusing brute.py's S), then for k=1..14 studies the k+1 distinct length-k
factors and their occurrence positions.

Reports:
  1. For each factor of length k (in sorted order of the word): the leftmost
     occurrence position and the next few occurrence positions (up to 8 total).
  2. L(k) = sorted set of leftmost occurrence positions of the k+1 factors.
  3. The right-special factor R_k (the unique length-k factor with both a 0
     and a 1 right-extension within f), and whether R_k is a prefix of some S_n.
  4. First-digit counts: how many of the k+1 factors start with 0 vs start
     with 1.

Exact integer arithmetic throughout; everything is finite over the finite
prefix of f.
"""

from brute import S


def fib_word(min_length):
    """The infinite Fibonacci word's prefix of length >= min_length as a str."""
    n = 0
    while True:
        w = S(n)
        if len(w) >= min_length:
            return w
        n += 1


def occurrence_data(word, k):
    """Return dict: factor -> list of starting positions (left to right)."""
    data = {}
    for i in range(len(word) - k + 1):
        factor = word[i:i + k]
        data.setdefault(factor, []).append(i)
    return data


def leftmost_set(data):
    """L(k) = sorted set of leftmost occurrence positions."""
    return sorted(v[0] for v in data.values())


def right_special(word, k, factors):
    """The unique factor of length k with both right-extensions 0 and 1.

    A length-k factor is right-special if it occurs at some start i with next
    letter 0 and at some start i' with next letter 1 (both within the prefix).
    """
    nxt = {}
    for i in range(len(word) - k):
        factor = word[i:i + k]
        nxt.setdefault(factor, set()).add(word[i + k])
        assert factor in factors, "right-special factor must be a length-k factor"
    rs = [f for f, exts in nxt.items() if exts == {'0', '1'}]
    return rs


def is_prefix_of_some_Sn(word_fragment):
    """True if the (exact) string is a prefix of some finite S_n."""
    n = 0
    while True:
        w = S(n)
        if len(w) >= len(word_fragment):
            return w[:len(word_fragment)] == word_fragment
        n += 1


def main():
    word = fib_word(20000)
    lines = []
    lines.append(f"Fibonacci word prefix length used: {len(word)}")
    lines.append("")

    first_digit_counts = {}
    L_sets = {}
    R_k = {}

    for k in range(1, 15):
        data = occurrence_data(word, k)
        factors_sorted = sorted(data)
        assert len(factors_sorted) == k + 1, f"k={k}: expected {k+1} factors, got {len(factors_sorted)}"

        lines.append(f"===== k = {k}  ({len(factors_sorted)} factors) =====")
        for f in factors_sorted:
            pos = data[f]
            shown = [str(p) for p in pos[:8]]
            tail = "..." if len(pos) > 8 else ""
            lines.append(f"  {f}  leftmost={pos[0]:3d}  positions={', '.join(shown)}{tail}")
        lines.append("")

        # L(k)
        L = leftmost_set(data)
        L_sets[k] = L
        lines.append(f"  L({k}) = {L}")
        lines.append("")

        # Right-special factor
        rs = right_special(word, k, factors_sorted)
        lines.append(f"  R_{k} = {rs}  (right-special factors: {rs})")
        for r in rs:
            lines.append(f"      R_{k} is prefix of some S_n: {is_prefix_of_some_Sn(r)}")
        lines.append("")

        # First-digit counts
        first_digit = {'0': 0, '1': 0}
        for f in factors_sorted:
            first_digit[f[0]] += 1
        first_digit_counts[k] = first_digit
        lines.append(f"  first-digit counts: start0={first_digit['0']}, start1={first_digit['1']}")
        lines.append("")
        lines.append("")

        if len(rs) > 1:
            lines.append(f"  NOTE: {len(rs)} right-special factors found (expected exactly 1)!")
            lines.append("")

    # Summary section
    lines.append("=" * 50)
    lines.append("SUMMARY")
    lines.append("")
    lines.append("L(k) sets:")
    for k in range(1, 15):
        lines.append(f"  k={k:2d}: {L_sets[k]}")
    lines.append("")
    lines.append("R_k strings:")
    for k in range(1, 15):
        rs = right_special(word, k, set(occurrence_data(word, k)))
        lines.append(f"  k={k:2d}: R={rs}")
    lines.append("")
    lines.append("first-digit counts (start0 : start1):")
    for k in range(1, 15):
        fd = first_digit_counts[k]
        lines.append(f"  k={k:2d}: 0-count={fd['0']}, 1-count={fd['1']}")

    out = "\n".join(lines)
    print(out)

    import os
    os.makedirs("code/out", exist_ok=True)
    with open("code/out/positions.txt", "w") as fh:
        fh.write(out + "\n")
    print()
    print("Wrote code/out/positions.txt")


if __name__ == "__main__":
    main()
