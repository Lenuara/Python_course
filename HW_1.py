# Python сourse
# HomeWork 1

# Переменные
my_string = 'Python'    # 1) Создать переменную типа String
my_int = 3              # 2) Создать переменную типа Integer
my_float = 3.1415       # 3) Создать переменную типа Float
my_bytes = bytes(100)   # 4) Создать переменную типа Bytes
my_list = [1, 2, 33, 'script', ['a', 'b', 'c'], {"key0": 123, "key1": "program", "key3": ['qw', 'er', 12] }]  # 5) Создать переменную типа List
my_tuple = ('q', 'w', 'r', 't', 'y')    # 6) Создать переменную типа Tuple
my_set = {'qq', 'ww', '123', 456}       # 7) Создать переменную типа Set
my_frozen_set = frozenset(my_set)       # 8) Создать переменную типа Frozen set
my_dict = {'name': 'Vasya', 'age': 25}  # 9) Создать переменную типа Dict

# 10) Вывод в консоль переменных и их типов данных
print(type(my_string), my_string)
print(type(my_int), my_int)
print(type(my_float), my_float)
print(type(my_bytes), my_bytes)
print(type(my_list), my_list)
print(type(my_tuple), my_tuple)
print(type(my_set), my_set)
print(type(my_frozen_set), my_frozen_set)
print(type(my_dict), my_dict)

string_1 = 'Quality'    # 11) Создать переменную String
string_2 = 'assurance'  # 11) Создать переменную String
union_string = string_1 + ' ' + string_2 # 11) Cоздать переменную в которой сканкатенируете эти переменные
print(union_string)     # 11) Вывести в консоль.

print(my_string, my_int)  # 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(my_string + ' ' + str(my_int))  # 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
