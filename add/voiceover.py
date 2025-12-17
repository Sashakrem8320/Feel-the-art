from gtts import gTTS
import os
from add import markup

# Function to convert text to speech and save it as an audio file
def voice(text):  # Use this function for voicing individual files
    language = 'ru'  # Set the language to Russian

    # Create a gTTS object with normal speech
    tts = gTTS(text=text, lang=language, slow=False)  # Set slow=True for slower speech
    tts.save("Start.mp3")

    # Play the audio file (for Windows)
    os.system("start Start.mp3")  # Launch the saved file

# Function to activate text-to-speech for multiple texts
def activate():
    language = 'ru'  # Set the language to Russian
    texts = markup.get_text()  # Retrieve texts from markup

    # Create gTTS objects for each text and save them as audio files
    for i in range(len(texts)):
        tts = gTTS(text=texts[i], lang=language, slow=False)  # Set slow=True for slower speech

        # Save the audio file with a unique name
        tts.save(f"voice/{i}.mp3")  # Save each audio file in the 'voice' directory


# Function to create a list of zeros
def create(n):
    st = []  # Initialize an empty list
    for _ in range(n):
        st.append(0.0)  # Append 0.0 to the list n times
    return st  # Return the list of zeros
