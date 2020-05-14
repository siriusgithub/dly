def prime(number):
    oldnum = number
    factor = 1
    while number > 1:
        factor += 1
        if number % factor == 0:
            if 1 < factor < oldnum:
                return False # is not prime
            number //= factor
    return True # is prime!

print(prime(11))

# BY Tim Pietzcker

'''
Your code never reaches the line return 1 (which should be return True, by the way) because

your break statement would only break out of the inner while loop
that break statement isn't ever reached because you return 0 before that.
Your inner while loop should be an if, anyway (since you're not actually doing anything that requires looping).

If you change that (and remove the unreachable code), it "works" (besides the erronenous result of prime(1) being True), it's a very inefficient way of finding prime numbers.
'''
