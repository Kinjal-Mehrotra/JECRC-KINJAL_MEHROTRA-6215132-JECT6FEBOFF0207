#Write a program to create a function which can take n number of int/float numbers and returns only their addition

def add_nums(*args):
    print(args,type(args))
    sum=0
    for num in args:
        sum+=num

    return sum

result=add_nums(1,2,3,4,1.9,5.3)
print(result)


def add_nums_2(*args):
    args=list(args)
    print(args,type(args))
    sum=0
    for num in args:
        sum+=num

    return sum

result=add_nums_2(4,3,5,222,4242,9.999)
print(result)

#create a function which wil take n number of inputs from the user and return the sum , please make sure that user is capable of passing all type of values
def add_nums_3(*args):
    # print(args,type(args))
    sum=0
    for num in args:
        if type(num) in [int,float]:
            sum+=num

    return sum

result=add_nums_3(1,2,3,6.6)
print(result)

#double packing
# def fun_name(**kwargs):
#     statement block 

# fun_name(k1=v1,k2=v2,...,kn=vn)

def print_details(**kwargs):
    print(kwargs)
print_details(user='Kinjal',password='****',logged_in_devices=['android','windows','linux'])

#unpacking
def add_nums_4(*args):

    sum=0
    for num in args:
        if type(num) in [int,float]:
            sum+=num

    return sum

print(add_nums_4(*eval(input("Enter a list of values: "))))

