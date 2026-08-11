# Index — toolkits

One file per function, so reading the one you need costs almost nothing.

Import with `from toolkits.<file> import <function>`. Scripts run with
`/workspace` as their working directory, so this resolves without any path
setup.

| File | Purpose |
| --- | --- |

_No toolkit functions yet._

## Adding one

A helper earns a file here when a second script would otherwise repeat it, or
when getting it right took real work — exact arithmetic, an off-by-one in a
recurrence, a verified base case. A single-use expression does not.

Write `toolkits/<name>.py` holding **one** function with a docstring, check it
against a case whose answer is already known, then `describe_file` it. The
description carries the signature, what it returns, and what established that
it is correct — an unverified helper must say `unverified`, so a later agent
knows what it is standing on.

Every helper uses exact integer or rational arithmetic unless its row says
otherwise. Say so explicitly when a function returns a float.
