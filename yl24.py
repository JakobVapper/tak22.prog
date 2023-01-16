def upc(x):

    if(len(x) < 11):
        aux = 11 - len(x)

        while True:
            x = "0" + x

            if(len(x) == 11):
                break

    num_list = list(x)
    odd_num = 0
    even_num = 0

    for i in range(0, 11):

        if(i % 2 == 0):
            odd_num = odd_num + int(num_list[i])

        else:
            even_num = even_num + int(num_list[i])
    result = (even_num + odd_num * 3) % 10

    if(result != 0):
        result = 10 - result
        return result
    else:
        return result

print(upc('4210000526')) 
print(upc('3600029145'))
print(upc('12345678910')) 
print(upc('1234567')) 