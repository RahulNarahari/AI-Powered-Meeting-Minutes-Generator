import nltk
from nltk.tokenize import sent_tokenize
import re

nltk.download('punkt')

def clean_text(text):
    text = re.sub(r'\s+', ' ', text.strip())
    sentences = sent_tokenize(text)
    return sentences
