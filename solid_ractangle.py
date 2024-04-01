# solid ractangle with star
row = 4
col = 5
# row = int(input("enter rows: "))
# col = int(input("enter cols: "))
"""uncomment the row and col to take user input"""
for i in range(row):
    for j in range(col):
        print("*",end=" ")
    print()
    
# solid ractangel with numbers
for i in range(row):
    for j in range(col):
        print(i,end= " ")
    print()