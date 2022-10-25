import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm

@pytest.fixture
def six_one_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    return machine

##UCID: mk994, Date: October 23
##Test six to check if the total cost is correctly calculated

@pytest.mark.four
def test_total_cost1(six_one_order):
    assert six_one_order.calculate_cost() == '3.25'

@pytest.fixture
def second_order(machine):
    machine.reset()
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    return machine

@pytest.mark.four
def test_total_cost2(second_order):
    assert second_order.calculate_cost() == '2.00'