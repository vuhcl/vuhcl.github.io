import glob

txt = '# Replays\n\n'

for i, file in enumerate(glob.glob("G*.md"), start=1):
    ln = f"+ [Replay {i}]({file})\n"
    txt += ln

print(txt)
md_file = 'index.md'
with open(md_file, 'w') as f:
    f.write(txt)
