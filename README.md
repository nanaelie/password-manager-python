![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/nanaelie/psmgr)
[![PyPI version](https://badge.fury.io/py/pmgr.svg)](https://pypi.org/project/psmgr/)
![License](https://img.shields.io/github/license/nanaelie/psmgr?color=green)
![Issues](https://img.shields.io/github/issues/nanaelie/psmgr)
![Last Commit](https://img.shields.io/github/last-commit/nanaelie/psmgr)
![Stars](https://img.shields.io/github/stars/nanaelie/psmgr?style=social)
![Forks](https://img.shields.io/github/forks/nanaelie/psmgr?style=social)
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
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate/?hosted_button_id=A8FW9JNVMMPAU)

# Password Manager in Python

This is a Python-based **password manager** that helps you securely store and manage your passwords. With features like password generation, account storage, retrieval, updating, and deletion, this tool is perfect for individuals looking to manage their passwords securely and efficiently.

### Key Features:
- **Generate Strong Passwords**: Automatically generate strong, secure passwords of customizable lengths.
- **Store Accounts**: Add new accounts and their corresponding passwords securely to the database.
- **Retrieve Accounts**: Get the saved information of a specific account when needed.
- **Update Account Details**: Update the password for an existing account.
- **Remove Accounts**: Delete accounts you no longer need from the database.
- **Display All Accounts**: View all stored accounts and their passwords.
Here are the instructions you can provide to others for installing and using your `psmgr` project:

## Installation

To install **psmgr**, follow these steps:

1. **Clone the GitHub repository**:
   ```bash
   git clone https://github.com/nanaelie/psmgr.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd psmgr
   ```

3. **Install the package locally using `pip`**:
   ```bash
   pip install .
   ```
   
## Usage

Once installed, you can use **psmgr** directly from the command line.

### Global
```
$ psmgr --help   
usage: psmgr [-h] [--remove-account RM_ACCOUNT] [--generate GENERATE]
             [--get-account GET_ACCOUNT] [--update-account UPDATE_ACCOUNT] [-v]
             {add-account,display-accounts} ...

Gestionnaire de compte permettant de :
- Générer un mot de passe robuste (taille >= 12)
- Sauvegarder le mot de passe d'un compte
- Récupérer les informations d'un compte
- Supprimer un compte
- Mettre à jour le mot de passe d'un compte

positional arguments:
  {add-account,display-accounts}
    add-account         Add a new account
    display-accounts    Display all accounts information

options:
  -h, --help            show this help message and exit
  --remove-account RM_ACCOUNT
                        Remove account by ID
  --generate GENERATE   Generate a new password
  --get-account GET_ACCOUNT
                        Get information of an account
  --update-account UPDATE_ACCOUNT
                        Update an account's information
  -v, --version         show program's version number and exit
```

### Add a new account:
To add a new account, use the `add-account` command:
```bash
psmgr add-account --name "account_or_website_name" --pswd "your_password_here"
```

### Generate a password:
To generate a new password of a specified length:
```bash
psmgr --generate 16
```

### View all saved accounts:
To display all saved accounts:
```bash
psmgr display-accounts
```

### Update an account:
To update the password for an account by its ID:
```bash
psmgr --update-account ID
```

### Remove an account:
To remove an account by its ID:
```bash
psmgr --remove-account ACCOUNT_ID
```

## Technologies Used
- **Python 3.x**: The script is written in Python and leverages standard libraries.
- **Argparse**: For handling command-line arguments.
- **SQLite**: For storing account data securely in a local database.
- **Pandas**: For formatting and displaying account data in a readable tabular format.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate/?hosted_button_id=A8FW9JNVMMPAU)

### Optimized for SEO:
- **Password Manager Python**: A reliable, open-source password manager built with Python.
- **Secure password storage**: Safely store your passwords with this Python tool.
- **Password generator**: Create strong passwords with customizable lengths.

Feel free to create issues or pull requests if you'd like to contribute or have suggestions!

### Support

*If you find this project useful and want to support its development, you can make a donation [here](https://www.paypal.com/donate/?hosted_button_id=A8FW9JNVMMPAU).
Every contribution helps me dedicate more time to improving this tool. Thank you!*

*Si ce projet vous est utile et que vous souhaitez encourager son développement, vous pouvez faire un don [ici](https://www.paypal.com/donate/?hosted_button_id=A8FW9JNVMMPAU).
Chaque contribution m'aide à consacrer plus de temps à améliorer cet outil. Merci !*
