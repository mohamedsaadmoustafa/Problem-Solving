#Time Limit Exceeded
class Solution:
    def __init__(self):
        self.primes = []

    def is_prime(self, number):
        if number <= 1: return False
        if number == 2: return True
        if number > 2 and number % 2 == 0: return False

        for i range(3, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    def return_primes(self, start, end):
        for num in range(start, end):
            if self.is_prime(num):
                self.primes.append(num)
        return self.primes

    def countPrimes(self, n):
        start = 0
        self.return_primes(start, n)
        return len(self.primes)
        
        
# Another Solution
class Solution:
    def __init__(self):
        self.primes = []

    def countPrimes(self, number):
        if number == 0 or number == 1: return 0

        self.primes = [1]*(number)
        self.primes[0] = self.primes[1] = 0

        p = 2 
        while (p**2 <= number):
            # If prime[p] is not changed, then it is a prime
            if self.primes[p] == 1:
                # Update all multiples of p
                for idx in range(p**2, number, p):
                    #print(p, '--', idx)
                    self.primes[idx] = 0
            p += 1
        #print(list(range(0, number)))
        #print(self.primes)
        return sum(self.primes)

x = Solution()
x.countPrimes(110)#, x.countPrimes(0), x.countPrimes(1), x.countPrimes(2)
