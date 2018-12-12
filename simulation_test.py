from person import Person
from simulation import Simulation
from virus import Virus

def test_simulation_instantiation():
    virus = Virus("HIV", 0.8, 0.3)
    test = Simulation(100000, 0.9, virus)

    assert test.pop_size == 100000
    assert test.vacc_percentage == 0.9
    assert test.initial_infected == 1
    assert test.virus.name == "HIV"

def test_create_population():
    virus = Virus("Ebola", 0.25, 0.7)
    test = Simulation(500, 0.9, virus, 10)

    assert test.pop_size == 500
    assert test.initial_infected == 10

def test_simulation_should_continue(self):
    
