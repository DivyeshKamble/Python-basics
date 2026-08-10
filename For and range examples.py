print("For and range examples")
#print from 1 to 100
'''for i in range (1,101):
    print(i)
'''
#print from 100 to 1
'''for i in range(100, 0, -1):
    print(i)
'''
#print from 1 to 100 but only even numbers
'''for i in range(1, 101):
    if i % 2 == 0:
        print(i)
'''
#print from 1 to 100 but skip 5 
'''for i in range(1,101):
    if i == 5:
        continue
    print(i)
'''
#print from 1 to 100 but skip 5 and its multiples
'''for i in range(1,101):
    if i % 5 == 0:
        continue
    print(i)
'''
#print the multiplication table of n
'''n = int(input('Enter a number: '))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
'''