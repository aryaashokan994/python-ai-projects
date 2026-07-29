print("---BMI Calculator---")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
print(f"\nYour BMI: {bmi:.2f}")

if bmi <18.5:
    print("Category: Underweight")
elif bmi<24.9:
    print("Catergory: Normal")
else:
    print("Category: Overweight")