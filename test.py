class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = _id
        self.is_alive = True # Boolean
        self.is_vaccinated = is_vaccinated # Boolean
        self.infection = infection # V


pop_size = 10

class test():
    person = Person(0, True, True)
    pop_size = 10
    for i in range(0, pop_size):
        person._id += 1
        print(person._id)

test()
