#  6. Write a generator function in Python that yields the powers of 2 up to a given
#      exponent.

def exponent(expo):
    for i in range(1,expo+1):
        finalvalue=base**i
        yield finalvalue
base=2
inpvalue=int(input("Enter the Max Value of Exponent for base 2 :"))
result=exponent(inpvalue)
print("Now Using 'next(result)' function , you can iterate to subsiquent values.")
