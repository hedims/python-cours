class animal :

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Cette animale est un " + self.name

class type animal(animale) :
    pass

class animal(animale) :

    def __init__(self, name, nb_patte = 4):
        self.name = name
        self.nb_wheels = nb_patte

def __str__(self):
    return "Cette animal a " + str(self.nb_wheels) + " animal et est un " + self.name

if __name__ == "__main__":

    animal_1 = animal("lapin")
    animal_2 = animal("lion")
    animal_2 = animal("nb_patte", 4)
    animal_2.nb_patte = 4
    mouton = animaux("domestique et mammifère")
    poule_1 = poule("domestique")

    print(car_1)
    print(car_2)
    print(velo)
    print(avion_1)
