This project report details the development of an ATM simulator. 
The simulator allows users to perform basic banking functions such as checking balances, withdrawing money, and depositing money. 
Additionally, it includes an admin mode for managing user accounts.
The ATM simulator is implemented in Python. 
The main functionalities include user authentication, balance checking, withdrawing and depositing money, and admin functionalities like adding and deleting users, viewing all balances, and plotting user balances.

Test Cases

Test Case ID Description Input Expected Output Actual Output Pass/Fail

TC01 Successful login Username: User1, PIN: 1234 Main menu displayed Main menu displayed Pass

TC02 Incorrect PIN Username: User1, PIN: 0000 Error message Error message Pass

TC03 Check balance Option: 1 Current balance displayed Current balance displayed Pass

TC04 Withdraw amount (valid) Option: 2, Amount: 100 Balance updated, success message Balance updated, success message Pass

TC05 Withdraw amount (invalid) Option: 2, Amount: 1500 Error message Error message Pass

TC06 Deposit amount Option: 3, Amount: 500 Balance updated, success message Balance updated, success message Pass

TC07 Change PIN Option: 4, New PIN: 5678 PIN updated, success message PIN updated, success message Pass
Test Data

· User1: Username: User1, PIN: 1234, Balance: $1000

· User2: Username: User2, PIN: 2222, Balance: $2000

· User3: Username: User3, PIN: 3333, Balance: $3000

· SysAdmin: Username: SysAdmin, PIN: 1357
