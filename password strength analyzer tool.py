import re
import sys

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Common passwords list (can be expanded)
    common_passwords = {"password", "123456", "qwerty", "abc123", "letmein", "password1"}
    
    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    
    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    
    # Digit check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&* etc.).")
    
    # Common password check
    if password.lower() in common_passwords:
        feedback.append("Avoid using common passwords.")
        strength = 1  # Force it to weak
    
    # Strength evaluation
    if strength == 5:
        return "Strong", feedback
    elif strength >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

# CLI Interaction
def main():
    print("\n🔐 Password Strength Analyzer 🔐\n")
    
    try:
        print("Enter your password:", end=" ")
        password = sys.stdin.readline().strip()  # Using sys.stdin.readline to avoid I/O errors in restricted environments
        
        if not password:
            print("Error: No input detected.")
            return
        
        strength, feedback = check_password_strength(password)
        
        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions:")
            for tip in feedback:
                print(f"- {tip}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
