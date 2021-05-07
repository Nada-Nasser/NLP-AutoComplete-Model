from nltk.tokenize import RegexpTokenizer
import numpy as np

f = open("Combined.txt", "r", encoding="utf8")

tokenizer = RegexpTokenizer("[\w']+")
tokens = tokenizer.tokenize(f.read())

trigram_model = {}
n = 2

for i in range(len(tokens) - n):
    key = ' '.join(tokens[i:i + n])
    if key not in trigram_model.keys():
        trigram_model[key] = []
    trigram_model[key].append(tokens[i + n])

model = {}
unsorted_model = {}

for w1_w2 in trigram_model:
    unique_classes, counts_unique_classes = np.unique(trigram_model[w1_w2], return_counts=True)
    for i in range(len(unique_classes)):
        x = float(counts_unique_classes[i]) / (float(len(trigram_model[w1_w2])) * 1.0)
        unsorted_model[w1_w2, unique_classes[i]] = x
        if w1_w2 not in model:
            model[w1_w2] = []
        model[w1_w2].append([x, unique_classes[i]])

    model[w1_w2] = sorted(model[w1_w2], reverse=True)
