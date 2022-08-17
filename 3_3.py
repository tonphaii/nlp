from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.metrics.distance import edit_distance

d = open('1-1000.txt','r')
dic = d.read()
dicts = word_tokenize(dic)
sentence = "I opan a bax ant reed a leter"
words = word_tokenize(sentence)
a = lambda v:v[0]
data=[]

for i in words: 
    check = [(edit_distance(i,word),word)
             for word in dicts 
                 if i[0] == word[0]
        ]
    for j in dicts:
        k = sorted(check, key = a)[0][1]
    data.append(k)
    print("%s can be replaced by ('%s', '%s')"%(i,k,(edit_distance(i,k,substitution_cost=2))))

print("Misspelled sentence is >> ",sentence)
print("New sentence is        >> " ,end=' ')
for i in data:
    print(i,end=' ')
    
    
    


