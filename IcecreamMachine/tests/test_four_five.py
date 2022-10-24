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
def four_five_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    return machine
##UCID: mk994 Date October 23
##tests 4 & 5 checking if scoops & toppings are less than 3
@pytest.mark.four
def test_four(four_five_order):
    c = 0
    for i in four_five_order.inprogress_icecream:
        if i.name.lower() in ["vanilla", "chocolate", "strawberry"]:
            c += 1
    print(c)
    assert c <= 3

@pytest.mark.five
def test_five(four_five_order):
    c = 0
    for i in four_five_order.inprogress_icecream:
        if i.name.lower() in ["sprinkles", "m&ms", "chocolate chips", "gummy bears", "peanuts"]:
            c += 1
    print(c)
    assert c <= 3