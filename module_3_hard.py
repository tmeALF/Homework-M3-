data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_structure):
    _sum = 0
    if isinstance(data_structure, str):
        _sum += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        _sum += data_structure
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            _sum += calculate_structure_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            _sum += calculate_structure_sum(key)
            _sum += calculate_structure_sum(value)
    return _sum


result = calculate_structure_sum(data_structure)
print(result)
