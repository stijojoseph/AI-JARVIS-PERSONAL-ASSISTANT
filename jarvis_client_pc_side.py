import speech_recognition as sr
# to speech conversion
from gtts import gTTS
i=0
import paramiko

host = "raspberrypi.local"#TYPE YOUR IP ADDRESS RASPI
port = "22"
username = "pi"##YOUR USER NAME
password = ""# YOUR PASSWORD

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command("sudo python3 read.py")
stdin, stdout, stderr = ssh.exec_command("sudo python3 talker.py")
stdin, stdout, stderr = ssh.exec_command("sudo python3 servotalk.py")
stdin, stdout, stderr = ssh.exec_command("sudo python3 speechclue.py")
stdin, stdout, stderr = ssh.exec_command("sudo python3 chatbotplusrules.py")

# import Os module to start the audio file
import os
s=[]
def stt(mytext):

# Language we want to use
 language = 'en'

 myobj = gTTS(text=mytext, lang=language, slow=False)

 myobj.save("output.mp3")

# Play the converted file
 os.system("start output.mp3")

r = sr.Recognizer()
import pyaudio
import wave
while command != "exit":

 FORMAT = pyaudio.paInt16
 CHANNELS = 1
 RATE = 44100
 CHUNK = 512
 RECORD_SECONDS = 5
 WAVE_OUTPUT_FILENAME = "output2.wav"
 device_index = 2
 audio = pyaudio.PyAudio()


 info = audio.get_host_api_info_by_index(0)
 numdevices = info.get('deviceCount')
 import speech_recognition as sr

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
 #       print("Microphone with name \"{1}\" found for microphone(device_index{0})".format(index, name))

 k="2"
 index =int(k)
 print(" index "+str(index))

 stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,input_device_index = index,
                frames_per_buffer=CHUNK)
 print ("recording started")
 k2="sudo python3 write1.py 1"
 stdin, stdout, stderr = ssh.exec_command(str(k2))
 Recordframes = []

 for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    Recordframes.append(data)
 print ("recording stopped")

 stream.stop_stream()
 stream.close()
 audio.terminate()

 waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
 waveFile.setnchannels(CHANNELS)
 waveFile.setsampwidth(audio.get_sample_size(FORMAT))
 waveFile.setframerate(RATE)
 waveFile.writeframes(b''.join(Recordframes))
 waveFile.close()
 print ("recording stopped")
 k="output2.wav"
 with sr.AudioFile(k) as source:
    audio = r.listen(source)

    try:
        k1=" "
        text = r.recognize_google(audio)
        print('Working on...')
        print(text)
       # if text != "top":
         #stt(text)
        s=text.split()
        print(s)
        for word in s:
           if word!="jarvis" or word!="Jarvis":
            k1=k1+word+" "
           print(k1)
           if word == "stop": 
            i=1
            print(i)
        command=k1  
        k="sudo python3 write.py " +" "+ command
        stdin, stdout, stderr = ssh.exec_command(str(k))
 #lines = stdout.readlines()
 #line=stdin.readlines()
        print("finish")
        if command=="stop":
         stdin, stdout, stderr = ssh.exec_command("sudo pkill -f chatbotplusrules.py") 
         stdin, stdout, stderr = ssh.exec_command("sudo python3 chatbotplusrules.py")  
         stdin, stdout, stderr = ssh.exec_command("sudo python3 read.py")
         stdin, stdout, stderr = ssh.exec_command("sudo python3 talker.py")
         stdin, stdout, stderr = ssh.exec_command("sudo python3 servotalk.py")
         
    except:
        print('Sorry.. run again...')
        text="none"

 if text == "stop" or i==1:
     stdin, stdout, stderr = ssh.exec_command("sudo pkill -f chatbotplusrules.py") 
     stdin, stdout, stderr = ssh.exec_command("sudo pkill -f speechclue.py")
     print("process stopped")
     break
