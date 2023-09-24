def get_file_data():
    NULL_WORD = 'нет данных'
    return_data = {'headers': [], 'table_data': []}
    with open('data.txt', 'r') as file:
        for i, line in enumerate(file):
            if i == 0: return_data['headers'] = line.rstrip().split('\t')
            else:
                appendable_data = []
                for element in line.rstrip().split('\t'):
                    if element.isnumeric():
                        appendable_data.append(int(element))
                    elif element.replace('.', '', 1).isnumeric():
                        appendable_data.append(float(element))
                    elif element == NULL_WORD:
                        appendable_data.append(None)
                    else: appendable_data.append(element)
                return_data['table_data'].append(appendable_data)
    return return_data

        