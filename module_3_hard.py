def calculate_structure_sum(*l):
    sum = 0
    for i in l:
        if isinstance(i, int):
            sum += i
        elif isinstance(i,str):
            sum += len(i)
        elif isinstance(i, list) or isinstance(i, set) or isinstance(i, tuple):
            sum += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            sum += calculate_structure_sum(*i.items())
    return sum


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
