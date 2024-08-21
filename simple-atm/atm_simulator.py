import time
import json
import matplotlib.pyplot as plt # type: ignore

class ATM:
    def __init__(self):
        self.users_file = 'users.json'
        self.load_users()
        
    def load_users(self):
        try:
            with open(self.users_file, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {
                "User1": {"PIN": "1234", "balance": 1000},
                "User2": {"PIN": "2222", "balance": 2000},
                "User3": {"PIN": "3333", "balance": 3000},
                "SysAdmin": {"PIN": "1357"}
            }
            self.save_users()
    
    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file)
    
    def authenticate(self, username, pin):
        user = self.users.get(username)
        if user and user["PIN"] == pin:
            return True
        return False
    
    def main_menu(self):
        while True:
            username = input("Enter your username: ")
            pin = input("Enter your 4 digit ATM Pin: ")
            if self.authenticate(username, pin):
                if username == "SysAdmin":
                    self.admin_menu()
                else:
                    self.user_menu(username)
            else:
                print("Invalid username or PIN. Try again.")
    
    def user_menu(self, username):
        while True:
            print("\n1 = Check Balance")
            print("2 = Withdraw Money")
            print("3 = Deposit Money")
            print("4 = Change PIN")
            print("5 = Exit")
            
            try:
                option = int(input('Choose any option above: '))
            except ValueError:
                print("Please choose a valid option")
                continue
            
            if option == 1:
                self.check_balance(username)
            elif option == 2:
                self.withdraw(username)
            elif option == 3:
                self.deposit(username)
            elif option == 4:
                self.change_pin(username)
            elif option == 5:
                break
            else:
                print("Invalid option. Please choose a valid option.")

    def plot_balances(self):
        usernames = []
        balances = []
        
        for username, data in self.users.items():
            if username != "SysAdmin":
                usernames.append(username)
                balances.append(data["balance"])
        
        plt.figure(figsize=(10, 5))
        plt.bar(usernames, balances, color='blue')
        plt.xlabel('Usernames')
        plt.ylabel('Balances')
        plt.title('User Balances')
        plt.show()
    
    def admin_menu(self):
        while True:
            print("\n1 = Add User")
            print("2 = Delete User")
            print("3 = View All Balances")
            print("4 = Plot User Balances")  # New option
            print("5 = Exit")
            
            try:
                option = int(input('Choose any option above: '))
            except ValueError:
                print("Please choose a valid option")
                continue
            
            if option == 1:
                self.add_user()
            elif option == 2:
                self.delete_user()
            elif option == 3:
                self.view_all_balances()
            elif option == 4:
                self.plot_balances()  # New function call
            elif option == 5:
                break
            else:
                print("Invalid option. Please choose a valid option.")
    
    def check_balance(self, username):
        print('----------------------------------')
        print(f'Your current balance is {self.users[username]["balance"]}')
    
    def withdraw(self, username):
        try:
            amount = int(input('Enter the Withdraw Amount: '))
        except ValueError:
            print("Please enter a valid amount")
            return
        if amount % 10 != 0:
            print("The amount must be a multiple of 10")
        elif amount > 1000:
            print("You can only withdraw up to $1000 at a time")
        elif amount > self.users[username]["balance"]:
            print("You do not have sufficient balance")
        else:
            self.users[username]["balance"] -= amount
            self.save_users()
            print('----------------------------------')
            print(f'{amount} is debited from your account')
            print(f'Your current balance is {self.users[username]["balance"]}')
    
    def deposit(self, username):
        try:
            amount = int(input('Enter the Deposit Amount: '))
        except ValueError:
            print("Please enter a valid amount")
            return
        self.users[username]["balance"] += amount
        self.save_users()
        print('----------------------------------')
        print(f'{amount} is credited to your account')
        print(f'Your current balance is {self.users[username]["balance"]}')
    
    def change_pin(self, username):
        new_pin = input('Enter new 4 digit PIN: ')
        if len(new_pin) == 4 and new_pin.isdigit():
            self.users[username]["PIN"] = new_pin
            self.save_users()
            print('PIN successfully changed')
        else:
            print('Invalid PIN format. Must be 4 digits.')
    
    def add_user(self):
        username = input('Enter new username: ')
        pin = input('Enter new 4 digit PIN: ')
        if len(pin) == 4 and pin.isdigit():
            self.users[username] = {"PIN": pin, "balance": 0}
            self.save_users()
            print('User added successfully')
        else:
            print('Invalid PIN format. Must be 4 digits.')
    
    def delete_user(self):
        username = input('Enter username to delete: ')
        if username in self.users:
            del self.users[username]
            self.save_users()
            print('User deleted successfully')
        else:
            print('User not found')
    
    def view_all_balances(self):
        for username, data in self.users.items():
            if username != "SysAdmin":
                print(f'{username}: {data["balance"]}')

if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
