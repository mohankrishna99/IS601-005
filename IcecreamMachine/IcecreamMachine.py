from enum import Enum
# make a tests folder under the folder you're putting these files in
# add an empty __init__.py to the tests folder
from IcecreamExceptions import ExceededRemainingChoicesException, InvalidChoiceException, NeedsCleaningException, OutOfStockException
from IcecreamExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0

class Container(Usable):
    pass

class Flavor(Usable):
    pass

class Toppings(Usable):
    pass

class STAGE(Enum):
    Container = 1
    Flavor = 2
    Toppings = 3
    Pay = 4

class IceCreamMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 100
    MAX_SCOOPS = 3
    MAX_TOPPINGS = 3


    containers = [Container(name="Waffle Cone", cost=1.5), Container(name="Sugar Cone", cost=1), Container("Cup", cost=1)]
    flavors = [Flavor(name="Vanilla", quantity=100, cost=1), Flavor(name="Chocolate", quantity=100, cost=1), Flavor(name="Strawberry", quantity=100, cost=1)]
    toppings = [Toppings(name="Sprinkles", quantity=200, cost=.25), Toppings(name="Chocolate Chips", quantity=200, cost=.25), Toppings(name="M&Ms", quantity=200, cost=.25), \
    Toppings(name="Gummy Bears", quantity=200, cost=.25), Toppings(name="Peanuts", quantity=200, cost=.25)] 

    container_names = []
    for i in containers:
        container_names.append(i.name.lower())
    flavors_names = []
    for i in flavors:
        flavors_names.append(i.name.lower())
    toppings_names = []
    for i in toppings:
        toppings_names.append(i.name.lower())

    def check_flav_top(self):
        flav_top = self.flavors_names + self.toppings_names
        c = 0 
        for i in range(1, len(self.inprogress_icecream)):
            if self.inprogress_icecream[i].name.lower() in flav_top:
                c += 1
        return c

    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_scoops = MAX_SCOOPS
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_icecreams = 0

    inprogress_icecream = []
    currently_selecting = STAGE.Container

    # rules
    # 1 - container must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - scoops can't exceed max
    # 4 - toppings can't exceed max
    # 5 - a container and at least 1 scoop or toppings must be selected
    # 6 - proper cost must be calculated and shown to the user
    # 7 - cleaning must be done after certain number of uses before any more icecreams can be made
    # 8 - total sales should calculate properly based on cost calculation
    # 9 - total_icecreams should increment properly after a payment
    

    def pick_container(self, choice):
        for c in self.containers:
            if c.name.lower() == choice:
                c.use()
                self.inprogress_icecream.append(c)
                return
        raise InvalidChoiceException

    def pick_flavor(self, choice):
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_scoops <= 0:
            raise ExceededRemainingChoicesException
        for f in self.flavors:
            if f.name.lower() == choice:
                f.use()
                self.inprogress_icecream.append(f)
                self.remaining_scoops -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_toppings(self, choice):
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice:
                t.use()
                self.inprogress_icecream.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        self.remaining_scoops = self.MAX_SCOOPS
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_icecream = []
        self.currently_selecting = STAGE.Container

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_container(self, container):
        self.pick_container(container)
        self.currently_selecting = STAGE.Flavor

    def handle_flavor(self, flavor):
        try:
            if self.inprogress_icecream[0].name in self.container_names:
                pass
        except:
            print("Choose a container first")
        if flavor == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_flavor(flavor)

    def handle_toppings(self, toppings):
        if toppings == "done":
            if self.check_flav_top():
                self.currently_selecting = STAGE.Pay
            else:
                print("Choose atleast one flavor or topping")
                self.currently_selecting = STAGE.Flavor
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if total == str(expected):
            print("Thank you! Enjoy your icecream!")
            self.total_icecreams += 1
            self.total_sales += float(expected) # only if successful
            self.reset()
        else:
            raise InvalidPaymentException
            
    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_icecream
        ##UCID: mk994   Date: October 20
        ##setting cost to zero initially and looping the inprogress_icecream list to calculate the cost
        cost = 0
        for i in self.inprogress_icecream:
            cost += (i.cost)
        return format(cost, '.2f')

    def run(self):
        try:
            if self.currently_selecting == STAGE.Container:
                container = input(f"Would you like a {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.containers))))}?\n")
                self.handle_container(container)
            elif self.currently_selecting == STAGE.Flavor:
                flavor = input(f"Would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.flavors))))}? Or type next.\n")
                self.handle_flavor(flavor)
            elif self.currently_selecting == STAGE.Toppings:
                toppings = input(f"Would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                self.handle_toppings(toppings)
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                ##UCID:mk994 Date: October 20, formatting the cost to display two decimals
                total = input(f"Your total is {expected}, please enter the exact value.\n")
                self.handle_pay(expected, total)
                choice = input("What would you like to do? (icecream or quit)\n")
                if choice == "quit":
                    exit()
        
        ##UCID: mk994  Date:October 22
        ## adding the OutOfStockException and printing the message for user to choose from available options
        except OutOfStockException:
            print("Requested choice is out of stock, Please choose from the options available")
        
        ##UCID: mk994  Date:October 22
        ## adding the InvalidPaymentException and printing the message for user to enter the correct total
        except InvalidPaymentException:
            print(f"You entered the wrong amount, Please enter the correct total {expected}")
        
        ##UCID: mk994  Date:October 22
        ## adding the ExceededRemainingChoicesException and printing the message for user and moving to next step
        except ExceededRemainingChoicesException:
            print(f"Sorry you have exceeded the choices in {self.currently_selecting}, Please go on to the next step")
            if self.currently_selecting == STAGE.Flavor:
                self.handle_flavor("next")
            elif self.currently_selecting == STAGE.Toppings:
                self.handle_toppings("done")
        
        ##UCID: mk994  Date:October 22
        ## adding the NeedsCleaningException and printing the message for user and asking input from the user to clean or not
        except NeedsCleaningException:
            need_cleaning = True
            while need_cleaning:
                print("Sorry, The machine needs cleaning.")
                response = input("Would you like to proceed with cleaning? Type yes or no\n")
                if response.lower() == "yes":
                    self.clean_machine()
                    need_cleaning = False
        
        ##UCID: mk994  Date:October 22
        ## adding the InvalidChoiceException and printing the message for user to enter the choice again
        except InvalidChoiceException:
            print("The entered choice is not available or the spelling is incorrect. Please enter again")

        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    icm = IceCreamMachine()
    icm.start()