'''
if (5 > 2):
    print("5 is greater than 2!")
else:
    print("error")
'''

income = float(input())
tax = income / 10
if income < 1000000:
    tax = 0
print(tax)