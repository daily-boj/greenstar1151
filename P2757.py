Table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def excelcolumn(number):
    output = ''
    while number > 0:
        number, r = divmod(number - 1, 26)
        c = Table[r]
        output += c
    return output[::-1]


while True:
    query = tuple(input().split('C'))
    row = int(query[0][1:])
    column = int(query[1])
    if (row + column) == 0:
        break
    else:
        pass
    print(excelcolumn(column) + str(row))
