expenses = []
expense1 = {'amount': '1999.00', 'category': 'dailywears'}
expenses.append(expense1)
expense2 = {'amount': '385.00', 'category': 'mobile recharge'}
expenses.append(expense2)


def removeExpenses():
  while True:
    listExpenses()
    print("What expense would you like to remove?")
    try:
      expenseToRemove = int(input("> "))
      del expenses[expenseToRemove]
      print("The Expense",expenseToRemove,"has been removed")
      break
    except:
      print("Invalid input. Please try again.")


def addExpenses(category,amount):
  expense = {'category': category,'amount': amount }
  expenses.append(expense)


def printMenu():
  print("Please choose from one of the following options...")
  print("1. Remove Any Exepense")
  print("2. Add The New Expense")
  print("3. List All the Spent Exepenses")


def listExpenses():
  print("\nHere is a list of your expenses...")
  print("------------------------------------")
  counter = 0
  for expense in expenses:
    print("[",counter,"]", expense['amount'], " - ", expense['category'])
    counter += 1
  print("\n\n")


if __name__ == "__main__":
  while True:
    ### Prompt the user
    printMenu()
    optionSelected = input("> ")
    if (optionSelected == "3"):
      listExpenses()
    elif (optionSelected == "2"):
     
      print("What category was this expense?")
      while True:
        try:
          category = input("> ")
          break
        except:
          print("Invalid input. Please try again.")

      print("How much was this expense?")
      while True:
        try:
          amountToAdd = input("> ")
          break
        except:
          print("Invalid input. Please try again.")

      addExpenses(category,amountToAdd)
    elif (optionSelected == "1"):
      removeExpenses()
   
    else:
      print("Invalid input. Please try again.")￼Enter
