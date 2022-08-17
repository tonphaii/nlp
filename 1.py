from nltk.tokenize import word_tokenize
import re
from nltk.corpus import gutenberg, nps_chat
import nltk


moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
data = []

for w in moby:
    if(re.search('\w+ess$',w)):
        data.append(w)
mylist = list(dict.fromkeys(data))
print(sorted(mylist))



