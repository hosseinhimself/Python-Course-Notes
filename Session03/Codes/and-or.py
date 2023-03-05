#  False    True
if 1 > 2 or 1 < 3:
    print("OK!")

#  False    False
if 1 > 2 or 1 > 3:
    print("OK!")
else:
    print("Not OK!")

#  False    False
if 1 > 2 and 1 > 3:
    print("OK!")
else:
    print("Not OK!")

#  True    False
if 1 < 2 and 1 > 3:
    print("OK!")
else:
    print("Not OK!")

#  True    True
if 1 < 2 and 1 < 3:
    print("OK!")
else:
    print("Not OK!")
