expenses= []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show all Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice= input("Enter your choice (1-5)")

    if choice == '1':
        print("Add Expenses")

    elif choice == '2':
        print("View Expenses")

    elif choice == '3':
        print("Show all Expenses")

    elif choice == '4':
        print("Delete Expenses")

    elif choice == '5':
        print("Thank you! Expense tracker closed...")
        break    

    else:
        print("Invalid choice! Please try again.")

        

