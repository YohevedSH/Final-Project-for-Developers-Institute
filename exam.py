import string
from utils import unzip_with_7z

zip_file_path = 'congrats.7z'  # keep as is
dest_path = '.'  # keep as is

# List of possible characters (assuming lowercase letters only for simplicity)
possible_chars = string.ascii_lowercase

# Try all combinations of two letters
for char1 in possible_chars:
    for char2 in possible_chars:
        find_me = char1 + char2
        secret_password = find_me + 'bcmpda'
        
        # Attempt to unzip with the generated password
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            print(f"Success! The password is: {secret_password}")
            break
