from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
import re
from termcolor import colored

sentences = """French defender William Saliba, 21, who has been on loan 
at Marseille from Arsenal has suggested he is keen to remain in France next season."""

token = word_tokenize(sentences)
sen1 = (pos_tag(token))  # Part of speech tagging
sen2 = (ne_chunk(sen1))  # Create named entity tree of tagged tokens
iob_tags =tree2conlltags(sen2)  # Get tag structure
tree =  conlltags2tree(iob_tags)

n = ["NN", "NNS", "NNP", "NNPS"]
v = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

print("POS: ")
for i in iob_tags:
    if i[1] in n :
        print(colored(i[0], 'red'), end=" ")
    elif i[1] in v:
        print(colored(i[0], 'green'), end=" ")
    else :
        print(colored(i[0], 'white'), end=" ")

print("\nNER: ")
for i in iob_tags:
    if (i[2] == "B-PERSON" or i[2] == "I-PERSON"):
        print(colored(i[0], 'yellow'), end=" ")
    elif (i[2] == "B-GPE"):
        print(colored(i[0], 'green'), end=" ")
    elif (i[2] == "B-ORGANIZATION"):
        print(colored(i[0], 'blue'), end=" ")
    else :
        print(colored(i[0], 'white'), end=" ")
