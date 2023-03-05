fruit = 'Apple'

if fruit == 'Apple':
    is_apple = True
else:
    is_apple = False

print(is_apple)

fruit = 'banana'
# (value_when_true) if (condition) else (value_when_false)
is_apple2 = True if fruit == 'Apple' else False
print(is_apple2)

llist = [1, 2, 3]
print("ok") if 4 in llist else print("error")

# Instruction for x in y
y = [1, 2, 3, 4, 5]
a = [2*x for x in y]
print(a)

# Instructions for x in y if condition
x = [1, 2, 3, 4, 5]
y = [2*a for a in x if a % 2 != 0]
print(y)

# (value_when_true) if (condition) else (value_when_false) (instruction) (x) for in (y)
x = ['Apple', 'Apple', 'Banana', 'Cherry', 'Apple']

y = [True if a == 'Apple' else False for a in x]
print(x)
print(y)
