import subprocess, time, sys

def probe(n, budget=25):
    cmd = ["nauty-geng", str(n), "-c", "-d4", "-k"]
    t0 = time.time()
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True, bufsize=1)
    except FileNotFoundError:
        print("NAUTY-GENG NOT FOUND on PATH")
        return
    c = 0
    try:
        for ln in proc.stdout:
            line = ln.rstrip("\n")
            if line and not line.startswith(">") and not line.startswith("#") and \
               all(63 <= ord(ch) <= 126 for ch in line):
                c += 1
                if time.time() - t0 > budget:
                    print(f"n={n}: counted {c} graphs in {time.time()-t0:.1f}s (TIMEOUT)")
                    proc.kill()
                    return
    finally:
        proc.kill()
        proc.wait()
    print(f"n={n}: completed {c} graphs in {time.time()-t0:.1f}s")

if __name__ == "__main__":
    probe(12)
