# Step 1 — Initialize Account
balance = 1000
transactions = []

# Step 3 — Deposit Function
def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposited ${amount}")
    print(f"Successfully deposited ${amount}. New balance: ${balance}")

# Step 4 — Withdraw Function
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        transactions.append(f"Withdrew ${amount}")
        print(f"Successfully withdrew ${amount}. New balance: ${balance}")
    else:
        print("Insufficient funds!")

# Step 5 — Check Balance Function
def check_balance():
    print(f"Current balance: ${balance}")

# Step 6 — View Transactions Function
def view_transactions():
    if transactions:
        print("Transaction History:")
        for t in transactions:
            print("-", t)
    else:
        print("No transactions available.")

# Step 2 — Display Menu
while True:
    print("\n--- Bank Account Menu ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. View Transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == "3":
        check_balance()
    elif choice == "4":
        view_transactions()
    elif choice == "5":
        print("Thank you for using our bank system!")
        break
    else:
        print("Invalid choice! Please select a valid option.")

