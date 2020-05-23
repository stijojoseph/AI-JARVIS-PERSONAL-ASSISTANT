import re

#text="ya i forgot to introduce myself"
#p=""

#k=len(text)
#for y in text:
  #  i=i+1
 #   print(y,i)

#m=""

#t=re.findall(r'',text)
#for x in t:
 #   print(x)
def name(text):    
 import nltk     
 #text=input("user:")
 i=0  
 from nltk.tokenize import PunktSentenceTokenizer,word_tokenize

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
    
 e=0  
#print(dict)

#print(dict["PRP"])
 j=1000
 i=0
#d.clear()
 for s in p:
    i=i+1
    if s=="iam":
        j=i
        print(s)
    if dict[s]=="NN" and i-j==1: 
      r=s
      e=1
      print("iam executed")

 j=1000
 i=0
 l=0
 if e==0:
  for s in p:
    i=i+1
    if s=="my":
        j=i
        l=l+1
        
    if s=="name" or s=="is" and i-j==1: 
        i=j
        l=l+1
       
    
    if dict[s]=="NN" and l==3:
        r=s
        print("my name exeued")
 return(r)  




    