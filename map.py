import pygame

class Map():
    def __init__(self, file_name):
        self.image = pygame.image.load(file_name)

    def is_traverseable(self, x, y):
        pixel = self.image.get_at(x, y)

        r, g, b, a = pixel

        # Hvis farven er rød, så er det en mur som man ikke kan gå igennem
        return r is 255 and g is 0 and b is 0
