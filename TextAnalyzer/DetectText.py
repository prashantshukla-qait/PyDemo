import spacy
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
#
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)

class DetectText:

    def detectTextIn(self,Text):
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(u'This is a man')
        for ent in doc.ents:
            print(ent.text,ent.label_)

            if ent.label==u'PERSON':
                return "PERSON"
