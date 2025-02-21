
def input_data():
    data = {}
    with open("../common/input_file.txt", 'r') as file:
        for line in file:
            key, value = line.strip().split('=', 1)
            data[key.strip()] = value.strip()
    return data
