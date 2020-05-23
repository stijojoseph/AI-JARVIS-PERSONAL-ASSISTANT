def voice(x):
 import pyttsx3
 engine = pyttsx3.init() # object creation


 rate = engine.getProperty('rate')   # getting details of current speaking rate
 print (rate)                        #printing current voice rate
 engine.setProperty('rate', 125)     # setting up new voice rate



 volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
 print (volume)                          #printing current volume level
 engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1


 voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
 engine.setProperty('voice', voices[12].id)   #changing index, changes voices. 1 for female

 engine.say(x)
#engine.say("iam jarvis 2.0")
 engine.runAndWait()
 engine.stop()
k="Mohanlal Viswanathan born 21 May 1960 known mononymously as Mohanlal is an Indian actor producer playback singer and distributor who predominantly works in Malayalam cinema He has had a prolific career spanning over four decades during which he has acted in more than 340 films In addition to Malayalam he has also appeared"
voice(k) 