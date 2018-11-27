""" Viewer klasse """

import pygame

class Viewer():
    def __init__(self, game):
        """ Initialiserer viewer klasse """
        self.game = game

        pygame.init()
        self.font = pygame.font.SysFont("monospace", 15)

    def start_clock(self):
        """ Starter spillet """
        self.screen = pygame.display.set_mode((self.game.map.width * 16, self.game.map.height * 16))
        pygame.display.set_caption("Pacman")
        clock = pygame.time.Clock()

        self.running = True

        while self.running:
            self.tick()
            clock.tick(50)
    
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

                if value is 1:
                    # Tjek om der er en mur til alle fire sider
                    above = False if -1 < y-1 < self.game.map.height and self.game.map.matrix[x][y-1] is not 1 else True
                    below = False if -1 < y+1 < self.game.map.height and self.game.map.matrix[x][y+1] is not 1 else True
                    left = False if -1 < x-1 < self.game.map.width and self.game.map.matrix[x-1][y] is not 1 else True
                    right = False if -1 < x+1 < self.game.map.width and self.game.map.matrix[x+1][y] is not 1 else True

                    if above is False:
                        # Der er ikke en mur over
                        draw_wall_line((x*16, y*16), (x*16+16, y*16))
                    if below is False:
                        # ...
                        draw_wall_line((x*16, y*16+16), (x*16+16, y*16+16))
                    if left is False:
                        # ...
                        draw_wall_line((x*16, y*16), (x*16, y*16+16))
                    if right is False:
                        # ...
                        draw_wall_line((x*16+16, y*16), (x*16+16, y*16+16))
                elif value is 2:
                    pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(x*16+7, y*16+7, 2, 2))

        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.game.player.pos[0], self.game.player.pos[1], 13, 13))
