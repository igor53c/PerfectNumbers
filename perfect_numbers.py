def is_perfect_number(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    total = sum(divisors)
    return {
        "divisors": divisors,
        "total": total,
        "is_perfect": total == num
    }


def find_mersenne_primes(n):
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    mersenne_primes = []
    p = 2
    while True:
        mersenne = (2 ** p) - 1
        if mersenne >= n:
            break
        if is_prime(mersenne):
            mersenne_primes.append(mersenne)
        p += 1
    return mersenne_primes


def find_perfect_numbers(n):
    mersenne_primes = find_mersenne_primes(n)
    perfect_numbers = []
    for mp in mersenne_primes:
        p = mp.bit_length()
        perfect_number = (2 ** (p - 1)) * mp
        if perfect_number < n:
            perfect_numbers.append(perfect_number)
    return perfect_numbers
