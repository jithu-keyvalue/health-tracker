print("Welcome to Vitals Tracker!")

name = input("What is your name? ")
gender = input("What is your gender? (male/female): ")
hb = float(input("Enter your hemoglobin (Hb) value: "))

# 🧪 Hb Level Check Rule
# ----------------------
# - If male and Hb < 13 → "Low"
# - If female and Hb < 12 → "Low"
# - Else → "Normal"

if gender == "male" and hb < 13:
    status = "Low"
elif gender == "female" and hb < 12:
    status = "Low"
else:
    status = "Normal"

print(f"Hello, {name}! Your hemoglobin level is {gender}.")
