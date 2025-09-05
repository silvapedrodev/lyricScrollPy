import os
from time import sleep
from colorama import init, Style, Fore, Cursor

# Color
bg_text = Fore.LIGHTBLACK_EX
highlight = Style.BRIGHT + Fore.CYAN # <- choose color here

init(autoreset=True)

# Functions
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def show_header(title, desc):
    print("\n")
    print(title)
    if desc:
        print(desc)
    print("-")

def render_lyrics(lyrics, current_index, window):
    start = max(0, current_index - 2)
    end = min(len(lyrics), current_index + window)

    for i in range(start, end):
        verse, _ = lyrics[i]
        if i == current_index:
            print(highlight + verse)
        else:
            print(bg_text + verse)

def show_lyrics(title, desc, lyrics):
    window_size = 4
    for i, (_, delay) in enumerate(lyrics):
        clear_console()
        show_header(title, desc)
        render_lyrics(lyrics, i, window_size)
        sleep(delay)
