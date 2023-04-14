from nltk.tokenize import word_tokenize
text = " NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all NLTK is a free, open source, community-driven project."
print(word_tokenize(text))

from nltk.tokenize import sent_tokenize
text2=" NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project."
print(sent_tokenize(text2))

#___________

import pandas as pd
data = pd.read_csv("Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv")
data.head(5)