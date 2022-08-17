import re
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

n=2
Sentence = """Cherry blossom represents the nature of life and a season of renewal 
in Japanese culture. Last year, the season attracted nearly five million people and boosted the
score of economy by about $2.7 billion, according to figures from Bloomberg."""


words = (re.sub('[^A-Za-z0-9\s]',' ',Sentence.lower()))
       
unigrams_1 = word_tokenize(words)

print("Unigram = ",unigrams_1)

unigrams_2 = list(ngrams(unigrams_1,n))

print("\nThe 2 -gram =",unigrams_2)







