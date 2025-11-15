from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# #######################################

class App:
  def __init__(self):
    self.on = True
    self.MAINTENANCE = ['off', 'report']
    self.Menu = Menu()
    self.CoffeeMaker = CoffeeMaker()
    self.MoneyMachine = MoneyMachine()

  def print_report(self):
    self.CoffeeMaker.report()
    self.MoneyMachine.report()

  def get_choice(self):
    choice = None
    while choice == None:
      choice = input(f"What would you like? ({self.Menu.get_items()}): ").strip().lower()
      if choice in self.MAINTENANCE: break
      choice = self.Menu.find_drink(choice)
    return choice

  def run(self):
    choice = self.get_choice()
    if choice == 'off':
      self.on = False
      return
    if choice == 'report':
      self.print_report()
      return
    if not self.CoffeeMaker.is_resource_sufficient(choice): return
    invalid_coin = True
    while invalid_coin:
      try:
        if not self.MoneyMachine.make_payment(choice.cost): return
        invalid_coin = False
      except ValueError:
        print("Invalid coin")
    self.CoffeeMaker.make_coffee(choice)
 
app = App()
while app.States.on: app.run()