def parse_table(name, lines):
    results = {}
    stop_word = ("Revenue" if name == "Expenses" else "Expenses")
    index = lines.index(name) + 1
    column_names = lines[index].split()
    index += 1
    rows = {}
    while index < len(lines) and lines[index] != stop_word:
            r = lines[index].split()
            rows[r[0]] = [int(e) for e in r[1:]]
            index+=1
    for col_idx, column_name in enumerate(column_names):
        results[column_name] = {}
        for row_index in rows:
            results[column_name][row_index] = rows[row_index][col_idx]
    return results     

def parse_input(lines):
    revenues = parse_table("Revenue", lines)
    expenses = parse_table("Expenses", lines)
    for person in revenues:
        comission = 0
        for item in revenues[person]:
            total = revenues[person][item] - expenses[person][item]
            if total > 0:
                comission += total * 0.062
        print(person, format(comission, '.2f'))

if __name__ == '__main__':
    with open("input.txt") as fh:
        lines = fh.readlines()
    clean_lines = [line.strip() for line in lines if line != "\n"]
    parse_input(clean_lines)  