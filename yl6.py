a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
c = float(input("Kolmas arv: "))
 
if (a > b) and (a > c):
   largest = a
elif (b > a) and (b > c):
   largest = b
else:
   largest = c
 
print("Suurim arv on",largest)