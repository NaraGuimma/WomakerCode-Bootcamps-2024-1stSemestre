import os
import secrets

secret_key = secrets.token_hex(16)  # Generate a 32-character hexadecimal string
print("Generated secret key:", secret_key)