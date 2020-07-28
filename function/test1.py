import math

def is_prime2(num):
    '''
    Улучшенный метод проверки простых чисел. 
    '''
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


print(is_prime2(17))