# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels(l):
    s=0
    a=0
    for i in range(len(l)):
        if l[i]=="i" or l[i] == "a"or l[i]=="u" or l[i]=="o" or l[i]=="e" or l[i]==" o' ":
            s+=1
    return l,s
l="wqevfswdecvfxaiacdfvd"
print(count_vowels(l))
