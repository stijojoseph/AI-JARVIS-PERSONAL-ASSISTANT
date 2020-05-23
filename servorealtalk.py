import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(37, GPIO.OUT)
#p = GPIO.PWM(37, 50) 
   

#p.start(0)
x=90
d=(x/18)+2
def ledh():
    GPIO.setup(36,GPIO.OUT)
    GPIO.setup(35,GPIO.OUT)
    
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(35,GPIO.HIGH)
def ledl():
    GPIO.output(36,GPIO.LOW)
    GPIO.output(35,GPIO.LOW)    

def talk(h,pj=7.2):
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(36,GPIO.OUT)
    GPIO.setup(35,GPIO.OUT)
    p = GPIO.PWM(37, 50) 
   
    p.start(0)
    u=0
    print("talk",h,u)
    while u<h:
      u=u+1  
      i=6.66
      e=0
      while i< pj:
       e=e+1
       if (e%3)==0:
           ledh()
       else:
           ledl()
           
       print("talk",h,u)   
       p.ChangeDutyCycle(i)
       i=i+0.2# turn towards 180 degree
       time.sleep(0.1)
      e=0
      if pj >7.3:
          time.sleep(4)
      while i>6.66:
       e=e+1
       if (e%3)==0:
           ledh()
       else:
           ledl()   
       p.ChangeDutyCycle(i)
       i=i-0.2# turn towards 180 degree
       time.sleep(0.1) # sleep 1 second
    p.stop()
    GPIO.cleanup()
      # p.ChangeDutyCycle(9.72) # turn towards 180 degree
       #time.sleep(2) 
def reads():  
 file2 = open("talk.txt","r+")  
 j=None 

  
 k=file2.readlines()
 for j in k:
    print(j)
 if j==None:
    print(j)
 file2. truncate(0)    
 file2.close()    
 return j
def cret():
 m=reads()
 time.sleep(0.5)
 print(type(m))
 if m is not None:
  
  h=int(m)
  print(type(h),h)
#minus(i+0.5)
#plus(i-0.5)
  i=7.5
  s=0.3
  e=4
#for x in range(2):
  

  i=talk(h/2,p)
  #time.sleep(1)
ledh()  