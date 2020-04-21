class Perso():
    sprite = "dk_bas.png"
    position = (0,0)
    direction = "B"

    def mouv(self, dir):
        if dir == "H" and position[0] - 1 >= 0:
            position = (position[0] - 1, position[1])
        elif dir == "B" and position[0] + 1 < 15:
            position = (position[0] + 1, position[1])
        elif dir == "G" and position[1] - 1 >= 0:
            position = (position[0], position[1] - 1)
        elif dir == "B" and position[1] + 1 < 15:
            position = (position[0], position[1] + 1)
        return position

