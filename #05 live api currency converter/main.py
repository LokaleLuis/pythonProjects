import requests

# Your API Key
api_key = "2211732f08e8a358c0a46a5a"

# Ask user for currencies
base = input("From currency (e.g. USD): ").strip().upper()
target = input("To currency (e.g. EUR): ").strip().upper()

# Make API request
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
response = requests.get(url)
data = response.json()

# Get all the conversion rates
all_rates = data["conversion_rates"]

# Find the rate for the target currency
rate = all_rates[target]

# Show the result
print("1 " + base + " = " + str(rate) + " " + target)

