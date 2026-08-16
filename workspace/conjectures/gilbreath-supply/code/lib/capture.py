#!/usr/bin/env python3
"""Atomic capture runner — the fix for Directive 23 (zero-byte capture).

Problem: a `> file` redirection opens (truncates) the output file *before* the
producing command runs, so if the command fails the target is left as an empty
or partial file that reads as a pass. This module runs a command, sends its
stdout+stderr to a temp file, and only atomically `os.replace`s the temp onto
the final target when the exit code is 0. On any nonzero exit or timeout it
deletes the temp file and leaves any previous capture at the target untouched,
so a failed run can never masquerade as a successful one.

Usage as a library:
    from lib.capture import capture_command
    rc, report = capture_command(["python3", "code/.../x.py"],
                                 target="code/out/x.captured.txt")

Usage as a CLI (the canonical way to run + capture a program):
    python3 -m lib.capture --target code/out/x.captured.txt -- python3 code/.../x.py

Returns (exit_code, report_dict). report_dict carries
    {"target", "written": bool, "time_s": float, "returncode": int,
     "output": str, "note": str}
The file content written to target is the command's stdout+stderr, and the
human note is also echoed to OUR stdout so the calling shell sees the exit
status explicitly.

Exact arithmetic / strings only; no floats in the decision path.
"""

import os
import subprocess
import sys
import time


def capture_command(cmd, target, timeout=None):
    """Run `cmd` redirecting stdout+stderr to a temp file; atomically promote
    it to `target` only if the exit code is 0. Return (returncode, report).

    On nonzero exit or timeout the temp file is deleted and any pre-existing
    `target` is left intact (never truncated, never replaced).
    """
    target = os.path.abspath(target)
    tmp = f"{target}.tmp.{os.getpid()}"
    report = {
        "target": target,
        "written": False,
        "time_s": None,
        "returncode": None,
        "output": "",
        "note": "",
    }
    start = time.monotonic()
    try:
        with open(tmp, "wb") as tf:
            proc = subprocess.run(cmd, stdout=tf, stderr=tf, timeout=timeout)
        elapsed = time.monotonic() - start
        report["time_s"] = elapsed
        report["returncode"] = proc.returncode
        with open(tmp, "rb") as tf:
            report["output"] = tf.read().decode("utf-8", errors="replace")
        if proc.returncode == 0:
            os.replace(tmp, target)          # atomic; leaves old target intact on failure
            report["written"] = True
            report["note"] = (f"OK  exit=0  {elapsed:.2f}s  -> {target}")
        else:
            os.unlink(tmp)
            report["note"] = (f"FAIL exited={proc.returncode}  {elapsed:.2f}s  "
                              f"temp discarded; previous {target} left intact")
    except subprocess.TimeoutExpired as exc:
        elapsed = time.monotonic() - start
        report["time_s"] = elapsed
        report["returncode"] = "TIMEOUT"
        report["output"] = (exc.stdout or b"").decode("utf-8", errors="replace")
        if os.path.exists(tmp):
            os.unlink(tmp)
        report["note"] = (f"TIMEOUT (>{timeout}s)  temp discarded; "
                          f"previous {target} left intact")
    except Exception as exc:  # noqa: BLE001 — report, do not lose the status
        elapsed = time.monotonic() - start
        report["time_s"] = elapsed
        report["returncode"] = "ERROR"
        report["note"] = f"ERROR running {cmd!r}: {exc!r}"
        if os.path.exists(tmp):
            try:
                os.unlink(tmp)
            except OSError:
                pass
    return report["returncode"], report


def _main(argv):
    """CLI: python3 -m lib.capture --target FILE [--timeout S] -- CMD..."""
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 1
    target = None
    timeout = None
    rest = list(argv)
    if "--target" in rest:
        i = rest.index("--target")
        target = rest[i + 1]
        del rest[i:i + 2]
    if "--timeout" in rest:
        i = rest.index("--timeout")
        timeout = float(rest[i + 1])
        del rest[i:i + 2]
    # optional explicit `--` separator before the command
    if rest and rest[0] == "--":
        rest = rest[1:]
    if not target or not rest:
        print("usage: python3 -m lib.capture --target FILE [--timeout S] -- CMD...",
              file=sys.stderr)
        return 2
    rc, rep = capture_command(rest, target, timeout=timeout)
    print(rep["note"], file=sys.stderr)
    sys.stderr.write(rep["output"] if not rep["output"].endswith("\n") else rep["output"])
    # exit status of this runner mirrors the captured command's, so callers
    # chained on `&&` behave correctly.
    return 0 if rep["returncode"] == 0 else 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
