from pdb import set_trace as breakpoint

class Dog():
    def __init__(self, name, age, breed, housebroke=True):
        self.name = name
        self.age = age
        self.housebrook = housebroke
        self.breed = breed
    def bark(self):
        print(f'{self.name} likes to Bark!') 


if __name__ ==  "__main__":

    lucky = Dog('Lucky', 3, 'Labrador')

    breakpoint()