
from datetime import datetime
from data_manager import load_customers, register_customer, save_transaction
from user_types import PersonalUser, BusinessUser, ResidentForeignUser


def start_program(customers):
  print("👋 Welcome to the Bank System")
  answer = input("Do you have an account? (yes/no): ").strip().lower()

  if answer == "yes":
    try:
      customer_id = input("Enter your ID: ").strip()
      if customer_id not in customers:
        print("❌ ID not found.")
        return None
      return customer_id
    except ValueError:
      print("❌ Invalid ID format.")
      return None
  elif answer == "no":
    return register_customer(customers)
  else:
    print("❌ Invalid input.")
    return None


def get_transactions():
  transactions = []
  try:
    num = int(
        input("How many transactions do you want to enter? (1-3): ").strip())
  except ValueError:
    print("❌ Invalid number.")
    return []

  for i in range(num):
    print(f"\nTransaction {i+1}:")
    try:
      amount = float(input("Amount: "))
      country = input("Country: ").strip()
      device = input("Device used: ").strip()
      time = datetime.now().isoformat()
      transactions.append({
          "amount": amount,
          "country": country,
          "device": device,
          "time": time
      })
    except ValueError:
      print("❌ Invalid input. Skipping this transaction.")
  return transactions


def analyze_transactions(customer_id, customers, transactions):
  user_type = customers[customer_id]['type']
  country = customers[customer_id]['original_country']

  if user_type == "personal":
    user = PersonalUser(transactions)
  elif user_type == "business":
    user = BusinessUser(transactions)
  elif user_type == "foreign":
    user = ResidentForeignUser(transactions, original_country=country)
  else:
    print("❌ Unknown customer type.")
    return

  # Save each transaction
  for tx in transactions:
    save_transaction(customer_id, tx)

  if user.is_fraudulent():
    print("\n⚠️ WARNING: This transaction may be FRAUDULENT!")
  else:
    print("\n✅ Transaction is safe.")


# ---------------- MAIN ----------------

customers = load_customers()
customer_id = start_program(customers)

if customer_id:
  transactions = get_transactions()
  if transactions:
    analyze_transactions(customer_id, customers, transactions)

