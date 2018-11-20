import math
from random import randint
from gamemap import Map

class Game:
    def __init__(self):
        self.state = 0
    
    def load_map(self, file_name):
        self.map = Map(file_name)
    
    def tick(self, pg, pressed):
        """ if self.state == 1:
            if pressed[pg.K_UP]:
                self.y -= 3
            if pressed[pg.K_DOWN]:
                self.y += 3
            if pressed[pg.K_LEFT]:
                self.x -= 3
            if pressed[pg.K_RIGHT]:
                self.x += 3
            if math.sqrt((self.target[0] - self.x)**2 + (self.target[1] - self.y)**2) < 40:
                self.points += 1
                self.target = [
                    randint(0, 800), randint(0, 600)] """
       

    def start_game(self):
        if self.state == 0:
            self.state = 1
            """ self.points = 0
            self.x = 100
            self.y = 100
            self.target = [randint(0, 800), randint(0, 600)] """

    def end_game(self):
        if self.state > 0:
            self.state = 0

    def toggle_pause(self):
        if self.state == 1:
            self.state = 2
        else:
            self.state = 1

    def started(self):
        # Jeg har ikke lavet denne funktion
        # return self.state > 0
        if self.state > 0:
            return True
        else:
            return False
