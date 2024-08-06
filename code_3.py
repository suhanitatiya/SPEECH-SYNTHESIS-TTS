#from gtts import gTTS 
import pyttsx3
engine = pyttsx3.init()
import os 

"""VOICES"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


"""RATE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

"""VOLUME"""
volume = engine.getProperty('volume')
engine.setProperty('volume', 1)

output=fh
fh=open("test.txt","r")
myText=fh.read().replace("\n"," ")

#language = 'en'

#output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

#engine.say("These aren't new types of loops but enhancements that give you more control over your loop's behavior. Ready to boost your coding skills? Let’s get started!")
#engine.runAndWait()


fh.close()
os.system("start output.mp3")