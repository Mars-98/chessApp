from window import chessWindow
from text_box import Get_names
 
# Take name window here and grab the values
# Below are commented out function calls for getting player names
rect_display = Get_names()
rect_display.addText()

# Then thise createWindow() remains, and uses the player names from the form to place in the window

chessWindow.createwindow()