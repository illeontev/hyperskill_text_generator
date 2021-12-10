from nltk.tokenize import regexp_tokenize
from collections import Counter
import random

filename = input()

with open(filename, "r", encoding="utf-8") as fin:

    text = fin.read()

    tokens = regexp_tokenize(text, "[^\s]+")

    trigrams = []
    for i in range(len(tokens) - 2):
        trigrams.append({"head": tokens[i] + " " + tokens[i + 1], "tail": tokens[i + 2]})

    model = {}
    for trigram in trigrams:
        model.setdefault(trigram["head"], []).append(trigram["tail"])

    for i in range(10):
        while True:
            random_trigram = random.choice(trigrams)
            head = random_trigram["head"]
            if head[0].isupper() and head.split()[0][-1] not in ['.', '!', '?']:
                break

        key = head
        chain = key.split()
        len_of_chain = 2

        while True:
            tail = model[key]
            if tail:
                index = 0
                key = chain[-1] + " " + tail[index]
                while key in chain and index < len(tail):
                    key = chain[-1] + " " + tail[index]
                    index += 1

                chain.append(key.split()[-1])
                len_of_chain += 1

                if len_of_chain >= 5:
                    if key[-1] in ['.', '!', '?']:
                        break
            else:
                break
        print(*chain)