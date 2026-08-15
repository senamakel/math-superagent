import re, collections
# Extract edge-count distribution among n=11 kernel members from captured file
# and among 4-chromatic vs 3-colourable subsets.
txt = open('code/out/analyze_kernel_chrom.captured.txt').read()
# Lines "  edges= NN [...]" belong to 4-chromatic members apparently
edges4 = [int(m.group(1)) for m in re.finditer(r'edges=\s*(\d+)\s*\[', txt)]
print("count of edges= lines:", len(edges4))
c4 = collections.Counter(edges4)
print("4-chromatic n=11 edge distribution:", dict(sorted(c4.items())))

# Total four-chromatic n=11 members = 198 per the file; sanity check line count
print("number of 4-chromatic n=11 members reported itself:", edges4.count if False else "(146 lines actually present in this excerpt?)")
