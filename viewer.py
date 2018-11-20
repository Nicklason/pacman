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
        for x in range(0, self.game.map.width):
            for y in range(0, self.game.map.height):
                thing = self.game.map.coordinates[x][y]

                if thing is 2:
                    pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(x*16+7, y*16+7, 2, 2))
