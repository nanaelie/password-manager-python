import random
import string
import sqlite3
import os
import pandas

class LengthError(ValueError):
    def __init__(self):
        super().__init__("Password length must be >= 12 for more security")

def create_database():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(project_dir, "data"), exist_ok=True)
    db_path = os.path.join(project_dir, "data", "database.db")
    if not os.path.exists(db_path):
        print("no")
        open(db_path, "w") 
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS password_manager (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

class PasswordManager:
    def __init__(self):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        os.makedirs(os.path.join(project_dir, "data"), exist_ok=True)
        self.db_path = os.path.join(project_dir, "data", "database.db")
        self.password_database = sqlite3.connect(self.db_path)
        self.cursor = self.password_database.cursor()
        create_database()

    def generate(self, length: int):
        if length < 12:
            raise LengthError

        chars = string.ascii_letters + string.digits + "!\"#$%&'()*+-./:;<=>?@^_~"
        password = "".join(random.choices(chars, k=length))

        show = input("Do you want to display the password here? (y/n): ").strip().lower()
        if show in ("y", "yes"):
            print(f"Generated password: {password}")

        save = input("Do you want to save this password (y/n)? ").strip().lower()
        if save in ("y", "yes"):
            account_name = input("Account name: ").strip()
            if account_name:
                self.add(account_name, password)
                print(f"Password saved for account: {account_name}")

    def add(self, account: str, password: str):
        try:
            self.cursor.execute("""
                INSERT INTO password_manager (account, password)
                VALUES (?, ?)""", (account, password))
            self.password_database.commit()
            print(f"'{account}' added successfully.")
        except sqlite3.IntegrityError:
            print(f"Error: Account '{account}' already exists.")

    def remove(self, account_id: int):
        self.cursor.execute("SELECT account FROM password_manager WHERE id=?", (account_id,))
        account = self.cursor.fetchone()
        
        if account:
            self.cursor.execute("DELETE FROM password_manager WHERE id=?", (account_id,))
            self.password_database.commit()
            print(f"'{account[0]}' removed successfully.")
        else:
            print("Account not found.")

    def show_all(self):
        data = self.cursor.execute("SELECT * FROM password_manager").fetchall()
        if data:
            df = pandas.DataFrame(data, columns=["ID", "ACCOUNT", "PASSWORD"])
            print(df.to_string(index=False))
        else:
            print("No accounts found.")

    def get(self, account_id: int):
        data = self.cursor.execute("SELECT * FROM password_manager WHERE id=?", (account_id,)).fetchone()
        if data:
            print(f"{data[0]} - {data[1]} - {data[2]}")
        else:
            print("Account not found.")

    def update(self, account_id: int):
        new_password = input("New Password: ").strip()
        self.cursor.execute("UPDATE password_manager SET password=? WHERE id=?", (new_password, account_id))
        self.password_database.commit()
        print("Password updated successfully.")
