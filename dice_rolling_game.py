import random

while True:
    # loop
    choice = input('Roll the dice? (y/n): ').lower()
    # If users enters y
    if choice == 'y':
        # generate two random numbers
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
    # print them
        print(f'({die1},{die2})')
    # If users enters N
    elif choice == 'n':
        print('Thank You')
        # print thank you
        # terminate
        break
    # else
    else:
       # invaild choice
        print('Invalid Code')
