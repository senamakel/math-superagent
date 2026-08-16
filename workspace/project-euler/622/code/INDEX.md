# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive out-faro shuffle oracle: models deck as a list, applies one out-faro shuffle at a time, counts shuffles to restore identity. Independent direct-iteration check of the ord_{n-1}(2) formula. Reproduced the statement's worked examples: s(52)=8, s(86)=8, sum of even n<500 with s(n)=8 is 412 (=18+52+86+256). Verified by running `python code/brute.py`. |
