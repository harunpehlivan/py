# Calculate expense sum for two lists without function
bharat_expenses = [20,30,45]
bilal_expenses = [45,67,34]

total = sum(bharat_expenses)
print("Bharat's total:",total)

total = sum(bilal_expenses)
print("Bilal's total:",total)

# Calculate expense sum for two lists by using a function
def find_total(exp):
    '''
    This function takes list of numbers as input and returns sum of that list
    :param exp: input list
    :return: total sum
    '''
    return sum(exp)

bharat_total=find_total(bharat_expenses)
print("Bharat's total:",bharat_total)

bilal_total=find_total(bilal_expenses)
print("Bilal's total:",bilal_total)

# Explain argument, return value, function body with visuals

# documentation strings
print(help(find_total))

# Positional argument vs named arguments
def cylinder_volume(radius,height=1):
    print("radius is:",radius)
    print("height is:",height)
    return 3.14*(radius**2)*height

r=5
h=10
print(cylinder_volume(height=h,radius=r))

# default arguments
r=5
h=10
print(cylinder_volume(radius=r))

# global vs local variables
