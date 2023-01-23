input_list = [line.split() for line in input('Enter the input >>> ').split('\n') if line]
input_splice = input_list.index(['Expenses'])
commissions = dict.fromkeys(input_list[1], 0)
revenues = {elem[0]: {name: int(revenue) for name, revenue in zip(input_list[1], elem[1:])} for elem in input_list[2: input_splice]}

for elem in input_list[input_splice + 2:]:
	for name, expense in zip(input_list[1], elem[1:]):
		commissions[name] += max(0, revenues[elem[0]][name] - int(expense))

print(' '*12 + ' '.join(f'{key:>{max(len(key), len(str(val)))}}' for key, val in commissions.items()) + '\nCommission  ' + ' '.join(f'{str(round(val * 0.062, 2)):>{max(len(key), len(str(val)))}}' for key, val in commissions.items()))