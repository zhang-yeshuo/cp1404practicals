class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician = ",".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        return "\n".join(musician.play() for musician in self.musicians)