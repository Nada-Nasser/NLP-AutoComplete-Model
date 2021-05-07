from nltk.tokenize import RegexpTokenizer
import numpy as np

f = open("report_2.txt", "r", encoding="utf8")

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

    model[w1_w2] = sorted(model[w1_w2],reverse=True)


text = 'لا شك أن خدمات الاتصالات باتت'
tokens = tokenizer.tokenize(text)

accumulator = 1.0
for i in range(len(tokens) - 2):
    t = " ".join(tokens[i:i+2])
    print(tokens[i:i+2])
    prob = unsorted_model[t, tokens[i+2]]
    accumulator *= prob

t = " ".join(tokens[-2:])
if t in model:
    print(model[t][0][1])
    accumulator *= model[t][0][0]
else:
    print("")

print("Probability of text = ", accumulator)


