# Write a Python function that takes a list of numbers as input and returns the sum of all
# even numbers in the list.

n=int(input('Enter the Total Amount of Numbers :'))
inplist=[]

for element in range (0,n):
    if element==n-1:
        print("This is the last term to Enter")
        inp=int(input('Enter the Number : '))
        inplist.append(inp)
    else:
        inp=int(input('Enter the Number : '))
        inplist.append(inp)

    
def suml(a):
    suml=0
    for i in a:
        suml+=i
    return suml
print("The Sum of all these is ",suml(inplist))
