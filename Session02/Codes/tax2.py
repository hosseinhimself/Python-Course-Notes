income = float(input())
if income < 1000000:
    tax = 0
else:
    tax = (income-1000000)/10
print(tax)