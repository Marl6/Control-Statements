import random
number = random.randint(0, 10)

for chance in range(3):
    guess = int(input('Enter a number: '))
    
    if guess == number:
        print('Tumpak Ganern')
        break;    
            
    elif guess != number and number >5 and guess<5:
        print('Higher!')
    elif guess != number and number <5 and guess>5:
        print('Lower!')
    elif guess-number > 0:
        print('Lower!')
    elif guess-number < 0:
        print('Higher!')
    elif chance>2:
        print('Nice try! You have run out of chances!')
