import pygame

class InputBox:

    color_inactive = pygame.Color('white')

    color_active = pygame.Color('black')

    rectangle = None

    text = ''

    txt_surface = None

    active = False

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.color_inactive
        self.text = text
        self.font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 28)
        self.txt_surface = self.font.render(text, True, self.color)
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
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key != pygame.K_BACKSPACE \
                        and event.key != pygame.K_BACKSLASH \
                        and len(self.text) < 9:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, window):
        # Blit the text.
        window.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(window, self.color, self.rect, 2)