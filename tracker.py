# Laboratory 3 - Installment 3: The Tracker Does Math
# Author: Gio Cenon F. Golpo
# Description: An expense tracker that asks the user for two expenses 
# and calculates the subtotal, average, tax, grand total, and budget.

print("=" * 40)
print("EXPENSE TRACKER".center(40))
print("Know where your money goes.".center(40))
print("=" * 40)

print("\nMAIN MENU")
print("[1] Add an expense\t\t(coming soon)")
print("[2] View all expenses\t\t(coming soon)")
print("[3] Show total spent\t\t(coming soon)")
print("[4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))

subtotal = subtotal + amount1

item2 = input("\nSecond expense? ")
amount2 = float(input("Amount? "))

subtotal = subtotal + amount2

average = subtotal / 2

tax_percent = float(input("\nTax rate %? "))
tax = subtotal * (tax_percent / 100)

total = subtotal + tax

budget = float(input("Your budget? "))

over_budget = total > budget
left = budget - total

print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)

print("Made by: Gio Cenon F. Golpo | Installment 3")