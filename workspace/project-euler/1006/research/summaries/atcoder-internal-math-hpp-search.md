# AtCoder internal_math.hpp — GitHub browser page (duplicate of the jsDelivr fetch)

<!-- source: https://github.com/atcoder/ac-library/blob/master/atcoder/internal_math.hpp | 2026-08-19 -->

## Verdict: duplicate, superseded by the jsDelivr fetch

The on-disk "full text" `research/sources/atcoder-internal-math-hpp-search.full.md` is the GitHub *browser page* of `atcoder/internal_math.hpp` at master. It carries the same 212-line header (safe_mod, barrett, pow_mod_constexpr, is_prime_constexpr, inv_gcd, primitive_root_constexpr, **floor_sum_unsigned**) as `research/sources/atcoder-internal-math-hpp.full.md`, which was fetched from the pinned jsDelivr mirror at tag v1.5.1.

Use the pinned v1.5.1 fetch, not the master-branch browser page: the pinned file has a stable version reference, while master can drift. The summary in `research/summaries/atcoder-internal-math-hpp.md` (floor_sum_unsigned = the O(log) Euclidean recursion behind atcoder::floor_sum; inv_gcd computes 10^{-1} mod 101001001; barrett = fast modular mul) applies unchanged to both.

## What it does NOT add

Nothing beyond the pinned fetch. No new statement for PE1006; the primitive anchor is already `governing-universal-euclidean` + `monoid-composition-formulas-verified`.
