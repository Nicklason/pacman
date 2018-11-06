import pygame

class Viewer():
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pacman")

        self.running = True

        pygame.init()
        self.font = pygame.font.SysFont("monospace", 15)

        self.start_clock()

    def start_clock(self):
        clock = pygame.time.Clock()

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
        if self.game.state == 0:
            pygame.draw.rect(self.screen, (30,30,30), pygame.Rect(380, 280, 80, 50))
            self.screen.blit(self.font.render("MENU", 1, (255,255,255)), (400, 300))
        elif self.game.state == 1:
            self.screen.fill((0, 10, 20))
            pygame.draw.rect(self.screen, (10,123,50), pygame.Rect(self.game.x, self.game.y, 50, 50))
            pygame.draw.rect(self.screen, (123,50,10), pygame.Rect(self.game.target[0], self.game.target[1], 50, 50))
            self.screen.blit(self.font.render("Points: {}".format(self.game.points), 1, (255,255,0)), (100, 100))
        elif self.game.state == 2:
            pygame.draw.rect(self.screen, (30,30,30), pygame.Rect(380, 280, 80, 50))
            self.screen.blit(self.font.render("PAUSE", 1, (255,255,255)), (400, 300))
