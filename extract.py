import spacy

nlp = spacy.load("en_core_web_sm")

def extract_action_items(text):
    doc = nlp(text)
    actions = []
    for sent in doc.sents:
        if any(token.pos_ == "VERB" and token.dep_ == "ROOT" for token in sent):
            actions.append(sent.text)
    return actions
