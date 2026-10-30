# Laboratory 5 - Installment 5: The Menu Comes Alive
# Author: Gio Cenon F. Golpo
# Description: An expense tracker with a working menu. It asks for the
# name, tax rate, and budget once, then lets the user add expenses,
# view the total with a budget verdict, or exit.

print("=" * 40)
print("EXPENSE TRACKER".center(40))
print("Know where your money goes.".center(40))
print("=" * 40)

name = input("\nWhat's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0.0
count = 0

while True:
    print("\nMAIN MENU")
    print("[1] Add an expense")
    print("[2] View all expenses (coming soon)")
    print("[3] Show total spent")
    print("[4] Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

        subtotal = subtotal + amount
        count = count + 1

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax

        over_budget = total > budget
        left = budget - total

        print(f"  Expenses:\t{count}")
        print(f"  Subtotal:\t${subtotal}")
        print(f"  Tax ({tax_percent}%):\t${tax}")
        print(f"  Grand total:\t${total}")

        if over_budget:
            print(f"  Over budget by ${total - budget}!")
        elif total > budget * 0.9:
            print(f"  Careful: only ${left} left.")
        else:
            print(f"  Within budget. ${left} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        break

    else:
        print("  Please choose 1, 2, 3 or 4.")

print("-" * 40)
print("Made by: Gio Cenon F. Golpo | Installment 5")
print("=" * 40)