import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

class EntityMatcher(object):
    name = "entity_matcher"

    def __init__(self, nlp, terms, label):
        patterns = [nlp.make_doc(text) for text in terms]
        self.matcher = PhraseMatcher(nlp.vocab)
        self.matcher.add(label, None, *patterns)

    def __call__(self, doc):
        matches = self.matcher(doc)
        for match_id, start, end in matches:
            span = Span(doc, start, end, label=match_id)
            doc.ents = list(doc.ents) + [span]
        return doc

nlp = spacy.load("en_core_web_sm")
terms = ("cat", "dog", "tree kangaroo", "giant sea spider","lion")
entity_matcher = EntityMatcher(nlp, terms, "ANIMAL")

nlp.add_pipe(entity_matcher, after="ner")

print(nlp.pipe_names)  # The components in the pipeline

doc = nlp("This is a text about Barack Obama and lion and a tree kangaroo")
print([(ent.text, ent.label_) for ent in doc.ents])