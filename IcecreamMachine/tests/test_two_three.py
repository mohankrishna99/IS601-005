import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
#this is an example test showing how to cascade fixtures to build up state
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
from IcecreamExceptions import InvalidPaymentException

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm

##UCID: mk994, Date: October 23
##testcase checking to add flavors or toppings only if remaing 
##scoops or toppings greater than zero
@pytest.fixture
def two_three_order(machine):
    ##Setting the quantity of flavors & toppings to 2 first
    ##and checking then
    machine.flavors[0].quantity = 2
    machine.toppings[2].quantity = 2
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_toppings("m&ms")

@pytest.mark.two
def test_flavor_stock(two_three_order, machine):
    try:
        assert machine.flavors[0].quantity > 0
        machine.handle_flavor("vanilla")
    except OutOfStockException:
        assert False
@pytest.mark.two
def test_three(machine):
    assert machine.toppings[2].quantity > 0
    machine.handle_toppings("m&ms")