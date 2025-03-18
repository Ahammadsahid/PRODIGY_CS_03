import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Check password length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Make your password at least 8 characters long.")
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    
    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    # Check for special characters
    if any(char in '!@#$%^&*(),.?":{}|<>' for char in password):
        strength += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&*, etc.).")
    
    # Determine password strength
    if strength >= 5:
        return "Strong Password!", feedback
    elif strength >= 3:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, suggestions = check_password_strength(password)
    print(f"Password Strength: {strength}")
    
    if suggestions:
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
