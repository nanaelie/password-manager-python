[![PyPI Downloads](https://static.pepy.tech/badge/psmgr)](https://pepy.tech/projects/psmgr)
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

To install **psmgr**, run this command below:

```bash
   pip install psmgr
```
   
## Usage

Once installed, you can use **psmgr** directly from the command line.

### Global
```
$ psmgr --help    
usage: psmgr [-h] [--remove RM_ACCOUNT] [--generate GENERATE] [--get GET_ACCOUNT] [--update UPDATE_ACCOUNT] [-v]
             {add-account,display-accounts} ...

Password manager allowing to: 
- Generate a strong password (length ≥ 12) 
- Save a password for an account 
- Retrieve account information 
- Delete an account - Update an account's password

positional arguments:
  {add-account,display-accounts}
    add-account         Add a new account
    display-accounts    Display all accounts information

options:
  -h, --help            show this help message and exit
  --remove RM_ACCOUNT, --rm RM_ACCOUNT
                        Remove account by ID
  --generate GENERATE   Generate a new password
  --get GET_ACCOUNT     Get information of an account
  --update UPDATE_ACCOUNT
                        Update an account's information
  -v, --version         show program's version number and exit
```

### Add a new account:
#### Global usage

```
$ psmgr add-account --help
usage: psmgr add-account [-h] --ptf PLATFORM --uname USERNAME --pswd PASSWORD

options:
  -h, --help        show this help message and exit
  --ptf PLATFORM    Platform name for the new account (ex: Facebook, Instagram)
  --uname USERNAME  Username for the new account
  --pswd PASSWORD   Password for the new account
```

### Params explanations

* `--ptf PLATFORM` → Platform name (e.g., Facebook, Instagram)
* `--uname USERNAME` → Username used on the platform
* `--pswd PASSWORD` → Password of the account

#### Example

```bash
psmgr add-account --ptf Github --uname my_github_username --pswd my_password
```

To add my `GitHub` account where my username is `my_github_username` and my password is `my_password` to the database.

> ⚠️ Username and password must not be empty and should not contain spaces.

### Generate a password:

To generate a new password of a specified length:
```bash
psmgr --generate 16
```

> Passwords must be at least 12 characters long. Shorter lengths will raise:

```
psmgr.core.LengthError: Password length must be >= 12 for more security
```

### View all saved accounts:
To display all saved accounts:
```bash
psmgr display-accounts
```

#### Example
```
$ psmgr display-accounts
 ID PLATFORM USERNAME     PASSWORD          CREATED_AT          UPDATED_AT
  3  Threads username E+x'6.w2cV@I 2025-05-15 08:57:16 2025-05-15 10:13:31
  4    Udemy  johndoe E+x'6.w2cV@I 2025-05-15 08:58:54 2025-05-15 08:58:54
```

### Update an account:
To update the password for an account by its ID:
```bash
psmgr --update ID
```

#### Example
```
$ psmgr --update 3
New Password: fubgziygih84fr8086
Password updated successfully.
```

### Remove an account:
To remove an account by its ID:
```bash
psmgr --remove-account ACCOUNT_ID
```

#### Example
```
$ psmgr --remove 3      
'Threads' removed successfully.
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

