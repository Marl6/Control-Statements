category = input('Enter your category:\n Easy\n Medium\n Hard\n').lower()
numbers = [1,2,3,4,5,6,7,8,9,0]

if category == "easy":
    password = input('Enter your password, must be atleast 6 characters: ')
    
    if len(password) > 5:
        print('Password passed!')
    else:
        print('Password must be atleast 6 characters long!')

elif category == "medium":
    password = input('Enter your password, must be atleast 8 characters long and must contain at least one uppercase letter, one lowercase letter, and one digit: ')
    
    if len(password) > 7:
        if any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
                print('Good!')
        
        else:
            print('Not Good!')
    else:
        print('Password length must be greater than 7 characters.')
