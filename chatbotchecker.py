import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model
model = load_model('chatbot_model5.h5')
import json
import random
from nltk.tokenize import PunktSentenceTokenizer,word_tokenize
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
#from chat.util import wiki
#from ap.api 


def clean(h):
 s=""
 p=['/', ',' ,'.','?','[',']','(',')']
 for t in h:
    if t not in p: 
     s+=t
 h=s
 return h   
 


def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words
# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words) 
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))
def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    
    m=[]
    k=0
    for j in res:
       # print(j)
        m.append({'intent':k,'prob':j})
        k=k+1
    o=0
    for j in m:
       print(j['intent'],j['prob'])
       if j['prob'] > o :
           o=j['prob']
           l=j['intent']
    print(o,l)
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    
    return_list.append({"intent": classes[l], "probability": str(o)})
    return return_list,o

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result
def chatbot_response(text):
    ints,o= predict_class(text, model)
    i=0
    for j in ints:
        if j['intent'] =="goodbye":
            i=1
    
    res = getResponse(ints, intents)
    
    
    return res,i,o
def bulbfan(k):
 p1=0
 s1=0
 y1="none"
 t1=word_tokenize(k)
 for sk in t1:
  print(sk)   
  if sk=="fan":
   p1=1   
   print(sk)  
  if sk=="lights" or sk=="light" or sk=="bulb":
      print(sk)
      p1=2
  if sk=="on":
      s1=1
  if sk=="off" or sk=="of":
      s1=2
 if p1==1:
     if s1==1:
         y1="fan successfully turned on"
     else:
         y1="fan successfully turned off"
 if p1==2:
     if s1==1:
         y1="light successfully turned on"
     else:
         y1="light successfully turned off" 
 return y1
 
from keras.models import load_model

#tezt="are you hungry now"
#k=clean_up_sentence(tezt)
#print(k)
#s=bow(tezt,k)
#print(s)
#p=predict_class(tezt, model)
#print(p)

def rules(t):
 i=0
 r=0

 t=word_tokenize(t)
 for k in t:
   print(k)  
   if k== "is" or k== "your" or k=="who" or k=="fucking" :
    i+=1
    print(i)
   if k== "is" or k== "your" or k=="what" or k=="fucking" :
     print(r)  
     r+=1
   if k=="weather" or k=="temperature" or k=="coldness":
      r=3
 if r > i:
      i=r
 print(i)     
 return i




while True:
 tezt=input("user:")
 u=rules(tezt)
 print(u)
 if u!=3:
  from chat.util import wiki   
  y=wiki(tezt)
  y=clean(y)
  print(y)
 else:
     y="none"
 if y == "none":
  y,s,o=chatbot_response(tezt)
  if y=="":
     print("your name")
     from nlip2 import name
     y=name(tezt)
     y="nice to meet you "+y
  if y=="weather":
      from weather import name
      y=name(tezt)
  if y=="bulbfan":
      y=bulbfan(tezt)
      
  if o < 0.68:
   print("browser getting activated")
  print("bot:",y)
  u=0
  if s==1:
     break
