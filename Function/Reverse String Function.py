# Create a Python function that accepts a string and returns the reverse of that string

def reversestr(a):
    finalstr=str()
    for i in reversed(a):
        finalstr+=i
    return finalstr

inpstr=input('Enter a String to Reverse it :')
print(reversestr(inpstr))
