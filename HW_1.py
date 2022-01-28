# Python сourse
# HomeWork 1

# Переменные
my_string = 'Python'
my_int = 3
my_float = 3.1415
my_bytes = bytes(100)
my_list = [1, 2, 33, 'script', ['a', 'b', 'c'], {"key0": 123, "key1": "program", "key3": ['qw', 'er', 12] }]
my_tuple = ('q', 'w', 'r', 't', 'y')
my_set = {'qq', 'ww', '123', 456}
my_frozen_set = frozenset(my_set)
my_dict = {'name': 'Vasya', 'age': 25}
string_1 = 'Quality'
string_2 = 'assurance'
union_string = string_1 + ' ' + string_2

# Вывод в консоль
print(type(my_string), my_string)
print(type(my_int), my_int)
print(type(my_float), my_float)
print(type(my_bytes), my_bytes)
print(type(my_list), my_list)
print(type(my_tuple), my_tuple)
print(type(my_set), my_set)
print(type(my_frozen_set), my_frozen_set)
print(type(my_dict), my_dict)
print(union_string)
print(my_string, my_int)
print(my_string + ' ' + str(my_int))
