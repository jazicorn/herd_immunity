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
        The vaccination percentage represents the total percentage of population vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result of the infection.
        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        self.logger = Logger("walking_dead.txt")
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.current_infected = initial_infected # Int
        self.newly_infected = []
        self.total_infected = initial_infected # Int
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int
        self.total_vaccinated = None
        self.population = self._create_population()
        self.total_dead = 0
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
        virus_name, pop_size, vacc_percentage, initial_infected)

        self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)


    def _create_population(self):
        '''This method will create the initial population.
            Returns:
                list: A list of Person objects.
        '''
        print('CREATING POPULATION')
        population = []
        vacc_num = int(self.pop_size * self.vacc_percentage)
        self.total_vaccinated = vacc_num
        unvacc_num = int(self.pop_size - vacc_num - self.initial_infected)
        assert vacc_num >= 0
        assert unvacc_num >= 0

        for i in range(unvacc_num):
            new_person = Person(i, False)
            population.append(new_person)

        for i in range(vacc_num):
            new_person = Person(i + unvacc_num, True)
            population.append(new_person)

        for i in range (self.initial_infected):
            new_person = Person(i + unvacc_num + vacc_num, False, self.virus)
            population.append(new_person)
        return population

    def _simulation_should_continue(self):

        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.
            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        print('SIM SHOULD CONTINUE')
        for person in self.population:
            if person.is_alive == True and person.is_vaccinated == False:
                return True
        return False

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        print('RUNNING')
        time_step_counter = 0

        while self._simulation_should_continue():
            time_step_counter += 1
            self.time_step(time_step_counter)
        print('The simulation has ended after {} turns.'.format(time_step_counter))

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
        print('IN TIME STEP FUNCTION')
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

        self.total_dead += num_died
        self.total_vaccinated += num_vaccinated

        # Resolve newly infected.
        self._infect_newly_infected()

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.
        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with. '''

        # Assert statements are included to make sure that only living people are passed
        # in as params

        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated:
            self.logger.log_interaction(person, random_person, random_person_sick=False,
                                        random_person_vacc=True, did_infect=False)
            return

        if random_person.infection is not None:
            self.logger.log_interaction(person, random_person, random_person_sick=True,
                                        random_person_vacc=False, did_infect=False)
            return

        random_variable = random.uniform(0,1)
        if random_variable < person.infection.repro_rate:
            self.newly_infected.append(random_person._id)
            self.logger.log_interaction(person, random_person, random_person_sick=False,
                                        random_person_vacc=False, did_infect=True)
        else:
            self.logger.log_interaction(person, random_person, random_person_sick=False,
                                        random_person_vacc=False, did_infect=False)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        print('INFECTING NEWLY INFECTED')
        for person_id in self.newly_infected:
            for person in self.population:
                if person._id == person_id:
                    person.infection = self.virus

        self.newly_infected = []


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_rate = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])

    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected=1)

    sim.run()
