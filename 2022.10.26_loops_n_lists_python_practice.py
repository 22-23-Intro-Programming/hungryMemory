#Loops n' Lists Python Practice

def consecutive_sevens(list_o_nums):
    if(len(list_o_nums) < 2):
        return(False)
    for i in range(0, len(list_o_nums)-1):
        if(list_o_nums[i] == 7 and list_o_nums[i+1] == 7):
            return(True)
    return(False)

def addthenumbersbutnotafterzero(list_o_nums):
    total = 0
    i = 0
    while(i < len(list_o_nums)):
        if(list_o_nums[i] != 0):
            total += list_o_nums[i]
            i += 1
        else:
            return(total)
    return(total)

def addthenumbersbutnotinbetweentwoandthreeforsomereason(list_o_nums):
    total = 0
    i = 0
    counting = True
    while(i < len(list_o_nums)):
        if(counting):
            if(list_o_nums[i] == 2):
                counting = False
            else:
                total += list_o_nums[i]
        elif(list_o_nums[i] == 3):
            counting = True
        i += 1
    return(total)



def main():
    print(consecutive_sevens([7, 5, 5]))
    print(consecutive_sevens([]))
    print(consecutive_sevens([7, 7, 7]))
    print(consecutive_sevens([7, 0, 7]))
    print(consecutive_sevens([7, 7, 5]))
    print(consecutive_sevens(["7", 7, 5]))
    print(consecutive_sevens([7, 77, 5]))
    print(consecutive_sevens([8, 7, 7]))
    print(addthenumbersbutnotafterzero([1, 4, 0, 3, 6]))
    print(addthenumbersbutnotafterzero([1, 20, 12, 8, 0, 8, 10]))
    print(addthenumbersbutnotafterzero([0, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(addthenumbersbutnotinbetweentwoandthreeforsomereason([1, 4, 4]))
    print(addthenumbersbutnotinbetweentwoandthreeforsomereason([1, 5, 6, 2, 99, 56, 3]))
    print(addthenumbersbutnotinbetweentwoandthreeforsomereason([1, 3, 4, 2, 3, 8]))
    
if(__name__ == "__main__"):
    main()


                    
