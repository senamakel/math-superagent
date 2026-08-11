# Toolkit

Reusable helpers this run has built, in `toolkit.py`. Import them instead of
rewriting a routine that already exists:

```python
from toolkit import <name>
```

Keep this file in step with the code. An entry that no longer matches its
function is worse than no entry, because the next agent will call it as
described here rather than reading the source.

## How to add one

A helper earns a place here when a second script would otherwise repeat it, or
when getting it right took real work — exact arithmetic, an off-by-one in a
recurrence, a verified base case. A single-use expression does not.

Write the function in `toolkit.py` with a docstring, check it against a case
whose answer is already known, then add a row below.

## Functions

| Function | Signature | Returns | Verified against |
| --- | --- | --- | --- |
| _(none yet)_ | | | |

## Notes

- Every helper uses exact integer or rational arithmetic unless its row says
  otherwise. Say so explicitly when a function returns a float.
- "Verified against" records what actually established the function is right: a
  worked example from the statement, agreement with the brute-force oracle up
  to some size, or a known value. An unverified helper must say `unverified`,
  so a later agent knows what it is standing on.
