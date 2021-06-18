from constants import *


# Группы
all_sprites = pygame.sprite.Group()  # Группа всех спрайтов
buttons = pygame.sprite.Group()  # Группа спрайтов кнопок

clock = pygame.time.Clock()  # Объект часов для отрисовки кадров

pygame.display.set_caption("Shields")  # Название окна
screen = pygame.display.set_mode(SCREEN_SIZE)  # Объект экрана\


# Функция выключения
def terminate():
    pygame.quit()
    sys.exit()


# Функция загрузки изображения
def load_image(name, colorkey=None):
    fullname = os.path.join('./data/images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# Функция, вырезающая кадры со спрайт-листа
def cut_sheet(sheet, columns, rows, obj_width, obj_height):
    frames = []
    rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                       sheet.get_height() // rows)
    for j in range(rows):
        for i in range(columns):
            frame_location = (rect.w * i, rect.h * j)
            image = pygame.transform.scale(sheet.subsurface(pygame.Rect(
                frame_location, rect.size)), (obj_width, obj_height))
            image = image.convert_alpha()
            frames.append(image)
    return frames


# Функция устанавливающая надпись на кнопке
def set_text(surface, text, font_size=90, color=WHITE):
    font_text = pygame.font.Font(FONT, font_size)
    text_result = font_text.render(text, True, color)
    screen.blit(text_result, text_result.get_rect(center=surface.rect.center))


# Затухание экрана (Передаётся задержка)
def transition(delay=15):
    for size in range(40):
        black_rect = pygame.Surface((1280, 20 * size))  # - переход сверху - вниз
        black_rect.fill(BLACK)
        screen.blit(black_rect, (black_rect.get_rect(center=screen.get_rect().center)))
        pygame.display.flip()
        pygame.time.delay(delay)


# Проверка наведён ли курсор на кнопку
def check_hovered():
    mouse_pos = pygame.mouse.get_pos()
    for btn in buttons:
        if btn.on_hovered(mouse_pos):
            btn.highlight()
        else:
            btn.set_default_image()


icon_sheet = cut_sheet(load_image("icon_sheet.png"), 4, 4, 65, 65)

icons = {"settings": icon_sheet[0], "cup": icon_sheet[1], "empty_cross": icon_sheet[2],
         "red_cross": icon_sheet[3], "black_cross": icon_sheet[4], "clock": icon_sheet[5],
         "empty_shield": icon_sheet[6], "full_shield": icon_sheet[7], "volume_off": icon_sheet[8],
         "volume_down": icon_sheet[9], "volume_up": icon_sheet[10]}
