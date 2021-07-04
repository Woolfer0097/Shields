# Библиотеки, константы для игры, глобальные функции и переменные


from game_functions import *


# Функция отвечающая за последовательность включения экранов
def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.mixer.music.load("./data/sounds/bg2.mp3")
    pygame.mixer.music.play(-1)
    start_screen()
    terminate()


if __name__ == '__main__':
    main()
