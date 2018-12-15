class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working as expected.
    # PROTIP: Write your tests before you solve each function, that way you can test them one by one as you write your class.

    def __init__(self, file_name):
        self.file_name = file_name
        self.f = open(file_name, "w")

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific parameters of the simulation as the first line of the file.
        '''
        self.f.write("Population Size: {} \tPercentage Vaccinated: {} \tVirus Name: {} \tMortality Rate {} \tVirus Reproduction Rate: {}".format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))

    def log_interaction(self, person, random_person, random_person_sick=None,random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        if did_infect == True:
            self.f.write("\nPerson #{} was infected by person #{}".format(person._id, random_person._id))
        elif random_person_vacc == True:
            self.f.write("\nPerson #{} is vaccinated against the infection.".format(person._id))
        elif random_person_sick == True:
            self.f.write("\nPerson #{} is already infected.".format(person._id))
        else:
            self.f.write("\nPerson #{} did not get infected by person #{}".format(person._id, random_person._id))


    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        if did_die_from_infection is True:
            self.f.write("{} died from infection".format(person._id))
        else:
            self.f.write("{} survived infection".format(person._id))
