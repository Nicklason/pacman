import pygame

class Player():
    def __init__(self, pos):
        # Positionen skal ganges med 16, ligger 1 til for at centrere mellem væggene
        pos[0] = pos[0]*16
        pos[1] = pos[1]*16

        self.pos = pos
        self.direction = 3 # Går mod vest
        self.heading = 3 # Vil prøve at gå mod vest når man kan
        self.stopped = False  # Hvis spilleren er stødt på en mur
        self.speed = 1 # Spillet vil ikke virke ordenligt hvis man ændre på farten

    def tick(self, pressed):
        # Hvilken vej som spilleren vil gå
        if pressed[pygame.K_UP]:
            self.heading = 0
        elif pressed[pygame.K_DOWN]:
            self.heading = 1
        elif pressed[pygame.K_RIGHT]:
            self.heading = 2
        elif pressed[pygame.K_LEFT]:
            self.heading = 3

        # Tjek om spilleren kan gå den vej
        if self.above is False and self.heading is 0:
            self.direction = 0
        elif self.below is False and self.heading is 1:
            self.direction = 1
        elif self.right is False and self.heading is 2:
            self.direction = 2
        elif self.left is False and self.heading is 3:
            self.direction = 3

        # Gå den vej
        if self.direction is 0 and self.above is False:
            # Spilleren bevæger sig mod nord, læg farten til y
            self.pos[1] -= self.speed
            self.stopped = False
        elif self.direction is 1 and self.below is False:
            # Spilleren bevæger sig mod syd, træk farten fra y
            self.pos[1] += self.speed
            self.stopped = False
        elif self.direction is 2 and self.right is False:
            # Spilleren bevæger sig mod øst, læg farten til i x
            self.pos[0] += self.speed
            self.stopped = False
        elif self.direction is 3 and self.left is False:
            # Spilleren bevæger sig mod vest, træk farten fra i x
            self.pos[0] -= self.speed
            self.stopped = False
        else:
            self.stopped = True
    
