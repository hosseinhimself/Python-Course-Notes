number = int(input())
counter = 1
divisor = 0
while counter <= number:
    if number % counter == 0:
        divisor = divisor + 1
    counter = counter + 1

if divisor == 2:
    print("YES!")
else:
    print("NO!")
