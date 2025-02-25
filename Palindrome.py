def palindrome(n):
    a = str(n)
    return a == a[::-1]


number = int(input("Проверяемое число: "))
if palindrome(number):
    print("Вы ввели палиндромное число!")
else:
    print("Нет, число не палиндромное!")
