
from random import randint

a = "-"*10

number = randint(1,52)

tahmin_sayısı = 0

while True:
    x = int(input(f"{a} Tahmin sayınızı giriniz: "))
    tahmin_sayısı += 1

    if x == 0:
        print(f"{a} Oyunu bitirdiniz. {a}")
        break

    elif x < number:
        print("Daha yüksek bir sayı giriniz.")

    elif x > number:
        print("Daha düşük bir sayı giriniz.")

    else:
        print(f"{a} Tebrikler!!! Doğru sayı {number}. {a}")
        print(f"{a} {tahmin_sayısı} denemede buldunuz. {a}")