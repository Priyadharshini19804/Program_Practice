"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

"""

rows = int(input("Enter the number of rows: "))
num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
