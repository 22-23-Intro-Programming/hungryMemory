#Python Problem Set 3

currency_conversion_factors = {
    "usd": {
        "usd": 1,
        "mxn": 19.75,
        "eur": 1.01,
        "hkd": 7.85,
        "bnd": 1.41,      
    },
    "mxn": 0.051,
    "eur": 0.99,
    "hkd": 0.13,
    "bnd": 0.71,
}

def convert_currency(amount, from_currency, to_currency):
    if(from_currency == "usd"):
        return amount * currency_conversion_factors.get("usd").get(to_currency)
    amount *= currency_conversion_factors.get(from_currency)
    amount *= currency_conversion_factors.get("usd").get(to_currency)
    return amount

currencies = {
    "1": "usd",
    "2": "mxn",
    "3": "eur",
    "4": "hkd",
    "5": "bnd"
}

def ask_currency():
    x=input("Please enter which type of currency you have. Choose from the list:\n1. United States Dollar\n2. Mexican Peso\n3. European Euro\n4. Hong Kong Dollar\n5. Brunei Dollar\n: ")
    print("")
    y=float(input("Please enter how much money you have: "))
    print("")
    z=input("Please enter which type of currency you would like to convert to. Choose from the list:\n1. United States Dollar\n2. Mexican Peso\n3. European Euro\n4. Hong Kong Dollar\n5. Brunei Dollar\n: ")
    print(convert_currency(y, currencies.get(x), currencies.get(z)))

grocery_prices = {
    "apple": 1.5,
    "orange": 1,
    "banana": 1,
    "bagel": 1.25,
    "cabbage": 1.5,
    "spinach": 4.25,
    "milk": 2.75,
    "eggs": 3.25,
    "cake": 8,
    "pasta": 3.50,
}

def grocery_list(groceries):
    total = 0
    for i in groceries:
        total += grocery_prices.get(i)
    return total
    
        
    
def main():
    ask_currency()
    print("Price of groceries: {:.2f}".format(grocery_list(["pasta", "cake", "orange", "orange"])))
   
if(__name__ == "__main__"):
    main()
    


