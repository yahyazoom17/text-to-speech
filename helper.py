import asyncio
import pygame

async def play_audio(filepath: str):
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

def remove_thinking(text):
    start = text.find("<think>")
    end = text.find("</think>")
    think_text = text[:end+8]
    final_text = text.replace(think_text, "").lstrip()
    return final_text