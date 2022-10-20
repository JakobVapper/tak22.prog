a=int(input("Sisesta esimene arv:"))
b=int(input("Sisesta teine arv: "))

if(a<b):
    print("{} on väikseim".format(a))

elif(b<a):
    print("{} on väikseim".format(b))
    
else:
    print("{} ja {} on võrdsed".format(a,b))