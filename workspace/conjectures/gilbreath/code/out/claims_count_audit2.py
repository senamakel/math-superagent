import re, json

# Reuse the block-finder from the first script inline
import glob, os, collections

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
            for m in re.finditer(r'```(?:claim|txt|markdown)?\s*\n(.*?)```', text, re.S):
                body = m.group(1)
                im = re.search(r'^\s*id:\s*(\S+)', body, re.M)
                if im:
                    blocks.append((im.group(1), path, body))
    return blocks

blocks = find_claim_blocks(['research/**/*.md','code/out/**/*.md','research/*.md','code/**/*.md'])
# unique first-occurrence
seen = {}
for cid, path, body in blocks:
    if cid not in seen:
        seen[cid] = (path, body)

rendered = set(re.findall(r'^\| `([^`]+)`', open('research/CLAIMS.md',encoding='utf-8').read(), re.M))

# Also ids that appear ANYWHERE in the rendered file (incl contradiction/loadbearing sections)
allrendered_text = open('research/CLAIMS.md',encoding='utf-8').read()
rendered_anywhere = set(re.findall(r'`([a-z0-9][a-z0-9-]+)`', allrendered_text))

on_disk = set(seen.keys())
not_rendered_table = sorted(on_disk - rendered)
print(f"Unique claim ids on disk: {len(on_disk)}")
print(f"Rendered as table row: {len(rendered)}")
print(f"On disk but NOT a rendered table row: {len(not_rendered_table)}")
print(f"Of those, appearing anywhere in rendered file (contradiction/loadbearing sections): {len(set(not_rendered_table) & rendered_anywhere)}")
not_anywhere = sorted(set(not_rendered_table) - rendered_anywhere)
print(f"On disk and NOT mentioned anywhere in rendered CLAIMS.md: {len(not_anywhere)}")
print("\nIds on disk but with NO mention at all in rendered file (potentially 'dropped' from view):")
for cid in not_anywhere:
    st = re.search(r'status:\s*(\S+)', seen[cid][1])
    print(f"   {cid}  [{st.group(1) if st else '?'}]")
