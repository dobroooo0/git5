n = int(input("Введите число: "))
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
print("Число с цифрами в обратном порядке:", rev)