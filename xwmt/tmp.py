import os

pairs = os.listdir("test")
pairs.sort()

for pair in pairs:
    src = pair.split("-")[0]
    tgt = pair.split("-")[1]
    print(f"\t{pair}:\n\t- 100<n<1K")