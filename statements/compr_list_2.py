for i in range(1,100):
    if i % 3 == 0:
        print(f"{i} - Fizz div 3")
    if i % 5 == 0:
        print(f"{i} - Buzz div 5")
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} - FizzBuzz div 3and5") 