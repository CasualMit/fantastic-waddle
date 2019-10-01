def readfile(file):
    file = open(file, 'r')
    content = file.readlines()
    file.close()
    new_string = 'heeft kaartnummer: '
    for item in content:
        item = item.split(', ')
        item.append(new_string)
        item[1] = item[1].strip('\n')
        item[0], item[1], item[2] = item[1], item[2], item[0]
        item = ' '.join(item)
        print(item)

readfile('kaartnummers.txt')