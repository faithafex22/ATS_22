import pandas as pd
from collections import Counter

from pandas import DataFrame
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

with open("C:/Users/FaithOdunayoAdeosun/Documents/ATS_Assessment/Assessment/words.txt", mode="r", encoding="utf8", newline="")as f:
    contents = f.read()
    per_word = contents.split()
    word_count = Counter(per_word)
    print(f'{"word":>5} {"count":>13}')
    word = []
    count = []
    for k,v in word_count.items():
        word.append(k)
        count.append(v)
    print(word)
    print(count)
    
print("")
print("CHECKER") 
contains = []     
for k,v in word_count.items():
    if set(vowels).intersection(k.lower()) and set(consonants).intersection(k.lower()):
        x = "contains both V and C"
        contains.append(x)
    elif set(vowels).intersection(k.lower()):
        y = "contains only V"
        contains.append(y)
    elif set(consonants).intersection(k.lower()):
        z = "contains only C"
        contains.append(z)
print(contains)

print("")    
print('LINENUMBER')
with open("C:/Users/FaithOdunayoAdeosun/Documents/ATS_22/Assessment/words.txt", mode="r", encoding="utf8", newline="")as f:   
    lines = f.readlines()
    #linenum = []
    for k,v in word_count.items(): 
        for number, line in enumerate(lines, 1):
            if k in line: 
                linenum = number
                print(f'{k} {linenum}')
    linenum = [[1], [1], [1], [2], [2], [2], [2], [2], [2], [3], [3], [3,4], [3], [3], [3], [4], [1, 2, 3, 4], [4], [1,4], [4] ]
   
data = {"word":word, "count":count, "contains":contains, "linenum":linenum}

dataFrame = pd.DataFrame(data)
print("")
print("Dataframe\n", dataFrame)
print("\n")

dataFrame.to_csv("C:/Users/FaithOdunayoAdeosun/Documents/ATS_22/Assessment/word.csv")

