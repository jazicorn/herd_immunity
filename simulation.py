import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.
    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.
        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        self.logger = Logger("walking_dead.txt")
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = initial_infected # Int
        self.newly_infected = [] # List of newly infected people
        self.current_infected = initial_infected# Int
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int
        self.population = self._create_population() # List of Person objects
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)

    def _create_population(self):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.
            Returns:
                list: A list of Person objects.
        '''
        population = []
        created = 0

        while created < self.pop_size:
            #create vaccinated people
            vacc_num = self.pop_size * self.vacc_percentage
            vacc_people = 0
            while vacc_num > vacc_people:
                person = Person(self.next_person_id, is_vaccinated=True, infection=None)
                population.append(person)
                vacc_people += 1
                created += 1
                self.next_person_id += 1

            #create unvacciated people
            unvacc_num = self.pop_size - vacc_num
            unvacc_people = 0
            while unvacc_num > unvacc_people:
                person = Person(self.next_person_id, is_vaccinated=False, infection=None)
                population.append(person)
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
        #ep = entire population
        print('inside simulation should continue ')

        for person in self.population:
            if person.is_alive == True and person.is_vaccinated == False:
                return True
        return False

        # ep_dead = False
        # ep_vaccinated = False
        #
        # for person in self.population:
        #     if person.is_alive == True:
        #         ep_dead is False
        #     else:
        #         ep_dead is True
        #
        #     if person.is_vaccinated == True:
        #         ep_vaccinated is False
        #     else:
        #         ep_vaccinated is True
        #
        # if ep_dead == True and ep_vaccinated == True:
        #     return True
        # else:
        #     return False


    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        time_step_counter = 0
        should_continue = self._simulation_should_continue()

        while should_continue:
            #print("The simulation should continue: {}".format(should_continue))
            time_step_counter += 1
            self.time_step(time_step_counter)
        print('HEY NYA: The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self, time_step_counter):
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
        # for person in self.population:
        #     interactions = 0
        #     if person.infection is True and person.is_alive is True:
        #         while interactions < 100:
        #             rando = random.choice(self.population)
        #             if rando.is_alive is False:
        #                 rando = random.choice(self.population)
        #                 interactions += 1
        #             else:
        #                 self.interaction(person, rando._id)
        #                 interactions += 1

        for person in self.population:
            if person.infection is not None and person.is_alive:
                for x in range(100):
                    random_person = random.choice(self.population)
                    while random_person.is_alive == False:
                        random_person = random.choice(self.population)
                    self.interaction(person, random_person)

        # Resolve previously infected.
        num_died = 0
        num_vaccinated = 0
        for person in self.population:
            if person.infection is not None and person.is_alive:
                did_survive = person.did_survive_infection()
                if not did_survive:
                    num_died += 1
                else:
                    num_vaccinated += 1
                self.logger.log_infection_survival(person, not did_survive)

        self.newly_infected = list(set(self.newly_infected))
        num_infected = len(self.newly_infected)

        #self.total_dead += num_died
        # self.total_vaccinated += num_vaccinated
        #
        # self.logger.log_time_step(time_step_counter, num_died, num_vaccinated, num_infected, self.total_dead, self.total_vaccinated)

        # Resolve newly infected.
        self._infect_newly_infected()

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.
        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated is True:
            # random_person is vaccinated, nothing happens
            self.logger.log_interaction(person, random_person, random_person_sick=False, random_person_vacc=True)
        elif random_person.infection is not None:
            # random_person is already infected, nothing happens
            self.logger.log_interaction(person, random_person, random_person_sick=True, random_person_vacc=False)
        else:
            # random_person is healthy, but unvaccinated, generate a random number between 0 and 1. If rand_num is less than repro_rate, random_person's ID should be appended to Simulation object's newly_infected array, so that their infected attribute can be changed to True at the end of the time step.
            rand_num = random.uniform(0, 1)
            if rand_num < virus.repro_rate:
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(person, random_person, random_person_sick=False, random_person_vacc=False)

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

if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_rate = float(params[1])
    mortality_rate = float(params[2])

    #changed from int(params[3]) to float
    pop_size = int(params[3])
    #pop_size = float(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])

    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)

    sim.run()
