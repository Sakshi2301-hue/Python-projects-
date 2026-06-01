expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense Added!")

    elif choice == "2":
        print("\nExpenses:")

        for item in expenses:
            print(item["name"], "-", item["amount"])

    elif choice == "3":
        total = 0

        for item in expenses:
            total += item["amount"]

        print("Total Expense =", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
        
