# Laboratory 4 - Installment 4: The Tracker Makes Decisions
# Author: Gio Cenon F. Golpo
# Description: An expense tracker that checks the size of each expense
# and gives a budget verdict based on the grand total.

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

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

subtotal = subtotal + amount1

item2 = input("\nSecond expense? ")
amount2 = float(input("Amount? "))

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

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

if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > budget * 0.9:
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" * 40)

print("Made by: Gio Cenon F. Golpo | Installment 4")