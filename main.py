import speech_recognition as sr
import random
count = 0
#imports speech_recognition and random libraries
print("This Program is using SpeechRecognition version [" + sr.__version__ + "]")

def displayoption():
    Topics = ["Tell me about yourself","What are you strengths?","What are your development areas?"]
    print('*********************************')
    Impromptu = input("Do you want a topic for your Speech (Yes) or do you already have a prepared speech (No)?  - ")
    if Impromptu.lower() == "yes":
        print('Here is your Speech Prompt ---> ' + random.choice(Topics))
    print("----> Go ahead!!!!")
#This function lists all the prompts and makes it so that it returns a random Topic


def speech2text():
    rec = sr.Recognizer()
    # rec.recognize_google()
    mic = sr.Microphone()
    # sr.Microphone.list_microphone_names()
    with mic as source:
        print('Present Your Speech Now....Listening......')
        print(' ')
        audio = rec.listen(source, phrase_time_limit=25)

    print('Give us a moment....using Google to convert to text......')
    text = rec.recognize_google(audio)
    return text
#This function makes it so that you can use the mic

def count_occurences(word, sentence):
    return sentence.lower().split().count(word)
#This function counts the number of times that a filler word is used in some audio

def analyzeText(text):
    print("**************  Here is your Speech in the form of text  *****************")
    print(text)
    print("**************  End of Speech  *****************")
    print(' ')
    filler_words = ["like", "so", "basically", "i mean", "actually", "yeah", "stuff"]
    splittedText = text.split()
    length = len(filler_words)
    #print(splittedText)
    totalFillerWords = 0
    for i in filler_words:
        p=count_occurences(i, text)
        print('You Used [' + i+ '] - '+ str(p) + ' times')
        totalFillerWords = totalFillerWords + p
#This function formats the output and prints some outputs that tells the user what is happening
    print(' ')
    if totalFillerWords >= 12:
        print("There are (" + str(totalFillerWords) + ") filler words and that is a lot in 25 seconds so you need to do better! But I BELIEVE in you!")
        print('')
        print('YOUR preparedness level is 1')
    elif totalFillerWords >= 10:
        print("You used (" + str(totalFillerWords) + ") filler words. Try again, you can prepare better. KICK those nerves out of here!:)")
        print('')
        print('Your PREPAREDNESS level is 2')
    elif totalFillerWords >= 7:
        print("Decent, you used (" + str(totalFillerWords) + ") filler words but you can do a little better. YOU GOT THIS!!!!!")
        print('')
        print('Your PREPAREDNESS level is 3')
    elif totalFillerWords >= 4:
        print("GOOD JOB! You used (" + str(totalFillerWords) + ") filler words. Try again! I know you got this!!")
        print('')
        print('Your PREPAREDNESS level is 4')
    else:
        print("Very well done, you got only (" + str(totalFillerWords) + ") filler words, you are on your way to success!!")
        print('')
        print('Your PREPAREDNESS level is 5')
#All these statements return a statement based on how many filler words that you used and tells you your preparedness levels
    return totalFillerWords


displayoption()
text = speech2text()
analyzeText(text)
#print(count)