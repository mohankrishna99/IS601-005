import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm

##UCID: mk994, Date: October 23
##testcase checking to add flavors or toppings only if remaing sccops or toppings greater than zero
@pytest.fixture
def two_three_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")

def test_two(machine):
    assert machine.remaining_scoops >= 0
    machine.handle_flavor("vanilla")

def test_three(machine):
    assert machine.remaining_toppings >= 0
    machine.handle_toppings("m&ms")