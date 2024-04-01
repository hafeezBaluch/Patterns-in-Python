row = 6
"""uncomment the line if you want the user to 
give input of row"""
#row = int(input("enter row: "))
for i in range(row):
    for j in range(i):
        print(i, end=' ')
    print()

# for printing star triangle
for i in range(row):
    for j in range(i):
        print("*",end=" ")
    print()