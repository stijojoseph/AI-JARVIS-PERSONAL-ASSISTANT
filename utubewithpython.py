#!/usr/bin/python3
import sys
import time
#print(sys.path)
sys.path.append('/home/pi/.local/lib/python3.7/site-packages')
#print(sys.path)
import pafy
import vlc

from nltk.tokenize import PunktSentenceTokenizer,word_tokenize


import urllib.request
import urllib.parse
import re
print("enter some fuck")
def utube(k):
 
 query_string = urllib.parse.urlencode({"search_query" :k})
 html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
 search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
 print("http://www.youtube.com/watch?v=" + search_results[0])
 s="http://www.youtube.com/watch?v=" + search_results[0]

 url = s
 video = pafy.new(url)
 best = video.getbest()
 playurl = best.url
 media=vlc.MediaPlayer(best.url)
 media.play()

def name(text):    
 import nltk   
 r=None  
 #text=input("user:")
 i=0  
 
 p=word_tokenize(text)


 k=nltk.pos_tag(p)  
 print(k)  
 u=[]
 for j in k:
    for o in j:
        print(o)
        u.append(o)
 print(u)

 d=[]
 for n in u :
  i=i+1
  if (i%2)==1:  
     d.append(n)
     print(d)


#d.clear()
 dict={}
 i=0
 for n in u :
  i=i+1
  
  if (i%2)==0:  
      s=int(i/2)-1
      print(s)
      dict[d[s]]=n
      print(n)
 n=" "  
 e=0  
#print(dict)

#print(dict["PRP"])
 j=1000
 i=0
#d.clear()
 for s in p:
   
    if dict[s]=="NN" or dict[s]=="NNS" or dict[s]=="JJ": 
      n=n+s+" "

 print(n)
 utube(n)
#name("lucifer song utube")
 time.sleep(200)
#name("utube play the malayalam song from oppam movie")
#while True:
 #   print("hello")