def sum1(*args):
    s=0
    for i in args:
        s=s+i
    return s
args=list(input("Enter the Numbers to be added : "))
print(args)
print(sum1(args))
print(args)
