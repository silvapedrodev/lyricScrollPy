def generate(lyrics, delay):
    for line in lyrics.strip().split('\n'):
        print(f'("{line}", {delay:.1f}),')

# === ⬇️ EDIT ONLY THIS SECTION ⬇️ ===

delay = 1  # Set the delay time here (in seconds)

lyrics = """
Example lyric line 1, abobora, saci,
Example lyric line 2
Example lyric line 3
"""  # Replace with your own lyrics, one line per phrase

generate(lyrics, delay)