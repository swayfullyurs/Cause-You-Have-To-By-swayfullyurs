import sys, time, os
import pygame
os.system('')

# ANSI colors
WHITE  = "\033[97m"
DIM    = "\033[90m"
BLUE   = "\033[94m"
RED    = "\033[91m"
PINK   = "\033[95m"
RESET  = "\033[0m"

# Terminal width
try:
    import shutil
    WIDTH = shutil.get_terminal_size().columns
except Exception:
    WIDTH = 80


def center_pad(text):
    padding = max(0, (WIDTH - len(text)) // 2)
    return " " * padding


def type_out(text, speed=0.09, color=WHITE):
    pad = center_pad(text)
    sys.stdout.write(pad)
    for ch in text:
        sys.stdout.write(color + ch)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET + "\n")


# Lyrics
# (delay_seconds, lyric_text, typing_speed, color)
lyrics = [
    (1.5,  "I'm so sorry...",                     0.19, BLUE),
    (5.9,  "I wish I could be",                   0.18, WHITE),
    (10.0, "The one to love you more.",            0.18, WHITE),
    (18.0, "I hope you find somebody",             0.19, WHITE),
    (23.7, "Who's got everything",                 0.22, WHITE),
    (29.0, "You're searching for",                 0.15, WHITE),
    (37.0, "The silence is getting too cold",      0.12, BLUE),
    (40.0, "We stopped fighting",                  0.11, BLUE),
    (43.5, "'Cause deep down inside we both know", 0.07, RED),
    (45.6, "Just for once, what do you want,",     0.08, DIM),
    (48.0, "Baby, tell me the truth",              0.09, PINK),
    (51.2, "Did you only love me",                 0.09, PINK),
    (53.0, "'Cause you had to?",                   0.11, PINK),
]


# Audio setup
AUDIO_FILE = "cause_you_have_to.mp3"

pygame.mixer.init()
pygame.mixer.music.load(AUDIO_FILE)

# Intro countdown
os.system('cls' if os.name == 'nt' else 'clear')
print("\n")

for i in range(3, 0, -1):
    msg = f"♪  starting in {i}..."
    sys.stdout.write(DIM + center_pad(msg) + msg + RESET + "\r")
    sys.stdout.flush()
    if i == 3:
        time.sleep(1)                  # 1 second silence before song
        pygame.mixer.music.play()      # song starts here
        time.sleep(0.25)                  # rest of "3" beat
    else:
        time.sleep(0.25)                  # "2" and "1" each last 1 second

sys.stdout.write(" " * WIDTH + "\r")
sys.stdout.flush()
print("\n")


# Playback — start = time when lyrics loop begins
# Note: song has been playing for ~3s by this point (1s silence + 2s of countdown)
# Adjust lyric delay values if they feel off
start = time.time()

for delay, line, speed, color in lyrics:
    elapsed = time.time() - start
    wait = delay - elapsed
    if wait > 0:
        time.sleep(wait)
    type_out(line, speed, color)


# Outro
time.sleep(2.5)
note = "♪♪♪"
sys.stdout.write("\n" + DIM + center_pad(note) + note + RESET + "\n\n")
sys.stdout.flush()

pygame.mixer.music.stop()
pygame.mixer.quit()