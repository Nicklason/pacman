""" Viewer klasse """

import pygame
from gamemap import Map

class Viewer():
    def __init__(self, game):
        """ Initialiserer viewer klasse """
        self.game = game

        pygame.init()
        self.font = pygame.font.SysFont("monospace", 15)

        sheet = pygame.image.load("sprites/entities.png")
        self.sprites = []
        rects = [(33,1,13,13), (1,33,13,13), (17,33,13,13), (1,48,13,13), (17,48,13,13), (1,17,13,13), (17,17,13,13), (1,1,13,13), (17,1,13,13)]
        for r in rects:
            # https://gamedev.stackexchange.com/questions/47901/pygame-set-colorkey-transparency-issues
            image = pygame.Surface(pygame.Rect(r).size, pygame.SRCCOLORKEY, 32)
            transColor = image.get_at((0,0))
            image.set_colorkey(transColor)
            image.blit(sheet, (0, 0), pygame.Rect(r))
            self.sprites.append(image)

    def start_clock(self):
        """ Starter spillet """
        self.screen = pygame.display.set_mode((self.game.map.width * 16, self.game.map.height * 16))
        pygame.display.set_caption("Pacman")
        clock = pygame.time.Clock()

        self.running = True

        while self.running:
            self.tick()
            clock.tick(60)
    
    def tick(self):
        """ Kaldes hver iteration mens spillet køre """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.game.toggle_pause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.game.state is 1:
                    self.game.end_game()
                else:
                    self.game.start_game()

        pressed = pygame.key.get_pressed()
        self.game.tick(pressed)

        pygame.display.flip()
        self.draw_game()
    
    def draw_game(self):
        """ Tegn alt der sker i spillet - kaldes efter game tick """
        def draw_wall_line(start, end):
            """ Offset linjer med -1 for at centerer dem """
            startx, starty = start
            endx, endy = end

            pygame.draw.line(self.screen, (33, 33, 255), (startx-1, starty-1), (endx-1, endy-1))

        self.screen.fill((0, 0, 0))
        for x in range(0, self.game.map.width):
            for y in range(0, self.game.map.height):
                value = self.game.map.matrix[x][y]

                if value is Map.WALL:
                    # Tjek om der er en mur til alle fire sider
                    if self.game.map.grid_type([x, y-1]) is not Map.WALL:
                        # Der er ikke en mur over
                        draw_wall_line((x*16, y*16), (x*16+16, y*16))
                    if self.game.map.grid_type([x, y+1]) is not Map.WALL:
                        # ...
                        draw_wall_line((x*16, y*16+16), (x*16+16, y*16+16))
                    if self.game.map.grid_type([x-1, y]) is not Map.WALL:
                        # ...
                        draw_wall_line((x*16, y*16), (x*16, y*16+16))
                    if self.game.map.grid_type([x+1, y]) is not Map.WALL:
                        # ...
                        draw_wall_line((x*16+16, y*16), (x*16+16, y*16+16))
                elif value is Map.POINT:
                    pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(x*16+7, y*16+7, 2, 2))      
        
        self.screen.blit(self.player_sprites(), (self.game.player.pos[0]+1, self.game.player.pos[1]+1))
        #pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.game.player.pos[0], self.game.player.pos[1], 15, 15))
    
    def player_sprites(self):
        """ Retunere den sprite der skal bruges, afhænger af tiden og spillerens retning """
        sprites = [self.sprites[0]]

        if self.game.player.direction is 0:
            sprites = sprites + self.sprites[1:3]
        elif self.game.player.direction is 2:
            sprites = sprites + self.sprites[7:9]
        elif self.game.player.direction is 3:
            sprites = sprites + self.sprites[5:7]
        else:
            sprites = sprites + self.sprites[3:5]

        # rækkefølge: ingen mund, lidt åben mund, helt åben mund

        # Vælg hvilken sprite der skal bruges

        if self.game.player.stopped is True:
            return sprites[2]

        # Billedet skal ændre sig hver 60. tick
        cycle = int(pygame.time.get_ticks()/60) % 4

        index = 0
        if cycle is 0:
            index = 1
        elif cycle is 1:
            index = 2
        elif cycle is 2:
            index = 0
        elif cycle is 3:
            index = 2

        return sprites[index]
