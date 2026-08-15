import re, glob, os, collections

# Count fenced 'claim' blocks across research/ and code/out/
def find_claim_blocks(root_globs):
    blocks = []
    for pat in root_globs:
        for path in glob.glob(pat, recursive=True):
            if os.path.basename(path).endswith('.full.md'):
                continue
            try:
                text = open(path, encoding='utf-8').read()
            except Exception:
                continue
            # fenced blocks containing claim *
            for m in re.finditer(r'```(?:claim|txt|markdown)?\s*\n(.*?)```', text, re.S):
                body = m.group(1)
                im = re.search(r'^\s*id:\s*(\S+)', body, re.M)
                if im:
                    blocks.append((im.group(1), path))
    return blocks

blocks = find_claim_blocks(['research/**/*.md', 'code/out/**/*.md', 'research/*.md', 'code/**/*.md'])
ids = collections.Counter()
byfile = collections.defaultdict(list)
for cid, path in blocks:
    ids[cid] += 1
    byfile[path].append(cid)

print(f"TOTAL claim blocks found on disk: {len(blocks)}")
print(f"UNIQUE claim ids: {len(ids)}")
dups = {k:v for k,v in ids.items() if v>1}
print(f"ids with DUPLICATE blocks: {len(dups)}")
for k,v in sorted(dups.items()):
    print("   DUP", k, v)

# Check the three ids named in the audit
check = ['g-supply-transfer','regeneration-thread-blocked-by','rule90-periodic-window-collapse','g-supply-transfer-universal-refuted','dyadic-collapse-proved','g-supply-switch-count-not-one-point','nu2w-minima-reconciled','thue-morse-sublinear-supply-witness']
print("\nTarget id presence on disk:")
for cid in check:
    print(f"  {cid}: {ids.get(cid,0)} block(s)")

# files containing claim blocks, grouped
print("\nFiles with claim blocks (count):")
for path, lst in sorted(byfile.items()):
    print(f"  {path}: {len(lst)}")

print("\n=== RENDERED FILE ANALYSIS ===")
try:
    text = open('research/CLAIMS.md', encoding='utf-8').read()
except Exception as e:
    print("err", e)
    text = ""
# data rows
data_rows = [l for l in text.splitlines() if l.startswith('| `') or (l.startswith('| ') and not l.startswith('| ---') and 'Statement' not in l and 'Holds' not in l)]
print(f"Rendered data rows in CLAIMS.md: {len([l for l in text.splitlines() if l.startswith('| `')])}")
import re as _re
# count lines that are table data rows: | `id` | ...
rows = _re.findall(r'^\| `([^`]+)`', text, _re.M)
print(f"Rendered claim rows (| `id` |): {len(rows)}")
print("First 5 rendered:", rows[:5])
print("Last 5 rendered:", rows[-5:])
