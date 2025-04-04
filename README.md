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
