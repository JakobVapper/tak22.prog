a=int(input("Sisesta esimene number:"))
b=int(input("Sisesta teine number: "))

if(a<b):
    print("{} on väikseim".format(a))

elif(b<a):
    print("{} on väikseim".format(b))
    
else:
    print("{} ja {} on võrdsed".format(a,b))