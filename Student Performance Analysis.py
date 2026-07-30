print("==Student Performance Analysis==")

name = input("Enter student name: ")
#Take marks for 5 subjects
english = float(input("Enter English marks: "))
physics = float(input("Enter Physics marks: "))
maths = float(input("Enter Maths marks:"))
biology = float(input("Enter Biology marks:"))
computer = float(input("Enter Computer marks:"))
total = english+physics+maths+biology+computer
average= total/5
#Decide grades
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B+"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F- Fail"
print("\n---Result ---")
print(f"Student: {name}")
print(f"Total Marks: {total}/500")
print(f"Average: {average:.2f}%") # f  <-- make sure F is small
print(f"Grade: {grade}")

if average >= 40:
    print(" Status: PASS🎉")
else:
     print("Status: FAIL 😢 Keep Trying")