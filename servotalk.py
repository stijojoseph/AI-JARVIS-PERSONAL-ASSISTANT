import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)

p = GPIO.PWM(40, 50)

p.start(0)
p.ChangeDutyCycle(7.5)

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

def minus(d):
 global i   
 while i>d:     # turn towards 180 degree
  #time.sleep(0.01)
  i=i-0.2# sleep 1 second
  print(i)
  p.ChangeDutyCycle(i)
  time.sleep(0.3)
  #f= open("databr.txt","a+")
  if i<2.5:
      i=2.5
      break
  
 p.stop()



def plus(s,e):
 global i
 y=0
 while y<(e-1):
  d=i+s
  y=y+1
  if i>12:
      i=12
      break
  while i < d:   # turn towards 180 degree
  #time.sleep(0.01)
   i=i+0.2# sleep 1 second
   print(i)
   p.ChangeDutyCycle(i)
   time.sleep(0.07)

   if i>12:
      i=12
      break
  print(i)
 y=0
 while y<(e+2):
  y=y+1   
  if i<2.5:
      i=2.5
      break   
  d=i-s
  while i>d:     # turn towards 180 degree
  #time.sleep(0.01)
   i=i-0.2# sleep 1 second
   print(i)
   p.ChangeDutyCycle(i)
   time.sleep(0.07)
  #f= open("databr.txt","a+")
   if i<2.5:
      i=2.5
      break
 y=0
 while y<e:
  d=i+s
  y=y+1
  if i>7.5:
      i=7.5
      break
  while i < d:   # turn towards 180 degree
  #time.sleep(0.01)
   i=i+0.2# sleep 1 second
   print(i)
   p.ChangeDutyCycle(i)
   time.sleep(0.07)

   if i>7.5:
      i=7.5
      break
  print(i) 
 p.stop()   
 return i
h=int(reads())
print(h)
#minus(i+0.5)
#plus(i-0.5)
i=7.5
s=0.3
e=4
#for x in range(2):
i=plus(s,h)
#@time.sleep(0.5)
# print("m")
#for y in range(2):
print("####",i)
#minus(i-2.5)
 #time.sleep(0.5)
 #print("p")