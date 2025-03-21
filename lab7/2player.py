import pygame  

pygame.init()  
pygame.mixer.init()  

songs = ["c152-hold-up.mp3", "Корган - Шок кыздар.mp3", "Егор Крид feat. Филипп Киркоров - Цвет Настроения Чёрный.mp3"]
idx = 0  

def play(): pygame.mixer.music.load(songs[idx]); pygame.mixer.music.play()  
def stop(): pygame.mixer.music.stop()  
def next_song(): global idx; idx = (idx + 1) % len(songs); play()  
def prev_song(): global idx; idx = (idx - 1) % len(songs); play()  

while True:  
    key = input("Play (P), Stop (S), Next (N), Prev (B), Quit (Q): ").lower()  
    if key == "p": play()  
    elif key == "s": stop()  
    elif key == "n": next_song()  
    elif key == "b": prev_song()  
    elif key == "q": break  
