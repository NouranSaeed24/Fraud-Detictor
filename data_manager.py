import json
import os

CUSTOMERS_FILE = "customers.json"


def load_customers():
    if os.path.exists(CUSTOMERS_FILE):
        with open(CUSTOMERS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_customers(customers):
    with open(CUSTOMERS_FILE, "w") as f:
        json.dump(customers, f, indent=4)


def register_customer(customers):
    new_id = str(max(map(int, customers.keys()), default=100) + 1)

    print("1 - personal")
    print("2 - business")
    print("3 - foreign")

    choice = input("Enter: ").strip()

    if choice == "1":
        user_type = "personal"
        original_country = "USA"
    elif choice == "2":
        user_type = "business"
        original_country = "USA"
    elif choice == "3":
        user_type = "foreign"
        original_country = input("Enter your original country: ").strip()
    else:
        print("Invalid input.")
        return None

    customers[new_id] = {
        "type": user_type,
        "original_country": original_country
    }
    save_customers(customers)

    print(f"Registration successful. Your ID is: {new_id}")
    return new_id


def save_transaction(customer_id, transaction):
    filename = f"transactions_{customer_id}.json"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(transaction)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
