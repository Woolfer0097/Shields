from data import *


# Класс доски для игры в "Щиты"
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, WHITE, (self.cell_size * x + self.left,
                                                 self.top + self.cell_size * y,
                                                 self.cell_size, self.cell_size),
                                 1)

    def get_cell(self, pos):
        return ((pos[0] - self.left) // self.cell_size,
                (pos[1] - self.top) // self.cell_size)


# Класс, описывающий кнопку
class Button(pygame.sprite.Sprite):
    def __init__(self, frame, x, y, text="", text_size=60, icon=pygame.Surface((0, 0))):
        super(Button, self).__init__(buttons)
        self.frames = frame
        self.icon = icon
        self.image = frame
        self.text_size = text_size
        self.standard_btn = frame
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = (x, y)
        self.x, self.y = x, y
        self.text = text
        self.hovered = False

    # Функция, устанавливающая иконку
    def set_icon(self):
        screen.blit(self.icon, self.icon.get_rect(center=self.rect.center))

    # Функция увеличивает кнопку (выделяет/подсвечивает)
    def highlight(self):
        self.image = pygame.transform.scale(self.frames,
                                            (int(self.width * SCALE_COEFFICIENT),
                                             int(self.height * SCALE_COEFFICIENT)))
        self.rect = self.image.get_rect()
        difference_width = (self.width - int(self.width * SCALE_COEFFICIENT)) // 2
        difference_height = (self.height - int(self.height * SCALE_COEFFICIENT)) // 2
        self.rect.x = self.x + difference_width
        self.rect.y = self.y + difference_height

    # Функция возвращает картинку кнопки в изначальную (после наведения)
    def set_default_image(self):
        self.rect = self.frames.get_rect()
        self.rect.x, self.rect.y = self.pos
        self.hovered = False
        self.image = self.frames

    # Проверяет наведён ли курсор на кнопку
    def on_hovered(self, pos):
        if self.rect.collidepoint(*pos):
            self.hovered = True
            return True
        return False

    # Функция, выполняющаяся каждый цикл (высчитывает текущий кадр, накладывает текст)
    def update(self):
        self.image = self.frames
        if self.text:
            set_text(self, self.text, self.text_size)
        if self.icon:
            self.set_icon()


# Класс, описывающий выборочный список
class Selector(pygame.sprite.Sprite):
    #                  x  y  Список элементов списка
    def __init__(self, x, y, item_list):
        super(Selector, self).__init__(all_sprites)
        self.x = x
        self.y = y
        self.item_list = item_list

    def next_item(self):
        screen.blit()
        return self.item_list


# Класс, описывающий Поле для ввода текста
class TextBox(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super(TextBox, self).__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.set_position()

    def set_position(self):
        self.rect.x = self.x
        self.rect.y = self.y


class Shields(Board):
    def __init__(self, width, height):
        super(Shields, self).__init__(width, height)
        self.width = width
        self.height = height
        self.board = {}
        self.fill_board()

    def fill_board(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or y == 0 or y == 5 or x == 5:
                    self.board[(x, y)] = {"shield": False, "attacked": (False, False), "points": 10}
                elif x == 1 or y == 1 or y == 4 or x == 4:
                    self.board[(x, y)] = {"shield": False, "attacked": (False, False), "points": 20}
                else:
                    self.board[(x, y)] = {"shield": False, "attacked": (False, False), "points": 40}

    def render(self, attack=False):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[(x, y)]["shield"] and not attack:
                    screen.blit(pygame.transform.scale(icons["full_shield"], (25, 25)),
                                (self.cell_size * x + self.left + 85, self.top + self.cell_size * y + 5))
                if attack:
                    # Если клетка атакована и игрок не попал по щиту
                    if self.board[(x, y)]["attacked"][0] and not self.board[(x, y)]["attacked"][1]:
                        screen.blit(pygame.transform.scale(icons["full_cross"], (25, 25)),
                                    (self.cell_size * x + self.left + 85, self.top + self.cell_size * y + 5))
                    elif self.board[(x, y)]["attacked"][0] and self.board[(x, y)]["attacked"][1]:
                        screen.blit(pygame.transform.scale(icons["empty_cross"], (25, 25)),
                                    (self.cell_size * x + self.left + 85, self.top + self.cell_size * y + 5))
                else:
                    bg_rect = pygame.rect.Rect(self.cell_size * x + self.left, self.top + self.cell_size * y,
                                               self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, WHITE, bg_rect, 2)
                pygame.draw.rect(screen, WHITE, (self.cell_size * x + self.left,
                                                 self.top + self.cell_size * y,
                                                 self.cell_size, self.cell_size),
                                 2)
                font_text = pygame.font.Font(FONT, 25)
                text_result = font_text.render(str(self.board[(x, y)]["points"]), True, WHITE)
                screen.blit(text_result,
                            (self.cell_size * x + self.left + 5,
                             self.top + self.cell_size * y))

    def highlight_cell(self, pos, color="#21D19F"):
        x, y = self.get_cell(pos)
        if 6 > x >= 0 and 6 > y >= 0:
            pygame.draw.rect(screen, color, (self.cell_size * x + self.left,
                                             self.top + self.cell_size * y,
                                             self.cell_size, self.cell_size),
                             8)

    def set_shield(self, pos):
        x, y = self.get_cell(pos)
        self.board[(x, y)]["shield"] = True

    def set_attacked(self, pos, is_damaged):
        x, y = self.get_cell(pos)
        if 6 > x >= 0 and 6 > y >= 0:
            if is_damaged:
                self.board[(x, y)]["attacked"] = (True, True)
            else:
                self.board[(x, y)]["attacked"] = (True, False)

    def remove_shield(self, pos):
        x, y = self.get_cell(pos)
        self.board[(x, y)]["shield"] = False

    def get_shields_points(self):
        return [value["points"]
                for value in self.board.values()
                if value["shield"]]

    def get_shields_coordinates(self):
        return [key
                for key, value in self.board.items()
                if value["shield"]]

    def get_count_shields(self, points):
        return self.get_shields_points().count(points)

    def get_points(self, pos):
        if self.get_cell(pos) in self.board.keys():
            return self.board[self.get_cell(pos)]["points"]

    def check_shield(self, pos):
        if self.get_cell(pos) in self.get_shields_coordinates():
            return True
        return False

    def check_count_shields(self, points):
        if points == 10:
            if self.get_count_shields(points) < 9:
                return True
            return False
        elif points == 20:
            if self.get_count_shields(points) < 7:
                return True
            return False
        elif points == 40:
            if self.get_count_shields(points) < 3:
                return True
            return False
        return False
