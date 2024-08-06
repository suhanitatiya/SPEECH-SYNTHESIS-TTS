import pyttsx3
engine = pyttsx3.init()

# =============================================================================

"""VOICES"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


"""RATE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)

"""VOLUME"""
volume = engine.getProperty('volume')
engine.setProperty('volume', 1)


engine.say("These aren't new types of loops but enhancements that give you more control over your loop's behavior. Ready to boost your coding skills? Let’s get started!")
engine.runAndWait()

