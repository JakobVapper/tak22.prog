me = {
  'first-name': 'Jakob',
  'last-name': 'Vapper',
  'birth-year': 2006,
  'home': 'Muhu',
  'dessert': 'kohuke'
}

print(me.get('home'))

me['dessert'] = 'ice-cream'

me['height'] = '1.80'

del me['birth-year']

me.clear()

for k, v in me.items():
    print(k, v)

#me['personal_code'] = '12345678910'

if 'personal_code' in me:
    print(me['There is a personal code in the dictionary'])
else:
    print('There is no personal code in the dictionary')

print(len(me))
