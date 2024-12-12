import datetime
import gtts
import bs4
import random
import speech_recognition as sr

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    # Get current time
    now = datetime.datetime.now()
    time_string = now.strftime("%H:%M:%S")

    # Generate speech
    tts = gtts.gTTS(time_string, lang=lang)
    tts.save(filename)


def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    # Example joke database
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t programmers like nature? It has too many bugs."
    ]
    
    # Choose a random joke
    joke = random.choice(jokes)
    
    # Generate speech
    tts = gtts.gTTS(joke, lang=lang)
    tts.save(audiofile)


def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.
    
    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    # Get current date and day of the week
    now = datetime.datetime.now()
    day_string = now.strftime("%A, %Y-%m-%d")

    # Generate speech
    tts = gtts.gTTS(day_string, lang=lang)
    tts.save(audiofile)

    # URL to view the calendar for this month and year
    url = f"https://www.google.com/calendar/render?tab=mc&pli=1#calendar/view/month"
    return url


def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    # Listen for a command from the user
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said: ", command)

        if "time" in command:
            what_time_is_it(lang, filename)
        elif "day" in command:
            what_day_is_it(lang, filename)
        elif "joke" in command:
            tell_me_a_joke(lang, filename)
        else:
            print("Sorry, I didn't understand the command.")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

