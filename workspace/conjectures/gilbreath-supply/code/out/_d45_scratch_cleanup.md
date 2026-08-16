# Scratch cleanup note — directive-45 librarian scaffolding

The three wrapper files `code/out/_SHOOT.md`, `code/out/_run_d45.py`,
`code/out/_invoke_d45.py` were librarian scaffolding for wrapping the capture
CLI. I (librarian) do not hold an execution tool, so they were never the
execution path — coder runs the discrimination via the canonical
`python3 -m lib.capture --target code/out/librarian_directive45_capture.txt -- \
python3 code/out/librarian_directive45_discriminate.py`.

They are recorded as obsolete in `code/out/INDEX.md` and left only to document
that the scaffolding was dead, not part of the computation. If any file needs
to go, these three and the unwritten capture target are the candidates.
