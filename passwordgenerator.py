import string
import random


def generator():
    
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
  
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    while True:
        
        passlen = int(input("Enter the password length: "))
        if passlen > 0:
            print("Your password generating...")
            random.shuffle(s)
            pas = ("".join(s[0:passlen]))
            print(pas)
            break
        else:
            print("Enter positive integers: ")
                
    '''random.shuffle(s)
    pas = ("".join(s[0:passlen]))
    print(pas)'''
    
    
                  
generator()