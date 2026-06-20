Password Generator

Overview

This is a simple Python-based Password Generator tool that creates strong random passwords, evaluates their strength, and allows users to save passwords securely in a local text file.

Features

- Generates secure random passwords
- Ensures inclusion of uppercase, lowercase, digits, and symbols
- Checks password strength (Weak, Medium, Strong)
- Saves passwords to a local file
- Simple command-line interface

Tech Stack

- Python3
- Random module
- String module
- Regular expressions (re module)

How It Works

1. User selects password generation option
2. User enters desired password length
3. System generates a strong random password
4. Password strength is evaluated
5. User can choose to save password to file

Project Structure

password-generator/
│
├── main.py
├── passwords.txt
└── README.md

Installation and Setup

1. Clone the repository
git clone https://github.com/your-username/password-generator.git

2. Go to project folder
cd password-generator

3. Run the program
python main.py

Example Output

Generated Password: A7@kLp9#zT
Strength: Strong

Future Improvements

- GUI version using Tkinter or Streamlit
- Copy-to-clipboard feature
- Password history manager
- Encryption for saved passwords
- Web version of generator

Author

Name: Yama Kavitha  
GitHub: https://github.com/your-username  

License

This project is for educational purposes only.
