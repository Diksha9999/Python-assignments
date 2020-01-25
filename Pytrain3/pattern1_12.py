rows = input("Enter number of rows ")
rows = int (rows)
for i in range(0,rows):
    for j in range(rows,i,-1):
        print("*", end=' ')

    print("\r")

for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")

print("--------------------------------------------------------------")


num_rows = int(input("Enter the number of rows"))
k = 0
for i in range(1, num_rows + 1):
    for j in range (1, (num_rows - i) + 1):
        print(end = " ")
    while k != (2 * i - 1):
        print("*", end = "")
        k = k + 1
    k = 0
    print()
k = 2
m = 1
for i in range(1, num_rows):
    for j in range (1, k):
        print(end = " ")
    k = k + 1
    while m <= (2 * (num_rows - i) - 1):
        print("*", end = "")
        m = m + 1
    m = 1
    print()



print("--------------------------------------------------------------")


max = 100
def plus(str):
    n=len(str)
    if(n%2==0):
        print("Pls enter odd length string")
    else:
        arr = [[False for x in range(max)]
               for y in range(max)]
        m=n//2
        for i in range(n):
            for j in range(n):
                arr[i][j] = ' '
        for i in range(n):
            arr[i][m] = str[i]
        for i in range(n):
            arr[m][i] = str[i]
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")

            print()
str = "*******"
plus(str)


print("--------------------------------------------------------------------")

side = int(input("Please Enter any Side of a Square  : "))
ch = input("Please Enter any Character  : ")

print("Hollow Square Star Pattern")
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1 ):
            print('%c' %ch, end = '  ')
        else:
            print(' ', end = '  ')
    print()



print("--------------------------------------------------------------------")



def printPattern(n):
    k = 0
    for i in range(1, n + 1):
         for j in range(i, n):
            print(' ', end='')

         while (k != (2 * i - 1)):
             if (k == 0 or k == 2 * i - 2):
                print('#', end='')
             else:
                print(' ', end='')
             k = k + 1
         k = 0;
         print("")


    for i in range(0, 2 * n - 1):
        print('#', end='')




n = 6
printPattern(n)




