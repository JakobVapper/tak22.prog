def sales(data):
    lines = [line.strip().split() for line in data.split("\n") if line]

    _, *revenue = zip(*lines[2:len(lines)//2])
    _, *expenses = zip(*lines[2+len(lines)//2:])
    
    commission = [sum(max(0, int(r)-int(e))*.062 for r, e in zip(*data)) for data in zip(revenue, expenses)]

    print(f"           {' '.join(lines[1])}")
    print(f"Commission {' '.join([f'{value//1:>{len(name)}.0f}' for value, name in zip(commission, lines[1])])}")
    
sales('''Revenue

            Johnver Vanston Danbree Vansey  Mundyke
Tea             190     140    1926     14      143
Coffee          325      19     293   1491      162
Water           682      14     852     56      659
Milk            829     140     609    120       87

Expenses

            Johnver Vanston Danbree Vansey  Mundyke
Tea             120      65     890     54      430
Coffee          300      10      23    802      235
Water            50     299    1290     12      145
Milk             67     254      89    129       76''')
