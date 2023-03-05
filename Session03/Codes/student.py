score_list = []

counter = int(input("Enter students numbers: "))

for i in range(counter):
    score = float(input("Enter Score:"))
    while score < 0 or score > 20:
        print("Error")
        score = float(input("Enter Score:"))
    score_list.append(score)

print(score_list)