while True:
    switch_mode = int(input('Enter numbers between 1-5 to toggle light dimmer, \n Off(1)\n Low(2)\n Medium(3)\n High(4)\n Maximum(5)\n:'))
    if switch_mode != 0:
        print('Your chosen mode is', switch_mode, '\n')
    
    else:
        print('Session Ended')
        break
    
