import datetime

EXPENSE_FILE = 'expenses.txt'

def add_expense():
    """Prompts the user for expense details and saves it to the file."""
    print("\n--- Add New Expense ---")
    
    date_str = input("Enter date (YYYY-MM-DD, leave blank for today): ")
    if not date_str:
        date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    category = input("Enter category (e.g., Food, Transport, Rent): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expense_entry = f"{date_str},{category},{amount:.2f}\n"

    try:
        with open(EXPENSE_FILE, 'a', encoding='utf-8') as f:
            f.write(expense_entry)
        print("Expense recorded successfully!")
    except IOError:
        print("Error writing to file.")

def view_expenses():
    """Reads and prints all existing expenses from the file."""
    print("\n--- Current Expenses ---")
    try:
        with open(EXPENSE_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines:
                print("No expenses recorded yet.")
                return

            print(f"{'Date':<10} | {'Category':<15} | {'Amount':>10}")
            print("-" * 39)
            
            total = 0.0
            for line in lines:
                try:
                    date, category, amount_str = line.strip().split(',')
                    amount = float(amount_str)
                    total += amount
                    print(f"{date:<10} | {category:<15} | {amount:.2f:>10}")
                except ValueError:
                    print(f"Error reading line: {line.strip()}")
            
            print("-" * 39)
            print(f"Total Expenses: {'':<22}{total:.2f:>10}")

    except FileNotFoundError:
        print("No expense file found. Start by adding a new expense.")
    except IOError:
        print("Error reading file.")

def expense_tracker():
    """Main loop for the expense tracker program."""
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add new expense")
        print("2. View existing expenses")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

expense_tracker()