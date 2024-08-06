import pyttsx3
from pydub import AudioSegment
import os

# Function to convert text to speech and save as mp3
def text_to_speech(input_file, output_file):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Read the text file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Save the speech as a WAV file
    temp_wav = "temp_output.wav"
    engine.save_to_file(text, temp_wav)
    engine.runAndWait()
    
    # Convert WAV to MP3 using pydub
    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_file, format="mp3")
    
    # Remove the temporary WAV file
    os.remove(temp_wav)
    print(f"Audio content saved as {output_file}")

# Input and output file paths
input_file = 'test.txt'   # Path to the input text file
output_file = 'output.mp3' # Desired path for the output MP3 file

# Convert the text file to speech
text_to_speech(input_file, output_file)















