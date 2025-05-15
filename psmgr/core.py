import random
import string
import sqlite3
import pandas
import os
import subprocess as sp
from datetime import datetime

class LengthError(ValueError):
    def __init__(self):
        super().__init__("Password length must be >= 12 for more security")

def create_database(db_path):
    if not os.path.exists(db_path):
        open(db_path, "w")
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plateformes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plateform TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

class PasswordManager:
    def __init__(self):
        user_home = os.path.expanduser("~")
        os.makedirs(os.path.join(user_home, ".psmgr"), exist_ok=True)
        db_path = os.path.join(user_home, ".psmgr", "database.db")
        self.db_path = db_path
        self.password_database = sqlite3.connect(self.db_path)
        self.cursor = self.password_database.cursor()

    def generate(self, length: int):
        if length < 12:
            raise LengthError

        chars = string.ascii_letters + string.digits + "!\"#$%&'()*+-./:;<=>?@^_~"
        password = "".join(random.choices(chars, k=length))

        self.copy(password)
        print(f"Generated password stored in clipboard memory.")
        
        while True:
            save = input("Do you want to save this password (y/n)? ").strip().lower()
            
            if save in ("y", "yes"):
                platform = input("Platform name: ").strip()
                if not platform:
                    print("Platform name cannot be empty.")
                    continue

                username = input("Username: ").strip()
                if not username or " " in username:
                    print("Invalid username. It must not be empty or contain spaces.")
                    continue

                self.add(platform, username, password)
                print(f"Password saved for account: {platform}")
                break

            elif save in ("n", "no"):
                print("Password not saved.")
                break

            else:
                print("Invalid input. Please type 'y' or 'n'.")
                
    @staticmethod
    def timestamp():
        return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def add(self, plateform: str, username: str, password: str):
        created_at = self.timestamp()
        modified_at = created_at
        self.cursor.execute("""
            INSERT INTO plateformes (plateform, username, password, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?)""", (plateform, username, password, created_at, modified_at))
        self.password_database.commit()
        print(f"'{plateform}' added successfully.")
    
    def remove(self, account_id: int):
        self.cursor.execute("SELECT plateform FROM plateformes WHERE id=?", (account_id,))
        account = self.cursor.fetchone()
        
        if account:
            self.cursor.execute("DELETE FROM plateformes WHERE id=?", (account_id,))
            self.password_database.commit()
            print(f"'{account[0]}' removed successfully.")
        else:
            print("Account not found.")

    def show_all(self):
        data = self.cursor.execute("SELECT * FROM plateformes").fetchall()
        if data:
            df = pandas.DataFrame(data, columns=["ID", "PLATFORM", "USERNAME", "PASSWORD", "CREATED_AT", "UPDATED_AT"])
            print(df.to_string(index=False))
        else:
            print("No accounts found.")

    def get(self, account_id: int):
        data = self.cursor.execute("SELECT * FROM plateformes WHERE id=?", (account_id,)).fetchone()
        if data:
            df = pandas.DataFrame([data], columns=["ID", "PLATFORM", "USERNAME", "PASSWORD", "CREATED_AT", "UPDATED_AT"])
            print(df.to_string(index=False))
        else:
            print("Account not found.")

    def update(self, account_id: int):
        self.cursor.execute("SELECT * FROM plateformes WHERE id=?", (account_id))
        platform = self.cursor.fetchone()
        
        if platform:
            new_password = input("New Password: ").strip()
            updated_at = self.timestamp()
            self.cursor.execute("UPDATE plateformes SET password=?, updated_at=? WHERE id=?", (new_password, updated_at, account_id))
            self.password_database.commit()
            print("Password updated successfully.")
        else:
            print("No platform with this id.")
        
    @staticmethod
    def copy(password):
        sp.run(f"echo '{password}' | xclip -selection clipboard", shell=True)
        

