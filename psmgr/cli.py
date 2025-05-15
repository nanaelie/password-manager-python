#!/usr/bin/python3

import argparse
import os
from .__version__ import __version__

try:
    from .core import PasswordManager, create_database
except ModuleNotFoundError:
    raise FileNotFoundError("Can't continue without the core.py file.")

user_home = os.path.expanduser("~")
os.makedirs(os.path.join(user_home, ".psmgr"), exist_ok=True)
db_path = os.path.join(user_home, ".psmgr", "database.db")

if not os.path.exists(db_path):
    create_database(db_path)

def main():
    parser = argparse.ArgumentParser(
        description="Password manager allowing to: \n"
                    "- Generate a strong password (length ≥ 12)\n"
                    "- Save a password for an account\n"
                    "- Retrieve account information\n"
                    "- Delete an account\n"
                    "- Update an account's password"
    )
    
    subparsers = parser.add_subparsers(dest="command")

    add_account_parser = subparsers.add_parser("add-account", help="Add a new account")
    add_account_parser.add_argument("--ptf", dest="platform", help="Platform name for the new account (ex: Facebook, Instagram)", required=True)
    add_account_parser.add_argument("--uname", dest="username", help="Username for the new account", required=True)
    add_account_parser.add_argument("--pswd", dest="password", help="Password for the new account", required=True)
    subparsers.add_parser("display-accounts", help="Display all accounts information")

    parser.add_argument("--remove", "--rm", dest="rm_account", help="Remove account by ID")
    parser.add_argument("--generate", dest="generate", type=int, help="Generate a new password")
    parser.add_argument("--get", dest="get_account", help="Get information of an account")
    parser.add_argument("--update", dest="update_account", help="Update an account's information")

    parser.add_argument("-v", "--version", action="version", version=f"psmgr {__version__}")
    
    args = parser.parse_args()

    psmgr = PasswordManager()

    if args.command == "add-account":
        platform = args.platform.strip()
        username = args.username.strip()
        password = args.password.strip()

        if not platform or len(platform.split()) > 1:
            raise ValueError("Invalid platform name.")
        if not username or len(username.split()) > 1:
            raise ValueError("Invalid username.")
        if not password or len(password.split()) > 1:
            raise ValueError("Invalid password.")
        
        psmgr.add(platform, username, password)

    elif args.rm_account:
        psmgr.remove(args.rm_account)
    elif args.generate:
        psmgr.generate(args.generate)
    elif args.get_account:
        psmgr.get(args.get_account)
    elif args.command == "display-accounts":
        psmgr.show_all()
    elif args.update_account:
        psmgr.update(args.update_account)

if __name__ == "__main__":
    main()


