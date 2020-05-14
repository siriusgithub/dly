def prime(number):
    oldnum = number
    factor = 1
    while number > 1:
        factor += 1
        while number % factor == 0:
            if 1< factor < oldnum:
                return 0 # is not prime
                print("yay")
                break
            number //= factor
    return 1 #prime!
