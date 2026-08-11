# Index — code/lib

What other programs import. One subject per module, so reading the part you
need costs almost nothing.

`/workspace/code` is on `PYTHONPATH`, so a module here is importable by name
from any working directory and any invocation:

```python
from lib.perms import lex_ranks
```

Never write `sys.path.insert`. If an import fails, the file is in the wrong
place and moving it is the fix.

| File | Purpose |
| --- | --- |

_No library modules yet._

## Adding one

A routine earns a place here when a second program would otherwise repeat it,
or when getting it right took real work — exact arithmetic, an off-by-one in a
recurrence, a verified base case. A single-use expression does not. The third
time you type a routine out, it belonged here the first time.

Write `code/lib/<subject>.py` holding the functions for one subject, each with
a docstring, each callable without reading its source: explicit arguments, one
job, no reliance on globals or on a file written earlier in the run. Check it
against a case whose answer is already known, then `describe_file` it. The
description carries each function's signature, what it returns, and what
established that it is correct — an unverified helper must say `unverified`, so
a later agent knows what it is standing on.

Keep a module small enough to read whole. A second subject is a second module.

Every helper uses exact integer or rational arithmetic unless its row says
otherwise. Say so explicitly when a function returns a float.
