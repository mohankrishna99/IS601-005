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
def first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    machine.handle_pay(3.25,"3.25")
    return machine

##UCID: mk994, Date: October 23 
##Test 7 & 8 checking total_sales and total_icecreams are calculated or not
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    machine.handle_pay(2.25,"2.25")
    return machine

@pytest.mark.five
def test_seven(first_order, second_order, machine):
    assert machine.total_sales == 5.50

@pytest.mark.five
def test_eight(second_order, machine):
    assert machine.total_icecreams == 2