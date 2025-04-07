print("Welcome to Vitals Tracker!")

name = input("What is your name? ")
gender = input("What is your gender? (male/female): ")
hb = float(input("Enter your hemoglobin (Hb) value: "))

if gender == "male" and hb < 13:
    status = "Low"
elif gender == "female" and hb < 12:
    status = "Low"
else:
    status = "Normal"

print(f"Hello, {name}! Your hemoglobin level is {gender}.")
