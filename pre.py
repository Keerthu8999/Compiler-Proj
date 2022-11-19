import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
def pre_processing(inp):
	porter_stemmer = PorterStemmer()
	stop_words = set(stopwords.words('english'))
	wordnet_lemmatizer = WordNetLemmatizer()
	l = []
	nltk_tokens = nltk.word_tokenize(inp)
	l = [w for w in nltk_tokens if not w in stop_words]
	return l
