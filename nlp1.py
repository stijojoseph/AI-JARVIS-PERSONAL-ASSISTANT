import spacy
nlp=spacy.load("en_core_web_sm")
doc1=nlp("dogs best friend")
doc2=nlp(" dogs best friend")
t=doc1.similarity(doc2)
print(t*100,'%')