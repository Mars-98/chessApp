import pygame
from input_boxes import InputBox

class Box:


    def __init__(self, x, y, w, h, color_inactive, text='', FONT):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color_inactive
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = color_active if self.active else color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)


    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, window):
        # Blit the text.
        window.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(window, self.color, self.rect, 2)

    def rectDisplay(self, window, rect_color, rect_place, rect_width_height):
        pygame.draw.rect(window, rect_color, (rect_place, rect_width_height))



    def displayPlayertext(self, window, font_size, text, font_color, box_color, placement):
        font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", font_size)
        text = font.render(text, True, font_color, box_color)
        text_rect = text.get_rect()
        text_rect.center = placement
        window.blit(text, text_rect)

