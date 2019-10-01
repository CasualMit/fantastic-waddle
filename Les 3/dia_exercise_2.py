# gather facts
name = input('Enter your name: ')
age = input('Enter your age: ')


# generate result and print result
if int(age) >= 18:
    result = name + ', You are eligible to vote!'
    print(result)
else:
    years = 18 - int(age)

    print(name + ', You are not eligible to vote. You will be eligible in ' + str(years) + ' years!')

# debug
# print(name)
# print(age)