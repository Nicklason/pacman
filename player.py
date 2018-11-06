class Player():
    def __init__(self, coords):
        self.coords = coords
        self.direction = 3 # Går mod vest
        self.heading = 3 # Vil prøve at gå mod vest når man kan
        self.stopped = False  # Hvis spilleren er stødt på en mur
        self.speed = 10

    def tick(self, py, pressed):
        if self.stopped:
            return

        if self.direction is 0:
            # Spilleren bevæger sig mod nord, læg farten til y
            self.coords[1] += self.speed
        elif self.direction is 1:
            # Spilleren bevæger sig mod syd, træk farten fra y
            self.coords[1] -= self.speed
        elif self.direction is 2:
            # Spilleren bevæger sig mod øst, læg farten til i x
            self.coords[0] += self.speed
        elif self.direction is 3:
            # Spilleren bevæger sig mod vest, træk farten fra i x
            self.coords[0] -= self.speed
        
