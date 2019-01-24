class Mario():

    def move(self):
        print('I\'m moving')

class Shroom():

    def eats_shroom(self):
        print('I\'m big')

class BigMario(Mario, Shroom):

    pass

bm = BigMario()
bm.move()
bm.eats_shroom()
