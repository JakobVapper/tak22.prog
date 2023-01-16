import random

n = random.randrange(1,100)
guess = int(input("Sisesta arv: "))

while n!= guess:

    if guess < n:
        print("Liiga madal!")
        guess = int(input("Sisesta arv uuesti: "))
    elif guess > n:
        print("Liiga kõrge!")
        guess = int(input("Sisesta arv uuesti: "))    
    else:
      break

print("Õige vastus!")