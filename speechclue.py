import time
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
GPIO.setup(33, GPIO.OUT)
def lightl():
    GPIO.output(33,GPIO.LOW)
def lighth():
    GPIO.output(33,GPIO.HIGH)
    
def reads():  
 file2 = open("clue.txt","r+")  
 t=None 

  
 k=file2.readlines()
 print(k)
 print(type(k))
 for t in k:
     print(type(t))
 if t is not None:    
  t=int(t)
 file2. truncate(0)    
 file2.close()    
 return t

while True:
    k=reads()
    if k is not None:
      if k==1:
          print("recording on")
          lighth()
          time.sleep(5)
      
    print("recording off")
    lightl()    
    time.sleep(1)    
          