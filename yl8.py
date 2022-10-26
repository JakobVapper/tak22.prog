a=int(input("Sisesta arv:"))

if(a%4==0 and a%100!=0 or a%400==0):
    print("See on liigaasta")

else:
    print("See on lihtaasta")