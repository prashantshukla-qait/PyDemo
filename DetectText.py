from textblob import TextBlob

class DetectText:

    def detectText(self,Text):
        text = TextBlob(Text)
        nouns=text.noun_phrases
        print(nouns)
        
