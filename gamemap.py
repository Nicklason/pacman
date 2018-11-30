""" Map klassen """

import pygame
import math

class Map():    
    EMPTY = 0
    WALL = 1
    POINT = 2
    PLAYER = 3
    RED_GHOST = 4
    CYAN_GHOST = 5
    PINK_GHOST = 6
    ORANGE_GHOST = 7

    """ Initialiserer map klasse """
    def __init__(self, file_name):
        image = pygame.image.load("maps/{0}".format(file_name))

        self.removed_points = 0

        self.construct(image)

    def construct(self, image):
        """ Bruget det indlæste billede til at lave en matrice over alle  """
        self.width = image.get_width()
        self.height = image.get_height()

        points = 0

        matrix = []
        for x in range(0, self.width):
            matrix.append([])
            for y in range(0, self.height):
                pixel = image.get_at((x, y))
                r, g, b, a = pixel

                if a is 0:
                    matrix[x].append(Map.EMPTY)
                elif r is 0 and g is 0 and b is 0:
                    # Mur
                    matrix[x].append(Map.WALL)
                elif r is 255 and g is 255 and b is 0:
                    # Ost
                    matrix[x].append(Map.POINT)
                    points += 1
                elif r is 255 and g is 80 and b is 0:
                    # Spiller
                    matrix[x].append(Map.PLAYER)
                elif r is 255 and g is 0 and b is 0:
                    # Rødt spøgelse
                    matrix[x].append(Map.RED_GHOST)
                elif r is 0 and g is 255 and b is 255:
                    # Tyrkis spøgelse
                    matrix[x].append(Map.CYAN_GHOST)
                elif r is 255 and g is 192 and b is 203:
                    # Pink spøgelse
                    matrix[x].append(Map.PINK_GHOST)
                elif r is 255 and g is 165 and b is 0:
                    # Orange spøgelse
                    matrix[x].append(Map.ORANGE_GHOST)
                else:
                    # Intet match = tomt
                    matrix[x].append(Map.EMPTY)

        self.total_points = points
        self.matrix = matrix
    
    def inside_grid(self, pos):
        """ Find ud af om en position er helt inde i grid """
        grid = self.get_grid(pos)
        grid_pos = self.grid_to_pos(grid)

        inside = self.pos_match(pos, grid_pos)
        return inside

    def pos_match(self, pos1, pos2):
        """ Tjek om positioner matcher """
        return pos1[0] == pos2[0] and pos1[1] == pos2[1]
    
    def grid_to_pos(self, grid):
        """ Konverter grid til position """
        x = grid[0]*16
        y = grid[1]*16

        return [x,y]
    
    def get_grid(self, pos, offset=0):
        """ Retunerer position i grid """
        x = math.floor((pos[0]+offset)/16)
        y = math.floor((pos[1]+offset)/16)

        return [x, y]
    
    def grid_type(self, pos, convert=False):
        """ Retunerer grid type """

        grid = pos
        if convert is True:
            grid = self.get_grid(pos)

        x = grid[0]
        y = grid[1]
        
        if -1 < x < self.width and -1 < y < self.height:
            return self.matrix[x][y]

        return None

    def get_player_pos(self):
        """ Få spillerens start position """
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.matrix[x][y] is Map.PLAYER:
                    return [x, y]
        
        return None

    def remove_point(self, grid):
        """ Fjerner et point fra banen ved at lave det om til en tom plads """
        self.matrix[grid[0]][grid[1]] = Map.EMPTY
        self.removed_points += 1
