import random

def sifre_uret(parola_uzunlugu):
    characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password = ""

    for i in range(parola_uzunlugu):
        
        rasgele_karakterler = random.choice(characters)
        password += random.choice(characters)



    return password