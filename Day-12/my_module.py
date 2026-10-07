def genererate_full_name(firstname, lastname): 
    return firstname, lastname

def sum_two_nums(a, b): 
    return a + b 

def person(): 
    gender_var = int(input("1 for male, 2 for female: "))
    
    if int(gender_var) > 2 and int(gender_var) < 1: 
        raise ValueError("Must be between 1 and 2")
    #print(type(gender_var))
    
    if gender_var == 1: 
        print('Male')
    elif gender_var == 2: 
        print('Female')
    
    return gender_var
