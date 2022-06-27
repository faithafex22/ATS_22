
import random

names = ["blessing", "hope", "john", "faith", "love", "peace", "joy", "convenant", "joshua","praise"]
verbs = ["eating", "dancing", "reading", "watching", "washing", "cooking", "sleeping", "talking", "sewing", "drinking"]
objects = ["food", "book", "drum", "television", "clothes","pot","bed", "thread",  "mouth", "cup"]

def gen(n:int):
    sentences = []
    for i in range (n):
        merge = f"{random.choice(names)} is {random.choice(verbs)}  {random.choice(objects)}"
        if merge not in sentences:
            sentences.append(merge)
            print(merge)
        else:
            print("no more unique sentences to generate")
            break;
    print(len(sentences))    
(gen(1000))