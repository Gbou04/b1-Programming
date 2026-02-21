# Exercise 3: Personal Expense Tracker

# 1. Initialize Data Structures
# TODO: Create an empty list, `expense_records`, to store each expense as a tuple `(category, amount, date)`.
expense_records = []
category_totals = {}
unique_categories = set()

print("Hello, Welcome to Your Own Personal Expense Tracker!")


# 2. Collect Expense Data
# TODO: Implement a loop to prompt the user for 5-7 individual expenses.

for i in range(1, 6):
    print(f"\nEnter Expense {i} category:", end=" ")
    category = input()
    amount = float(input(f"Enter expense {i} amount: "))
    date = input(f"Enter Expense {i} date (YYY-MM-DD): ")

# store an expense entry as a dictionary
expense = {
    "category": category,
    "amount": amount,
    "date": date,
}

expense_records.append(expense)


# 3. Categorize and Sum Expenses
# TODO: Iterate through `expense_records`.

amounts = [exp["amount"] for exp in expense_records]

total_spending = sum(amounts)
average_expense = total_spending / len(expense_records)
highest_expense = max(amounts)
lowest_expense = min(amounts)

# unique categories

unique_categories = set(exp["category"] for exp in expense_records)


# 4. Calculate Overall Statistics
# TODO: Extract all expense amounts into a separate list.

for exp in expense_records:
    category = exp["category"]
    amount = exp["amount"]

    category_totals[category] = category_totals.get(category, 0) + amount

# 5. Generate Spending Report
# TODO: Print a comprehensive report.

print("\n=== OVERALL SPENDING SUMMARY ===")
print(f"Total Spending: ${total_spending:.2f}")
print(f"Average Expense: ${average_expense:.2f}")
print(f"Highest Expense: ${highest_expense['amount']:.2f} "
      f"(Category: {highest_expense['category']}, Date: {highest_expense['date']})")
print(f"Lowest Expense: ${lowest_expense['amount']:.2f} "
      f"(Category: {lowest_expense['category']}, Date: {lowest_expense['date']})")

print("\n=== UNIQUE CATEGORIES SPENT ON ===")
print(unique_categories)
print(f"Total unique categories: {len(unique_categories)}")

print("\n=== SPENDING BY CATEGORY ===")
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")