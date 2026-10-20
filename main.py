import json

def load():
    try:
        with open('expenses.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []

def save(data):
    with open('expenses.json', 'w') as f:
        json.dump(data, f)

def add(data):
    name = input("Name: ")
    amount = float(input("Amount: "))
    expense_type = input("Type: ")
    data.append({"name": name, "amount": amount, "type": expense_type})
    save(data)
    print("Added!")

def show(data):
    for expense in data:
        print(f"Name: {expense['name']}, Amount: {expense['amount']}, Type: {expense['type']}")

def summary(data):
    totals = {}
    for expense in data:
        if expense['type'] in totals:
            totals[expense['type']] += expense['amount']
        else:
            totals[expense['type']] = expense['amount']
    for key, value in totals.items():
        print(f"{key}: ${value:.2f}")

def main():
    data = load()
    while True:
        print("What would you like to do?\n1) Add an expense\n2) View expenses\n3) Show Monthly summary\n4) Exit")

        choice = input("> ")
        if choice == '1':
            add(data)
        elif choice == '2':
            show(data)
        elif choice == '3':
            summary(data)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

main()