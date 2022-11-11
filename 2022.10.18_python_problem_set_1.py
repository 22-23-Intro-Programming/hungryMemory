#Python Problem Set #1
#Thomas Sands

def greeting():#define greeting function
    name = input("Enter your name: ")#ask the user for their name and set the variable 'name' to what they say
    print(f"Good afternoon, {name}!")#print 'Good afternoon' and then their name
    
def is_multiple(x, y):#define is_multiple function
    if(x%y == 0):#if x modulo y is equal to zero then:
        return(f"{y} is a multiple of {x}.")#return y 'is a multiple of' x
    else:#if it isnt equal to zero then:
        return(f"{y} is not a multiple of {x}.")#return y 'is not a multiple of' x

def palindrome():#define palindrome function
    word = input("Enter a word: ")#ask the user for a word and set the variable 'word' to what they say
    if(word == word[::-1]):#if the value stored in variable word is equal to the value stored in variable word but reversed, then:
        print(f"{word} is a palindrome!")#print word 'is a palindrome!'
    else:#otherwise
        print(f"{word} is not a palindrome.")#print word 'is not a palindrome!'
    

def main():#define main function
    greeting()#call greeting function with no parameters
    print(is_multiple(9,4))#print the output of the is_multiple function with the parameters 9 and 4
    print(is_multiple(140, 10))#rint the output of the is_multiple function with the parameters 140 and 10
    palindrome()#call palindrome with no parameters

if(__name__ == "__main__"):#if the variable __name__ is equal to '__main__'
   main()#call main function
    
    
