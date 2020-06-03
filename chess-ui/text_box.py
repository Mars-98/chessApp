import pygame, sys


class Get_names:
    pygame.init()
    pygame.quit()

    def addTextWindow(self):
        window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("chessApp")
        window.fill((128, 0, 0))
        play_game = True
        self.rectDisplay(window, (128, 128, 128), (80, 80), (450, 450))
        self.rectDisplay(window, (255, 255, 255), (100, 275), (200, 32))
        self.displayPlayertext(window, 22, ("Player 1"), (0, 0, 0), (128, 128, 128), (150, 260))
        self.rectDisplay(window, (0, 0, 0), (95, 90), (420, 120))
        self.displayPlayertext(window, 30, ("Enter your names"), (255, 0, 0), (0, 0, 0), (305, 150))
        self.makeTextBox(window, (100, 275), (200, 32))
        #font = pygame.font.Font(None, 28)
        #clock = pygame.time.Clock()
        #input_box = pygame.Rect(100, 275, 200, 32)
        #color_inactive = pygame.Color('lightskyblue3')
        #color_active = pygame.Color('black')
        #color = color_inactive
        #active = False
        #text = ''


        while play_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_game = False
            pygame.display.flip()
                #if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    #if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        #active = not active
                    #else:
                        #active = False
                    # Change the current color of the input box.
                    #color = color_active if active else color_inactive
                #if event.type == pygame.KEYDOWN:
                    #if active:
                        #if event.key == pygame.K_RETURN:
                            #print(text)
                            #text = ''
                        #elif event.key == pygame.K_BACKSPACE:
                            #text = text[:-1]
                        #else:
                            #text += event.unicode

            #window.fill((128, 0, 0))
            #self.rectDisplay(window, (128, 128, 128), (80, 80), (450, 450))
            #self.rectDisplay(window, (255, 255, 255), (100, 275), (200, 32))
            #self.displayPlayertext(window, 22, ("Player 1"), (0, 0, 0), (128, 128, 128), (150, 260))
            #self.rectDisplay(window, (0, 0, 0), (95, 90), (420, 120))
            #self.displayPlayertext(window, 30, ("Enter your names"), (255, 0, 0), (0, 0, 0), (305, 150))
            # Render the current text.
            #txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            #width = max(200, txt_surface.get_width()+10)
            #input_box.w = width
            # Blit the text.
            #window.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            #pygame.draw.rect(window, color, input_box, 2)

            #pygame.display.flip()
            #clock.tick(30)

    def rectDisplay(self, window, rect_color, rect_place, rect_width_height):
        pygame.draw.rect(window, rect_color, (rect_place, rect_width_height))



    def displayPlayertext(self, window, font_size, text, font_color, box_color, placement):
        font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", font_size)
        text = font.render(text, True, font_color, box_color)
        text_rect = text.get_rect()
        text_rect.center = placement
        window.blit(text, text_rect)

    def makeTextBox(self, window, rect_place, rect_width_height):
        font = pygame.font.Font(None, 28)
        clock = pygame.time.Clock()
        input_box = pygame.Rect(rect_place, rect_width_height)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('black')
        color = color_inactive
        active = False
        text = ""
        for event in pygame.event.get():
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
                pygame.display.flip()
                txt_surface = font.render(text, True, color)
                width = max(200, txt_surface.get_width()+10)
                input_box.w = width
                window.blit(txt_surface, (input_box.x+5, input_box.y+5))
                # Blit the input_box rect.
                pygame.draw.rect(window, color, input_box, 2)
                pygame.display.flip()
                clock.tick(30)