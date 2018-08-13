import spacy 

class DetectText:

    def detectTextIn(self,Text):
        classFromText=[]
        nlp = spacy.load('en_core_web_sm')
        uni_string=str(Text)
        doc = nlp(uni_string)

        for ent in doc.ents:
            # print(ent.text, ent.start_char, ent.end_char, ent.label_)
            classFromText.append(ent.label_)

        for token in doc:
            # """token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            #       token.shape_, token.is_alpha, token.is_stop"""
                if not token.is_stop or not token.txt=="picture" or not token.txt=="pics" or not token.txt=="potrait":
                    # print(token.text,token.lemma_)
                    classFromText.append(token.lemma_)
                    classFromText.append(token.text)

        classFromText=[a.lower() for a in classFromText]
        classFromText=set(classFromText)
        return classFromText
             

       

                


