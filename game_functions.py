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
                return_btn = Button(icons["black_cross"], 854, 130)
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
                set_text(sound_textbox, f"{int(volume * 100)}", 50)
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
            rating_btn = Button(icons["cup"], 1150, 37)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONUP:
                    if start_btn.on_hovered(event.pos):
                        transition()
                        p1_name, p2_name = ask_names()
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
    board = Shields(6, 6)
    volume = 0.2
    settings_flag = False
    help_flag = False
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
                return_btn = Button(icons["black_cross"], 854, 130)
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
                set_text(sound_textbox, f"{int(volume * 100)}", 50)
                buttons.update()
                # Отрисовка
                pygame.display.flip()
                clock.tick(FPS)
        else:
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
                        if board.check_shields(board.get_points(event.pos)):
                            board.set_shield(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if pause_btn.on_hovered(event.pos):
                        settings_flag = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print(board.board)
            screen.fill("#8FF6FF")
            flipped_mark = pygame.transform.flip(wall_mark, True, False)
            text_box_remaining = TextBox(flipped_mark, 1040, 110)
            set_text(text_box_remaining,
                     "Осталось щитов:", 25)
            text_box_10 = TextBox(flipped_mark, 1040, 210)
            text_box_20 = TextBox(flipped_mark, 1040, 310)
            text_box_40 = TextBox(flipped_mark, 1040, 410)
            screen.blit(flipped_mark, (1040, 210))
            screen.blit(flipped_mark, (1040, 310))
            screen.blit(flipped_mark, (1040, 410))
            set_text(text_box_10,
                     f"Для 10: {MAX_F - board.get_count_shields(10)}", 40)
            set_text(text_box_20,
                     f"Для 20: {MAX_S - board.get_count_shields(20)}", 40)
            set_text(text_box_40,
                     f"Для 40: {MAX_T - board.get_count_shields(40)}", 40)
            check_hovered()
            board.render()
            mouse_pos = pygame.mouse.get_pos()
            if board.get_cell(mouse_pos):
                board.highlight_cell(mouse_pos)
            buttons.draw(screen)
            buttons.update()
            # Отрисовка
            pygame.display.flip()
            clock.tick(FPS)


def ask_names():
    active_box = 1
    player1_name = TextBox(input_box_frame, 149, 310)
    text_input_player1 = ""
    player2_name = TextBox(input_box_frame, 831, 310)
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
                    return text_input_player1, text_input_player2
            elif event.type == pygame.KEYDOWN:
                if active_box == 1:
                    if event.key == pygame.K_BACKSPACE:
                        text_input_player1 = text_input_player1[:-1]
                    else:
                        if len(text_input_player1) <= LIMIT_SYMBOLS:
                            text_input_player1 += event.unicode
                else:
                    if event.key == pygame.K_BACKSPACE:
                        text_input_player2 = text_input_player2[:-1]
                    else:
                        if len(text_input_player2) <= LIMIT_SYMBOLS:
                            text_input_player2 += event.unicode
        screen.blit(ask_bg, (0, 0))
        screen.blit(input_box_frame, (149, 310))
        screen.blit(input_box_frame, (831, 310))
        if active_box == 1:
            text_rect = set_text(player1_name, text_input_player1, font_size=30, color=COLOR_ACTIVE, returnable=True)
            pygame.draw.line(screen, COLOR_INACTIVE, (text_rect.right, text_rect.y),
                             (text_rect.right, text_rect.y + 30), 2)
            set_text(player2_name, text_input_player2, font_size=30, color=COLOR_INACTIVE)
        else:
            set_text(player1_name, text_input_player1, font_size=30, color=COLOR_INACTIVE)
            text_rect = set_text(player2_name, text_input_player2, font_size=30, color=COLOR_ACTIVE, returnable=True)
            pygame.draw.line(screen, COLOR_INACTIVE, (text_rect.right, text_rect.y),
                             (text_rect.right, text_rect.y + 30), 2)
        if text_input_player1 and text_input_player2:
            check_hovered()
            buttons.draw(screen)
            buttons.update()
        # Отрисовка
        pygame.display.flip()
        clock.tick(FPS)
