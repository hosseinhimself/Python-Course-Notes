list_5 = [2, 4, 5, 3, 5, 5, 6, 7, 12, 13, 45]

list_5.append(123)
print('append:', list_5)

list_5.insert(3,43)
print('insert:',list_5)

list_5.pop(4)
print('pop 1:',list_5)

list_5.pop()
print('pop 2:',list_5)

list_5.remove(2)
print('remove:', list_5)

list_5.reverse()
print('reversed:', list_5)

list_5.sort()
print('sort:', list_5)

list_6 = [1, 2, 3, 'hello', 23.5, [2, 34, 45]]
# list_6.sort()

# [4, 5, 5, 5, 6, 7, 12, 13, 43, 45]
print('index of 12:', list_5.index(12))

print('count of 5: ', list_5.count(5))

