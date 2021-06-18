from libraries import *


# Константы для игры:
ACCEPTED_SYMBOLS = "abcdefghijklmnopqrstuvwxyz" \
                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                   "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" \
                   "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" \
                   "0123456789 _"  # Символы которые игрок может вписывать в поле ввода имени
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE = 1280, 720  # Размеры экрана
FPS = 60  # Кадры в секунду (Frame Per Second)
FONT = "./data/fonts/Proxima_Nova.ttf"
WHITE = pygame.Color("white")  # Белый цвет
BLACK = pygame.Color("black")  # Чёрный цвет
SCALE_COEFFICIENT = 1.2  # Коэффициент увеличения объектов (у меня кнопок)
