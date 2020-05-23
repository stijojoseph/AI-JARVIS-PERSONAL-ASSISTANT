import sys
#print(sys.path)
sys.path.append('/home/pi/.local/lib/python3.7/site-packages')
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model
model = load_model('chatbot_model4.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
from nlip2 import name

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

while True:
 tezt=input("user:")
 k,s,o=chatbot_response(tezt)
 if k=="":
     print("your name")
     k=name(tezt)
     k="nice to meet you "+k
 if o < 0.68:
     print("browser getting activated")
 print("bot:",k)
 if s==1:
     break








