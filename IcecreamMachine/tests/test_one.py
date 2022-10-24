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
##testcase checking if the icecream is selecting a container or not
@pytest.fixture
def one_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    return machine

@pytest.mark.one
def test_one(one_order):
    x = one_order.inprogress_icecream[0].name.lower()
    assert x in ["waffle cone", "sugar cone", "cup"]
    print("\ncontainer is the first selection")