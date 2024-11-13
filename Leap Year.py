inp=int(input("Enter the Year"))
output=inp%4
output2=inp%100
output3=inp%400
if (output==0):
    if (output2 == 0) :
        if(output3 == 0) :
            print("The given year is a Leap Year")
        else :
            print("The given year is  not a Leap Year")
    else :
        print("The given year is a Leap Year")
else :
    print("The given year is not a Leap Year")

    
    
