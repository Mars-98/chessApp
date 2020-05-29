import pygame, sys


class Get_names:
    pygame.init()
    #pygame.quit()

    def addText(self):
        window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("chessApp")
        font = pygame.font.Font(None, 32)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(100, 100, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('grey')
        color = color_inactive
        active = False
        text = ''
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(text)
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            window.fill((128, 0, 0))
            self.rectDisplay(window, (128, 128, 128), (80, 80), (450, 450))
            self.rectDisplay(window, (0, 0, 0), (95, 90), (420, 120))
            self.displayPlayertext(window, 30, ("Enter your names"), (255, 0, 0), (0, 0, 0), (305, 150))
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            window.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(window, color, input_box, 2)

            pygame.display.flip()
            clock.tick(30)

    def rectDisplay(self, window, rect_color, rect_place, rect_width_height):
        pygame.draw.rect(window, rect_color, (rect_place, rect_width_height))



    def displayPlayertext(self, window, font_size, text, font_color, box_color, placement):
        font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", font_size)
        text = font.render(text, True, font_color, box_color)
        text_rect = text.get_rect()
        text_rect.center = placement
        window.blit(text, text_rect)

