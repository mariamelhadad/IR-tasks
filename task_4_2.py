import csv
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer


# opening the CSV file

with open('F:\college\sem2\IR\sec\code\populationbycountry.csv', mode ='r')as file:

    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)

#tokenization 
print(word_tokenize(lines))
print(sent_tokenize(csvFile))

# #stem
sb = SnowballStemmer(language="english")
ps = PorterStemmer()
for i in csvFile:
    print("the porter steming : ", i ,":", ps.stem(i))
    print("the snowballs steming : ", i ,":", sb.stem(i))

#removing stop words
for j in range(1):
    text_tokens = word_tokenize(csvFile)
file_without_sw = [word for word in text_tokens if not word in stopwords.words()]

print(file_without_sw)
