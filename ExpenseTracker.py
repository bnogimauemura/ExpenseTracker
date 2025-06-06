class bcolors:
    HEADER = '\033[95m'      # Light Magenta / Purple
    OKBLUE = '\033[94m'      # Light Blue
    OKCYAN = '\033[96m'      # Light Cyan / Aqua
    OKGREEN = '\033[92m'     # Light Green
    WARNING = '\033[93m'     # Yellow
    FAIL = '\033[91m'        # Light Red
    ENDC = '\033[0m'         # Reset all attributes
    BOLD = '\033[1m'         # Bold text
    UNDERLINE = '\033[4m'    # Underlined text
class Expense: 
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print(f"{bcolors.OKGREEN}\nExpense removed successfully!{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}\nInvalid expense index.{bcolors.ENDC}")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print(f"{bcolors.FAIL}\nNo expenses found.{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKBLUE}\nExpense list:{bcolors.ENDC}")
            for i, expense in enumerate(self.expenses, start = 1):
                print(f"{bcolors.OKCYAN}{i}.{bcolors.ENDC} Date {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}.") # Format Amount with 2 decimal places

    def view_expenses_by_date(self, target_date):
        filtered = [exp for exp in self.expenses if exp.date == target_date]

        if filtered:
            print(f"{bcolors.OKBLUE}\nExpenses on {target_date}:{bcolors.ENDC}")
            for i, expense in enumerate(filtered, start=1):    # enumerate gives the index (i) and the item (expense) while looping
                print(f"{bcolors.OKCYAN}{i}.{bcolors.ENDC} Description: {expense.description}, Amount: ${expense.amount:.2f}, Category: {expense.category}.")    # start=1 makes the counter start from 1 instead of 0 (more user-friendly)
        else:
            print(f"{bcolors.FAIL}\nNo expenses found for {target_date}.{bcolors.ENDC}.")

    def view_categories(self):
        if len(self.expenses) == 0:
            print(f"{bcolors.FAIL}\nNo expenses found.{bcolors.ENDC}")
        else:
            categories = set(expense.category for expense in self.expenses) # set is used to avoid duplicate category names
            print(f"{bcolors.OKBLUE}Categories:{bcolors.ENDC}")
            for category in categories:
                print(f"{bcolors.OKCYAN}-{bcolors.ENDC} {category}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"\n{bcolors.OKGREEN}{bcolors.BOLD}Total Expenses:{bcolors.ENDC}{bcolors.ENDC} ${total:.2f}")

def main():
        tracker = ExpenseTracker()

        while True:
            print(f"{bcolors.HEADER}\nExpense Tracker Menu:{bcolors.ENDC}") # \n is a newline character, this add a line before printing this message
            print(f"{bcolors.OKGREEN}1.{bcolors.ENDC} Add Expense")
            print(f"{bcolors.OKGREEN}2.{bcolors.ENDC} Remove Expense")
            print(f"{bcolors.OKGREEN}3.{bcolors.ENDC} View Expenses")
            print(f"{bcolors.OKGREEN}4.{bcolors.ENDC} View Expenses by Date")
            print(f"{bcolors.OKGREEN}5.{bcolors.ENDC} Expenses by Category")
            print(f"{bcolors.OKGREEN}6.{bcolors.ENDC} Total Expenses")
            print(f"{bcolors.OKGREEN}7.{bcolors.ENDC} Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                date = input(f"\n{bcolors.OKBLUE}Enter the date{bcolors.ENDC}(YYYY-MM-DD): ")
                description = input(f"{bcolors.OKBLUE}Enter the description:{bcolors.ENDC} ")
                amount = float(input(f"{bcolors.OKBLUE}Enter the amount:{bcolors.ENDC} "))
                category = input(f"{bcolors.OKBLUE}Enter the category: {bcolors.ENDC}")
                expense = Expense(date, description, amount, category)
                tracker.add_expense(expense)
            elif choice == "2":
                index = int(input("Enter the expense index to remove: ")) - 1
                tracker.remove_expense(index)
            elif choice == "3":
                tracker.view_expenses()
            elif choice == "4":
                date = input("Enter the date to filter (YYYY-MM-DD): ")
                tracker.view_expenses_by_date(date)
            elif choice == "5":
                tracker.view_categories()
            elif choice == "6":
                tracker.total_expenses()
            elif choice == "7":
                print("Goodbye!")
                break
            else: 
                print(f"{bcolors.FAIL}Invalid choice. Please try again!{bcolors.ENDC}")

if __name__ == "__main__":
    main()                  # Prevents the menu from running automatically when this file is imported

# get the percentage of expenses by day and the total amount based on day, separate in % per category
# EXAMPLE: 2025-06-01 Total: 20000 yen, Food: 56%, hobby 20%, shopping: 24%, ....something like this 
# 1. map through all the expenses by date
# 2. sum based on category 
# 3. return in percentage the amount (per category) compared with the total of the day


# Feature?	                         Feasible?	              Tech Needed
# Track by month	                    ✅	                 Django ORM, date filtering
# Set and check monthly limits	        ✅	                 Django forms + logic
# Warn if hobby > 20%	                ✅	                 Django query + math
# Compare to previous month	            ✅	                 Date logic, Django ORM
# Per-category % comparison	            ✅	                 Aggregate by category
# ML prediction after 6 months	        ✅	                 Scikit-learn / PyTorch later