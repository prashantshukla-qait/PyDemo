import spacy

class DetectText:

    def detectTextIn(self,Text):
        classFromText=[]
        nlp = spacy.load('en_core_web_sm')
        uni_string=str(Text)
        doc = nlp(uni_string)
        print(len(doc.ents))
        for ent in doc.ents:
            print(ent.text, ent.start_char, ent.end_char, ent.label_)
            if ent.label_=='PERSON':
                return "person"
             

       

                


