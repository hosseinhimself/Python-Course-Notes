num = int(input("Enter a number: "))

# student = dict()
student = {}
for std in range(num):
    std_name = input("Enter Student's name: ")
    std_score = float(input("Enter student's score: "))
    student[std_name] = std_score

print(student)
