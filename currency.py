import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("key")
API_URL = f"api url"

def convert_currency(amount, from_currency, to_currency):
    try:
        response = requests.get(API_URL + from_currency)
        data = response.json()

        if data["result"] == "success":
            rate = data["conversion_rates"][to_currency]
            converted = amount * rate
            return converted
        else:
            print("Invalid currency code.")
            return None

    except Exception as e:
        print("Error:", e)
        return None


while True:
    from_currency = input("From: ").upper()
    to_currency = input("To: ").upper()
    amount = float(input("Amount: "))

    result = convert_currency(amount, from_currency, to_currency)

    if result:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

    again = input("Again? (yes/no): ").lower()
    if again != "yes":
        break