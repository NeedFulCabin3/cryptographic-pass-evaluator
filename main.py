import re
import numpy as np
from sklearn.linear_model import LogisticRegression

def extract_features(password):
    """Extract numerical features from a given password string."""
    length = len(password)
    upper_count = sum(1 for c in password if c.isupper())
    lower_count = sum(1 for c in password if c.islower())
    digit_count = sum(1 for c in password if c.isdigit())
    special_count = sum(1 for c in password if not c.isalnum())
    
    # Check for predictable patterns
    has_sequence = 1 if re.search(r'(012|123|234|345|456|567|678|789|abc|bcd|cde|def)', password.lower()) else 0
    has_repetition = 1 if re.search(r'(.)\1{2,}', password) else 0
    
    return [length, upper_count, lower_count, digit_count, special_count, has_sequence, has_repetition]

def generate_synthetic_dataset():
    """Generates a synthetic training dataset of passwords (0: Vulnerable, 1: Secure)."""
    vulnerable_samples = [
        "password", "123456", "admin123", "qwerty", "welcome1", 
        "abc123", "letmein", "111111", "password123", "12345678",
        "abc", "12345", "iloveyou", "monkey", "dragon"
    ]
    
    secure_samples = [
        "Tr0ub4d0ur&9!", "Correct-Horse-Battery-Staple-2026", "Xkcd#Passphrase*77", 
        "M#9zQ!vL2p$kR8w", "B3.St-Pr0t3ct10n!", "Alpha-Bravo-77-Delta!", 
        "Secure#Pass_9921", "P@ssw0rd_Is_Not_Enough!", "V3ry-S3cur3-Str1ng#99",
        "Quantum_Leap_2026_Secure!"
    ]
    
    X = [extract_features(p) for p in vulnerable_samples + secure_samples]
    y = [0] * len(vulnerable_samples) + [1] * len(secure_samples)
    
    return np.array(X), np.array(y)

def main():
    print("=== Synthetic Password Strength Evaluator ===")
    print("Training classifier model on synthetic character distribution metrics...")
    
    X_train, y_train = generate_synthetic_dataset()
    model = LogisticRegression()
    model.fit(X_train, y_train)
    print("Model training complete.\n")
    
    while True:
        try:
            user_input = input("Enter a passphrase to evaluate (or type 'exit' to quit): ").strip()
            if user_input.lower() == 'exit':
                print("Exiting program. Stay secure!")
                break
            if not user_input:
                print("Passphrase cannot be empty. Please try again.\n")
                continue
            
            features = np.array([extract_features(user_input)])
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0][prediction]
            
            status = "SECURE" if prediction == 1 else "VULNERABLE"
            print(f"Result: [{status}] (Confidence: {probability * 100:.2f}%)\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\nExiting program.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    main()