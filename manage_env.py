#!/usr/bin/env python
import os
import sys
from pathlib import Path

def create_env_file():
    """Create .env file from .env.example if it doesn't exist."""
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_example.exists():
        print("Error: .env.example file not found!")
        sys.exit(1)
    
    if env_file.exists():
        print(".env file already exists!")
        return
    
    # Read .env.example
    with open(env_example, 'r') as f:
        content = f.read()
    
    # Write to .env
    with open(env_file, 'w') as f:
        f.write(content)
    
    print(".env file created successfully!")

def check_env_vars():
    """Check if all required environment variables are set."""
    required_vars = [
        'SECRET_KEY',
        'DEBUG',
        'ALLOWED_HOSTS',
        'EMAIL_HOST_USER',
        'EMAIL_HOST_PASSWORD',
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("Warning: The following required environment variables are not set:")
        for var in missing_vars:
            print(f"  - {var}")
    else:
        print("All required environment variables are set!")

def main():
    """Main function to manage environment variables."""
    if len(sys.argv) < 2:
        print("Usage: python manage_env.py [create|check]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'create':
        create_env_file()
    elif command == 'check':
        check_env_vars()
    else:
        print("Unknown command! Use 'create' or 'check'")
        sys.exit(1)

if __name__ == '__main__':
    main() 