import sys
#print(sys.path)
sys.path.append('/home/pi/.local/lib/python3.7/site-packages')
def name(text):   
 q=None    
 #text=input("user:")
 i=0  
 import nltk
 from nltk.tokenize import PunktSentenceTokenizer,word_tokenize

 p=word_tokenize(text)


 k=nltk.pos_tag(p)  
 #print(k)  
 u=[]
 for j in k:
    for o in j:
        print(o)
        u.append(o)
# print(u)

 d=[]
 for n in u :
  i=i+1
  if (i%2)==1:  
     d.append(n)
  #   print(d)


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
 i=0    
 #print(dict) 
 for d in p:
    if i==1:
        i=2
    print(d)
    if d=="weather" or d=="temperature" or d=="cold" or d=="hot":
         i=1
    if i==2 and dict[d]=="NN":
        from googlemap import gomap
        q,w=gomap(d)
      #  print(q)
         
 if i==1:
   print("vijayawada")
   from googlemap import gomap
   q,w=gomap("vijayawada")        
 if q is not None:
    p="the current temperature of the place is"+str(q["temp_max"])+"the maximum temperature is"+str(q["temp_min"])+"and the humadity is"+str(w)         
 else:
     p=2
 return p



      