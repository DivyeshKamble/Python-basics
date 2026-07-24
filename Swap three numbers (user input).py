#code to input three numbers from user and swap them 
x = float(input("Enter 1st number : "))
y = float(input("Enter 2nd number : "))
z = float(input("Enter 3rd number : "))
print ("Original numbers :",x,y,z )
x,y,z =y,z,x 
print("After swapping : ",x,y,z)