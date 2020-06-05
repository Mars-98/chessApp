from window import chessWindow
from text_box import Get_names
import pygame
pygame.init()
# Take name window here and grab the values
rect_display = Get_names
rect_display.addTextWindow()

# Then thise createWindow() remains, and uses the player names from the form to place in the window
chessWindow.createwindow()
  