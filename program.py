print("Welcome to Health Tracker!")

name = input("What is your name? ")
gender = input("What is your gender? (male/female): ")
hb = float(input("Enter your haemoglobin (Hb) value: "))

# 🧪 Hemoglobin Reference Ranges
# ----------------------------
# Male:   < 13 → Low
# Female: < 12 → Low
# Otherwise → Normal

if gender == "male" and hb < 13:
    status = "Low"
# TODO: Add the female check and else part

print(f"Hello, {name}! Your haemoglobin level is {gender}.")
