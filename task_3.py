from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer

sb = SnowballStemmer(language="english")
ps = PorterStemmer()

words = [input(" please input A word ")]
i = input("input your choise please from 1 to 4 :")

if i =="1":
    print(word_tokenize(words))
elif i =="2":
    print(sent_tokenize(words))
elif i=="3":
    print(words)
elif i=="4":
    for i in words:
        n=input("are you wont a porter stemer or snowballs stemer : ")
        if n == "porter" :
            print(i,":",ps.stem(i))
        else :
            print(i,":",sb.stem(i))
