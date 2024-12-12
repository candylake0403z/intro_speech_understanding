import gtts

def synthesize(text, lang, filename):
    '''
    Use gtts.gTTs(text=text, lang=lang) to synthesize speech, then write it to filename.
    
    @params:
    text (str) - the text you want to synthesize
    lang (str) - the language in which you want to synthesize it
    filename (str) - the filename in which it should be saved
    '''
    try:
        # Generate the speech
        tts = gtts.gTTS(text=text, lang=lang)
        # Save it to the file
        tts.save(filename)
        print(f"Speech synthesis successful! File saved to {filename}.")
    except Exception as e:
        print(f"An error occurred during synthesis: {e}")
