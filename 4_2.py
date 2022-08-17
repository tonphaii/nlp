import re
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
import operator


n = 2
data = []
words = []
l_prob = {}
l1 = {}
l2 = {}

test_sentence = "I love X"
sentences =  ["I love you!","I love mom.","I love you so much","I love dog.",
              "I love mom so much","John love you so bad."]

for i in sentences:
    s = (re.sub('[^A-Za-z0-9\s]',' ',i))
    words.append(word_tokenize(s))


for w in words:
    for i in w:
        data.append(i)
        
find = BigramCollocationFinder.from_words(data)
finder = find.ngram_fd.most_common()

for w in finder :
    l_prob[w[0]] = operator.truediv(w[1], len(sentences))
    
test = word_tokenize(test_sentence)    

for w in words:
    if len(w) == len(test):
        bigram = list(ngrams(w, n))
        l1[bigram[1]] = l_prob[bigram[1]]
        l2[l_prob[bigram[1]]] = w[n]
        
print("bigram prob: " ,l1)
print(test_sentence+" : X should be '%s'")

