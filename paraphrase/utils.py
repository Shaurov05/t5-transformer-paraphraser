import spacy
nlp = spacy.load('en_core_web_sm')

def split_into_sentences(text):
    sentences = []
    tokens = nlp(text)
    for sent in tokens.sents:
        sentence = sent.string.strip()
        sentences.append(sentence)
    return sentences