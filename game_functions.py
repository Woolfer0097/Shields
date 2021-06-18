from game_classes import *


# Функция запуска начального экрана
def start_screen():
    volume = 0.2
    settings_flag = False
    rating_flag = False
    pygame.mixer.music.load("./data/sounds/bg.mp3")
    pygame.mixer.music.play(-1)
    while True:
        if settings_flag:
            # Настройки
            buttons.empty()
            volume_off_btn = Button(icons["volume_off"], 485, 327)
            volume_down_btn = Button(icons["volume_down"], 608, 327)
            volume_up_btn = Button(icons["volume_up"], 730, 327)
            return_btn = Button(icons["black_cross"], 766, 470)
            sound_box = pygame.Surface((262, 78))
            sound_box.fill(WHITE)
            sound_textbox = TextBox(sound_box, 470, 470)
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
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    settings_flag = False
            pygame.mixer.music.set_volume(volume)
            check_hovered()
            # Отрисовка нужных изображений
            screen.blit(blurred_bg, (0, 0))
            screen.blit(settings_window, (394, 162))
            # pygame.display.set_mode()
            buttons.draw(screen)
            all_sprites.draw(screen)
            set_text(sound_textbox, f"ЗВУК: {int(volume * 100)}", 50, BLACK)
            buttons.update()
            # Отрисовка
            pygame.display.flip()
            clock.tick(FPS)
        else:
            # Начальный экран
            buttons.empty()
            start_btn = Button(medium_button, 449, 314, "ИГРАТЬ")
            settings_btn = Button(long_button, 389, 447, "НАСТРОЙКИ")
            exit_btn = Button(medium_button, 449, 580, "ВЫХОД")
            rating_btn = Button(icons["cup"], 1150, 37)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONUP:
                    if start_btn.on_hovered(event.pos):
                        return
                    if rating_btn.on_hovered(event.pos):
                        info_flag = True
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
