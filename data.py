from global_functions import *

# Загрузка файлов
button = load_image("btn.png")
medium_button = load_image("medium_btn.png")
long_button = load_image("long_btn.png")
settings_window = load_image("settings_bg.png")
input_box_frame = load_image("input_box.png")
ask_bg = load_image("ask_bg.png")
wall_mark = load_image("mark.png")
help_window = load_image("help_window.png")
bg = load_image("bg.png")
warning_bg = load_image("warning_label.png")
star_particle = load_image("star_particle.png")

warning_sound = pygame.mixer.Sound("./data/sounds/warning_sound.wav")
warning_sound.set_volume(0.05)
success_sound = pygame.mixer.Sound("./data/sounds/success_sound.wav")
success_sound.set_volume(0.05)
fail_sound = pygame.mixer.Sound("./data/sounds/fail_sound.wav")
fail_sound.set_volume(0.05)

with open("./data/game_data.json") as raw_data:
    load_data = raw_data.read()
    leaderboard_data = json.loads(load_data)
    print(leaderboard_data)

data = [("./data/images/btn.png", "."), ("./data/images/medium_btn.png", "."),
        ("./data/images/long_btn.png", "."), ("./data/images/settings_bg.png", "."), ("./data/images/bg.png", "."),
        ("./data/images/blurred_bg.png", "."), ("./data/images/icon_sheet.png", "."),
        ("./data/sounds/bg.mp3", "."),
        ("./data/fonts/Proxima_Nova.ttf", ".")]
