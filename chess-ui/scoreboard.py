import pygame

# creates scoreboard for chess window
class chessScoreboard:
    player1 = ''
    player2 = ''
    player1_score = 0
    player2_score = 0

    # Make the scoreboard with given player names
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    # function for creating the scoreboard rect: (window, (color RGB), ((placement x, y), (width, height)))
    # calls designs (displaying rectangles and text) to display on the scoreboard
    def createScoreboard(self, window):
        pygame.draw.rect(window, (128, 128, 128), ((430, 10), (150, 120)))
        pygame.draw.rect(window, (0, 0, 0), ((440, 15), (130, 30)))
        font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 23)
        text = font.render('Score', True, (255, 0, 0), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (505, 30)
        window.blit(text, text_rect)
        self.makePlayerName(window, 15, self.player1, (0, 0, 0), (128, 128, 128), (470, 62))
        self.makePlayerName(window, 15, self.player2, (0, 0, 0), (128, 128, 128), (540, 62))
        self.scoreDisplay(window, (0, 0, 0), (447, 73), (40, 40))
        self.scoreDisplay(window, (0, 0, 0), (517, 73), (40, 40))
        self.makePlayerName(window, 20, str(self.player1_score), (255, 0, 0), (0, 0, 0), (467, 93))
        self.makePlayerName(window, 20, str(self.player2_score), (255, 0, 0), (0, 0, 0), (537, 93))

    # Makes text for the player name and their score
    def makePlayerName(self, window, font_size, player_name, font_color, box_color, placement):
        font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", font_size)
        text = font.render(player_name, True, font_color, box_color)
        text_rect = text.get_rect()
        text_rect.center = placement
        window.blit(text, text_rect)

    # Draws rectangles for the score
    def scoreDisplay(self, window, rect_color, rect_place, rect_width_height):
        pygame.draw.rect(window, rect_color, (rect_place, rect_width_height))