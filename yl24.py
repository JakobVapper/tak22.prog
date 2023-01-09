def upc(x):
    if(len(x) < 11):
        aux = 11 - len(x)
        while True:
            x = "0" + x
            if(len(x) == 11):
                break
    number_list = list(x)
    odd_numbers = 0
    even_numbers = 0
    for i in range(0, 11):
        if(i % 2 == 0):
            odd_numbers = odd_numbers + int(number_list[i])
        else:
            even_numbers = even_numbers + int(number_list[i])
    result = (even_numbers + odd_numbers * 3) % 10
    if(result != 0):
        result = 10 - result
        return result
    else:
        return result

print(upc("12345678901"))