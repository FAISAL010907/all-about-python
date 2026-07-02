#pip installed flask               '''using pip install xyz
#pip installed django                  then to run it use import xyz'''
#pip installed pyjokes and used 
#pyjokes is python library which is used to get jokes in python
import pyjokes

print(pyjokes.get_joke())
#or you can use this code
import pyjokes

joke = pyjokes.get_jokes()

print(joke)

'''if you want one joke ata time use above code
and want to get a whole lot the use the second one'''
#voice modules that convert text to voice
import pyttsx3
engine = pyttsx3.init()
engine.say("Hey I am good")
engine.runAndWait()
