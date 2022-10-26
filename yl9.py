a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
	print("Võrdkülgne kolmnurk")

elif a==b or b==c or c==a:
	print("Võrdhaarne kolmnurk")

else:
	print("Erikülgne kolmnurk")