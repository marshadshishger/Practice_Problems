# Factorial Number Finding

inp=int(input("Enter a Numbr to find its Factorial : "))

def f(x):
    factorial=1
    if x>=1:
        for i in range(1,x+1):
            factorial=factorial*i
        return factorial
    elif x<0:
        return print("Factorial do not exist.")
    elif x==0:
        return factorial
    else:
        print("ERROR")
    

print(f(inp))
        
