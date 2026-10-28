#Laboratory 2 - Installment 2: Talking to the User
#Author: Gio Cenon F. Golpo
#Description: An expense tracker that asks the user for two expenses and calculates the total and average.

print("="*40)
print("EXPENSE TRACKER".center(40))
print("know where your money goes".center(40))
print("="*40)

print("\nWelcome! This is your personal expense tracker.\n")

print("MAIN MENU")
print("[1] Add an expense\t\t(coming soon)")
print("[2] View all expenses\t\t(coming soon)")
print("[3] Show total spent\t\t(coming soon)")
print("[4] Exit\t\t\t(coming soon)")

name = input("\nWhat's your name? ")
print(f"\nWelcome, {name}! Let's log two expenses.\n")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("\nSecond expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("-"*40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"\nTotal spent:\t${total}")
print(f"Average spent:\t${average}")
print("-"*40)

print("Made by: Gio Cenon F. Golpo | Installmet 1")
