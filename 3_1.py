
import nltk

str1 = input("Str1 : ")
str2 = input("Str2 : ")
distance = (nltk.edit_distance(str1,str2,substitution_cost=2))

print("The edit distance of %s and %s is %s"%(str1,str2,distance))

