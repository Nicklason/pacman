class Ghost():
    def __init__(self, coords, color):
        self.coords = coords
        self.color = color # Spøgelsets farve
        self.stopped = False  # Hvis spilleren er stødt på en mur
        self.speed = 10

    def tick(self, py, pressed):
        if self.stopped:
            return

        # Logik for at bevæge sig (afhænger af farven på spøgelset og hvor spilleren er)
        