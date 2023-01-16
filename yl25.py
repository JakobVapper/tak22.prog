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

