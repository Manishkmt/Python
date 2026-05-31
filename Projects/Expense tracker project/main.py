
#! Expence Tracker Project

expenseslist = []  #list of all expences in form of dictionary

print("Welcome to Expence Tracker")

while True:
  print("===MENUE===")
  print("1. Add Expence\n")
  print("2. View all Expences\n")
  print("3. View total pay\n")
  print("4. Exit\n")

  choice = int(input("Please enter your choice:"))

# Add Expenses:-
  if(choice == 1):
    date = input("Enter the date:")
    category = input("Enter category:")
    description = input("Enter description:")
    amount = float(input("Enter the amount:"))

    expense = {
      "date": date,
      "category": category,
      "description": description,
      "amount": amount
    }

    expenseslist.append(expense)
    print("Expenses is added successfully")

# View All Expenses:-
  elif(choice == 2):
    if(len(expenseslist) == 0):
      print("No Expenses added")
    else:
      print("===All Expense===")
      count = 1
      for eachPayment in expenseslist:
        print(f"payment no. {count}->{eachPayment["date"]}, {eachPayment["category"]}, {eachPayment["amount"]}")
        count = count + 1


# 3. View total spending:-
  elif(choice == 3):
    total = 0
    for eachPayment in expenseslist:
      total = total + eachPayment["amount"]

      print("\nTotal payment  is:", total)

# 4.Exit      
  elif(choice == 4):
     print("Thaks to visit our project")
     break
  
  else:
    print("Invalid Choice,Try again later")
