""" Map klassen """

import pygame

class Map():
    """ Initialiserer map klasse """
    def __init__(self, file_name):
        image = pygame.image.load(file_name)

        self.construct(image)

    def construct(self, image):
        """ Bruget det indlæste billede til at lave en matrice over alle  """
        matrix = []
        for x in range(0, image.get_width()):
            matrix.append([])
            for y in range(0, image.get_height()):
                pixel = image.get_at((x, y))
                r, g, b, a = pixel

                if a is 0:
                    matrix[x].append(0)
                elif r is 0 and g is 0 and b is 0:
                    # Mur
                    matrix[x].append(1)
                elif r is 255 and g is 255 and b is 0:
                    # Ost
                    matrix[x].append(2)
                elif r is 255 and g is 80 and b is 0:
                    # Spiller
                    matrix[x].append(3)
                elif r is 255 and g is 0 and b is 0:
                    # Rødt spøgelse
                    matrix[x].append(4)
                elif r is 0 and g is 255 and b is 255:
                    # Tyrkis spøgelse
                    matrix[x].append(5)
                elif r is 255 and g is 192 and b is 203:
                    # Pink spøgelse
                    matrix[x].append(6)
                elif r is 255 and g is 165 and b is 0:
                    # Orange spøgelse
                    matrix[x].append(7)
                else:
                    # Intet match = tomt
                    matrix[x].append(0)

        self.matrix = matrix
        self.width = image.get_width()
        self.height = image.get_height()
