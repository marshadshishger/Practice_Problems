# Factorial Number Finding using Recurssion
# Max Possible input is 1024

inp=int(input("Enter a Numbr to find its Factorial : "))

def f(x):
    if x==0:
        return 1
    else:
        return x*f(x-1)

print(f(inp))       
