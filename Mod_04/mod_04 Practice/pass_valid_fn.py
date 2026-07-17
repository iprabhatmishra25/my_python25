def validate_password(password, min_length=8):
    reasons = []
    
    # Minimum length check
    if len(password) < min_length:
        reasons.append(f"Password must be at least {min_length} characters long.")
        
    # At least one uppercase letter
    if not any(char.isupper() for char in password):
        reasons.append("Password must contain at least one uppercase letter.")
        
    # At least one digit
    if not any(char.isdigit() for char in password):
        reasons.append("Password must contain at least one digit.")
        
    # If reasons list is empty, password is valid
    is_valid = len(reasons) == 0
    return is_valid, reasons

# --- Test Cases ---
test_passwords = [
    "SecureP@ss12",  # Valid (Meets length, has uppercase and digit)
    "Python2026",    # Valid (Meets length, has uppercase and digit)
    "short1",        # Invalid (Too short, lacks uppercase)
    "NoDigitsHere"   # Invalid (Lacks a digit)
]

print("--- Password Validation Results ---")
for pwd in test_passwords:
    valid, errors = validate_password(pwd)
    print(f"Password: {pwd!r}")
    print(f"  Valid:  {valid}")
    if not valid:
        print(f"  Errors: {errors}")
    print("-" * 35)