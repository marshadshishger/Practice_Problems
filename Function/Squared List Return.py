# Implement a Python function that takes a list of integers and returns a new list
# containing the squares of each number.

intlist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def sqrlist(a):
    squared_list=[]
    for i in a:
        squared_list.append(i**2)
    return squared_list

print(sqrlist(intlist))
