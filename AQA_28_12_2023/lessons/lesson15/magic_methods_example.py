import datetime

class Rat:
    attempts_to_reach_cool_parametr = []
    def __init__(self):
        self.__color = 'Brown'

    def __str__(self):
        return f'I`m smol rat with {self.__color} fur'

    def __getattr__(self, item):
        if item == 'cool':
            self.attempts_to_reach_cool_parametr.append(datetime.datetime.now())
            return 'your attempt to reach cool parametr was notified!'
        else:
            return f'sorry but {item} is not supported for now'

    #def __repr__(self):
    #    return 'Rat()'

smol_rat = Rat()
#print(smol_rat)
#smol_rat_2 = eval(repr(smol_rat))
#print()
print(smol_rat.cool)
print(smol_rat.not_cool)
print(smol_rat.cool)
for attempt in smol_rat.attempts_to_reach_cool_parametr:
    print(attempt)

