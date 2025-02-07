#from datetime import datetime

class ExpenseTracker:
    def __init__(self, date, category, amount, current_total):
        self.date = date
        self.category = category
        self.amount = amount
        self.current_total = current_total
        
    
    def subtrackMoney(self, moneyToSubtract):
        self.current_total -= moneyToSubtract
        return self.current_total


    def addMoney(self, moneyToAdd):
        self.current_total += moneyToAdd
        return self.current_total
    
    def categoriesList(self):
        category_list = ["Grocery", "Coffee/Snack", "Laundry", "Clothing", 
                        "Medical", "Pets", "Kids Expense", "Online Order", 
                        "Electronic", "Kitchenware/Cleaning Supplies", 
                        "Furniture", "Other"]

        print("Category menu: ")
        print("Option 1: Display Categories.")
        print("Option 2: Add a Category.")
        print("Option 3: Remove a Category.")
        print("What would you like to do?")

        user_option = int(input("Select: "))

        if user_option == 1:
            print("Categories:")
            for category in category_list:
                print(category)

        elif user_option == 2:
            category_to_add = input("Name the Category to add: ").title().strip()
            category_list.append(category_to_add)
            print("Category added:", category_to_add)
            print("Updated Categories:", category_list)

        elif user_option == 3:
            category_to_remove = input("Name the Category to delete: ").title().strip()
            if category_to_remove not in category_list:
                print("Sorry! That Category is not available. Try again.")
            else:
                category_list.remove(category_to_remove)
                print("Category removed:", category_to_remove)
                print("Updated Categories:", category_list)

        else:
            print("Invalid option.")




expenses = ExpenseTracker(date="01/23/2001", category="Test", amount=500, current_total=500)
print("\n")
print(expenses.addMoney(50))

print(expenses.categoriesList())
