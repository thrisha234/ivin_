from gtts import gTTS
from datetime import datetime
import os

# Text for the audio sample
text = """Speaker 1: Action: Prepare the monthly report by next Monday.
Speaker 2: We will schedule the follow-up meeting on Friday."""

# Generate a unique filename with timestamp
filename = f"meeting_sample_{int(datetime.utcnow().timestamp())}.mp3"

# Save in the current folder
filepath = os.path.join(os.getcwd(), filename)

# Generate speech
tts = gTTS(text=text, lang='en')
tts.save(filepath)

print(f"Audio sample saved as {filename}")
