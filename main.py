from colorama import init, Style, Fore, Cursor

# Color
bg_text = Fore.LIGHTBLACK_EX
highlight = Style.BRIGHT + Fore.CYAN # <- choose color here

init(autoreset=True)

# Functions
def show_header(title, desc):
    print("\n")
    print(title)
    if desc:
        print(desc)
    print("-")