import asyncio
import edge_tts
from helper import play_audio
from deepseek import ask_deepseek
import time
import re
import markdown

voices = ["en-AU-NatashaNeural", "en-AU-WilliamNeural"]
text = "Hi Sir, How may I help you?"
voice = voices[0]

async def amain(text) -> None:
    result = ask_deepseek(text)
    voice_text = re.sub(r"[^a-zA-Z0-9.,'(:)?!\s]", '', result[0])
    communicate = edge_tts.Communicate(voice_text, voice, rate="+18%")
    await communicate.save("test.mp3")
    html = markdown.markdown(result[0])
    print(html)
    await play_audio("test.mp3")

loop = asyncio.get_event_loop_policy().get_event_loop()

def say_vectora(text: str):
    try:
        loop.run_until_complete(amain(text))
    finally:
        loop.close()

print("Hey, Who are you?")
say_vectora("Who are you?")