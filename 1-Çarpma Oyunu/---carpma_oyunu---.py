
from random import randint

for i in range(5):
 
    x = randint(1,5)
    y = randint(1,5)

    result = (x * y)
    print(f"{x} x {y} = ?")
    user_result = int(input("Lütfen cevabınızı giriniz: "))

    if user_result == result:
        print("Tebrikler doğru cevap.")
       
    else:
        print("Malesef kaybettiniz. Doğru cevap {}".format(result))
        break

print("Tebrikler 2. seviyeye geçtiniz.")

for i in range(5):
 
    x = randint(6,10)
    y = randint(6,10)

    result = (x * y)
    print(f"{x} x {y} = ?")
    user_result = int(input("Lütfen cevabınızı giriniz: "))

    if user_result == result:
        print("Tebrikler doğru cevap.")
       
    else:
        print("Malesef kaybettiniz. Doğru cevap {}".format(result))
        break

print("Tebrikler 3. seviyeye geçtiniz.")

for i in range(5):
 
    x = randint(11,20)
    y = randint(11,20)

    result = (x * y)
    print(f"{x} x {y} = ?")
    user_result = int(input("Lütfen cevabınızı giriniz: "))

    if user_result == result:
        print("Tebrikler doğru cevap.")
       
    else:
        print("Malesef kaybettiniz. Doğru cevap {}".format(result))
        break

print("Tebrikler 4. seviyeye geçtiniz.")

for i in range(5):
 
    x = randint(21,100)
    y = randint(21,100)

    result = (x * y)
    print(f"{x} x {y} = ?")
    user_result = int(input("Lütfen cevabınızı giriniz: "))

    if user_result == result:
        print("Tebrikler doğru cevap.")
       
    else:
        print("Malesef kaybettiniz. Doğru cevap {}".format(result))
        break

print("Tebrikler son seviyeye geçtiniz.")

for i in range(5):
 
    x = randint(101,999)
    y = randint(101,999)

    result = (x * y)
    print(f"{x} x {y} = ?")
    user_result = int(input("Lütfen cevabınızı giriniz: "))

    if user_result == result:
        print("Tebrikler doğru cevap.")
       
    else:
        print("Malesef kaybettiniz. Doğru cevap {}".format(result))
        break

print("Tebrikler kazandınız!!!")