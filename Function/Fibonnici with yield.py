# Create an iterator class in Python that generates the Fibonacci sequence up to
# a specified number of terms.

def fib(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
    

terms=int(input("Enter no. of terms : "))
value=fib(terms)
print("Now Using 'next(value)' function , you can iterate to subsiquent values.")
        
    


    
