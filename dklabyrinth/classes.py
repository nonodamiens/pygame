class Perso():
    """ blabla """

    def __init__(self):
        """ blabla 2 """
        self.sprite = "dk_bas.png"
        self.position = (0,0)
        self.direction = "B"

    def mouv(self, dir):
        if dir == "G" and self.position[0] - 1 >= 0:
            self.position = (self.position[0] - 1, self.position[1])
        elif dir == "D" and self.position[0] + 1 < 15:
            self.position = (self.position[0] + 1, self.position[1])
        elif dir == "H" and self.position[1] - 1 >= 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif dir == "B" and self.position[1] + 1 < 15:
            self.position = (self.position[0], self.position[1] + 1)
        return self.position

