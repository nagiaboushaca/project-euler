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
        for i in range(2, math.ceil(math.sqrt(x))+1):
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

def prob5():
    product = 1

    list = []
    for i in range(1, 21):
        list.append(i) #1-20

    list.reverse() #20-1

    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    
    for i in range(0, len(primes)):
        product = product * primes[i]
    product = product * 2**3 # to get 4, 8, 16, 14
    product = product * 3 # to get 9. Now we also have 6 and 12, 18
    print(product)


def prob6():
    sumOfSquares = 0
    squareOfSum = 0
    for i in range(1, 101):
        sumOfSquares += i**2
        squareOfSum += i

    print(sumOfSquares - squareOfSum**2) # project euler accepted positive version of this answer


def prob7():
    count = 1 # count 2 already, as it is the only even prime
    num = 3

    def checkPrime(x):
        for i in range(2, math.ceil(math.sqrt(x))+1):
            if num % i == 0:
                return False
        return True


    while count < 10000:
        num+=2
        if checkPrime(num):
            count+=1
    print(num)

def prob8():
    num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    # find 13 adjacent digits that don't have a 0, and find highest product
    # string processing for ease

    string = str(num)
    highScore = 0

    for i in range(0, len(string)):
        substring = string[i:i+13]
        if "0" in substring:
            indexOfZero = string[i:i+13].find("0")
            i = i + indexOfZero
        else:
            product = 1
            for j in range(0, len(substring)):
                product = product * int(substring[j])
            if product > highScore:
                highScore = product
    print(highScore)


prob8()