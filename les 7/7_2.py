def list(invoer):
    numbers = invoer.split('-')
    numbers = [int(x) for x in numbers]
    numbers.sort()
    print(numbers)
    largest = max(numbers)
    smallest = min(numbers)
    som = sum(numbers)
    count = numbers.count(\d)
    print(f'Largest number: {largest}, Smallest number: {smallest} ')
    print(count)










invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
list(invoer)