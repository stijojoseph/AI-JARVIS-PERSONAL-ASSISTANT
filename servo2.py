import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT)

p = GPIO.PWM(37, 50)

p.start(0)
x=180
d=(x/18)+2

u=[]
contents=[]     
f=open("databr.txt", "r")
if f.mode == 'r':
    #contents.append(f.read())
    u=f.readlines()   
i=0
for x in u:
    i=i+1
    #print(x)
 
print(x)

i=float(x)
d=i-0.5
i=float(x)
#try:
# while i>=1.5:
      # p.ChangeDutyCycle(0)  # turn towards 90 degree
       #time.sleep(1) # sleep 1 second
#        p.ChangeDutyCycle(0)  # turn towards 0 degree
#        time.sleep(1) # sleep 1 second
while i>=d:     # turn towards 180 degree
  time.sleep(0.001)
  i=i-0.01# sleep 1 second
  p.ChangeDutyCycle(i)
  f= open("databr.txt","a+")
  if i<2.5:
      i=2.5
      break
  f.write(str(i)+"\n")
  f.close() 
p.stop()
#except KeyboardInterrupt:
  #  p.stop()
 #   GPIO.cleanup()
 
 
def plus():
 global i   
 while i>=d:     # turn towards 180 degree
  #time.sleep(0.01)
  i=i-0.01# sleep 1 second
  p.ChangeDutyCycle(i)
  f= open("databr.txt","a+")
  if i<2.5:
      i=2.5
      break
  f.write(str(i)+"\n")
  f.close() 
 p.stop()
plus() 