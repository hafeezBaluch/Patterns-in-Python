row = 4
col  = 5

# hollow ractangle for numbers
for i in range(row):
    for j in range(col):
        if i == 1 or j ==1 or i ==row or j == col:
            print(i,end=" ")
    print()