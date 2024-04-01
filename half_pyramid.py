row = 6
# n = int(input(enter the row: ))
"""uncomment the line to take user input"""
# half pyramid with numbers
for i in range(row):
    for j in range(i):
        print(i,end=" ")
    print()
    
# half pyramid with star
row = 6
for i in range(row):
    for j in range(i):
        print("*",end=" ")
    print()