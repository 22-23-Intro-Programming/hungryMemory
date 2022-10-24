#Python Problem Set #2
#Thomas Sands

def factorial(num):
    i = num - 1
    while(i != 0):
        num *= i
        i -= 1
    return(num)

def double_it(phrase):
    result = ""
    for i in range(len(phrase)):
        result += (phrase[i])*2
    print(result)

def camel_case(filename):#  joe mama   3/3 
    filename = (filename.strip()).replace("/", "-").title()
    if(filename[0].isalpha()):
        filename = filename.split()#strings are arrays bit for some reason YOU CANT ASSIGN THE DIFFERENMT INDEXES wth tjhats such a scam i hate python
        filename[0] = filename[0].casefold()
        filename = "".join(filename)
    return(filename)

def main():
    print(factorial(4))
    print(factorial(6))
    print(factorial(8))
    print(double_it(input("Enter a phrase to double: ")))#it prints none after i call this function idk why i tried a billion different things python is weird sometimes
    print(camel_case(input("Enter a filename: ")))

if(__name__ == "__main__"):
    main()
    
    
        
