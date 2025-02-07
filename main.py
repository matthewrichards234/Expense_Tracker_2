from datetime import datetime

class Expenses:
    def __init__(self, date, category, amount):
        #self.expense_entry_dict = {date: "", category: "", amount = 0}

        self.date = date
        self.category = category
        self.amount = amount

        self.date_string = input("Enter a date in YYYY-MM-DD format: ")
        self.date_format = "%Y-%m-%d"

    def expenseEntry(self, expense):
        

        # Date
        self.date = self.date_string
        if self.isValidDate(self.date, self.date_format) == True:
            print("Valid Date\n")
        else:
            print("Invalid Input\n")

        # Category
        category_list = ["Grocery", 
                         "Coffee/Snack", 
                         "Laundry", 
                         "Clothing", 
                         "Medical", 
                         "Pets", 
                         "Kids Expense",
                         "Online Order",
                         "Electronic",
                         "Kitchenware/Cleaning Supplies",
                         "Furniture",
                         "Other"]
        category_input = input("Enter what category you spend money on: ").title()
        while True:
            try:
                if category_input in category_list:
                    continue
            except ValueError:
                pass

    def isValidDate(self, date_string, date_format):
        try:
            datetime.strptime(self.date_string, self.date_format)
            return True
        except ValueError:
            return False


    def showAllExpense(self, expenses):
        pass


    def addMoney(self):
        pass


#expense_obj = Expenses()
#print(expense_obj.expenseEntry())

def main():
    expense_obj = Expenses()