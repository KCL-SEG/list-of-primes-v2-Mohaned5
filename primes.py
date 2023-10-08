"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    try:
        list = []
        if number_of_primes <= 0:
            raise ValueError
        num = 2
        while len(list) < number_of_primes:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                list.append(num)
            num += 1
        return list
    except ValueError as e:
        raise e
        