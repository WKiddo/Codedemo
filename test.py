import pygame
from pygame.locals import *

colors = {"blue_bg": "#1D1D2E", "race_yellow": "#f5d365", "text_red": "#FB8F85", "text_green": "#B1FEB1"}

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 36)

shapes = []

menu = ["B1", "B2", "B3", "Quit"]
selected_option = None

def B1():
    pygame.quit()
    quit()


def B2():
    pygame.quit()
    quit()

def B3():
    global shapes
    drawing = False
    running = True
    start_pos = None
    end_pos = None

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = pygame.mouse.get_pos()
                    end_pos = start_pos  # Update end_pos with start_pos initially
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    end_pos = pygame.mouse.get_pos()
                    shape = (start_pos, end_pos)
                    shapes.append(shape)
            elif event.type == KEYDOWN:
                if event.key == K_z:
                    if len(shapes) > 0:
                        shapes.pop()
                elif event.key == K_x and pygame.key.get_mods() & KMOD_CTRL:
                    shapes.clear()

        screen.fill(colors["blue_bg"])

        if drawing:
            end_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, colors["race_yellow"], start_pos, end_pos, 2)

        for shape in shapes:
            pygame.draw.line(screen, colors["race_yellow"], shape[0], shape[1], 2)

        pygame.display.flip()







def main_menu():
    global shapes
    global selected_option
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, option in enumerate(menu):
                        text_surface = font.render(option, True, colors["text_red"])
                        text_rect = text_surface.get_rect(center=(800 // 2, 600 // 2 + i * 40))
                        if text_rect.collidepoint(mouse_pos):
                            selected_option = i
                            return

        screen.fill(colors["blue_bg"])

        for i, option in enumerate(menu):
            if i == selected_option:
                text_surface = font.render(option, True, colors["text_red"])
            else:
                text_surface = font.render(option, True, colors["text_green"])
            text_rect = text_surface.get_rect(center=(800 // 2, 600 // 2 + i * 40))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()


while True:
    main_menu()
    if selected_option == 0:
        B1()
    elif selected_option == 1:
        B2()
    elif selected_option == 2:
        B3()
    elif selected_option == 3:
        quit_game()

pygame.display.update()