import numpy
import pygame
import random
from astar import astar
from gamemap import Map

class Ghost():
    def __init__(self, pos, tile_type):
        pos[0] = pos[0]*16
        pos[1] = pos[1]*16

        self.pos = pos
        self.direction = 3
        self.type = tile_type  # Spøgelsets farve
        self.stopped = False
        self.speed = 1
        self.state = 0
    
    def load_matrix(self, map_matrix):
        """ Gemmer matrice til pathfinding """
        self.matrix = numpy.array(map_matrix)

    def tick(self, player):
        """ Kaldes hvert tick """

        # Hvilken algoritme skal spøgelset bruge?
        if self.state == 0:
            self.scatter()
        else:
            self.chase(player)

        # Ændre kun path hvis retningen ikke er modsat af hvad man går nu
    
    def chase(self, player):
        """ Går direkte efter spilleren """
        targetgrid = Map.get_grid(player.pos)
        nexttarget = self.pathfinding(targetgrid)
        if nexttarget is None:
            return

        self.move(nexttarget)
    
    def scatter(self):
        #if self.type is Map.RED_GHOST:
        # Bevæg sig mod det tile som er længst til højre

        # Find det tile som er tættest på hjørne
        # Antager at tiles i hjørnerne aldrig er vægge og man kan komme hen til dem

        #currentgrid = Map.get_grid(self.pos)
        targetgrid = [len(self.matrix)-2, 1]
        nexttarget = self.pathfinding(targetgrid)
        if nexttarget == None:
            self.state = 1
        else:
            self.move(nexttarget)

    def pathfinding(self, targetgrid):
        """ Find den korteste vej """
        currentgrid = Map.get_grid(self.pos)

        """ matrix = self.matrix.copy()
        if hasattr(self, "prev_grid"):
            # Bloker tile som er bag spøgelse for at den ikke bevæge sig modsat
            # Gem den tile som spøgelset sidst var inde i
            matrix[self.prev_grid[0]][self.prev_grid[1]] = 1 """

        path = astar(self.matrix, tuple(currentgrid), tuple(targetgrid))
        if path is False or len(path) is 0:
            return None

        nextgrid = list(path[-1])
        nextpos = Map.grid_to_pos(nextgrid)

        # Path må kun ændre sig hvis man ikke kommer til at bevæge sig den modsatte vej af hvad man gør nu

        
        return nextpos
        
    def move(self, target):
        """ Vil prøve at bevæge sig til en bestemt position"""

        if Map.inside_grid(self.pos) is True:
            self.prev_grid = Map.get_grid(self.pos)

        if Map.inside_grid(self.pos) is False and Map.axis_aligned(self.pos, target) is False:
            # Hvis man ikke er inde i en grid, og x- eller y-aksen ikke er den samme, så gå helt ind i den grid man er i
            # Dette tvinger spøgelserne til kun at bevæge sig inde i tiles
            currentgrid = Map.get_grid(self.pos)
            target = Map.grid_to_pos(currentgrid)
        
        if self.pos[0] < target[0]:
            self.pos[0] = target[0] if self.pos[0] + self.speed > target[0] else self.pos[0] + self.speed
            self.direction = 3
        elif self.pos[0] > target[0]:
            self.pos[0] = target[0] if self.pos[0] - self.speed < target[0] else self.pos[0] - self.speed
            self.direction = 4
        elif self.pos[1] < target[1]:
            self.pos[1] = target[1] if self.pos[1] + self.speed > target[1] else self.pos[1] + self.speed
            self.direction = 1
        elif self.pos[1] > target[1]:
            self.pos[1] = target[1] if self.pos[1] - self.speed < target[1] else self.pos[1] - self.speed
            self.direction = 0

