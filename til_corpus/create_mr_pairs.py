import os
import pandas as pd
import editdistance

src = 'en'
tgt = 'tr'
data_path = f"data/{src}-{tgt}/train"


#source = open(f"{data_path}/{src}-{tgt}/{src}-{tgt}.{src}", "r")
#target = open(f"{data_path}/{src}-{tgt}/{src}-{tgt}.{tgt}", "r")

source = []
target = []
count = 0
with open(f"{data_path}/{src}-{tgt}/{src}-{tgt}.{src}") as infile:
    for line in infile:
        source.append(line)
        count += 1
        if count == 5_000_000:
            break
        
count = 0
with open(f"{data_path}/{src}-{tgt}/{src}-{tgt}.{tgt}") as infile:
    for line in infile:
        target.append(line)
        count += 1
        if count == 5_000_000:
            break

df = pd.DataFrame(zip(source, target), columns=['source_sentence', 'target_sentence'])



print(df.head())
print(len(df))

# df_dup = df.drop_duplicates()

df_dup_index = df.duplicated(subset='source_sentence', keep=False)

df_dup = df[df_dup_index]

df_dup = df_dup.sort_values("source_sentence")


count = 0

source_output = open(f"{src}-{tgt}.test.{src}", "w")
target_output = open(f"{src}-{tgt}.test.{tgt}", "w")

weird_symbols = ["&", "\\", "ent_", "[[", "%s","%"]

CYRILLIC_VOWELS = (
    'а', 'А', 'е', 'Е', 'ё', 'Ё', 'и', 'И', 'о', 'О', 'у', 'У', 'э', 'Э',
    'ю', 'Ю', 'я', 'Я', 'ў', 'Ў'
)

target_list = []

def add_target(target_list, sentence):
    sentence = sentence.replace("\n", "").replace("\t", "")

    for letter in sentence:
        if letter in CYRILLIC_VOWELS:
            return target_list
    for s in target_list:
        if editdistance.eval(s.lower(), sentence.lower()) < 3:
            return target_list
    
    target_list.append(sentence)
    return target_list
        
def is_weird(sentence):

    for symbol in weird_symbols:
        if symbol not in row["source_sentence"]:
            continue
        else:
            return True

    return False
    
last = None
for index, row in df_dup.iterrows():

    
    if is_weird(row["source_sentence"]):
        continue

    if row['source_sentence'] == last:
        target_list = add_target(target_list, row["target_sentence"])
        
    else:
        
        if len(target_list) > 1:
            count += 1
            source_output.write(last)
            target_output.write("\t".join(target_list) + "\n")

        target_list = []
        last = row['source_sentence']
        target_list = add_target(target_list, row['target_sentence'])
        






