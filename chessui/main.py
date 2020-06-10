from window import ChessWindow
import player_names
import pygame

pygame.init()
# Take name window here and grab the values
player_names.window_boxes()

# Then this createWindow() remains, and uses the player names
# from the form to place in the window.
ChessWindow().createWindow()
