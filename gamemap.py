import pygame

class Map():
    def __init__(self, file_name):
        image = pygame.image.load(file_name)

        self.construct(image)
    
    def construct(self, image):
        things = []
        for x in range(0, image.get_width()):
            things.append([])
            for y in range(0, image.get_height()):
                pixel = image.get_at((x, y))
                r, g, b, a = pixel

                '''
                0 = tom
                1 = mur
                2 = ost
                3 = spiller
                4 = rød spøgelse
                5 = tyrkis spøgelse
                6 = pink spøgelse
                7 = orange spøgelse
                '''

                if a is 0:
                    things[x].append(0)
                elif r is 0 and g is 0 and b is 0:
                    # Mur
                    things[x].append(1)
                elif r is 255 and g is 255 and b is 0:
                    # Ost
                    things[x].append(2)
                elif r is 255 and g is 80 and b is 0:
                    # Spiller
                    things[x].append(3)
                elif r is 255 and g is 0 and b is 0:
                    # Rødt spøgelse
                    things[x].append(4)
                elif r is 0 and g is 255 and b is 255:
                    # Tyrkis spøgelse
                    things[x].append(5)
                elif r is 255 and g is 192 and b is 203:
                    # Pink spøgelse
                    things[x].append(6)
                elif r is 255 and g is 165 and b is 0:
                    # Orange spøgelse
                    things[x].append(7)
                else:
                    # Intet match = tomt
                    things[x].append(0)
        
        self.coordinates = things
        self.width = image.get_width()
        self.height = image.get_height()
    
    """ def get_player(self):
        for x in range(0, self.objects.get_width()):
            for y in range(0, self.image.get_height()):
                thing = self.objects[x][y]

                if thing is 3:
                    return (x,y)
    
    def get_ghosts(self):
        ghosts = []
        for x in range(0, self.image.get_width()):
            for y in range(0, self.image.get_height()):
                thing = self.objects[x][y]

                if thing is 4:
                    ghosts.append((x, y, 'red'))
                elif thing is 5:
                    ghosts.append((x, y, 'cyan'))
                elif thing is 6:
                    ghosts.append((x, y, 'pink'))
                elif thing is 7:
                    ghosts.append((x, y, 'orange'))
        
        return ghosts """

    def is_traverseable(self, x, y):
        thing = self.objects[x][y]

        # Hvis det er en mur, så kan man ikke gå der
        return thing is not 1