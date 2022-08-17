
from  spellchecker import Spellchecker

from tokenize import String
from nltk.tokenize import word_tokenize,sent_tokenize
from  nltk.probability import FreqDist
from nltk.corpus import stopwords
import re
import  nltk

data=[]
fdist_sen = FreqDist()
fdist_word = FreqDist()

with open('Will_Smith.txt','r') as f:
    file = f.read()

word = word_tokenize(file)
sentence = sent_tokenize(file)


for s in sentence:
    fdist_sen[s] +=1

for w in word:
    if(re.search('^[a-zA-Z]{3,}',w)):
        data.append(w)
        fdist_word[w] += 1

mylist = list(dict.fromkeys(data))
print("The number of sentences: ",fdist_sen.N())
#print(sorted(mylist))

fdist_word = FreqDist(data)
count =fdist_word.most_common()
for i in count:
    print(i,end='\n')



spell = Spellchecker()


spell.word_frequency.load_text_file('1-1000.txt')

with open('1-1000.txt','r') as ch:
    check_word = ch.read()

with open('data.txt','r') as f:
    file = f.read()
