# Expense Tracker - Simple Python Version

expenses = []

def add_expense():
    category = input("Enter category (Food, Transport, Bills, Health, Other): ")
    amount = float(input("Enter amount £: "))
    note = input("Enter note: ")
    expenses.append({"category": category, "amount": amount, "note": note})
    print("Expense added successfully! ✅\n")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
        return
    print("\n--- All Expenses ---")
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['category']} - £{exp['amount']} - {exp['note']}")
        total += exp['amount']
    print(f"\nTotal Spent: £{total:.2f}\n")

def summary_by_category():
    print("\n--- Summary by Category ---")
    categories = {}
    for exp in expenses:
        categories[exp['category']] = categories.get(exp['category'], 0) + exp['amount']
    
    for cat, total in categories.items():
        print(f"{cat}: £{total:.2f}")
    print()

def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summary by Category")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_by_category()
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.\n")

main()