from nltk.tokenize import word_tokenize
import re
from nltk.corpus import gutenberg, nps_chat
import nltk


moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
data = []

data1=[]
'''
for w in moby:
    if(re.search('\w+ess$',w)):
        data.append(w)
mylist = list(dict.fromkeys(data))
print(mylist)'''

'''
data1=[]

for w in moby:
    if(re.search('\w+(pen|men)\w*',w)):
         data.append(w)
    if(re.search('\w+(pen|men)\w+',w)):
         data1.append(w)
    
mylist = list(dict.fromkeys(data))



mylist1 = list(dict.fromkeys(data1))
#print(mylist)
print("\n")
print("Len ListDATA ",len(mylist))
print("\n")
print("Len ListDATA1 ",len(mylist1))
l=[]
for i in data: 
    if (i not in data1):
        l.append(i)
mylist2 = list(dict.fromkeys(l))
print(mylist2)
print("Len ListDATA2 ",len(mylist2))
'''

'''
for w in moby:
    if(re.search('^(un|pre)\w+',w)):
         data.append(w)
mylist = list(dict.fromkeys(data))
print(mylist)
'''



for w in moby:
    if(re.search('\d{2}$',w)):
         data.append(w)
mylist = list(dict.fromkeys(data))
print(mylist)






        
    
    




