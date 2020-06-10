import pygame
from inputbox import InputBox


# Displays static text on window.
def display_player_text(window, font_size, text, font_color, placement):
    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", font_size)
    words = font.render(text, True, font_color)
    window.blit(words, placement)


# Makes the window input boxes appear and checks high-level inputs.
def window_boxes():
    window = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("chessApp")
    window.fill((128, 0, 0))

    clock = pygame.time.Clock()
    input_box1 = InputBox(150, 200, 140, 32)
    input_box2 = InputBox(150, 400, 140, 32)
    input_boxes = [input_box1, input_box2]

    display_player_text(window, 30, ("Enter your names"), (0, 255, 0), (25, 0))
    display_player_text(window, 30, ("Player 1: "), (0, 255, 0), (25, 200))
    display_player_text(window, 30, ("Player 2: "), (0, 255, 0), (25, 400))

    button = pygame.Rect(300, 500, 115, 35)
    pygame.draw.rect(window, (0, 0, 0), button)
    font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 30)
    text = font.render('SUBMIT', True, (255, 255, 255))
    window.blit(text, button)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    done = True
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.draw(window)

        pygame.display.flip()
        clock.tick(30)

    for box in input_boxes:
        print(box.text)
