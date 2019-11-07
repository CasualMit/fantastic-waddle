# nums = [1, 2, 3, 4, 5]
#
# for num in nums:
#     if num < 3:
#         continue
#     else:
#         print(num)
#
# print()
#
# for num in nums:
#     if num == 3:
#         break
#     else:
#         print(num)

def sum():
    total = 0
    while True:
        nextInt = input('next int: ')
        if nextInt == 'quit':
            break
        total += int(nextInt)
    print(total)

sum()

