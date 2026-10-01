# # Bank Management System Using OOP
#
# class BankAccount:
#
#     def __init__(self, username, initial_deposit):
#         self.username = username
#         self.balance = initial_deposit
#         self.transactions = []
#
#         transaction = f"Account created with initial deposit: Rs.{initial_deposit}"
#         self.transactions.append(transaction)
#         self.log(transaction)
#
#     def log(self, message):
#         file = open("bank_log.txt", "a")
#         file.write(message + "\n")
#         file.close()
#
#     def deposit(self, amount):
#         if amount <= 0:
#             print("Please enter a valid amount.")
#             return
#
#         self.balance += amount
#
#         transaction = f"Deposited: Rs.{amount}"
#         self.transactions.append(transaction)
#
#         self.log(
#             f"{self.username} - {transaction} - Balance: Rs.{self.balance}"
#         )
#
#         print("Money deposited successfully.")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Please enter a valid amount.")
#             return
#
#         if amount > self.balance:
#             print("Insufficient balance.")
#             return
#
#         self.balance -= amount
#
#         transaction = f"Withdrawn: Rs.{amount}"
#         self.transactions.append(transaction)
#
#         self.log(
#             f"{self.username} - {transaction} - Balance: Rs.{self.balance}"
#         )
#
#         print("Money withdrawn successfully.")
#
#     def check_balance(self):
#         print("\nUsername:", self.username)
#         print("Balance: Rs.", self.balance)
#
#         self.log(
#             f"{self.username} - Checked balance - Balance: Rs.{self.balance}"
#         )
#
#     def show_transactions(self):
#         print("\nTransaction History")
#         print("-------------------")
#
#         for transaction in self.transactions:
#             print(transaction)
#
#         self.log(
#             f"{self.username} - Viewed transaction history"
#         )
#
#
# print("WELCOME TO BANK MANAGEMENT SYSTEM")
#
# username = input("Enter username: ")
# initial_deposit = float(input("Enter initial deposit: Rs."))
#
# account = BankAccount(username, initial_deposit)
#
# print("\nAccount created successfully!")
#
# while True:
#
#     print("\nSELECT AN OPTION")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. View Transactions")
#     print("5. Exit")
#
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         amount = float(input("Enter amount to deposit: Rs."))
#         account.deposit(amount)
#
#     elif choice == "2":
#         amount = float(input("Enter amount to withdraw: Rs."))
#         account.withdraw(amount)
#
#     elif choice == "3":
#         account.check_balance()
#
#     elif choice == "4":
#         account.show_transactions()
#
#     elif choice == "5":
#         print("Thank you for using the Bank Management System.")
#         account.log(f"{username} - Logged out")
#         break
#
#     else:
#         print("Invalid choice. Please try again.")
