
import random
import time

As = 1
J = 10
Q = 10
P = 10

kartlar = (As,2,3,4,5,6,7,8,9,10,J,Q,P)

print("1 => kart çek")
print("2 => bekle")

user_k1 = random.choice(kartlar)
user_k2 = random.choice(kartlar)

kasa_k1 = random.choice(kartlar)
kasa_k2 = random.choice(kartlar)

user_toplam = int(user_k1 + user_k2)
kasa_toplam = int(kasa_k1 + kasa_k2)

print("Kasanın kartları: {} ve X".format(kasa_k1))

print(f"Sizin kartlarınız: {user_k1} ve {user_k2}")
print(f"Kartlarınızın toplamı: {user_toplam}")

if user_toplam == 21:
    print("---------- Tebrikler blackjack yaptınız!!! ----------")
else:
    while True:
        if user_toplam < 21:
            islem = int(input("Yapmak istediğiniz işlemi girin: "))
            if islem == 1:
                cekilen_kart_user = random.choice(kartlar)
                user_toplam += cekilen_kart_user
                time.sleep(1)
                print(f"-♠- {cekilen_kart_user} çektiniz -♠-")
                time.sleep(1)
                print(f"-★- Destenizin toplamı: {user_toplam} -★-")
            elif islem == 2:
                time.sleep(1)
                print(f"{user_toplam} de/da durdunuz.")
                time.sleep(1)
                print(f"Kasanın kartları: {kasa_k1} ve {kasa_k2}")
                time.sleep(1)
                print(f"Kasanın toplamı: {kasa_toplam}")
                break   
        elif user_toplam == 21:
            time.sleep(1)
            print(f"---------- Destenizin toplamı: 21 ----------")
            break
        else:
            time.sleep(1)
            print("---------- Kaybettiniz ----------")
            break

while True:
    if user_toplam > 21:
        time.sleep(1)
        print("---------- Kasa kazanır ----------")
        break
    elif kasa_toplam < user_toplam:
        cekilen_kart_kasa = random.choice(kartlar)
        kasa_toplam += cekilen_kart_kasa
        time.sleep(1)
        print(f"-♠- Kasa {cekilen_kart_kasa} çekti -♠-")
        time.sleep(1)
        print(f"-★- Kasanın toplamı: {kasa_toplam} -★-")
        continue
    elif kasa_toplam == user_toplam:
        time.sleep(1)
        print("---------- Berabere bitti ----------")
        break
    elif kasa_toplam > 21:
        time.sleep(1)
        print("---------- Kazandınız!!! ----------")
        break
    else:
        time.sleep(1)
        print("---------- Kasa kazanır ----------")
        break