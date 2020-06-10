import pygame


# A textbox where the user can enter their name.
class InputBox:

    # The rectangle where the input box resides.
    rectangle = None

    # Current color of the input box.
    color = pygame.Color('white')

    # Current text in the input box.
    text = ''

    # The pygame surface the text resides on.
    txt_surface = None

    # If this input box is active or not.
    active = False

    # Constructor of inputbox
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 28)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    # Where the input box changes color and the saves the keys
    # the user has pressed.
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = pygame.Color('black') if self.active else pygame.Color('white')
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

    # Redraws the boxes based on colors and text inside
    def draw(self, window):
        # Blit the text.
        window.blit(self.txt_surface, (self.rect.x, self.rect.y))
        # Blit the rect.
        pygame.draw.rect(window, self.color, self.rect, 2)