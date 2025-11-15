MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def app(dict_menu, resources):
  # Create Menu from database
  _menu = dict_menu.copy()
  if 'money' not in resources: resources["money"] = 0
  menu_list = [key for key in _menu]

  # Show menu
  input_question = "\nWhat would you like? (espresso/latte/cappuccino): "
  input_responds = input(input_question).strip().lower()

  # Validate Input
  while input_responds not in menu_list + ['off', 'report']:
    print("\nERROR: INVALID INPUT\n")
    input_responds = input(input_question)
    # Input is 'off'
  if input_responds == 'off': return
    # Input is 'report'
  if input_responds == 'report':
      for key, value in resources.items():
        if key == 'money': _value = f"${value}"
        elif key == 'coffee': _value = f"{value}g"
        else: _value = f"{value}ml"
        print(f"{key.capitalize()}: {_value}")
      return
  
    # Check if resources sufficient
  coffee = _menu[input_responds]
  is_resource_sufficient = True
  for key, value in resources.items():
    if key not in coffee["ingredients"]: continue
    if value < coffee["ingredients"][key]:
      # Insufficient resources
      is_resource_sufficient = False
      print(f"Sorry there is not enough {key}.")
      break
  if not is_resource_sufficient: return

    # Process Coin
  print("\nPlease insert coins.")
  coins = {
    'list': ['quarters', 'dimes', 'nickles', 'pennies'],
    'totals': 0,
  }
  for coin_name in coins['list']:
    input_question = f"How many {coin_name}?: "
    input_coin = ''
    is_invalid_input = False
    while type(input_coin) != int: 
      try:
        if is_invalid_input: print("\nERROR: INVALID INPUT\n")
        input_coin = input(input_question).strip()
        input_coin = int(input_coin) if input_coin != '' else 0
        is_invalid_input = False
      except ValueError:
        is_invalid_input = True
        continue
    if coin_name == 'quarters': multiplier = 0.25
    elif coin_name == 'dimes': multiplier = 0.1
    elif coin_name == 'nickles': multiplier = 0.05
    else: multiplier = 0.01
    coins['totals'] += round(input_coin * multiplier, 2)

  # Check if coin enough
  is_enough_coin = coins['totals'] >= coffee['cost']
    # Refund coin
  if not is_enough_coin:
    print(f"\nSorry that's not enough money. ${coins['totals']} refunded.")
    return
    # Process Transcaction
  resources['money'] += coffee['cost']
  coins_change = round(coins['totals'] - coffee['cost'], 2)
  if coins_change: print(f"\nHere is ${coins_change} in change.")

    # Make coffee
  for key_r, _ in resources.items():
    if key_r == 'money': continue
    for key_c, value_c in coffee["ingredients"].items():
      if key_r == key_c: resources[key_r] -= value_c

    # Print coffee
  print(f"\nHere is your {input_responds} ☕ Enjoy!")
  
app(MENU, resources)

# Note:
# Question printed in input_responds_menu was NOT DYNAMIC
# No easy input for input_responds_menu such as 1,2,3