# break
list_7 = [2, 3, 4, 5, 5, 6, 7, 8, 10]

for i in list_7:
    if i == 7:
        print('index is:', list_7.index(i))
        break
    else:
        print('OK')
