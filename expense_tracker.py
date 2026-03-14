import csv
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


# Create CSV if not exists
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount"])


# Add expense or income
def add_entry():
    date = input("Enter date (YYYY-MM-DD): ")
    entry_type = input("Type (Income/Expense): ")
    category = input("Category: ")
    amount = float(input("Amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, entry_type, category, amount])

    print("Entry added successfully!")


# Show all entries
def view_entries():
    df = pd.read_csv(FILE_NAME)
    print(df)


# Monthly summary
def monthly_summary():
    df = pd.read_csv(FILE_NAME)

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    summary = df.groupby(["Month", "Type"])["Amount"].sum()
    print(summary)


# Export to Excel
def export_excel():
    df = pd.read_csv(FILE_NAME)
    df.to_excel("expenses.xlsx", index=False)
    print("Exported to expenses.xlsx")


# Create chart
def create_chart():
    df = pd.read_csv(FILE_NAME)

    summary = df.groupby("Type")["Amount"].sum()

    summary.plot(kind="pie", autopct='%1.1f%%')
    plt.title("Income vs Expense")
    plt.ylabel("")
    plt.savefig("expense_chart.png")

    plt.show()


# Menu
def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Monthly Summary")
        print("4. Export to Excel")
        print("5. Create Chart")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            export_excel()
        elif choice == "5":
            create_chart()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


create_file()
menu()