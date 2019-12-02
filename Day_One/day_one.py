# ----- Part One ----
# get data from file
dataFile = open('./values_to_process.txt')

# convert the lines into a list
masses_of_modules = dataFile.readlines()


def calculate(mass_of_module):
    mass_divided = mass_of_module // 3
    fuel_needed = mass_divided - 2
    return fuel_needed if fuel_needed > 0 else 0


fuel_for_each_module = map(lambda mass: calculate(int(mass)), masses_of_modules)

total_fuel_needed = sum(fuel_for_each_module)
print(f'{total_fuel_needed}')


# ---- End of Part One ---

# ---- Part Two ----
def calculate_including_fuel(mass):
    if mass == 0:
        return 0
    else:
        return mass + calculate_including_fuel(calculate(mass))


def true_fuel_need_for_mdoule(mass_of_module):
    initial_fuel_needed = calculate(mass_of_module)
    return calculate_including_fuel(initial_fuel_needed)


all_fuel_needed_for_modules = map(lambda mass: true_fuel_need_for_mdoule(int(mass)), masses_of_modules)
all_fuel_needed = sum(all_fuel_needed_for_modules)

print(f'{all_fuel_needed}')
# ---- End of Part Two ---
