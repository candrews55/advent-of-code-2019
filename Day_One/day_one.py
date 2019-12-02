# ----- Part One ----
# get data from file
dataFile = open('./values_to_process.txt')

# convert the lines into a list
masses_of_modules = dataFile.readlines()


def calculate(mass_of_module):
    mass_divided = mass_of_module // 3
    return mass_divided - 2


fuel_for_each_module = map(lambda mass: calculate(int(mass)), masses_of_modules)

total_fuel_needed = sum(fuel_for_each_module)
print(f'{total_fuel_needed}')
# ---- End of Part One ---

