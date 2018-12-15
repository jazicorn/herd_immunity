import random
random.seed(42)
from virus import Virus

class Person(object):
    ''' Person objects will populate the simulation. '''
    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    def did_survive_infection(self):

        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        if self.infection is not None:
            random_variable = random.uniform(0,1)
            if random_variable  < self.infection.mortality_rate:
                self.is_alive = False
                self.infection = None
                return False
            else:
                self.is_vaccinated = True
                self.infection = None
                return True
