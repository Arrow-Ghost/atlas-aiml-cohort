expenses=[]
while True:
    print("\nExpense Tracker Menu:")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Show Total Expense")
    print("4.Exit")

    choice=input("Enter choice:")
    if choice=='1':
        category=input("enter category:")
        amount=float(input("Enter amt: "))
        expense={
            "category ":category,
            "amount":amount
        }
        expenses.append(expense)
        print("Expense added successfully")

    elif choice=='2':
        if len(expenses)==0:
            print('No expenses found.')
        else :
            print("\n expense list:")
            for i, expense in enumerate(expenses,start=1):
                print(f"{i}. Category: {expense['category ']}, Amount: {expense['amount']}")
    elif choice=='3':
        total=sum(expense['amount'] for expense in expenses) 
        print(f"\n Total Expense: {total}")

    elif choice=='4':
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid choice. Please select a valid option.")