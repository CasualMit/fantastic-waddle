def readfile(file):
    file = open(file, 'r')
    content = file.readlines()
    file.close()

    file_lines = len(content)
    highest = max(content)
    highest_number = highest.split(',')
    line_number = content.index(highest) + 1

    output = f'Deze file telt {file_lines} regels \nHet grootste kaartnummer is: {highest_number[0]} en dat staat op regel {line_number}'
    print(output)


readfile('kaartnummers.txt')
