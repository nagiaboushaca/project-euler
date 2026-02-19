import math

# even number squared is even (2n * 2n = 4n^2), odd number squared is odd (2n+1)(2n+1)=4n^2=4n+1=2(2n^2+2n) + 1
def prob0():
    i = 1
    ans = 0

    while i < 167000:
        ans+=i**2
        i = i+2
    print(ans)


def prob1():
    #sum of multiples of 3 + multiples of 5 - multiples of 15
    numThrees = math.floor(1000 / 3)
    numFives = math.floor(1000/5)
    numFifteens = math.floor(1000/15)

    #333 multiples of 3: 3*(1+2+...+333)
    #200 multiples of 5: 5*(1+2+...+200)
    #x multiples of 15: 15*(1+2+...+x)

    def sumToX(x):
        ans = 0
        for i in range(1,x+1):
            ans+=i
        return ans
    
    # minus 1000 bc strictly below 1000 (included in multiples of 5)
    print(3*sumToX(numThrees) + 5*sumToX(numFives) - 15*sumToX(numFifteens) - 1000)

# find sum of even fibonnacci terms less than 4 million
# terms go: odd, even, odd, odd, even, odd, odd ...
# so need to add every fibonnaci term 2 mod 3 (1 mod 3 for 0-based index)
def prob2():
    x = 1
    y = 2
    sum = 0
    list = [] #fibonacci list

    while x < 4000000 or y < 4000000:
        list.append(x)
        list.append(y)
        x = x+y
        y = x+y

    for i in range(0, len(list)):
        if i % 3 == 1:
            sum += list[i]
    print(sum)

# find largest prime factor of num
# probably there is a better way to do this, it took like ~20-30 sec
def prob3():
    num = 600851475143
    listFactors = []

    def checkPrime(x):
        for i in range(2, math.ceil(math.sqrt(x))):
            if num % i == 0:
                return False
        return True
    
    # am only adding prime factors, and then dividing that prime factor out of num
    # as many times as divisible
    for i in range (2, math.ceil(math.sqrt(num))):
        if checkPrime(i) and num % i == 0:
            listFactors.append(i)
            while num % i == 0:
                num = num / i
    print(listFactors[-1]) # last element largest

def prob4():
    def isPalindrome(x):
        return str(x) == str(x)[::-1] # checks if palindrome as a reversed string
    x = 999
    y = 999

    # assuming both 3-digit numbers are in the 900+ range.
    while x > 900:
        y=999
        while y > 900:
            if isPalindrome(x*y):
                print(x*y)
                return
            else:
                y = y - 1
        x = x-1

