import os

# File to store expense data
EXPENSE_FILE = "expenses.txt"

def add_expense():
    """Adds an expense to the file."""
    name = input("Enter expense name: ")
    amount = input("Enter expense amount: ")
    
    # Save to file
    with open(EXPENSE_FILE, "a") as file:
        file.write(f"{name},{amount}\n")
    print(f"Expense '{name}' added successfully!\n")

def view_expenses():
    """Displays all expenses from the file."""
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.\n")
        return

    print(f"{'Expense':<20} {'Amount':<10}")
    print("-" * 30)

    with open(EXPENSE_FILE, "r") as file:
        total_amount = 0
        for line in file:
            name, amount = line.strip().split(",")
            print(f"{name:<20} {amount:<10}")
            total_amount += float(amount)

    print("-" * 30)
    print(f"Total Expense: {total_amount}\n")

def main():
    """Main function to run the expense tracker."""
    while True:
        print("Simple Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
