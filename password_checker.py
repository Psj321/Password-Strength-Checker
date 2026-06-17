import string

password = input("Enter your password: ")

length = len(password)

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)

score = 0

if length >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1

if score <= 2:
    strength = "Weak Password"
elif score <= 4:
    strength = "Medium Password"
else:
    strength = "Strong Password"

print("\nPassword Analysis")
print("------------------")
print(f"Length: {length}")
print(f"Uppercase Present: {has_upper}")
print(f"Lowercase Present: {has_lower}")
print(f"Number Present: {has_digit}")
print(f"Symbol Present: {has_symbol}")
print(f"\nPassword Strength: {strength}")

common_passwords = [
    "123456",
    "password",
    "admin",
    "qwerty"
]

if password.lower() in common_passwords:
    print("Very Weak Password ❌ (Common Password)")
