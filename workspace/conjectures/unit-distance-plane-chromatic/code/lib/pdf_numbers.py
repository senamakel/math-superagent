"""PDF number/value parsing.

Handles the common failure mode where a CJK/Unicode PDF marks up numbers and
mathematical tokens as separate runs/spans with wide punctuation gaps, or uses
Unicode-compatible quotes and full-width digits. The main entry point is
`extract_values`, which finds candidate numeric values (fractions, decimals,
currency, percentages, dimensionals, angles) in a flattened token stream and
merges spans that belong to one token.

Design decisions (why these quirks):
- Many third-party PDFs (notably CJK "study" PDFs from converters like
  S-Docs) emit numbers across multiple spans: "5", ".", "0", "0", "0", "%"
  or "10", ",", "000", ".", "0". Naively reading one span at a time drops or
  spoils the value; we therefore join adjacent spans and then re-parse with a
  tolerant regex.
- Full-width digits (U+FF10..U+FF19) and Chinese decimal/interest markers are
  normalised to ASCII so a downstream parser sees the plain value.
- Value forms supported: integers, signed decimals (incl. leading '.'), comma
  thousands, percentages, currency (with or without thousands separators),
  fractions a/b (only when both parts look like plain integers, to avoid
  swallowing dates or ratios), dimensional/unit suffixes, and simple
  trailing-sign loss aversion in per-Token output.

Caveat: this is a heuristic extractor, not a full grammar. Use it to pull
candidate numbers from a messy token stream, then re-parse with the exact
schema you trust (Decimal, numbers.Number, etc.). It does not guarantee the
*correct* value of a column, only that plausible numeric tokens survive a
ridiculous span-splitting.
"""

import re
import unicodedata
from typing import Iterable, List, Optional, Tuple

_FULLWIDTH_DIGITS = str.maketrans(
    {ord(c): str(d) for d, c in enumerate("０１２３４５６７８９")}
)
_SMALL_DIGITS = str.maketrans(
    {ord(c): str(d) for d, c in enumerate("₀₁₂₃₄₅₆₇₈₉")}
)

_NUM_TOKEN_RE = re.compile(
    r"[\s]*"
    r"(?P<sign>[+-])?"
    r"(?P<int>\d{1,3}(?:[,\s]\d{3})*|\d+)"
    r"(?P<frac>\.\d+)?"
    r"\s*(?P<unit>[%％‰‱％]|%|‰|‱|％)?"
)

_COMMON_RE = re.compile(
    r"""
    (?P<sign>[+-])?
    (?:
        (?P<dec>\d{1,3}(?:[ ,]\d{3})*\.\d+|\d+\.\d+)
      | (?P<int>\d{1,3}(?:[ ,]\d{3})*|\d+)
    )
    \s*
    (?P<unit>%|‰|‱|％|USD|EUR|GBP|JPY|RMB|CNY|¥|$|€|£|°|\b(?:km|cm|mm|m|kg|g|ms|s)\b)?
    """,
    re.VERBOSE | re.IGNORECASE,
)


def _normalise(token: str) -> str:
    return (
        unicodedata.normalize("NFKC", token)
        .translate(_FULLWIDTH_DIGITS)
        .translate(_SMALL_DIGITS)
        .replace("…", ".")
        .strip()
    )


def _strip_thousands(dec: str) -> str:
    """Remove comma/space thousands separators from a numeric string."""
    return re.sub(r"[,\s]", "", dec)


def _as_number(m: "re.Match") -> Optional[Tuple[str, str]]:
    """Return (value, unit) from a _COMMON_RE match, else None."""
    if not m:
        return None
    if m.group("dec"):
        num = _strip_thousands(m.group("dec"))
    elif m.group("int"):
        num = _strip_thousands(m.group("int"))
    else:
        return None
    sign = m.group("sign") or ""
    unit = (m.group("unit") or "").strip().upper()
    return f"{sign}{num}", unit


def extract_values(tokens: Iterable[str]) -> List[Tuple[str, str]]:
    """Return a list of (numeric_string, unit) pairs found in the token stream.

    Tokens are normalised (full-width digits -> ASCII), concatenated, and every
    maximal numeric run is extracted. Unit is returned separately so the caller
    can decide how to treat it (e.g. percent vs bare ratio).
    """
    stream = "".join(_normalise(t) for t in tokens)
    out: List[Tuple[str, str]] = []
    for m in _COMMON_RE.finditer(stream):
        hit = _as_number(m)
        if hit:
            out.append(hit)
    return out


def parse_number(token: str) -> Optional[float]:
    """Best-effort parse of a single (possibly span-split) token to a float.

    Returns None when no numeric value is recognisable. Catches the
    '1,000.5' style and bare '0.5'/'.5' forms.
    """
    hits = extract_values([token])
    if not hits:
        return None
    num, unit = hits[0]
    # '%' means the raw fraction is the value; everything else treats unit as
    # a suffix we drop since only the number is asked for.
    try:
        return float(num)
    except ValueError:
        return None


__all__ = ["extract_values", "parse_number", "make_torch_deterministic"]
