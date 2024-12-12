import speech_recognition as sr

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
    recognizer = sr.Recognizer()
    try:
        # Load the audio file
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)  # Record the audio data
            # Recognize speech using Google's speech recognition engine
            text = recognizer.recognize_google(audio_data, language=language)
            return text
    except sr.RequestError as e:
        return f"Error: Could not request results from the recognition service; {e}"
    except sr.UnknownValueError:
        return "Error: Unable to recognize speech from the audio file."
    except FileNotFoundError:
        return "Error: The specified file was not found."
    except Exception as e:
        return f"Error: {e}"
