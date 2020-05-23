import sys
#print(sys.path)
sys.path.append('/home/pi/.local/lib/python3.7/site-packages')
api_key="AIzaSyDXf4HVw9v7IOWOIAb-bxPx8Pq5kj7kxHs"

import bs4 as bs
import urllib.request
from apiclient.discovery import build
resource = build("customsearch", 'v1', developerKey=api_key).cse()
from nltk.tokenize import PunktSentenceTokenizer,word_tokenize

def mysearch(s):
 result = resource.list(q=s, cx='010887918748926121456:qio1wvdmcsz').execute()

 k=[]
 for item in result['items']:
    k.append(item['link'])
 print(k[0])



 source = urllib.request.urlopen(k[0]).read()
 soup = bs.BeautifulSoup(source,'lxml')    
 d=" "
 for paragraph in soup.find_all('p'):
    #print(paragraph.string)
     d+=str(paragraph.text)
 c=0
 p=" "
 for t in d:
  if t==".":
    c=c+1
  if c<=2:
    p+=t    
 #print(p)
 return p 




def rules(t):
 i=0
 j=0
 t=word_tokenize(t)
 for k in t:
   if k== "is" or k== "your" or k=="who" or k=="fucking" :
    i+=1
    print(i)
   if k== "is" or k== "your" or k=="what" or k=="fucking" :
     j+=1  
 if j > i:
      i=j
 return i