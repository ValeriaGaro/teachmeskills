# Написать программу, которая будет выводить приветствие с именем
user_name = "Valeria"
print("Hello, " + user_name)

# Написать программу, которая посчитает и выведет результат выражения
# Проверить, является ли результат выражения типом данных int
user_string = ((2 ** 5) * 2 - 16 * 2) / (8 ** 8)
print(user_string)
print(user_string is int)

# Создать и вывести список, хранящий в себе все рассмотренные в данной лекции типы данных.
user_None_type = None
user_boolean = True
user_string = "This is string"
user_dictionary = {"Course": "Python development", "School": "TeachMeSkills"}
user_integer = 22
user_float = 3.2
user_list = ["Alex", "Sam", 8, 2.5]
user_tuple = ("January", "February", "March", "April")
user_set = {1, 2, 3, 5}
types_of_data = [user_None_type, user_boolean, user_string, user_dictionary, user_integer, user_float, user_list,
                 user_tuple, user_set]
print(types_of_data)
