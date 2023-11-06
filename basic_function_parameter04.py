# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def calculate_average(l):
    s=0
    a=0
    for i in range(len(l)):
        s+=l[i]
        a+=1
    return s/a, l 
l=[1,2,3,4,5,6,7,8]
print(calculate_average(l))