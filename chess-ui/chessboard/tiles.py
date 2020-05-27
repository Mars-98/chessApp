class Tiles:
    tile_map = [[]]
    distance_from_center = 300
    
    def __init__(self, window):
        color_black = False
        for length in range():
            for width in range():
                if color_black:
                    self.tile_map[length][width] = pygame.draw.rect(window, (0,0,0), ((300-length*10, 300-width*10), (10,10)))
                else:
                    self.tile_map[length][width] = pygame.draw.rect(window, (0,0,0), ((300-length*10, 300-width*10), (10,10)))
                color_black = not color_black
