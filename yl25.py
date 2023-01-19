me = {
  'eesnimi': 'Jakob',
  'perenimi': 'Vapper',
  'sünniaasta': 2006,
  'elukoht': 'Muhu',
  'magustoit': 'kohuke'
}

print(me.get('elukoht'))

me['magustoit'] = 'jäätis'

for k, v in me.items():
    print(k, v)

#me['personal_code'] = '12345678910'

if 'personal_code' in me:
    print(me['There is a personal code in the dictionary'])
else:
    print('There is no personal code in the dictionary')

print(len(me))

me = {
  'eesnimi': 'Jakob',
  'perenimi': 'Vapper',
  'sünniaasta': 2006,
  'elukoht': 'Muhu',
  'magustoit': 'kohuke'
  'pikkus': 1.8,
}