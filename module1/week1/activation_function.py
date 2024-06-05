import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def sigmoid(x):
    ans = 1/(1+ math.e**(-x))
    return ans

def relu(x):
    if x <= 0 :
        return 0
    else:
        return x
    
def elu(x):
    if x <= 0 :
        ans = 0.01*(math.e**x -1)
        return ans
    else:
        return x


def exercise2():
    x = input("Input x = ")
    if is_number(x) == False:
        print('x must be a number')
        return
    activation_function = input("Input activation Function ( sigmoid | relu | elu ) : ")
    x = float(x)
    print(f"Input x = {x}")
    print(f'Input activation Function ( sigmoid | relu | elu ) : {activation_function}')
    if activation_function == 'sigmoid':
        print(f"{activation_function}: f({x}) = {sigmoid(x)}")
    elif activation_function == 'relu':
        print(f"{activation_function}: f({x}) = {relu(x)}")
    elif activation_function == 'elu':
        print(f"{activation_function}: f({x}) = {elu(x)}")
    else:
        print(f"{activation_function} is not supportted")
    
exercise2()
exercise2()
exercise2()