import copy
class Building:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__stages = dict()

    def __len__(self):
        return len(self.__stages)

    def __setitem__(self, key, value):
        self.__stages[key] = value

    def __getitem__(self, item:int):
        return self.__stages[item]

    def __copy__(self):
        return copy.deepcopy(self)



class Company:
    def __init__(self, name, industry):
        self.__name = name
        self.__industry = industry

    @property
    def name(self):
        return self.__name



building1 = Building('Twice Tower', 'Myloslavska 65')
print(len(building1))
openai = Company('OpenAI', 'artificial intelligence')
nails_company = Company('Best Nails', 'beauty')
building1[1] = openai
building1[2] = nails_company
print(len(building1))
print(building1[2].name)
building2 = copy.copy(building1)
print(building1[2] == building2[2])
print(building1[2] is building2[2])