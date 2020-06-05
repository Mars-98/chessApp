import pygame, sys


class Get_names:
    pygame.init()
    pygame.quit()

    def addTextWindow(self):
        window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("chessApp")
        window.fill((128, 0, 0))
        done = False
        self.rectDisplay(window, (128, 128, 128), (80, 80), (450, 450))
        self.rectDisplay(window, (255, 255, 255), (100, 275), (200, 32))
        self.displayPlayertext(window, 22, ("Player 1"), (0, 0, 0), (128, 128, 128), (150, 260))
        self.rectDisplay(window, (0, 0, 0), (95, 90), (420, 120))
        self.displayPlayertext(window, 30, ("Enter your names"), (255, 0, 0), (0, 0, 0), (305, 150))
        self.makeTextBox(window, (100, 275), (200, 32))
        clock = pygame.time.Clock()
        input_box1 = InputBox(100, 100, 140, 32)
        input_box2 = InputBox(100, 300, 140, 32)
        input_boxes = [input_box1, input_box2]
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

        #window.fill((128, 0, 0))
            for box in input_boxes:
                box.draw(window)

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
