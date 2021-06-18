from data import *


# Класс доски для игры в "Щиты"
class Board(pygame.sprite.Sprite):
    def __init__(self, width, height, left, top):
        super().__init__(all_sprites)
        self.width = width
        self.height = height
        self.board = [[" "] * width for _ in range(height)]
        self.step = 0
        self.cell_size = 124
        self.left = left
        self.top = top
        self.cross_image = load_image("player_symbol.png")
        self.zero_image = load_image("irbis_symbol.png")
        self.screen = load_image("mini_game_frame.png")
        self.coord_ratio = {(0, 0): 0, (0, 1): 1, (0, 2): 2,
                            (1, 0): 3, (1, 1): 4, (1, 2): 5,
                            (2, 0): 6, (2, 1): 7, (2, 2): 8}
        self.win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                 (0, 4, 8), (2, 4, 6)]

    # Отрисовка
    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(self.screen, WHITE, (self.cell_size * x + 33,
                                                      self.cell_size * y + 119,
                                                      self.cell_size, self.cell_size), 2)

    # Обработка клика
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        return self.on_click(cell)

    # Получаем клетку
    def get_cell(self, mouse_pos):
        return ((mouse_pos[0] - (self.left + 33)) // self.cell_size,
                (mouse_pos[1] - (self.top + 119)) // self.cell_size)

    # Проверка клика
    def on_click(self, cell_coordinates):
        if self.width > cell_coordinates[0] >= 0 and self.height > cell_coordinates[1] >= 0:
            return cell_coordinates
        else:
            pass

    # Ход игрока
    def player_step(self, cell_coords):
        coordinates = self.get_click(cell_coords)
        if coordinates:
            x, y = coordinates
            for j in range(self.width):
                for i in range(self.height):
                    if j == x and i == y:
                        if self.board[i][j] != "X" and self.board[i][j] != "O":
                            self.board[i][j] = "X"
                            self.step += 1
                            return True
                        else:
                            return False
        else:
            pass

    # Проверка выигрыша
    def check_win(self):
        for x in range(self.width):
            for i, coord in enumerate(self.win_combinations):
                y1, x1 = self.get_key(coord[0])
                y2, x2 = self.get_key(coord[1])
                y3, x3 = self.get_key(coord[2])
                if self.board[x1][y1] == self.board[x2][y2] == self.board[x3][y3]:
                    return self.board[x1][y1]
        if self.step == 9:
            return "draw"
        return False

    # Ход компьютера
    def ai_step(self):  # artificial intellect`s step
        x, y = self.get_key(random.randint(0, 8))
        if self.board[x][y] != "X" and self.board[x][y] != "O":
            self.board[x][y] = "O"
            self.step += 1
        else:
            self.ai_step()

    # Взятие ключа словаря по значению
    def get_key(self, value_need):
        for key, value in self.coord_ratio.items():
            if value == value_need:
                return key


# Класс, описывающий кнопку
class Button(pygame.sprite.Sprite):
    def __init__(self, frame, x, y, text="", icon=pygame.Surface((0, 0))):
        super(Button, self).__init__(buttons)
        self.frames = frame
        self.icon = icon
        self.image = frame
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
            set_text(self, self.text, 60)
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
