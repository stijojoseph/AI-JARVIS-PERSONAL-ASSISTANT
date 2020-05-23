#servorealtalk homeauto speech clue

import sys

#print(sys.path)
sys.path.append('/home/pi/.local/lib/python3.7/site-packages')
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
#import sys
#k1=[]
#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv[1:]))
#k1=sys.argv[1:]
#print(k)
#s1=""
#for t1 in k1:
 #   s1=s1+t1+" "
#print(s1)    

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
   if k== "is" or k== "your" or k=="who" or k=="fucking"or k=="time" :
    i+=1
    print(i)
   if k== "is" or k== "your" or k=="what" or k=="fucking" or k=="time":
     print(r)  
     r+=1
   if k=="weather" or k=="temperature" or k=="coldness" or k== "time":
      r=3
 if r > i:
      i=r
 print(i)     
 return i
def voice(x):
 import pyttsx3
 engine = pyttsx3.init()
 t1=word_tokenize(x)
 sp1=0
 for k1 in t1:
   sp1=sp1+1  
   print(k1)

 f=open("talk.txt","a+")
 f.write(str(sp1)+"\n")
 f.close() 
 
 # object creation
 sp=0
 t=word_tokenize(x)
 for k in t:
   sp=sp+1  
   print(k)  

 rate = engine.getProperty('rate')   # getting details of current speaking rate
 print (rate)                        #printing current voice rate
 engine.setProperty('rate', 110)     # setting up new voice rate



 volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
 print (volume)                          #printing current volume level
 engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1


 voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
 engine.setProperty('voice', voices[13].id)   #changing index, changes voices. 1 for female

 engine.say(x)
#engine.say("iam jarvis 2.0")
 engine.runAndWait()
 engine.stop()
 
def reads():  
 file2 = open("data1.txt","r+")  
 time.sleep(1)
 j=None 

  
 k=file2.readlines()
 for j in k:
    print(j)
 if j==None:
    print(j)
 file2. truncate(0)    
 file2.close()    
 return j
def bulbfan(k):
 import homeauto as h1   
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
         h1.fanh()
         y1="fan successfully turned on"
     else:
         y1="fan successfully turned off"
         h1.fanl()
 if p1==2:
     if s1==1:
         y1="light successfully turned on"
         h1.lighth()
     else:
         y1="light successfully turned off"
         h1.lightl()
 return y1
def timer():
    
 from datetime import datetime

 now = datetime.now()

 current_time = now.strftime("%H:%M")
 y="The current time is "+ current_time
 return y
import time
while True:
 #time.sleep(0.5)
 tezt=reads()
 print(tezt)
 if tezt!=None:
  u=rules(tezt)
  print(u)
  if u!=3:
   from chat.util import wiki   
   y=wiki(tezt)
   y=clean(y)
   print(y)
   if y!="none":
    voice(str(y))
  else:
     y="none"
  if y == "none":
   y,s,o=chatbot_response(tezt)
  # print("wikiy",y)
   if y=="":
     print("your name")
     from nlip2 import name
     y=name(tezt)
     y="nice to meet you "+y
   if y=="weather":
      from weather import name
      y=name(tezt)
   if y=="youtube":
      from utubewithpython import name
      y=name(tezt)  
   if y=="bulbfan":
      y=bulbfan(tezt)
   if y=="helmet":
       import teter as t5
       t5.tet()
       y="helmet closed"
   if y=="time":
       y=timer()
   if o < 0.68:
    print("browser getting activated")
   print("bot:",y)
   if y!="none":
    voice(y)
  u=0




    
    
    
    