import spacy
nlp = spacy.load("en_core_web_lg")
with open("DELBOM-AI-INR.txt") as f:
    lines = nlp(f.read())
    
for token in lines:
    print(token.text, " ", token.ent_type_, token.pos_)