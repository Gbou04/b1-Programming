import string
import random # used for generating random elements

# PART A- Individual rule checkers

def check_min_length(password, min_len=8):
    return len(password) < min_len

def has_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)

def has_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    return any(char in string.punctuation for char in password)

# PART B: MASTER VALIDATION FUNCTION

def validate_password(password):
    results = {
        'min_length': check_min_length(password),
        'has_uppercase': has_uppercase(password),
        'has_lowercase': has_lowercase(password),
        'has_digit': has_digit(password),
        'has_special_char': has_special_char(password),
    }

    results["is_valid"] = all(results.values())
    return results

# PART C: USER INTERFACE AND TESTING

def main():
    password = input("Enter a password: ")

    results = validate_password(password)

    print("\nPassword Check Results:")
    print("------------------------")
    print(f"Minimum length (8+): {'Met' if results["min_length"] else 'Not Met'} ")
    print(f"Has uppercase: {'Met' if results["has_uppercase"] else 'Not Met'} ")
    print(f"Has lowercase: {'Met' if results["has_lowercase"] else 'Not Met'} ")
    print(f"Has digit: {'Met' if results["has_digit"] else 'Not Met'} ")
    print(f"Has special char: {'Met' if results["has_special_char"] else 'Not Met'} ")

    print("\nOverall Password Validation Results:")
    if results["is_valid"]:
        print("Strong password;)")
    else:
        print("Weak password:( Try again!")

        # Extra
        messages = [
            "Remember: What lies behind up and what lies before us are tiny matter compared to what lie within us. "
            "Never let the things you want make you forget the things you have. "
            "I'm proud of you."
        ]
        print("Hint:", random.choice(messages))

if __name__ == '__main__':
    main()