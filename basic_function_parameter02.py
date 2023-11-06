# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.
def calculate_sum(allamurod):
    s=0
    for i in range(len(allamurod)):
        s+=allamurod[i]
    return allamurod ,s
l=[2,5,5,6,6,45]
print(calculate_sum(l))
