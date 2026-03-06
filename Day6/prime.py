#create a function which will return a list of prime numbers, please make sure that user can pass n number of inputs. For checking whether a number is prime or not, u can create a function
def isPrime(num):
    # isPrime=True
    if num<2:
        return False
    for i in range(2,num//2+1):
    # for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    
    return True

def find_prime_numbers(*args):
    prime=[]
    for num in args:
        if isPrime(num):
            prime.append(num)

    return prime

result=find_prime_numbers(*eval(input("Enter number list: ")))
print(result)