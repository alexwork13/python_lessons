#### "Меньшее из двух чётных чисел": Напишите функцию, которая возвращает меньшее из двух чисел, *если* оба эти числа чётные. Иначе возвращает большее из двух чисел, если одно или оба числа нечётные.
# def lesser_of_two_evens(a,b):
#     if a % 2 ==0 and b % 2 ==0:
#         if a >= b: 
#             return b
#         else: return a
#     if a % 2 != 0 or b %2 != 0:
#         if a >= b: 
#             return a
#         else: return b


# print(lesser_of_two_evens(22,66))
# print(lesser_of_two_evens(1,5))

#### animal_crackers: Напишите функцию, которая получает на входе строку из двух слов, и возвращает True если оба слова начинаются с одной и той же буквы.

# def animal_crackers(text):
    
#     if (text.split()[0][0]).lower() == (text.split()[1][0]).lower():
#         return True
#     else: return False

# print(animal_crackers('Levelheaded llama'))
# print(animal_crackers('Crazy Kangaroo'))


#### OLD MACDONALD: Напишите функцию, которая переводит в верхний регистр первую и четвёртую буквы имени.
# def old_macdonald(name):
#     str1=''
#     for i,n in zip(name, range(len(name))):
#         if n == 0 or n == 3:
#             i = i.upper()
#         str1+=i
        
#     print(str1)

# old_macdonald("lobotra")


#### master_yoda: На входе фраза, на выходе вернуть слова в обратном порядке.

# def master_yoda(text):
    
#     list1 = text.split()
#     list1.reverse()
#     print(" ".join(list1))

# master_yoda('I am home')
# master_yoda('We are ready')



#### almost_there: на входе число n, вернуть True если n находится не далее чем на 10 от чисел 100 или 200.
# def almost_there(n):
#     if 90 < n and 110 > n or 190 < n and 210 > n:
#         return True
#     else: return False

# print(almost_there(150))


#### Найти 33: На входе список чисел, вернуть True если массив содержит где-нибудь 3 рядом с 3.
# def has_33(nums):
#     for i in range(len(nums)):
          
#       if i+1 < len(nums) and nums[i] == 3 and nums[i] == nums[i+1]:
#           return True
#     else: return False


# print(has_33([3, 1, 3]))

#### paper_doll: На входе строка, вернуть строку где каждый символ исходной строки повторяется три раза.
# def paper_doll(text):
#     strout=''
#     for i in text:
#         strout += i*3
#     print(strout)


# paper_doll('Mississippi')

#### blackjack: На входе три числа от 1 до 11. Если их сумма меньше или равна 21, то вернуть их сумму. Если сумма больше 21 *и* среди чисел есть 11, то уменьшить общую сумму на 10. И наконец, если сумма (в том числе после уменьшения) превышает 21, вернуть 'BUST'.
# def blackjack(*args):
#     if sum(args) <= 21:
#         return sum(args)
#     if sum(args) > 21 and 11 in args:
#         return sum(args) - 10
#     else: return "BUST"

# print(blackjack(9,9,11))

#### summer_69: Вернуть сумму чисел в массиве, кроме набора чисел который начинается с 6 и продолжается до 9 (для каждого числа 6 далее где-то будет число 9). Вернуть 0 если чисел нет.
# def summer_69(arr):
#     sum1 = 0
#     six = False
#     for i in arr:
#         if i == 6:
#             six = True
#             i = 0
        
#         if i == 9:
#             i=0
#             six = False
#         if six == True:
#             i = 0
          
#         sum1 += i

#     return sum1


# # проверка
# print(summer_69([1, 3, 5]))


#### spy_game: Напишите функцию, которая берёт список чисел, и возвращает True, если в списке содержатся числа 0 0 7 в указанном порядке. 
# def spy_game(nums):
#     str1 = ""
#     condition = False
#     for i in nums:
#         if i == 0:
#             str1 += 'o'
#         if i == 7:
#             str1 += 's'
#         if str1 == 'oos':
#             condition = True
#     return condition

# print(spy_game([1,7,2,0,4,5,0]))