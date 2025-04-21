![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/github/license/nanaelie/password-manager-python?color=green)
![Issues](https://img.shields.io/github/issues/nanaelie/password-manager-python)
![Last Commit](https://img.shields.io/github/last-commit/nanaelie/password-manager-python)
![Stars](https://img.shields.io/github/stars/nanaelie/password-manager-python?style=social)
![Forks](https://img.shields.io/github/forks/nanaelie/password-manager-python?style=social)
![Code Style](https://img.shields.io/badge/code%20style-pep8-orange)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue)
![SQLite](https://img.shields.io/badge/database-SQLite-lightgrey?logo=sqlite&logoColor=003B57)
![DB Secure](https://img.shields.io/badge/database-secured-green)
![CLI Tool](https://img.shields.io/badge/interface-CLI-orange)
![Open Source](https://img.shields.io/badge/open--source-yes-brightgreen)
![DB Secure](https://img.shields.io/badge/database-secured-green)
![Security](https://img.shields.io/badge/security-implemented-important)
![Encryption](https://img.shields.io/badge/encryption-enabled-blue)
![Data Privacy](https://img.shields.io/badge/data--privacy-GDPR%20friendly-success)

# Password Manager in Python

This is a Python-based **password manager** that helps you securely store and manage your passwords. With features like password generation, account storage, retrieval, updating, and deletion, this tool is perfect for individuals looking to manage their passwords securely and efficiently.

### Key Features:
- **Generate Strong Passwords**: Automatically generate strong, secure passwords of customizable lengths.
- **Store Accounts**: Add new accounts and their corresponding passwords securely to the database.
- **Retrieve Accounts**: Get the saved information of a specific account when needed.
- **Update Account Details**: Update the password for an existing account.
- **Remove Accounts**: Delete accounts you no longer need from the database.
- **Display All Accounts**: View all stored accounts and their passwords.

## Installation

To install and use the Password Manager, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/nanaelie/password-manager-python.git
   ```

2. Navigate to the project directory:
   ```bash
   cd password-manager-python
   ```

3. Run the application:
   ```bash
   python main.py --help
   ```

## Usage

### Add a new account:
To add a new account, use the `add-account` command:
```bash
python main.py add-account --name "account_or_website_name" --pswd "your_password_here"
```

### Generate a password:
To generate a new password of a specified length:
```bash
python main.py --generate 16
```

### View all accounts:
To display all saved accounts:
```bash
python main.py display-accounts
```

### Update an account:
To update an account's password by ID:
```bash
python main.py --update-account ID
```
and put the new password

### Remove an account:
To remove an account by its ID:
```bash
python main.py --remove-account --id ACCOUNT_ID
```

## Technologies Used
- **Python 3.x**: The script is written in Python and leverages standard libraries.
- **Argparse**: For handling command-line arguments.
- **SQLite**: For storing account data securely in a local database.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

### Optimized for SEO:
- **Password Manager Python**: A reliable, open-source password manager built with Python.
- **Secure password storage**: Safely store your passwords with this Python tool.
- **Password generator**: Create strong passwords with customizable lengths.

Feel free to create issues or pull requests if you'd like to contribute or have suggestions!
