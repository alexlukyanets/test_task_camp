import csv

"""Function reads from csv file and return list"""


def read_csv(filename):
    data = []
    with open(filename, newline='') as csvfile:
        fieldnames = ['Employee Name', 'Date', 'Work Hours']
        spamreader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in spamreader:
            data.append(row)
    return data


"""Function organizes keys and values. Also it removes the first element with fields"""


def change_keys_values(data):
    my_data = []
    for i in data[1:]:
        my_data.append({'Employee Name': i['Employee Name'], i['Date']: i['Work Hours']})
    return my_data


"""Function receives data and retrieves datetime fields for new file"""


def get_fields(data):
    date = []
    for item in data:
        for key in item.keys():
            if not key in date:
                date.append(key)
    return date


"""Function retrieve name for new file"""


def has_element(item, new_data):
    for elem in new_data:
        if elem['Employee Name'] == item['Employee Name']:
            return False
    return True


def get_names(data):
    new_data = []
    for item in data:
        if has_element(item, new_data):
            new_data.append({'Employee Name': item['Employee Name']})
    return new_data


"""Function updates to zero all date fields"""


def send_zero_names(names, fields):
    for item in names:
        for elem in fields[1:]:
            item[elem] = ""
    return names


"""Function adds date fields in the item"""


def add_date(zero_names, data):
    for item in data:
        for elem in zero_names:
            if elem['Employee Name'] == item['Employee Name']:
                for key, value in item.items():
                    if key != 'Employee Name':
                        elem.update(item)

    return zero_names


"""Function writes to csv file """


def write_csv(final_data, fieldnames, filename='final_worksheet.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in final_data:
            writer.writerow(item)


def main():
    read_data = read_csv('acme_worksheet.csv')
    # print(read_data)
    changed_data = change_keys_values(read_data)
    # print(changed_data)
    fieldnames = get_fields(changed_data)
    # print(fields)
    names = get_names(changed_data)
    # print(names)
    zero_names = send_zero_names(names, fieldnames)
    # print(zero_names)
    final_data = add_date(zero_names, changed_data)
    # print(final_data)
    final_data.sort(key=lambda x: x['Employee Name'])
    write_csv(final_data, fieldnames, 'sorted_final_worksheet.csv')


if __name__ == '__main__':
    main()
