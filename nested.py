def nested(n):
    for j in range(n):
        for i in range(n):
            print(i, end=' ')
        print()


nested(5)

print('\n')
# ook cool


def nested(n):
    for j in range(n):
        for i in range(j+1):
            print(i, end=' ')
        print()


nested(10)

print('\n')
# how to get record from list in list
lsta = [0, 1, 2]
lstb = [3, 4, 5]
lstc = [6, 7, 8]

lst = [lsta, lstb, lstc]

print(lst[1][1])

print('\n')


def print2d(t):
    for row in t:
        for item in row:
            print(item, end=' ')
        print()


print2d(lst)
