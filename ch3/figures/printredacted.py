import json
from pathlib import Path
from textwrap import fill

p = Path("myexample.json")
data = json.loads(p.read_text())
labels = [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0]

for i, (sent,label) in enumerate(zip(data['inputs'], labels)):
    if label:
        print(fill(f" ({i+1}) " + ' '.join(sent['tokens']), subsequent_indent="     "))
    #print(fill(f" ({i+1}) " + ' '.join(sent['tokens']), subsequent_indent="     "))
print()
exit()
classes = [
    ('nouns', set(["NOUN", "PROPN"])),
    ('adj/adv', set(["ADJ", "ADV"])),
    ('verb', set(["VERB", "PART", "AUX"])),
    ('func', set(["ADP", "CONJ", "CCONJ", "DET", "INTJ", "SCONJ"])),
]

for cname, tagset in classes:
    print("no " + cname)
    for i, sent in enumerate(data['inputs'][:10]):
        redacted = []
        for tok, tag in zip(sent['tokens'], sent['pos']):
            if tag in tagset:
                #redacted.append(u"\u25A0" * len(tok))
                redacted.append(u"\colorbox{black}{" + tok + "}" )
            else:
                redacted.append(tok)
        #print(fill(f"--item " + ' '.join(redacted), subsequent_indent="     "))
        print(f"\\item " + ' '.join(redacted))

