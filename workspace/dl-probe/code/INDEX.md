# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| report_downloads.py | Reports the outcome of three attempted download_document calls: prints the exact download error text and the byte size (via os.path.getsize) of the already-stored library summary file, or "MISSING". Correctness established by direct comparison against the three library summary files on disk (sizes 1947, 3266, 2489 bytes) and the task's stated error text. |
