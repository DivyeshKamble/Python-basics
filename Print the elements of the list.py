#print the element of the list using loop
val = [1, 2, 3, 4, 5 , 6 , 5]
val1 = int(input("Enter the number to check: "))
idx=0
for i in val :
    if i == val1:
        print("Found at index", idx)
    idx += 1
