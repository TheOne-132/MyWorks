def currency_converter():
    def convert_currency():
        rates = {
            'USD': {'NGN': 1604, 'GBP': 0.7479, 'YEN': 110.57, 'EUR': 0.85},
            'NGN': {'USD': 0.000623, 'GBP': 0.000466, 'YEN': 0.0904, 'EUR': 0.00053},
            'YEN': {'USD': 0.00905, 'NGN': 11.06, 'GBP': 0.0052, 'EUR': 0.0076},
            'EUR': {'USD': 1.18, 'NGN': 1885, 'YEN': 131.25, 'GBP': 0.88},
            'GBP': {'USD': 1.337, 'NGN': 2142, 'YEN': 147.12, 'EUR': 1.14},
        }
        if from_currency in rates and to_currency in rates[from_currency]:
            rate = rates[from_currency][to_currency]
            converted = amount * rate
            return round(converted, 2)
        else:
            return None

    amount = float(input("Enter amount: "))
    from_currency = input("From currency (USD, NGN, YEN, GBP, EUR): ").upper()
    to_currency = input("To currency (USD, NGN, YEN, GBP, EUR): ").upper()

    result = convert_currency()

    if result:
        print(f"{amount} {from_currency} is {result} {to_currency}")
    else:
        print("Conversion not available.")

    loop = input("Do you want to convert another currency? (yes/no): ").lower()
    if loop == 'yes':
        return True
    else:
        print("Thank you for using the currency converter!")
        return False
    
while currency_converter():
    pass
