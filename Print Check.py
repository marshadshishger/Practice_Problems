inp=input('Enter a String')
length=len(a)

#symmatrical
reverse_index=-1
if (length%2==0):
    for i in range(0,int(length/2)):
        if (inp[i]==inp[reverse_index]):
            continue
        reverse_index-=1
        else:
            print('The given String is not Symmetrical')
else:
    print('OVER')
