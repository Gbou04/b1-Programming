correct_pin = "1570293"
attempts = 0
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    print(f"Attempt {attempt} of {max_attempts}")
    entered_pin = input("Enter your custom PIN: ")

    if entered_pin == correct_pin:
        print("Welcome, User! ")
        break
    else:
        print("Invalid PIN. Please try again. ")

else:
    print("Too many invalid attempts. The account has been locked. ")