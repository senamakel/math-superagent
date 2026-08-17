"""Extract exact Psi(k) values from psi_data_1_150.txt."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
def main():
    path = os.path.join(HERE, "psi_data_1_150.txt")
    vals = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("-") or line.startswith("Psi") or line.startswith(" k") or line.startswith("#") or line.startswith("each") or line.startswith("Computed"):
                continue
            # format: " 10 : True : ... 4085011557551094804" -> last token is Psi
            if " : " not in line:
                continue
            parts = line.split(" : ")
            if len(parts) < 4:
                continue
            k = int(parts[0].strip())
            psi = int(parts[-1].strip())
            vals.append((k, psi))
    for k, p in vals:
        print(p)
    import sys
    sys.stderr.write("count=%d\n" % len(vals))
if __name__ == "__main__":
    main()
