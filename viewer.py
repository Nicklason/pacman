import pygame

class Viewer():
    def __init__(self, game):
        self.game = game

        pygame.init()
        self.font = pygame.font.SysFont("monospace", 15)

    def start_clock(self):
        self.screen = pygame.display.set_mode((self.game.map.width * 16, self.game.map.height * 16))
        pygame.display.set_caption("Pacman")
        clock = pygame.time.Clock()

        self.running = True

        while self.running:
            self.tick()
            clock.tick(60)
    
    def tick(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.game.toggle_pause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.game.started():
                    self.game.end_game()
                else:
                    self.game.start_game()

        pressed = pygame.key.get_pressed()
        self.game.tick(pygame, pressed)

        self.draw_game()
        pygame.display.flip()

    def draw_game(self):
        def draw_wall_line(start, end):
            startx, starty = start
            endx, endy = end

            pygame.draw.line(self.screen, (0, 0, 100), (startx-1, starty-1), (endx-1, endy-1))

        self.screen.fill((0, 0, 0))
        for x in range(0, self.game.map.width):
            for y in range(0, self.game.map.height):
                thing = self.game.map.coordinates[x][y]

                if thing is 1:
                    # Tjek om der er en mur til alle fire sider
                    above = False if -1 < y-1 < self.game.map.height and self.game.map.coordinates[x][y-1] is not 1 else True
                    below = False if -1 < y+1 < self.game.map.height and self.game.map.coordinates[x][y+1] is not 1 else True
                    left = False if -1 < x-1 < self.game.map.width and self.game.map.coordinates[x-1][y] is not 1 else True
                    right = False if -1 < x+1 < self.game.map.width and self.game.map.coordinates[x+1][y] is not 1 else True

                    if above is False:
                        draw_wall_line((x*16, y*16), (x*16+16, y*16))
                        #pygame.draw.line(self.screen, (0, 0, 100), (x*16, y*16), (x*16+16, y*16), 1)
                    if below is False:
                        draw_wall_line((x*16, y*16+16), (x*16+16, y*16+16))
                    if left is False:
                        draw_wall_line((x*16, y*16), (x*16, y*16+16))
                    if right is False:
                        draw_wall_line((x*16+16, y*16), (x*16+16, y*16+16))
                elif thing is 2:
                    pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(x*16+7, y*16+7, 2, 2))
