from game_classes import *


# Функция запуска начального экрана
def start_screen():
    volume = 0.2
    settings_flag = False
    help_flag = False
    rating_flag = False
    while True:
        if settings_flag:
            # Настройки
            if help_flag:
                buttons.empty()
                return_btn = Button(icons["full_black_cross"], 1205, 10)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if return_btn.on_hovered(event.pos):
                            help_flag = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        help_flag = False
                check_hovered()
                screen.blit(help_window, (0, 0))
                buttons.draw(screen)
                buttons.update()
                # Отрисовка
                pygame.display.flip()
                clock.tick(FPS)
            else:
                buttons.empty()
                volume_off_btn = Button(icons["volume_off"], 449, 300)
                volume_down_btn = Button(icons["volume_down"], 554, 300)
                volume_up_btn = Button(icons["volume_up"], 658, 300)
                help_btn = Button(icons["help"], 775, 303)
                return_btn = Button(icons["full_cross"], 854, 130)
                sound_textbox = TextBox(settings_window, 394, 250)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    # Обработка нажатий на кнопки
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if volume_down_btn.on_hovered(event.pos):
                            if volume > 0:
                                volume -= 0.1
                        if volume_up_btn.on_hovered(event.pos):
                            if volume + 0.1 <= 1:
                                volume += 0.1
                        if volume_off_btn.on_hovered(event.pos):
                            volume = 0
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if return_btn.on_hovered(event.pos):
                            settings_flag = False
                        if help_btn.on_hovered(event.pos):
                            transition()
                            help_flag = True
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        settings_flag = False
                pygame.mixer.music.set_volume(volume)
                check_hovered()
                # Отрисовка нужных изображений
                screen.blit(blur_surface(screen, 40), (0, 0))
                screen.blit(settings_window, (394, 162))
                buttons.draw(screen)
                set_text(sound_textbox, f"{int(pygame.mixer.music.get_volume() * 100)}", 50)
                buttons.update()
                # Отрисовка
                pygame.display.flip()
                clock.tick(FPS)
        else:
            # Начальный экран
            buttons.empty()
            start_btn = Button(long_button, 389, 314, "ИГРАТЬ")
            settings_btn = Button(long_button, 389, 447, "НАСТРОЙКИ")
            exit_btn = Button(long_button, 389, 580, "ВЫХОД")
            rating_btn = Button(button, 1150, 37, icon=icons["cup"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONUP:
                    if start_btn.on_hovered(event.pos):
                        transition()
                        p1_name, p2_name = ask_names()
                        transition()
                        open_help()
                        transition()
                        game(p1_name, p2_name)
                    if rating_btn.on_hovered(event.pos):
                        rating_flag = True
                    if exit_btn.on_hovered(event.pos):
                        transition()
                        terminate()
                    if settings_btn.on_hovered(event.pos):
                        settings_flag = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        terminate()
            check_hovered()
            screen.blit(bg, (0, 0))
            buttons.draw(screen)
            buttons.update()
            # Отрисовка
            pygame.display.flip()
            clock.tick(FPS)


def game(player1, player2):
    # Инициализация доски
    board = Shields(6, 6)
    volume = 0.2
    settings_flag = False
    help_flag = False
    action = {"player": player1, "action": "defence"}
    game_data = {player1: {"player_board": {}, "count_steps": 17, "score": 0},
                 player2: {"player_board": {}, "count_steps": 17, "score": 0}}
    while True:
        if settings_flag:
            # Настройки
            if help_flag:
                buttons.empty()
                return_btn = Button(icons["full_black_cross"], 1205, 10)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if return_btn.on_hovered(event.pos):
                            help_flag = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        help_flag = False
                check_hovered()
                screen.blit(help_window, (0, 0))
                buttons.draw(screen)
                buttons.update()
                # Отрисовка
                pygame.display.flip()
                clock.tick(FPS)
            else:
                buttons.empty()
                volume_off_btn = Button(icons["volume_off"], 449, 262)
                volume_down_btn = Button(icons["volume_down"], 554, 262)
                volume_up_btn = Button(icons["volume_up"], 658, 262)
                help_btn = Button(icons["help"], 775, 265)
                return_btn = Button(icons["full_cross"], 854, 130)
                quit_btn = Button(medium_button, 449, 439, "Главное меню", 50)
                sound_textbox = TextBox(settings_window, 394, 180)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    # Обработка нажатий на кнопки
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if volume_down_btn.on_hovered(event.pos):
                            if volume > 0:
                                volume -= 0.1
                        if volume_up_btn.on_hovered(event.pos):
                            if volume + 0.1 <= 1:
                                volume += 0.1
                        if volume_off_btn.on_hovered(event.pos):
                            volume = 0
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if return_btn.on_hovered(event.pos):
                            settings_flag = False
                        if quit_btn.on_hovered(event.pos):
                            transition()
                            return
                        if help_btn.on_hovered(event.pos):
                            transition()
                            help_flag = True
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        settings_flag = False
                pygame.mixer.music.set_volume(volume)
                check_hovered()
                # Отрисовка нужных изображений
                screen.blit(blur_surface(screen, 40), (0, 0))
                screen.blit(settings_window, (394, 162))
                buttons.draw(screen)
                set_text(sound_textbox, f"{int(pygame.mixer.music.get_volume() * 100)}", 50)
                buttons.update()
                # Отрисовка
                pygame.display.flip()
                clock.tick(FPS)
        else:
            if action["action"] == "defence":
                buttons.empty()
                board.set_view(300, 20, 114)
                pause_btn = Button(icons["pause"], 1205, 10)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 3:
                            board.remove_shield(event.pos)
                        elif event.button == 1:
                            if board.check_count_shields(board.get_points(event.pos)):
                                board.set_shield(event.pos)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if pause_btn.on_hovered(event.pos):
                            settings_flag = True
                screen.fill("#D8DDEF")

                flipped_mark = pygame.transform.flip(wall_mark, True, False)
                text_box_score = TextBox(flipped_mark, 1040, 110)

                set_text(text_box_score, "ОСТАЛОСЬ ЩИТОВ:", 20)
                text_box_10 = TextBox(flipped_mark, 1040, 210)
                text_box_20 = TextBox(flipped_mark, 1040, 310)
                text_box_40 = TextBox(flipped_mark, 1040, 410)

                screen.blit(flipped_mark, (1040, 210))
                screen.blit(flipped_mark, (1040, 310))
                screen.blit(flipped_mark, (1040, 410))

                p10, p20, p40 = board.get_count_shields(10), board.get_count_shields(20), board.get_count_shields(40)
                first, second, third = MAX_F - p10, MAX_S - p20, MAX_T - p40

                set_text(text_box_10, f"ДЛЯ 10: {first}", 40)
                set_text(text_box_20, f"ДЛЯ 20: {second}", 40)
                set_text(text_box_40, f"ДЛЯ 40: {third}", 40)

                text_box_action_title = TextBox(wall_mark, 0, 174)
                text_box_action = TextBox(wall_mark, 0, 274)
                text_box_nickname_title = TextBox(wall_mark, 0, 374)
                text_box_nickname = TextBox(wall_mark, 0, 474)
                screen.blit(wall_mark, (0, 274))
                screen.blit(wall_mark, (0, 474))
                set_text(text_box_action_title, "ДЕЙСТВИЕ:", 40)
                set_text(text_box_nickname_title, "ИМЯ:", 40)
                set_text(text_box_action, "ЗАЩИТА", 30)
                set_text(text_box_nickname, action["player"], 30)

                board.render()
                mouse_pos = pygame.mouse.get_pos()
                if board.get_cell(mouse_pos):
                    board.highlight_cell(mouse_pos)
                if first == 0 and second == 0 and third == 0:
                    continue_btn = Button(icons["continue"], 1196, 640)
                    pressed = pygame.mouse.get_pressed()
                    if pressed[0]:
                        if continue_btn.on_hovered(pygame.mouse.get_pos()):
                            if action["player"] == player1:
                                game_data[player1]["player_board"] = board.board
                                board.fill_board()
                                action["player"] = player2
                                transition()
                            else:
                                game_data[player2]["player_board"] = board.board
                                board.board = game_data[player2]["player_board"]
                                action["player"] = player1
                                action["action"] = "attack"
                                transition()
                    if continue_btn.on_hovered(pygame.mouse.get_pos()):
                        show_tip(continue_btn, "Продолжить")
                check_hovered()
                # Отрисовка
                buttons.draw(screen)
                buttons.update()
                pygame.display.flip()
                clock.tick(FPS)
            else:
                buttons.empty()
                board.set_view(300, 20, 114)
                pause_btn = Button(icons["pause"], 1205, 10)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1 and game_data[action['player']]["count_steps"] != 0:
                            if board.get_cell(event.pos) and board.check_attacked(event.pos):
                                if not board.check_shield(event.pos):
                                    if board.get_points(event.pos):
                                        print(board.board)
                                        game_data[action['player']]['score'] += board.get_points(event.pos)
                                        board.set_attacked(event.pos, True)
                                        game_data[action['player']]["count_steps"] -= 1
                                        success_sound.play()
                                else:
                                    board.set_attacked(event.pos, False)
                                    fail_sound.play()
                                    game_data[action['player']]["count_steps"] -= 1
                        if pause_btn.on_hovered(event.pos):
                            settings_flag = True
                    # Печать "отладочной информации" об игроках в формате .json
                    # elif event.type == pygame.KEYDOWN:
                    #     if event.key == pygame.K_SPACE:
                    #         print(board.board)
                screen.fill("#D8DDEF")

                flipped_mark = pygame.transform.flip(wall_mark, True, False)
                text_box_steps_title = TextBox(flipped_mark, 1040, 174)
                text_box_steps = TextBox(flipped_mark, 1040, 274)
                text_box_score_title = TextBox(flipped_mark, 1040, 374)
                text_box_score = TextBox(flipped_mark, 1040, 474)
                screen.blit(flipped_mark, (1040, 274))
                screen.blit(flipped_mark, (1040, 474))
                set_text(text_box_score_title, "СЧЁТ:", 30)
                set_text(text_box_score, f"{game_data[action['player']]['score']}", 40)
                set_text(text_box_steps_title, "ОСТАЛОСТЬ ХОДОВ:", 20)
                set_text(text_box_steps, f"{game_data[action['player']]['count_steps']}", 40)

                text_box_action_title = TextBox(wall_mark, 0, 174)
                text_box_action = TextBox(wall_mark, 0, 274)
                text_box_nickname_title = TextBox(wall_mark, 0, 374)
                text_box_nickname = TextBox(wall_mark, 0, 474)
                screen.blit(wall_mark, (0, 274))
                screen.blit(wall_mark, (0, 474))
                set_text(text_box_action_title, "ДЕЙСТВИЕ:", 40)
                set_text(text_box_action, "АТАКА", 30)
                set_text(text_box_nickname_title, "ИМЯ:", 40)
                set_text(text_box_nickname, action["player"], 30)

                board.render(attack=True)
                mouse_pos = pygame.mouse.get_pos()
                if board.get_cell(mouse_pos):
                    board.highlight_cell(mouse_pos)
                if game_data[action['player']]["count_steps"] == 0 and action["player"] == player2:
                    continue_btn = Button(icons["continue"], 1196, 640)
                    pressed = pygame.mouse.get_pressed()
                    if pressed[0]:
                        if continue_btn.on_hovered(pygame.mouse.get_pos()):
                            transition()
                            if game_data[player1]["score"] > game_data[player2]["score"]:
                                end_screen(player1)
                                return
                            else:
                                end_screen(player2)
                                return
                    if continue_btn.on_hovered(pygame.mouse.get_pos()):
                        show_tip(continue_btn, "Продолжить")
                if game_data[action['player']]["count_steps"] == 0 and action["player"] == player1:
                    board.set_board(game_data[player1]["player_board"])
                    action["player"] = player2
                    transition()
                check_hovered()
                # Отрисовка
                buttons.draw(screen)
                buttons.update()
                pygame.display.flip()
                clock.tick(FPS)


def ask_names():
    active_box = 1
    player1_name = TextBox(input_box_frame, 52, 310)
    text_input_player1 = ""
    player2_name = TextBox(input_box_frame, 833, 310)
    text_input_player2 = ""
    buttons.empty()
    play_btn = Button(medium_button, 449, 80, "ИГРАТЬ")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player1_name.rect.collidepoint(event.pos):
                    active_box = 1
                elif player2_name.rect.collidepoint(event.pos):
                    active_box = 2
            elif event.type == pygame.MOUSEBUTTONUP:
                if play_btn.on_hovered(event.pos):
                    if text_input_player1 == text_input_player2:
                        warning_window("Имена должны быть разными.")
                    if len(text_input_player1) < MIN_LIMIT_SYMBOLS or len(text_input_player2) < MIN_LIMIT_SYMBOLS:
                        warning_window(f"Минимум {MIN_LIMIT_SYMBOLS} символа в имени")
                    else:
                        return text_input_player1, text_input_player2
            elif event.type == pygame.KEYDOWN:
                if active_box == 1:
                    if event.key == pygame.K_RETURN:
                        if text_input_player1:
                            if len(text_input_player1) < MIN_LIMIT_SYMBOLS or \
                                    len(text_input_player2) < MIN_LIMIT_SYMBOLS:
                                warning_window(f"Минимум {MIN_LIMIT_SYMBOLS} символа в имени")
                            else:
                                active_box = 2
                    if event.key == pygame.K_BACKSPACE:
                        text_input_player1 = text_input_player1[:-1]
                    else:
                        if len(text_input_player1) <= LIMIT_SYMBOLS:
                            if event.unicode in ACCEPTED_SYMBOLS:
                                text_input_player1 += event.unicode
                            elif event.unicode in RUS_SYMBOLS:
                                warning_window("Смените раскладку клавиатуры")
                else:
                    if event.key == pygame.K_BACKSPACE:
                        text_input_player2 = text_input_player2[:-1]
                    else:
                        if len(text_input_player2) <= LIMIT_SYMBOLS:
                            if event.unicode in ACCEPTED_SYMBOLS:
                                text_input_player2 += event.unicode
                            elif event.unicode in RUS_SYMBOLS:
                                warning_window("Смените раскладку клавиатуры")

        screen.blit(ask_bg, (0, 0))
        screen.blit(input_box_frame, (52, 310))
        screen.blit(input_box_frame, (833, 310))
        set_text(player1_name, text_input_player1, font_size=30, color=COLOR_INACTIVE)
        set_text(player2_name, text_input_player2, font_size=30, color=COLOR_INACTIVE)
        if active_box == 1:
            text_rect = set_text(player1_name, text_input_player1,
                                 font_size=30, color=COLOR_ACTIVE, returnable=True)
            pygame.draw.line(screen, COLOR_INACTIVE, (text_rect.right, text_rect.y),
                             (text_rect.right, text_rect.y + 30), 2)
        else:
            text_rect = set_text(player2_name, text_input_player2,
                                 font_size=30, color=COLOR_ACTIVE, returnable=True)
            pygame.draw.line(screen, COLOR_INACTIVE, (text_rect.right, text_rect.y),
                             (text_rect.right, text_rect.y + 30), 2)
        if text_input_player1 and text_input_player2:
            check_hovered()
            buttons.draw(screen)
            buttons.update()
        # Отрисовка
        pygame.display.flip()
        clock.tick(FPS)


def open_help():
    buttons.empty()
    continue_btn = Button(icons["continue"], 1196, 640)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                if continue_btn.on_hovered(event.pos):
                    return
        check_hovered()
        screen.blit(help_window, (0, 0))
        if continue_btn.on_hovered(pygame.mouse.get_pos()):
            show_tip(continue_btn, "Продолжить")
        # Отрисовка
        buttons.draw(screen)
        buttons.update()
        pygame.display.flip()
        clock.tick(FPS)


def create_particles(position, particle_count=20):
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


def end_screen(winner_name):
    win_sound.play()
    timer = 0
    buttons.empty()
    all_sprites.empty()
    screen.fill("#6194a2")
    quit_btn = Button(medium_button, 449, 539, "Главное меню", 50)
    text_surf = pygame.Surface((1234, 345))
    text_surf.fill("#6194a2")
    text_box = TextBox(text_surf, 23, 22)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                if quit_btn.on_hovered(event.pos):
                    return
                create_particles(event.pos, 100)
        screen.fill("#6194a2")
        timer += 1
        check_hovered()
        if timer % 30 == 0:
            for i in range(random.randint(1, 5)):
                create_particles((random.randint(0, SCREEN_WIDTH - 200), random.randint(0, SCREEN_HEIGHT - 200)), 20)
        all_sprites.draw(screen)
        all_sprites.update()
        set_text(text_box, f"ПОБЕДИЛ ИГРОК {winner_name}!", font_size=65)
        # Отрисовка
        buttons.draw(screen)
        buttons.update()
        pygame.display.flip()
        clock.tick(FPS)


def warning_window(error):
    warning_sound.play()
    text_surf = pygame.Surface((400, 70))
    warning_textbox = TextBox(text_surf, 482, 325)
    screen.blit(warning_bg, (389, 314))
    set_text(warning_textbox, error, font_size=20)
    pygame.display.flip()
    clock.tick(FPS)
    pygame.time.delay(2000)


def extend_leaderboard(player1, player2):
    pass


# {(0, 0): {'shield': False, 'attacked': (True, True), 'points': 10},
# (1, 0): {'shield': True, 'attacked': (True, False), 'points': 10},
# (2, 0): {'shield': True, 'attacked': (True, False), 'points': 10},
# (3, 0): {'shield': False, 'attacked': (True, True), 'points': 10},
# (4, 0): {'shield': False, 'attacked': (True, True), 'points': 10},
# (5, 0): {'shield': False, 'attacked': (True, True), 'points': 10},
# (0, 1): {'shield': False, 'attacked': (True, True), 'points': 10},
# (1, 1): {'shield': False, 'attacked': (False, False), 'points': 20},
# (2, 1): {'shield': False, 'attacked': (True, True), 'points': 20},
# (3, 1): {'shield': False, 'attacked': (True, True), 'points': 20},
# (4, 1): {'shield': True, 'attacked': (False, False), 'points': 20},
# (5, 1): {'shield': True, 'attacked': (True, False), 'points': 10},
# (0, 2): {'shield': True, 'attacked': (True, False), 'points': 10},
# (1, 2): {'shield': True, 'attacked': (False, False), 'points': 20},
# (2, 2): {'shield': True, 'attacked': (True, False), 'points': 40},
# (3, 2): {'shield': True, 'attacked': (True, False), 'points': 40},
# (4, 2): {'shield': False, 'attacked': (True, True), 'points': 20},
# (5, 2): {'shield': True, 'attacked': (True, False), 'points': 10},
# (0, 3): {'shield': False, 'attacked': (False, False), 'points': 10},
# (1, 3): {'shield': True, 'attacked': (False, False), 'points': 20},
# (2, 3): {'shield': False, 'attacked': (True, True), 'points': 40},
# (3, 3): {'shield': True, 'attacked': (True, False), 'points': 40},
# (4, 3): {'shield': False, 'attacked': (True, True), 'points': 20},
# (5, 3): {'shield': False, 'attacked': (True, True), 'points': 10},
# (0, 4): {'shield': False, 'attacked': (False, False), 'points': 10},
# (1, 4): {'shield': True, 'attacked': (False, False), 'points': 20},
# (2, 4): {'shield': True, 'attacked': (False, False), 'points': 20},
# (3, 4): {'shield': True, 'attacked': (False, False), 'points': 20},
# (4, 4): {'shield': True, 'attacked': (True, False), 'points': 20},
# (5, 4): {'shield': True, 'attacked': (True, False), 'points': 10},
# (0, 5): {'shield': False, 'attacked': (False, False), 'points': 10},
# (1, 5): {'shield': True, 'attacked': (False, False), 'points': 10},
# (2, 5): {'shield': False, 'attacked': (False, False), 'points': 10},
# (3, 5): {'shield': True, 'attacked': (False, False), 'points': 10},
# (4, 5): {'shield': False, 'attacked': (True, True), 'points': 10},
# (5, 5): {'shield': True, 'attacked': (True, False), 'points': 10}}
