import csv
import json
import os

data_file = "expenses.csv"


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Rent, Transport, etc.): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    with open(data_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")


def view_expenses():
    if not os.path.exists(data_file):
        print("No expenses recorded yet.\n")
        return

    with open(data_file, mode='r') as file:
        reader = csv.reader(file)
        print("Date        | Category    | Amount | Description")
        print("-" * 50)
        expenses = list(reader)
        for index, row in enumerate(expenses):
            if index == 0:
                continue  # Skip header
            print(f"{index}. {row[0]} | {row[1]:<10} | ${row[2]:<6} | {row[3]}")
    print("\n")


def delete_expense():
    if not os.path.exists(data_file):
        print("No expenses recorded to delete.\n")
        return

    with open(data_file, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if len(expenses) <= 1:
        print("No expenses to delete.\n")
        return

    view_expenses()
    try:
        index = int(input("Enter the number of the expense to delete: "))
        if index <= 0 or index >= len(expenses):
            print("Invalid selection.\n")
            return

        del expenses[index]

        with open(data_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)

        print("Expense deleted successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")


def export_to_json():
    if not os.path.exists(data_file):
        print("No expenses recorded to export.\n")
        return

    expenses = []
    with open(data_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append({"date": row[0], "category": row[1], "amount": row[2], "description": row[3]})

    with open("expenses.json", mode='w') as json_file:
        json.dump(expenses, json_file, indent=4)

    print("Expenses exported to expenses.json!\n")


def main():
    if not os.path.exists(data_file):
        with open(data_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

    while True:
        print("Personal Finance Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Export to JSON")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            export_to_json()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
