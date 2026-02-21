passwords = ["Pass123", "SecurePassword1", "weak", "MyP@ssw0rd", "NOLOWER123"]

def is_valid(password):
    # Rule 1: Minimum length 8
    if len(password) < 8:
        return False
    # Rule 2: At least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    # Rule 3: At least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    # Rule 4: At least one digit
    if not any(char.isdigit() for char in password):
        return False
    return True

for password in passwords:
    if is_valid(password):
        print(f"{password} -> Compliant")
    else:
        print(f"{password} -> Not compliant")
