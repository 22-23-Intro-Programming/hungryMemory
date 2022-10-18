#Python Problem Set #1
#Thomas Sands

def greeting():
    name = input("Enter your name: ")
    print(f"Good afternoon, {name}!")
    
def is_multiple(x, y):
    if(x%y == 0):
        return(f"{y} is a multiple of {x}.")
    else:
        return(f"{y} is not a multiple of {x}.")

def palindrome():
    word = input("Enter a word: ")
    if(word == word[::-1]):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")
    

def main():
    greeting()
    is_multiple(9,4)
    is_multiple(140, 10)
    palindrome()

if(__name__ == "__main__"):
   main()
    
    
