try:
    import nltk
except ImportError:
    print("NLTK is not installed. Please install NLTK using 'pip install nltk'.")

nltk.download('punkt')
from nltk.stem.porter import PorterStemmer


def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    pass


def bag_of_words(tokenized_sentence, all_words):
    pass