# def vol(rad):
#     return 4/3*3.14*pow(rad,3)

# print(vol(2))

# **Напишите функцию, которая проверяет, содержится ли число в указанном диапазоне (включая верхнюю и нижнюю границы)**
# def ran_check(a,b,c):
#     list1=[a,b,c]
    
#     list1.sort()

#     return f"{list1[1]} is in the range between {list1[0]} and {list1[2]}"


# print(ran_check(5,2,7))


#**Напишите функцию Python, которая принимает на вход строку, и вычисляет количество букв в верхнем регистре и в нижнем регистре.**
# def up_low(s):
#     uper=0
#     lower=0
#     for i in s:
#         if i.isupper():
#             uper+=1
#         if i.islower():
#             lower+=1
#     return print(f'No. of Upper case characters :  {uper}\nNo. of Lower case Characters :  {lower}')
            

# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)


#**Напишите функцию Python, которая получает на входе список, и возвращает новый список, содержащий уникальные элементы из первого списка.**

# def unique_list(lst):
#     new_lst=[]
#     for i in lst:
#         if i in new_lst:
#             continue
#         else: new_lst.append(i)
#     return new_lst

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


# **Напишите функцию Python, которая перемножает все числа в списке.**
# def multiply(numbers):  
#     result=1
#     for i in numbers:
#         result*=i
#     return result


# print(multiply([1,2,3,-4]))




# **Напишите функцию Python, которая проверяет входную строку, является ли эта строка палиндромом или нет.**

# def palindrome(s):
#     if len(s) % 2 == 0:
#         s1 = s[:int(len(s)/2)]
#         return s1[::-1] == s[int(len(s)/2):]

#     else: 
#         s1 = s[:int(len(s)/2)]
#         return s1[::-1] == s[int(len(s)/2+1):]


# print(palindrome('lalalalalalalalalal'))


import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)
    print(alphaset)  
    alphaset <= set(str1.lower())
    print(alphaset) 

print(ispangram("The quick brown fox jumps over the lazy dog"))
