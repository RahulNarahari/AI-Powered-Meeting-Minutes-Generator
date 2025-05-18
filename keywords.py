from keybert import KeyBERT

def extract_keywords(text, top_n=10):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text, top_n=top_n)
    return [kw[0] for kw in keywords]