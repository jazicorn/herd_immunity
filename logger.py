class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working as expected.
    # PROTIP: Write your tests before you solve each function, that way you can test them one by one as you write your class.

    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific parameters of the simulation as the first line of the file.
        '''
        f = open(file_name, "w")
        f.write("Population Size: {} \tPercentage Vaccinated: {} \tVirus Name: {} \tMortality Rate {} \tVirus Reproduction Rate: {}".format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))

    def log_interaction(self, person, random_person, random_person_sick=None,random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        if did_infect == True:
            f.write("\nPerson #{} was infected by person #{}".format(person._id, random_person._id))
        elif person_vacc == True:
            self.saved_by_vaccine += 1
            f.write("\nPerson #{} is vaccinated against the infection.".format(person._id))
        elif person_sick == True:
            f.write("\nPerson #{} is already infected.".format(person._id))
        else:
<<<<<<< HEAD
            f.write("\nPerson #{} did not get infected by person #{}".format(person._id, random_person._id))
=======
            walking_dead.write("\nPerson #{} did not get infected by person #{}".format(person2._id, person1._id))
            file.close()

>>>>>>> b296db00683e69293fabf031a5e6e1f5d9b68461

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
<<<<<<< HEAD
        if did_die_from_infection is True:
            f.write("{} died from infection".format(person._id))
        else:
            f.write("{} survived infection".format(person._id))
=======
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        with open(self.file_name, "walking_dead") as file:
        if did_die_from_infection:
            self.file.write("%s died\n" % person._id)
        else:
            self.file.write("%s survived infection\n % person._id")
        file.close()
>>>>>>> b296db00683e69293fabf031a5e6e1f5d9b68461

    def log_time_step(self, number_of_dead, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!

        with open(self.file_name, "walking_dead") as file:
            file.writelines(["Time step number {} ended, beginning {} \n".format(
                time_step_number, time_step_number + 1)])
        file.close()
