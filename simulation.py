import random, sys
random.seed(42)
from person import Person
# from logger import Logger
from virus import Virus


class Simulation(object):
<<<<<<< HEAD
    # ''' Main class that will run the herd immunity simulation program.
    # Expects initialization parameters passed as command line arguments when file is run.
    #
    # Simulates the spread of a virus through a given population.  The percentage of the
    # population that are vaccinated, the size of the population, and the amount of initially
    # infected people in a population are all variables that can be set when the program is run.
    # '''
    def __init__():
=======
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.
    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, pop_size, vacc_percentage, Virus, initial_infected=1):
>>>>>>> a2fa0d03d1b45541466099a1d8701b6e723c8606
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.

        (1) The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.

        (2) The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.

        (3) You will need to keep track of the number of people currently infected with the disease.

        (4) The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.

        (5) You will also need to keep track of the number of people that have die as a result
        of the infection.

        (6) All arguments will be passed as command-line arguments when the file is run.

        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
<<<<<<< HEAD

        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        self.population = self._create_population(initial_infected)

        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.newly_infected = []

        self.logger = None
        self.population = [] # List of Person objects
=======
        logger = Logger("walking_dead.txt")
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = logger
        # Store the array that self._create_population will return in the self.population attribute.
>>>>>>> a2fa0d03d1b45541466099a1d8701b6e723c8606
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = 0 # Int
        self.newly_infected = 0 # Int
        self.current_infected = 0 # Int
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int
        self.population = [] # List of Person objects
        #self.population += self._create_population(initial_infected)
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(

            virus_name, pop_size, vacc_percentage, initial_infected)


            Virus, pop_size, vacc_percentage, initial_infected)


            # User parameters input
            # virus name (HIV)
            # population_size (1000)
            # vacc_percentage (50%)
            # initial_infected (10)

            # parameters for virus
            # virus = Virus("HIV", 0.8, 0.3)
            # assert virus.name == "HIV"
            # assert virus.repro_rate == 0.8
            # assert virus.mortality_rate == 0.3

            # parameters for person
            # person = Person(a,b,c,d)
            # (a)assert person._id == 1
            # (b)assert person.is_alive == True
            # (c)assert person.is_vaccinated == True
            # (d)assert person.infection == None

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''

        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (
            # correct number of people in the population,
            # correct percentage of people vaccinated,
            # correct number of initially infected people
            #).
        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.

        population = []
        created = 0

        while created < self.pop_size:
            #create vaccinated people
            vacc_num = self.pop_size * self.vacc_percentage
            vacc_people = 0
            while vacc_num > vacc_people:
                person = Person(self.next_person_id, is_vaccinated=True, infection=None)
                self.population.append(person)
                vacc_people += 1
                created += 1
                self.next_person_id += 1

            #create unvacciated people
            unvacc_num = self.pop_size - vacc_num
            unvacc_people = 0
            while unvacc_num > unvacc_people:
                person = Person(self.next_person_id, is_vaccinated=False, infection=None)
                self.population.append(person)
                unvacc_people += 1
                created += 1
                self.next_person_id += 1

        return population


    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

            Returns:
                bool: True for simulation should continue, False if it should end.
        '''

        # TODO: Complete this helper method.  Returns a Boolean.
        if self.dead == self.population_size or self.infected_count:

        #ep = entire population
        ep_dead = False
        ep_vaccinated = False
        for person in self.population:
            if person.is_alive == True:
                ep_dead is False
            else:
                ep_dead is True

            if person.is_vaccinated == True:
                ep_vaccinated is False
            else:
                ep_vaccinated is True

        if ep_dead == True and ep_vaccinated == True:
            return True
        else:
            return False


    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.
        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = self._simulation_should_continue()

        while should_continue:
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)
            self.time_step()
            should_continue = self._simulation_should_continue()
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''

        for person in self.population:
            interactions = 0
            if person.infection is True and person.is_alive is True:
                while interactions < 100:
                    rando = random.choice(self.population)
                    if rando.is_alive is False:
                        rando = random.choice(self.population)
                    else:
                        self.interaction(person, rando._id)


    def interaction(self, person, rando):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert rando.is_alive == True

        # TODO: Finish this method.
        if rando.is_vaccinated is True:
            # random_person is vaccinated, nothing happens
            print('congrats babe')
        elif rando.infection is not None:
            # random_person is already infected, nothing happens
            print('sorry babe')
        else:
            # random_person is healthy, but unvaccinated, generate a random number between 0 and 1. If rand_num is less than repro_rate, random_person's ID should be appended to Simulation object's newly_infected array, so that their infected attribute can be changed to True at the end of the time step.
            rand_num = random.uniform(0, 1)
            if rand_num < virus.repro_rate:
                self.newly_infected.append(rando._id)

        #Call this method at the end of every time step and infect each Person.
        _infect_newly_infected()

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''

        for id in self.newly_infected:
            for person in self.population:
                if person._id == id:
                    person.infection = self.virus

        # Reset self.newly_infected back to an empty list.
        self.newly_infected = []

# if __name__ == "__main__":
#     params = sys.argv[1:]
#     virus_name = str(params[0])
#     repro_num = float(params[1])
#     mortality_rate = float(params[2])
#
#     pop_size = int(params[3])
#     vacc_percentage = float(params[4])
#
#     if len(params) == 6:
#         initial_infected = int(params[5])
#
#     virus = Virus(name, repro_rate, mortality_rate)
#     sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)
#
#     sim.run()


Simulation._create_population(1,initial_infected=10)
