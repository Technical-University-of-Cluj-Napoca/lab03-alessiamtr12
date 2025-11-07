import pygame

# some global constants
WIDTH = 800
HEIGHT = 800

# colors.
# if you find it more suitable, change this dictionary to standalone constants like: RED = (255, 0, 0)
COLORS = {
    # 'RED': (19, 42, 19),           # closed nodes
    # 'GREEN': (236, 243, 158),         # open nodes
    # 'BLUE': (188, 108, 37),          # start node
    # 'YELLOW': (255, 255, 0),      # end node
    # 'WHITE': (255, 255, 255),     # unvisited nodes
    # 'BLACK': (0, 0, 0),           # barrier
    # 'PURPLE': (128, 0, 128),      # path
    # 'ORANGE': (255, 165 ,0),      # nodes being considered
    # 'GREY': (128, 128, 128),      # grid lines
    # 'TURQUOISE': (64, 224, 208)   # neighbor nodes


    #kept the names so i dont have to change them in spot
    'RED': (220, 210, 160),       # closed nodes (Dark Beige)
    'GREEN': (240, 199, 132),     # open nodes (Light Gold)
    'BLUE': (64, 224, 208),      # start node (Gold)
    'YELLOW': (158, 42, 43),      # end node (Deep Red)
    'WHITE': (255, 243, 176),     # unvisited nodes (Pale Yellow)
    'BLACK': (51, 92, 103),       # barrier (Dark Teal)
    'PURPLE': (84, 11, 14),       # path (Very Dark Red)
    'ORANGE': (240, 199, 132),    # nodes being considered (Light Gold)
    'GREY': (170, 184, 188),      # grid lines (Light Teal-Grey)
    'TURQUOISE': (240, 199, 132) # neighbor nodes (Light Gold)

}