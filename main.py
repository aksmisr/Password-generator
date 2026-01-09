import random
import string
import pyperclip

def check_strength(pwd):
    score = 0
    if any(c.islower() for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in string.punctuation for c in pwd): score += 1

    levels = ["Weak", "Medium", "Strong", "Very Strong"]
    return levels[score - 1] if score > 0 else "Very Weak"


while True:
    print("\nChoose password strength:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    level = input("Enter choice (easy / medium / hard): ").lower()

    if level == "easy":
        chars = string.ascii_letters
        min_length = 6

    elif level == "medium":
        chars = string.ascii_letters + string.digits
        min_length = 8

    elif level == "hard":
        chars = string.ascii_letters + string.digits + string.punctuation
        min_length = 12

    else:
        print("❌ Invalid choice. Try again.")
        continue

    try:
        length = int(input(f"Enter password length (min {min_length}): "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if length < min_length:
        print(f"❌ Password must be at least {min_length} characters.")
        continue

