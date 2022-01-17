operationFuncs = {
    Operation.START: strategy_objects.StartObject
    Operation.STOP: strategy_objects.StopObject
    Operation.STATUS: strategy_objects.StatusObject
    (...)                  
}
try:
    strategy = operationFuncs[operation]()
except KeyError:
    strategy = strategy_objects.DefaultObject()

strategy = operationFuncs.get(operation(), DefaultObject())

deal2action = {
('iphone 7', '64', '700'):'ACT'
}

def green_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")
def blue_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")
def red_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")
def pink_function(color):
    # Execute some code, for example print the color + number "1"
    print(f"{color} 1")

colors_dict = {
    "green": green_function,
    "blue": blue_function,
    "red": red_function,
    "pink": pink_function,
}

user_input = input("")
colors_dict.get(user_input)(user_input)