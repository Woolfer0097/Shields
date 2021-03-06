from libraries import *


# Константы для игры:
ACCEPTED_SYMBOLS = "abcdefghijklmnopqrstuvwxyz" \
                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                   "0123456789_"  # Символы которые игрок может вписывать в поле ввода имени
RUS_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" \
              "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE = 1280, 720  # Размеры экрана
FPS = 60  # Кадры в секунду (Frame Per Second)
FONT = "./data/fonts/Proxima_Nova.ttf"  # Шрифт
WHITE = pygame.Color("white")  # Белый цвет
BLACK = pygame.Color("black")  # Чёрный цвет
RED = pygame.Color("red")  # Красный цвет
SCALE_COEFFICIENT = 1.2  # Коэффициент увеличения объектов (у меня кнопок)
MAX_F, MAX_S, MAX_T = 9, 7, 3  # Максимальное кол-во щитов для каждого поля
COLOR_INACTIVE = "#7293A0"  # Цвет неактивности поля
COLOR_ACTIVE = "#21D19F"  # Цвет активности поля
SCROLLING_SPEED = 50
LIMIT_SYMBOLS = 14
GRAVITY = 1
MIN_LIMIT_SYMBOLS = 4
