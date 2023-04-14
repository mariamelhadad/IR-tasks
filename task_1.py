doc1 = "new home sales top forecasts"
doc2 = "home sales rise in july"
doc3 = "increase in home sales in july"
doc4 = "july new home sales rise"

doc = [doc1,doc2,doc3,doc4]

inverted_index = {}
for i, doc in enumerate(doc):
    for item in doc.split():
        if item in inverted_index:
            inverted_index[item].add(i)
        else: inverted_index[item] = {i}
inverted_index
print(inverted_index)

from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

for i in range(1):
    text_tokens = word_tokenize(doc)
tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

print(tokens_without_sw)
