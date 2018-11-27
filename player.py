import pygame

class Player():
    def __init__(self, pos):
        # Positionen skal ganges med 16, ligger 1 til for at centrere mellem væggene
        pos[0] = pos[0]*16+1
        pos[1] = pos[1]*16+1

        self.pos = pos
        self.direction = 3 # Går mod vest
        self.heading = 3 # Vil prøve at gå mod vest når man kan
        self.stopped = False  # Hvis spilleren er stødt på en mur
        self.speed = 1

        # Kan spilleren bevæge sig op, ned, højre og venstre?

    def tick(self, pressed):
        if self.stopped:
            return
        
        if pressed[pygame.K_UP]:
            self.direction = 0
        elif pressed[pygame.K_DOWN]:
            self.direction = 1
        elif pressed[pygame.K_RIGHT]:
            self.direction = 2
        elif pressed[pygame.K_LEFT]:
            self.direction = 3

        if self.direction is 0:
            # Spilleren bevæger sig mod nord, læg farten til y
            self.pos[1] -= self.speed
        elif self.direction is 1:
            # Spilleren bevæger sig mod syd, træk farten fra y
            self.pos[1] += self.speed
        elif self.direction is 2:
            # Spilleren bevæger sig mod øst, læg farten til i x
            self.pos[0] += self.speed
        elif self.direction is 3:
            # Spilleren bevæger sig mod vest, træk farten fra i x
            self.pos[0] -= self.speed
        
