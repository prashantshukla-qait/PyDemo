from textblob import Word 
from textblob.wordnet import Synset

def compare(text,classlist):
      
      classlist=[x.lower() for x in classlist]
      if text is None:
          return False
      text=text.lower()
      #rule 1
      if text in classlist:
          return True
      #rule 2    
      word = Word(text)
      s1 = word.synsets[1] 
      s1text=s1.hypernyms()
      
      for a in s1text: 
        texta=a._name[:-5]
        if texta in classlist:
            return True
      #rule 3
      s2text=s1.hyponyms()
      for a in s2text: 
        texta=a._name[:-5]
        if texta in classlist:
            return True
      return False

