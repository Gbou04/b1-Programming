# calculator.py
# This program calculates profit and profit margin based on user input for revenue and costs.

# Get user input for revenue

revenue = float(input("Enter the total revenue: "))

# Get user input for costs

costs = float(input("Enter the total costs: "))

# Calculate profit

profit = revenue - costs

# Calculate profit margin percentage

margin = (profit / revenue) * 100

# Display formatted results to the user
print("Revenue:", revenue)
print("Costs:", costs)
print("Profit:", profit)
print("Profit Margin:", margin, "%")