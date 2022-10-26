a = input('Sisesta oma nimi:')
print('Tere', a)

b = input('Sisesta elukoht:')
if b=='Saaremaa':
    print('ok')

c = int(input('Sisesta oma vanus:'))
if (c < 18):
    print('Sa oled liiga noor, et autot juhtida.')

elif c==18:
    print('Palju õnne täisealiseks saamise puhul!')

else:
    print('Sa oled piisavalt vana, et autot juhtida.')