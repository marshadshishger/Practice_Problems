# Fibonicci Series

n=int(input("Enter the Number of Terms :"))

initial, final=0,1
print(0)
print(1)
for i in range(0,n-2):
    initial,final=final,initial+final
    
    print(initial+final)
