#Python Problem Set 3

currency_conversion_factors = {#define variable 'currency_conversion_factors' as dictionary with following values
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

def convert_currency(amount, from_currency, to_currency):#define function 'convert_currency' with parameters 'amount', 'from_currency', and 'to_currency'
    if(from_currency == "usd"):#if 'from_currency' is equal to the string "usd", then
        return amount * currency_conversion_factors.get("usd").get(to_currency)#return 'amount' times the value 'to_currency' in the dictionary 'usd' in the dictionary 'currency_conversion_factors'
    #otherwise
    amount *= currency_conversion_factors.get(from_currency)#set 'amount' to the value stored in 'amount' times the value 'from_currency' in the dictionary 'currency_conversion_factors'
    amount *= currency_conversion_factors.get("usd").get(to_currency)#set 'amount' to the value stored in 'amount' times the value 'to_currency' in the dictionary 'usd' in the dictionary 'currency_conversion_factors'
    return amount#return 'amount'

currencies = {#define variable 'currencies' as a dictionary with the following values
    "1": "usd",
    "2": "mxn",
    "3": "eur",
    "4": "hkd",
    "5": "bnd"
}

def ask_currency():#define function 'ask_currency' with no parameters
    x=input("Please enter which type of currency you have. Choose from the list:\n1. United States Dollar\n2. Mexican Peso\n3. European Euro\n4. Hong Kong Dollar\n5. Brunei Dollar\n: ")#ask the user to enter a number corresponding to a currency on the list, then set the local variable 'x' equal to what they say
    print("")#print a new line
    y=float(input("Please enter how much money you have: "))#ask the user to enter an amount of money, then set the local variable 'y' equal to what they say
    print("")#print a new line
    z=input("Please enter which type of currency you would like to convert to. Choose from the list:\n1. United States Dollar\n2. Mexican Peso\n3. European Euro\n4. Hong Kong Dollar\n5. Brunei Dollar\n: ")#ask the user to enter a number corresponding to a currency on the list, then set the local variable 'z' equal to what they say
    print(convert_currency(y, currencies.get(x), currencies.get(z)))#call the function 'convert_currency' with the arguments 'y', the value 'x' in the dictionary 'currencies', and the value 'z' in the dictionary 'currencies', and print the output

grocery_prices = {#define variable 'grocery prices' as a dictionary with the following values
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

def grocery_list(groceries):#define function 'grocery_list' with parameter 'groceries'
    total = 0#set local variable 'total' to integer 0
    for i in groceries:#iterate through 'groceries', where for each iteration, 'i' is equal to the element in 'groceries'
        total += grocery_prices.get(i)#set 'total' to 'total' plus the value 'i' in the dictionary 'grocery_prices'
    return total#return 'total'
    
        
    
def main():#define function 'main' with no parameters
    ask_currency()#call function 'ask_currency' with no parameters
    print("Price of groceries: {:.2f}".format(grocery_list(["pasta", "cake", "orange", "orange"])))#print "Price of groceries: ", then the output of the function 'grocery_list' with parameter ["pasta", "cake", "orange", "orange"]
   
if(__name__ == "__main__"):#if the variable '__name__' is equal to the string "__main__", then
    main()#call the function 'main' with no parameters
    


