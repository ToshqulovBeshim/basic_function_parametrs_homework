# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest(l):
    mi=l[0]
    for i in range(len(l)):
        if l[i]<=mi:
            mi=l[i]
    return mi
l=[23,3345,5456,6,7,77,72]
print(find_smallest(l))