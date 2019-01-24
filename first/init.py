class Tuna:
    def __init__(self):
        print('This is a tuna class')

    def swim(self):
        print('I\'m swimming')

flipper = Tuna()
flipper.swim()


class Enemy:
    def __init__(self, x):
        self.energy = x
    def get_energy(self):
        print(self.energy)

enemy1 = Enemy(5)
enemy2 = Enemy(18)

enemy1.get_energy()
enemy2.get_energy()

