class Horse:
    def __init__(self):
        self.speed = 10
        self.age = 5

    def __add__(self, other):
        return Mul(self.speed, other.strength)

    def __radd__(self, other):
        return Mul(self.speed, other.strength)

    def __del__(self):
        print('Horse is dead')

    def __iadd__(self, other):
        self.age +=1
        return self

    def __bool__(self):
        return False

    def __float__(self):
        return 2.5

    def __eq__(self, other):
        return self.age == other.age




class Donkey:
    def __init__(self):
        self.strength = 10
        self.age = 5


class Mul:
    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength

    def __str__(self):
        return f'{self.__class__.__name__}: \n\tspeed={self.speed}\n\tstrength={self.strength}'

horse1 = Horse()
donkey1 = Donkey()
mul1 = donkey1+horse1
horse1 += 1
print(horse1.age)
print(bool(horse1))
print(float(horse1))
print(horse1==donkey1)
