row = 6
# row = int(input(enter row ))
"""uncomment the line to take user input"""
for i in range(row):
    i = row
    if row>=1:
        row-=1
    for j in range(i):
        print(i,end=" ")
    print()


# Inverted half pyramid with start
row = 6
for i in range(row):
    i = row
    if row>=1:
        row-=1
    for j in range(i):
        print("*",end=" ")
    print()