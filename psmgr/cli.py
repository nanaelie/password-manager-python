#!/usr/bin/python3

import argparse
import os
from .__version__ import __version__

try:
    from .core import PasswordManager, create_database
except ModuleNotFoundError:
    raise FileNotFoundError("Can't continue without the core.py file.")

project_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(project_dir, "data"), exist_ok=True)
db_path = os.path.join(project_dir, "data", "database.db")
if not os.path.exists(db_path):
    create_database()

def main():
    parser = argparse.ArgumentParser(
        description="Gestionnaire de compte permettant de :\n"
                    "- Générer un mot de passe robuste (taille >= 12)\n"
                    "- Sauvegarder le mot de passe d'un compte\n"
                    "- Récupérer les informations d'un compte\n"
                    "- Supprimer un compte\n"
                    "- Mettre à jour le mot de passe d'un compte"
    )
    
    subparsers = parser.add_subparsers(dest="command")

    # Sous-commande add-account
    add_account_parser = subparsers.add_parser("add-account", help="Add a new account")
    add_account_parser.add_argument("--name", dest="account_name", help="Account name for the new account", required=True)
    add_account_parser.add_argument("--pswd", dest="password", help="Password for the new account", required=True)
    subparsers.add_parser("display-accounts", help="Display all accounts information")

    # Autres sous-commandes
    parser.add_argument("--remove-account", dest="rm_account", help="Remove account by ID")
    parser.add_argument("--generate", dest="generate", type=int, help="Generate a new password")
    parser.add_argument("--get-account", dest="get_account", help="Get information of an account")
    parser.add_argument("--update-account", dest="update_account", help="Update an account's information")

    parser.add_argument("-v", "--version", action="version", version=f"psmgr {__version__}")
    
    args = parser.parse_args()

    password_manager = PasswordManager()

    if args.command == "add-account":
        account_name = args.account_name.strip()
        password = args.password.strip()

        if not account_name or len(account_name.split()) > 1:
            raise ValueError("Invalid account name.")
        if not password or len(password.split()) > 1:
            raise ValueError("Invalid password.")
        
        password_manager.add(account_name, password)

    elif args.rm_account:
        password_manager.remove(args.rm_account)
    elif args.generate:
        password_manager.generate(args.generate)
    elif args.get_account:
        password_manager.get(args.get_account)
    elif args.command == "display-accounts":
        password_manager.show_all()
    elif args.update_account:
        password_manager.update(args.update_account)

if __name__ == "__main__":
    main()


