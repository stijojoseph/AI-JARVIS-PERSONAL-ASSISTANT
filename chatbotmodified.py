
import nltk
#from chat.utils import delete
from nltk.tokenize import PunktSentenceTokenizer,word_tokenize

from chat.util import Chat,reflections
#r="hello would you like to come for a coffee"
#cst=PunktSentenceTokenizer(r)
#k=word_tokenize(r)
#p=nltk.pos_tag(k)
#print(p,"\n")

#for s in p:
#    print(s[0],"-",s[1])


pair=[['iam (.*)',[' hi %1']],
['my name is (.*)',[' hai %1']],['hi bro|hai|',['hai manhh']]

]
#delete()

chat=Chat(pair,reflections)

chat.converse()