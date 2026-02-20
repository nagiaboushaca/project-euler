import math

def checkPrime(x):
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    return str(x) == str(x)[::-1] # checks if palindrome as a reversed string

def sumToX(x):
    ans = 0
    for i in range(1,x+1):
        ans+=i
    return ans

def numFactors(x):
    count = 0
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            if i == math.ceil(math.sqrt(x)):
                count+=1 # add only the square root
            else:
                count += 2 # add factor and its corresponding factor, since we are only checking up to square root
    return count

def nchooser(n,r):
    return factorial(n) / (factorial(r)*factorial(n-r))

def factorial(x):
    if x == 1 :
        return 1
    else:
        return x * factorial(x-1)