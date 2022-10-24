import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
"""
@pytest.fixture
def first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

def test_production_line(second_order):
    assert second_order is not None
"""
"""
@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
@pytest.fixture
def order(machine):
    machine.handle_flavor("vanilla")
    return machine
#@pytest.mark.parametrize("containers",["waffle cone", "sugar cone", "cup"])
def test_container_first_sel(order, containers):
    #print(order.inprogress_icecream[0].name)
    assert order.inprogress_icecream[0].name in containers
    """
def test_first_sel(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")

    y = machine.inprogress_icecream[0].name.lower()
    assert y in ["waffle cone", "sugar cone", "cup"]