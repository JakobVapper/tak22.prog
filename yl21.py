import random

n = random.randrange(1,100)
guess = int(input("Sisesta arv: "))

while n != guess:

    if guess < n:
        print("Liiga madal!")
    elif guess > n:
        print("Liiga kõrge!")

    guess = int(input("Sisesta arv uuesti: "))

print("Õige vastus!")