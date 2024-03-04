class Cat:
    def make_noise(self):
        pass

class Lion(Cat):
    def __init__(self):
        self.color = 'Yellow'
        self.tail = 'Long'

    def make_noise(self):
        print('Grrrrrrrrr')

class Tiger(Cat):
    def __init__(self):
        self.color = 'three colors'
        self.tail = 'Long'

    def make_noise(self):
        print('I`m from 3th OSHB')

class Puma(Cat):
    def __init__(self):
        self.color = 'Black'
        self.tail = 'Short'

    def make_noise(self):
        print('Buy new shoes')

lion = Lion()
lion.make_noise()
tiger = Tiger()
tiger.make_noise()
puma = Puma()
puma.make_noise()