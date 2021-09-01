import os


src = "en"
tgt = "uz"

source_path = f"{src}-{tgt}.test.{src}"
target_path = f"{src}-{tgt}.test.{tgt}"


source = open(source_path, "r").readlines()
targets = open(target_path, "r").readlines()


map = {}
for index, entry in enumerate(targets):
    map[index] = len(entry.split("\t")[0])

map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))


source_out = open(f"{src}-{tgt}.5k.{src}", "w")
target_out = open(f"{src}-{tgt}.5k.{tgt}", "w")


count = 0
i = 0
for key, value in map.items():
    i += 1

    if i > 2500 and i < 5000:
        continue
    # if i > 1000 and i < 2000:
    #     continue
    
    # if i > 11000 and i < 20000:
    #     continue
    
    # if i > 21000 and i < 30000:
    #     continue
    
    # if i > 31000 and i < 40000:
    #     continue
    
    # if i > 41000 and i < 50000:
    #     continue

    
    source_out.write(source[key])
    target_out.write(targets[key])
    count += 1
     
    if count == 5000:
        break

    




